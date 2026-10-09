"""Workspace layout, engine paths and the setup stamp (.engine/ok.json)."""
import json, os, pathlib, platform, sys

ENGINE = pathlib.Path(__file__).resolve().parent.parent          # skills/videomaker/engine
WEB = ENGINE / "web"
SKILLS = ENGINE.parent.parent                                    # skills/
# fx.js and reel.js are shared with the storyboard: read from the sibling video-template skill in a plugin install,
# or from the copy the marketplace build vendors into standalone packages (engine/runtime, engine/starter-kit).
RUNTIME = next((p for p in (SKILLS / "video-template" / "runtime", ENGINE / "runtime") if p.exists()), SKILLS / "video-template" / "runtime")
STARTER_KIT = next((p for p in (SKILLS / "video-template" / "kit", ENGINE / "starter-kit") if p.exists()), SKILLS / "video-template" / "kit")
STORYBOARD = next((p for p in (SKILLS / "video-template" / "scripts", ENGINE / "storyboard") if p.exists()), SKILLS / "video-template" / "scripts")

VIDEO_EXT = {".mov", ".mp4", ".m4v", ".webm", ".mkv", ".avi", ".mts"}
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".heic"}
AUDIO_EXT = {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".aif", ".aiff"}


def is_mac() -> bool:
    return platform.system() == "Darwin"


class Workspace:
    """A business's reel folder: clips/, music/, kit/, reels/, and the hidden .engine/ cache."""

    def __init__(self, root):
        self.root = pathlib.Path(root).expanduser().resolve()
        self.clips = self.root / "clips"
        self.music = self.root / "music"
        self.kit = self.root / "kit"
        self.reels = self.root / "reels"
        self.engine = self.root / ".engine"
        self.proxies = self.engine / "proxies"
        self.thumbs = self.engine / "thumbs"
        self.sheets = self.engine / "sheets"
        self.library_path = self.engine / "library.json"
        self.ok_path = self.engine / "ok.json"

    def rel(self, p) -> str:
        return pathlib.Path(p).resolve().relative_to(self.root).as_posix()

    def exists(self) -> bool:
        return self.engine.is_dir() or self.clips.is_dir() or self.kit.is_dir()

    def init(self):
        for d in (self.clips, self.music, self.reels, self.proxies, self.thumbs, self.sheets):
            d.mkdir(parents=True, exist_ok=True)

    def library(self) -> dict:
        if self.library_path.exists():
            return json.loads(self.library_path.read_text())
        return {"version": 1, "sources": {}, "shots": {}}

    def save_library(self, lib: dict):
        self.library_path.parent.mkdir(parents=True, exist_ok=True)
        self.library_path.write_text(json.dumps(lib, indent=1))

    def ok(self) -> dict:
        return json.loads(self.ok_path.read_text()) if self.ok_path.exists() else {}

    def reel(self, name) -> pathlib.Path:
        p = pathlib.Path(name)
        if not p.is_absolute():
            p = (self.root / p) if (self.root / p).exists() or str(name).startswith("reels/") else self.reels / name
        return p.resolve()


def find_workspace(arg=None) -> Workspace:
    root = arg or os.environ.get("REEL_WORKSPACE") or os.getcwd()
    return Workspace(root)


def die(msg, code=1):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)
