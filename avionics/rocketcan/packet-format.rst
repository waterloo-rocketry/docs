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

Reset Command (RESET_CMD)
-------------------------
Resets command for all microcontrollers on board

+--------+--------+--------+----------+----------+
| Byte 0 | Byte 1 | Byte 2 | Byte 3   | Byte 4-7 |
+========+========+========+==========+==========+
| 3 byte timestamp         | BOARD_ID | None     |
+--------------------------+----------+----------+

Actuator Analog Command (ACT_ANALOG_CMD)
----------------------------------------
Set analog actuator commanded state

+--------+--------+--------+-------------+----------+
| Byte 0 | Byte 1 | Byte 2 | Byte 3      | Byte 4-7 |
+========+========+========+=============+==========+
| 3 byte timestamp         | ACTUATOR_ID | None     |
+--------------------------+-------------+----------+

Debug Message (DEBUG_MSG)
-------------------------
Commands board to send arbitrary 4 byte debug message

+--------+--------+--------+---------------------+--------------+------------------+
| Byte 0 | Byte 1 | Byte 2 | Byte 3              | Byte 4       | Byte 5-7         |
+========+========+========+=====================+==============+==================+
| 3 byte timestamp         | Debug's Importance  | Line Number  | Defines Message  |
+--------------------------+---------------------+--------------+------------------+

Print Debug Message (DEBUG_PRINTF)
----------------------------------
Prints the debug message

+----------+
| Byte 1-7 |
+==========+
| Print    |
+----------+

