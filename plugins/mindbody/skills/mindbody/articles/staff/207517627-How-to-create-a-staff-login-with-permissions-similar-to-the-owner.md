---
title: How to create a staff login with permissions similar to the owner
category: staff
source: https://support.mindbodyonline.com/s/article/207517627-How-to-create-a-staff-login-with-permissions-similar-to-the-owner?language=en_US
source_updated: 2025-01-28
---
# How to create a staff login with permissions similar to the owner

Builds a near-owner-level staff login via a permission group, so a helper or co-owner can administer the site without sharing the single owner login.

## Where in Mindbody
- Staff Permissions: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_staff.asp (**Settings** > **Staff** > **Staff Permissions**)
- Staff list: https://clients.mindbodyonline.com/app/staff (**Staff** in left nav)

## Steps
### 1. Create a permission group
1. Open Staff Permissions, click **Edit/Add Groups** (right side).
2. Under "Add a New Permission Group", enter a **Group Name**.
3. Optional: tick the IP restrictions box.
4. Click **Add**; the group appears in the Permission Groups list.

### 2. Give the group high-level permissions
1. On Staff Permissions, pick the new group in the dropdown.
2. Expand each category (Marketing, Settings, Classes & Courses, etc.) and tick **SELECT ALL** at the top of each.
3. Leave these Reports permissions unchecked, since they restrict a user to their own data: Schedule at a Glance / Attendance (Own schedule ONLY); Cancellations - Only allow staff to view their own cancellations; Payroll Report / Payroll Export / Tips / Assistant / Commission Reports (Users can view their own only).
4. Click **Update**.

### 3. Add a new staff member (if needed)
- Create the profile first (see the add staff members article).

### 4. Assign the staff member to the group
1. Open **Staff**, click the staff member's name.
2. Under Login, enter their email address (an email is sent so they can set a password).
3. Under Permissions click **Edit permissions**; in the **Role** menu choose the new group.
4. Click **Save**.

## Gotchas
- ⚠️ Security-sensitive: this grants broad admin access; confirm with the user first.
- Only one owner login exists, and some settings are changeable only by it, so this staff login cannot do everything.
- Do not share the owner login; if it was shared, reset the owner password immediately.
- Feature availability (customizable permissions/groups) depends on software package.

## Related
- [203253743-Staff-permissions-explained](203253743-Staff-permissions-explained.md)
- [203987403-What-permissions-are-unique-to-the-Owner-login](https://support.mindbodyonline.com/s/article/203987403-What-permissions-are-unique-to-the-Owner-login?language=en_US)
- [203254383-How-to-reset-your-owner-password](https://support.mindbodyonline.com/s/article/203254383-How-to-reset-your-owner-password?language=en_US)
- [203253673-Adding-Staff-Instructors-Teachers-Stylists](203253673-Adding-Staff-Instructors-Teachers-Stylists.md)
- [Adding-staff-members-and-managing-credentials-New-Mindbody-Experience](Adding-staff-members-and-managing-credentials-New-Mindbody-Experience.md)
- [Staff-Permissions-Reports](https://support.mindbodyonline.com/s/article/Staff-Permissions-Reports?language=en_US)
- [Set-up-and-manage-owner-login-credentials](https://support.mindbodyonline.com/s/article/Set-up-and-manage-owner-login-credentials?language=en_US)
- [Logins-Owner-vs-Staff-vs-Consumer](https://support.mindbodyonline.com/s/article/Logins-Owner-vs-Staff-vs-Consumer?language=en_US)
- [I-m-a-new-staff-member-how-do-I-log-in-to-MINDBODY](https://support.mindbodyonline.com/s/article/I-m-a-new-staff-member-how-do-I-log-in-to-MINDBODY?language=en_US)
- [203270143-Staff-member-login-is-not-working-What-do-I-do](https://support.mindbodyonline.com/s/article/203270143-Staff-member-login-is-not-working-What-do-I-do?language=en_US)
- [203254253-MINDBODY-glossary](https://support.mindbodyonline.com/s/article/203254253-MINDBODY-glossary?language=en_US)
