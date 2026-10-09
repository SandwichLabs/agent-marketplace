"""A local static server for the compositor: range requests (video seeking needs 206 responses) and three mounts —
/_rt/ (the shared runtime), /_engine/ (comp.html, media.js) and / (the workspace)."""
import errno, http.server, mimetypes, pathlib, re, threading, time, urllib.parse

from .ws import RUNTIME, WEB

MIME = {".js": "text/javascript", ".mjs": "text/javascript", ".json": "application/json", ".woff2": "font/woff2", ".svg": "image/svg+xml",
        ".webm": "video/webm", ".mp4": "video/mp4", ".m4a": "audio/mp4", ".wav": "audio/wav", ".mp3": "audio/mpeg", ".html": "text/html"}
SPAN = 4 << 20  # an open-ended range ("bytes=N-") gets at most this much; the browser asks again for more


def _send(sock, data: bytes):
    """sendall, but macOS loopback can raise ENOBUFS/EAGAIN while several videos stream at once: wait and resume
    from the exact byte (send reports what went out), so a busy socket is a short pause, not a dead request."""
    view, waits = memoryview(data), 0
    while view:
        try:
            n = sock.send(view)
        except OSError as e:
            if e.errno not in (errno.ENOBUFS, errno.EAGAIN, errno.EWOULDBLOCK) or waits >= 500:
                raise
            waits += 1
            time.sleep(0.01)
            continue
        view, waits = view[n:], 0


def serve(root: pathlib.Path):
    root = root.resolve()
    mounts = [("/_rt/", RUNTIME.resolve()), ("/_engine/", WEB.resolve()), ("/", root)]

    class H(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def resolve(self):
            path = urllib.parse.unquote(urllib.parse.urlparse(self.path).path)
            for prefix, base in mounts:
                if path.startswith(prefix):
                    p = (base / path[len(prefix):]).resolve()
                    return p if (p == base or base in p.parents) and p.is_file() else None
            return None

        def do_HEAD(self):
            self.do_GET(head=True)

        def do_GET(self, head=False):
            p = self.resolve()
            if not p:
                self.send_response(404); self.end_headers(); return
            size = p.stat().st_size
            ctype = MIME.get(p.suffix.lower()) or mimetypes.guess_type(p.name)[0] or "application/octet-stream"
            m = re.match(r"bytes=(\d*)-(\d*)", self.headers.get("Range") or "")
            a, b = 0, size - 1
            if m:
                a = int(m[1]) if m[1] else 0
                b = int(m[2]) if m[2] else min(size - 1, a + SPAN - 1)
                b = min(b, size - 1)
                self.send_response(206)
                self.send_header("Content-Range", f"bytes {a}-{b}/{size}")
            else:
                self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Accept-Ranges", "bytes")
            self.send_header("Content-Length", str(b - a + 1))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            if head:
                return
            try:
                with open(p, "rb") as f:
                    f.seek(a)
                    left = b - a + 1
                    while left > 0:
                        chunk = f.read(min(1 << 16, left))
                        if not chunk:
                            break
                        _send(self.connection, chunk)
                        left -= len(chunk)
            except OSError:  # the browser cancelled (it often does mid-video), or the socket gave up: end this response
                self.close_connection = True

    class S(http.server.ThreadingHTTPServer):
        def handle_error(self, request, client_address):  # to a log file, not mixed into the command's output
            import traceback
            try:
                with open(root / ".engine" / "server.log", "a") as f:
                    f.write(time.strftime("%H:%M:%S ") + traceback.format_exc())
            except OSError:
                pass

    srv = S(("127.0.0.1", 0), H)
    srv.daemon_threads = True
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}"
