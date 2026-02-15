Flight Phase
============

Assignee: Shiming

States
------
- Idle
- Pad Filter
- Boost
- Actuation Allowed
- Recovery (actuation still allowed)
- Landed

Key Changes (2026)
------------------
- Boost entry uses acceleration threshold as a criterion in addition to CAN events.
- Boost → Actuation Allowed: sensor-triggered using velocity (estimator) or falling acceleration within a time window [P, Q].
- Actuation Allowed → Recovery: sensor-triggered when vertical velocity drops below threshold within [R, S].
- New *Landed* state enables safe termination of logging after time K.

Implementation Notes
--------------------
- Use a state queue and event queue (mutex-like behavior is sufficient).
- Record the Boost start time; compare each iteration for scheduled transitions.
- Disallow Init → Boost; require Pad Filter before Boost to avoid false triggers while transporting.
