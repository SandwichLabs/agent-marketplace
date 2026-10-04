---
title: Staff Permissions - Settings
category: staff
source: https://support.mindbodyonline.com/s/article/Staff-Permissions-Settings?language=en_US
source_updated: 2026-09-28
---
# Staff Permissions - Settings

Reference for every checkbox in the Settings section of a permission group: what it unlocks, which screens it touches, and which other checkboxes must also be on. Use it when a staff login cannot see or change something and you need to find the missing permission.

## Where in Mindbody
- Menu path: **Settings > Staff Permissions** (or **Staff > Staff Permissions**), then pick the permission group on the left.
- Some permissions depend on the software package.

## Class and schedule permissions
Most depend on **Manage class/event schedules**; that one in turn wants **Manage classes/events descriptions** and **View Services & Pricing**.
- **Manage class themes**: add/edit/delete class theme names (Services & Products > Classes).
- **Manage classes/events descriptions**: edit class/course descriptions.
- **Manage class/event schedules**: add, edit, cancel, un-cancel, delete schedules; open class setup.
- **Schedule free classes/events**: flip a class to free on the Edit Scheduled Class/Event screen.
- **Schedule resources for classes/events**: assign/remove rooms (turn off to stop staff changing a class's room).
- **Schedule substitute teachers**: set subs and add assistants; also lets managers get Substitution Management texts.
- **Block copy/cancel class and event schedules**: Block Cancel Classes and Block Copy Class Schedules on Manage Schedules.
- **Edit semester setup**: Settings > Classic Setup > Semesters.
- **Room scheduling**: run room-conflict check before assigning a room.
- **Resource Management screen**: add/edit/delete rooms at Settings > General > Rooms and Resources.
- **Mass cancel classes/events/appointments**: Settings > Clients > Cancel Class and Appointment Bookings; also required to modify recurring appointments.
- **Active Session Times (Scheduling Increments)**: Settings > Services > Scheduling Increments.
- **Manage closed day/holiday scheduling**: closed business days (General Setup & Options, or Classes > More).
- **Class & Events Options screen** / **Appointment Options screen**: edit Settings > Services option pages; both also grant Client Custom Fields.

## Staff permissions
- **Add new staff members**: Staff > Add Staff; no prerequisites.
- **View/edit staff member personal information**: edit phone etc.; base permission for the rest below.
- **Manage staff member settings**: photo, private notes, public bio; needs the personal-info permission.
- **Manage staff member Settings & Sales settings**: the checkboxes on the staff profile; needs personal-info.
- **Administer staff logins**: usernames, passwords, permissions; needs personal-info and manage settings.
- **Staff member availability**: appointment availability screen; needs personal-info.
- **Staff pay rates**: class/hourly and appointment pay rates, pay rate descriptions, Insights > Reports > Staff > Pay Rates (distinct from the Payroll report permission); needs personal-info.
- **Administer permission groups**: Staff > More > Staff Permissions > Add/Edit Groups. Deleting a group deletes the logins in it.
- **Deactivate Multi-Factor Authentication for other users**: Staff Profile screen.

## Business setup
- **Business Information screen**: Settings > General > Locations and Mindbody App Listing, Tax Rates, auto-deactivation of clients, Mindbody app dashboard and Affiliate Network. Shared with Marketing permissions (off in one = off in both).
- **General Setup & Options screen**; **News & Events screen** (Settings > Communications & Marketing); **Membership Setup screen** (Settings > Clients > Membership Settings); **Notifications setup** (auto emails/texts); **Links screen** (needs appointment view permission for appointment links); **Set up localization** (state/country/timezone and Words and Phrases; needs My Business access).
- **Media Management screen**: needs Media service categories and **Manage account credits, gift cards, contracts, and packages**.
- **Session Type/Class Type screens**: class/appointment types and Martial Arts Belts; needs **Staff Pay Rates**.
- **Service Categories screen**: highest-level service categories and navigation menu editing.
- **Revenue categories for services** / **for products**.
- **Set up cash registers**: needs the Cash Drawers (Multiple) feature on.
- **Add and manage ICD Codes**; **Manage client forms** (Settings > General > Client Forms and Liability Waivers); **Manage data privacy requests** (Settings > Clients > Data Privacy, approve/deny erasure); **Apply No-Show/Late Cancel Fees** (Settings > Clients > No-Show/Late Cancel Fees); **Download video on demand**; **Retention Marketing Settings** (needs View Marketing Automation Tools); **Access participation agreements** (franchise only, controls the prompt to accept updated terms).
- **Locate duplicate client records** / **Merge duplicate/Unmask client records**: Settings > Clients.
- **Constant Contact integration screen**: legacy; no longer available since June 2020.

## Pricing
- **View Services & Pricing**: read-only access to Services & Products and Pricing Options; prerequisite for the other pricing permissions.
- **Edit pricing option details**: all fields except name/price/promotion; can convert an existing option to an intro offer.
- **Edit pricing option tax rates**: needs details and View Services & Pricing; otherwise tax is view-only.
- **Edit pricing option price**; **Edit pricing option name**.
- **Add and deactivate pricing options**: add/deactivate/reactivate; create new intro offers (Create Intro Offer button on Insights > Client Acquisition needs the Client Acquisition dashboard report permission; promoted intro offers need Manage Mindbody Promote Settings in Marketing). Discontinuing from Pricing Options also needs View product wholesale costs and Edit product details.
- **Manage account credits, gift cards, contracts, and packages**: add/edit these and the sort order.
- **Manage contract activation/deactivation**, **sell online**, **online description**, **agreement terms**: finer-grained contract permissions; they only take effect when the broader permission above is disabled.
- **Item/membership discounts & restrictions**: Members Discount / Members Only lists; needs Complete sales transactions at POS.
- **Set up promotions/semester discounts**: Settings > Pricing > Promo Codes.

## Retail and inventory
- **View retail products** is the base; **View product (wholesale) costs**, **Edit product details** (also suppliers, colors, sizes, discontinuing, inventory settings), **Edit product price and taxes**, **Add products from the product screen** all need it.
- **Print product barcodes**: needs Ability to view all clients and Inventory - Adjust "on hand".
- **Inventory - Log incoming**, **Adjust "on hand"**, **Transfer** (multi-location only), **Purchase Orders screen**: no prerequisites.

## Sales and payments
- **Complete sales transactions at POS**: needs Ability to view all clients; also lets staff manage the branded app. Recommended: merchant account permissions and View client's billing info.
- **Create products at POS**, **Edit sale price and count** (also custom gift card amounts), **Edit sale discount**, **Pay for Another Client**: need POS permission (discount and pay-for-another also need view all clients).
- **Edit sale date**: needs view all clients, purchase history, POS. Without Manager corrections, cannot change location, payment method or commission recipient.
- **Edit sale activation dates**: needs POS and view all clients; on the Account Details screen it also needs "Edit client's series (duration/reassign payment)" or "Edit client's series counts & sessions".
- **Manager corrections - Edit Sales**: change client, payment method, commission recipient, date via Settings > Pricing > Manage Sales; needs POS, view all clients, purchase history, Void/edit past sales.
- **Void/edit past sales**: also voids card transactions; needs view all clients and purchase history.
- **Issue sale refunds**: Return All on a sale; needs the three above plus Void/edit past sales.
- **Issue sale refunds to credit cards**: if off, staff can refund only to account credit.
- **Set up payment methods**: Settings > Retail > Payment Methods; mark clients as third-party payers. **Set up room numbers** needs it. **Sell to third-party payers** needs POS. **Deny third-party payments** needs view all clients and purchase history.

## Locations
- **Allow users to switch between locations while logged in**: checked = staff pick location at login (default is per browser, lost when cache cleared), can change location on POS and schedules, and manage Marketing Suite. Unchecked = one location per login, owner assigns it, must log out to switch; a missing location can cause an "Invalid loc" login error. Shared with Marketing permissions. Multiple cash drawers still require logging out.
- **View reports for all locations**: only matters when switching is disabled; also gates Time Clock report and Marketing Suite tools.

## Gotchas
- ⚠️ Irreversible / financial — confirm with the user first: granting refund, void, edit-sale or credit-card-refund permissions; deleting a permission group (deletes its logins).
- Many permissions silently do nothing without their prerequisites; check the dependency listed above before debugging.
- Location permissions appear in both Settings and Marketing and are linked.

## Related
- [Staff Permissions - Clients](Staff-Permissions-Client-Permissions.md)
- [Staff Permissions - Appointments](Staff-Permissions-Appointment-Permissions.md)
- [Staff Permissions - Analytics](https://support.mindbodyonline.com/s/article/Staff-Permissions-Analytics?language=en_US)
- [Staff Permissions - Reports](https://support.mindbodyonline.com/s/article/Staff-Permissions-Reports?language=en_US)
- [Understanding Mindbody software packages](../settings-navigation/Why-isn-t-this-feature-available.md)
