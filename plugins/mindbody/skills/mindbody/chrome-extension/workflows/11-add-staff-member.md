---
workflow: Add a staff member
safety: 🟡 Changes data
---
# Add a staff member

Create a staff profile, optionally with a login and permission group, and set class or appointment pay. Typical phrasings: "add Jordan as a new yoga instructor", "give our new front desk hire a login", "set Alex's pay to $40 per class".

## Ask the person for
- Name, email, and gender (required), and the role: teaches classes, takes appointments, desk staff.
- Whether they need a login, and which permission group (Role). Do not choose a group yourself; if unknown, ask.
- Pay: for classes, which rate and amount; for appointments, Flat Rate or Percentage Rate and amount per appointment type. If pay is unspecified, skip it.
- Locations, if the site has several.

## Read first
- [How to add staff members](../../articles/staff/203253673-Adding-Staff-Instructors-Teachers-Stylists.md)
- [Staff login credentials (new experience)](../../articles/staff/Adding-staff-members-and-managing-credentials-New-Mindbody-Experience.md)
- [Staff Profile screen](../../articles/staff/203253783-Staff-profiles-Creating-logins-updating-info-and-enabling-settings.md)
- [Permission groups](../../articles/staff/203253763-Permission-groups.md)
- [Class and course pay rates](../../articles/staff/203253623-Class-and-enrollment-pay-rates.md)
- [Best practices for staff pay changes](../../articles/staff/215238918-Best-Practices-for-Staff-Pay-Changes.md)

## Steps
1. **Open Staff** — navigate to https://clients.mindbodyonline.com/app/staff. First search the list to make sure the person does not already exist (also check **Status** = inactive).
2. **Start the profile** — find and click the button labelled **+Add Staff** (older docs call it **Add New Staff**), top right.
3. **Fill details** — enter the required fields. To give a login, tick **I want to create a login for this staff member** and enter their real email (it must differ from other staff or owner emails). Pick the **Role** (permission group) the person approved. Click **Save**, or **Save and Add Another**. A setup email goes out; tell the person it expires after 24 hours. You never set the password.
4. **Set role flags** — open the profile, under Settings tick **Instructor (for classes)** and/or **Instructor/Therapist (for appointments)** as needed, plus **Earns commissions/tips** only if asked. Save.
5. **Class pay rates** — in the profile click **Class / Hourly / Commission Pay Rates** (top right; or three-dot menu > **Manage Class Pay Rates**). Fill the rate type the person named (per class, per client, percentage or incremental), choose the default pay rate, and **Save**. Use an unused rate slot for new amounts.
6. **Appointment pay** — open the profile > **Staff Appointment Setup**, click **+Assign Another Appointment Type**, search the type, enter the provider's time length, choose **Flat Rate** or **Percentage Rate**, enter the amount, **Assign**.
7. **Existing login later** — profile > **Set up login** / **Edit Login**, then **Set up permissions** / **Edit Permissions**, choose **Role**, locations, setup email date, **Send setup email**.
8. Next: availability (workflow 10) so they can be booked.

## Verify
- Search the new name on the **Staff** list; the Role and Email columns are filled.
- Re-open the pay rates and Staff Appointment Setup screens and read back amounts to the person.
- The staff member confirms the setup email arrived (check spam, confirm@mindbodyonline.com).

## If it goes wrong
- No **+Add Staff**: you need the **Add new staff members** permission.
- "Email in use": the email sits on another login; see the Staff Permissions group list in the login article before deleting anything, and ask the person.
- Login errors: a permission group must be chosen first.
- Pay rates: editing an existing rate rewrites past payroll; use a new slot. Pay screens need **Staff pay rates** permission.
- Staff Identity or the new staff screen may not be on every site; report what you see.

## Variations
- Add staff inline while scheduling a class or assigning an appointment type: **Add New** in the staff dropdown ([how to add staff](../../articles/staff/203253673-Adding-Staff-Instructors-Teachers-Stylists.md)).
- New group or owner-like login: [permission groups](../../articles/staff/203253763-Permission-groups.md), [owner-like login](../../articles/staff/207517627-How-to-create-a-staff-login-with-permissions-similar-to-the-owner.md).
- Copy class pay rates to up to 10 staff via **Copy these rates to**.
