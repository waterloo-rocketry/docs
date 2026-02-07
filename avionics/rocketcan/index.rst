RocketCAN
#########

.. toctree::
   :maxdepth: 1

   board-id.rst
   packet-format.rst

What is RocketCAN
*****************
RocketCAN is CAN bus on board rocket for inter-board avionics communication, RocketCAN is also used for on-the-pad rocket to GSE(Ground Support Equipment) communication. CAN bus supports data payload up to 8 bytes.

SID Format
**********
CAN 2.0B SID for 2026 rocket and beyond

+-----------+--------------+---------------+-------------------+----------+
| Bit 28:27 | Bit 26:20    | Bit 19:14     | Bit 13:8          | Bit 7:0  |
+===========+==============+===============+===================+==========+
| Priority  | Message Type | Board Type ID | Board Instance ID | Metadata |
+-----------+--------------+---------------+-------------------+----------+

Note the definition of the "Metadata" field is per message type, it's commonly used as an additional byte for storage.
The priority bits are allocated as following:

+-----------+----------+
| Bit value | Priority |
+===========+==========+
| 00        | Highest  |
+-----------+----------+
| 01        | High     |
+-----------+----------+
| 10        | Medium   |
+-----------+----------+
| 11        | Low      |
+-----------+----------+

History
*******
The development of RocketCAN have started at Fall 2018, it was running at 42 kbps with CAN 2.0A(11 bit SID) frame format, this format have been used until LOTS rocket. Since 2024's addition of airbrakes active control system, the messages being transmitted on the bus have increased, so the bitrate have been upgrade to 250 kbps. For 2025 rocket, due to more complex avionics and payload, board ID would exceed 11-bit SID limition, so the 2025 rocket would use a 250 kbps CAN 2.0B(29 bit SID). During 2026 development cycle the "Metadata" field has been added to SID to increase message payload capacity.
