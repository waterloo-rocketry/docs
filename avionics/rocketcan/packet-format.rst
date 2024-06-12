Packet Format
=============

This document is based on canlib `message_types.h <https://github.com/waterloo-rocketry/canlib/blob/master/message_types.h>`_.

General Command (GENERAL_CMD)
-----------------------------
Send a command code

+--------+--------+--------+--------------+----------+
| Byte 0 | Byte 1 | Byte 2 | Byte 3       | Byte 4-7 |
+========+========+========+==============+==========+
| 3 byte timestamp         | Command Type | None     |
+--------------------------+--------------+----------+

Actuator Command (ACTUATOR_CMD)
-------------------------------
Send actuator on/off command

+--------+--------+--------+--------------+----------------+----------+
| Byte 0 | Byte 1 | Byte 2 | Byte 3       | Byte 4         | Byte 5-7 |
+========+========+========+==============+================+==========+
| 3 byte timestamp         | Actuator ID  | Actuator State | None     |
+--------------------------+--------------+----------------+----------+

Altemeter Arm Command (ALT_ARM_CMD)
-----------------------------------
Sets altemeter arming

+--------+--------+--------+-------------------+----------+
| Byte 0 | Byte 1 | Byte 2 | Byte 3            | Byte 4-7 |
+========+========+========+===================+==========+
| 3 byte timestamp         | Altemer Arm State | None     |
+--------------------------+-------------------+----------+
