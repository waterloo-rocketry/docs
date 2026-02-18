Motor Handler
=============

Assignee: Michael

Responsibilities
----------------
- Communicate with the AK45-10 servo.
- Convert controller angle commands to servo commands (frequency TBD).

Open Questions
--------------
- What motor and exact datasheet revision?
- Behavior on comms loss / missed update?
- Update frequency?
- One module vs. split driver+application trade-offs (latency, complexity)?

Initial Todos
-------------
- Find working examples (GitHub) and evaluate.
- Implement command path: controller → servo.
- Integrate with CAN (see CAN Handler).
