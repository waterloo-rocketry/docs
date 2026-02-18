CAN Handler
===========

Assignee: Luke

- Reuse processor-board code; improve handling of the 3-message TX limitation to avoid drops.
- Use fixed-point integer payloads with predefined exponents where practical instead of ``float``.

Tx & Rx Message Set
-------------------
- See `RocketCAN packet format <https://docs.waterloorocketry.com/avionics/rocketcan/packet-format.html#packet-format>`_.

Telemetry Design (Scaling)
--------------------------
All telemetry values apply an exponent scaling defined in the `Controls Data Collection Rates <https://docs.google.com/spreadsheets/d/1isjiDjAHeaFbIcemxMDZfsfbDFZSkMUr7OAtPzHfreU/edit#gid=0>`_ sheet **before** transmit. Decoding on the ground reverses the scaling.

Implementation Sketch
~~~~~~~~~~~~~~~~~~~~~
- ``src/application/can_handler/can_telemetry_scaling.h`` defines:
  - ``can_scaling_id_t``: all scaling IDs across telemetry values.
  - ``can_types_t``: payload integer types.
  - ``can_scale_data_t``: per-signal metadata.
  - ``can_scale_map``: maps scaling IDs → type & scale factor (fixed-point constants).
- ``src/application/can_handler/can_handler.c`` provides:
  - ``can_encode_scaled(float32, scale_id)``: divide by scale, validate overflow, cast to integer.
  - Saturation rules for overflow/underflow and sign handling.
- Callers (e.g., ``controller.c``) do:
  - ``build_xxx_msg`` (from ``canlib``) → ``can_handler_transmit``.
- In ``canlib``, update payload field types as needed; keep scaling logic in the handler for maintainability.
