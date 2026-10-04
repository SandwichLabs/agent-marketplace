---
title: Rooms and resources
category: settings-navigation
source: https://support.mindbodyonline.com/s/article/203254103-Rooms-and-resources?language=en_US
source_updated: 2026-01-15
---
# Rooms and resources

How to add, edit, order, and assign rooms and other bookable resources for classes, courses, appointments, and rentals, including room requirements and a workaround for multi-person rooms.

## Where in Mindbody
- Manage Rooms: https://clients.mindbodyonline.com/app/business/ResourceManagement (**Settings** > **General** > **Rooms and Resources**)
- Service Categories: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_tg.asp (**Settings** > **Classic Setup** > **Service Categories**)
- Appointment Options: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_appt.asp (**Settings** > **Services** > **Appointment Options**)

## Steps
### Add a room
1. Open Manage Rooms, click **+Add a Room** (top right).
2. Fill the **Add a New Room** form: **Room name**, **Located at** (location dropdown for datashare sites), **This room can be used for** (**All services** or **Only specific services**, then pick service type Appointments/Classes/Enrollments and tick services under "Limit to these services").
3. **Save**.

### Edit a room
- Rename: expand the room, edit **Room name**, **Save**.
- Reorder: drag the square handle left of the name.
- Room schedule PDF: gear icon > **Show on room schedule PDF** (checkmark = included).
- Rental color: Service Categories > **Resources** section > click the multi-color circle in Color column (HEX allowed) > **Save**.

### Appointment room settings
1. Appointment Options > expand **Appointment System Policies**.
2. Set **Default Require Resource for Appointment Booking** and/or **Assign a different resource to each client in a multi-capacity appointment**, then **Update**.

### Seat two clients/providers in one room
1. Create two similarly named rooms; restrict the duplicate to the one appointment type.
2. Require a resource for that type and disable online booking for it.
3. Book client/provider 1 in the first room, client/provider 2 in the second.

## Settings & fields
- **Default Require Resource for Appointment Booking**: new appointment types require a room; must be on if rooms are required for consumer-site bookings.
- **Assign a different resource to each client...**: otherwise multi-capacity clients share the room, which only applies to the first client. Staff can still skip the room on the business site.
- **Show Resources in Consumer Mode** (Class and course Options): shows assigned rooms to online bookers; unsupported in the new Schedule widget.

## Gotchas
- Resource Scheduling must be enabled first. Permissions (Settings): **Resource Management screen**, **Service Categories screen** (color), **Appointment Options screen** (requirements).
- Choosing All locations shares the room across current and future locations; wrong location later means delete/deactivate and recreate. Recommended: separate rooms per location.
- Sort order sets room priority (highest available is auto-used for online appointment bookings) and room schedule display, not menu order.
- A room is greyed out when scheduling a class if already booked, not tied to that class type, or class type unassigned.
- A room or resource handles one appointment and one provider at a time.
- Deleting or deactivating rooms: see linked article (irreversible effects possible; confirm first).

## Related
- [Enable rooms](https://support.mindbodyonline.com/s/article/210899217-How-do-I-enable-rooms-on-my-site?language=en_US)
- [Delete or deactivate a room](https://support.mindbodyonline.com/s/article/210181958-How-do-I-delete-or-deactivate-a-room-resource?language=en_US)
- [Assign rooms to classes](https://support.mindbodyonline.com/s/article/203257623-Why-can-t-I-add-a-resource-room-to-my-class-or-enrollment?language=en_US)
- [Room requirement for appointments](https://support.mindbodyonline.com/s/article/Live-Chat-How-do-I-setup-a-room-requirement-for-appointments?language=en_US)
- [Rentals](https://support.mindbodyonline.com/s/article/203254093-Rentals?language=en_US)
- [Room rentals as appointments](https://support.mindbodyonline.com/s/article/204382343-Setting-up-Room-Rentals-Resources-as-Appointments?language=en_US)
- [Book a room](https://support.mindbodyonline.com/s/article/Booking-up-Rooms?language=en_US)
- [Pick-a-Spot setup](https://support.mindbodyonline.com/s/article/How-to-Set-Up-Your-Facility-for-Pick-A-Spot?language=en_US)
- [Room Builder](https://support.mindbodyonline.com/s/article/Room-Builder-screen?language=en_US)
- [Room Allocation Report](https://support.mindbodyonline.com/s/article/212668847-Classes-How-to-use-the-Room-Allocation-Report-check-room-conflicts?language=en_US)
- [Two rooms for one class](https://support.mindbodyonline.com/s/article/Can-I-assign-the-two-rooms-to-the-same-class?language=en_US)
- [Class and course options](../classes-courses/203259633-Class-enrollment-options-screen.md)
