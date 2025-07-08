Minerva Slackbot User Guide
===========================

.. note::

   This guide is based on the original Minerva documentation in Google Docs:

   - `Message Notify <https://docs.google.com/document/d/1otYHtmFHzkN8g7089EGQpxi9-7C_iKFhDt2L2tuwxHs>`__
   - `Meetings (Calendar Events) <https://docs.google.com/document/d/1vz9b3J8ghjsyqJtUuTTT1KHH7F9GhhCrGC5Nmy-X3rQ>`__


This guide explains how to use the Waterloo Rocketry **Minerva** Slackbot day-to-day.  It is intended for *all team members* (including single-channel guests) and covers meeting reminders, message notifications, and basic troubleshooting.

.. contents:: Table of Contents
   :depth: 2
   :local:

Meeting Reminders
-----------------

Minerva reads the **Waterloo Rocketry Google Calendar** and automatically posts two reminders for every event :

* **Six hours** before the start time - includes ✅ / ❌ / ❓ reaction emojis to collect attendance.
* **Five minutes** before - pings ``@channel`` in the meeting’s Slack channel.

If a user is a *single-channel guest* of any *default channel* (see below) **and** cannot see the reminder in its channel, Minerva sends them a DM copy .

Default Channels
^^^^^^^^^^^^^^^^

``#general``, ``#airframe``, ``#business``, ``#controls``, ``#electrical``,
``#flight-dynamics``, ``#infrastructure``, ``#payload``, ``#propulsion``,
``#recovery``, ``#software`` .

Creating Events for Minerva
---------------------------

Minerva uses *plain-text* metadata stored in the **description** of a Google Calendar event .  Follow these steps:

1. **Create** the event on the Waterloo Rocketry calendar.
2. **Invite** Minerva to every Slack channel you want reminded (mention ``@minerva`` and click *Invite*).
3. **Populate** the description:

   *Line 1*   - meeting channel, e.g. ``#general``.  Append ``no-dm`` to suppress DMs to single-channel guests .

   *Line 2*   - meeting URL, starting with ``http://`` or ``https://``.  If omitted, defaults to ``https://meet.waterloorocketry.com`` .

   *Lines 3+* - free-form meeting description.

4. (Optional) **Location** field - set a physical venue.

Editing & Cancelling
^^^^^^^^^^^^^^^^^^^^

*Just edit the description*—Minerva re-parses automatically.  To cancel, add ``[CANCELLED]`` to the event title; reminders still send but the five-minute ping is suppressed .

Manual Reminders
^^^^^^^^^^^^^^^^

Run in the meeting channel:

::

   /meeting-reminder [ping]

This re-posts the next upcoming event; pass ``ping`` to force an ``@channel`` ping.

Troubleshooting (Meetings)
^^^^^^^^^^^^^^^^^^^^^^^^^^

* **No reminder posted** → The event description metadata may be malformed; clear & rewrite.
* **not_in_channel** error in **#minerva-log** → Invite @minerva to that channel.

Message Notifications (/notify)
-------------------------------

Use **/notify** to reshare (or DM) a message link .

Syntax
^^^^^^

::

   /notify LINK {copy | copy-ping} [default] [#channel1 #channel2 …]

Arguments
~~~~~~~~~

* **LINK** - Slack message URL (right-click → *Copy link*).
* **copy | copy-ping** - optional notification type:

  * *(omitted)* → DM single-channel guests in target channels.
  * ``copy`` → repost the message in target channels.
  * ``copy-ping`` → repost **and** ``@channel`` ping (use sparingly!).

* **default / #channel…** - list of targets .

  * ``default`` = all default channels listed above.  Combine with explicit channels as needed.

Examples
^^^^^^^^

*DM single-channel guests in all default channels*

::

   /notify <link>

*Copy to #electrical*

::

   /notify <link> copy #electrical

*Mass ping (⚠️ disruptive!)*

::

   /notify <link> copy-ping default #weeb

See additional examples in the appendix.

Troubleshooting (/notify)
^^^^^^^^^^^^^^^^^^^^^^^^^

* **not_in_channel** error → Invite @minerva to the target channel.

Appendix A — Quick Reference
----------------------------

=======================  ============================================
Command                  Purpose
=======================  ============================================
``/meeting-reminder``    Manually send next meeting reminder.
``/notify``              Share a message with wider audience.
=======================  ============================================
