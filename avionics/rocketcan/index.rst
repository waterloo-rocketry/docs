RocketCAN
#########

.. toctree::
   :maxdepth: 1

   packet-format.rst

What is RocketCAN
*****************
RocketCAN is CAN bus on board rocket for inter-board avionics communication, RocketCAN is also used for on-the-pad rocket to GSE(Ground Support Equipment) communication. CAN bus supports data payload up to 8 bytes.

SID Format
**********
CAN 2.0B SID for 2025 rocket and beyond

+-----------+--------------+-----------+---------------+-------------------+
| Bit 28:27 | Bit 26:18    | Bit 17:16 | Bit 15:8      | Bit 7:0           |
+===========+==============+===========+===============+===================+
| SID (Identifier)         | EID (Extended Identifier)                     |
+-----------+--------------+-----------+---------------+-------------------+
| Priority  | Message Type | Reserved  | Board Type ID | Board Instance ID |
+-----------+--------------+-----------+---------------+-------------------+

CAN 2.0A SID for Borealis and older rockets

+--------------+----------+
| Bit 10:5     | Bit 4:0  |
+==============+==========+
| Message Type | Board ID |
+--------------+----------+

History
*******
The development of RocketCAN have started at Fall 2018, it was running at 42 kbps with CAN 2.0A(11 bit SID) frame format, this format have been used until LOTS rocket. Since 2024's addition of airbrakes active control system, the messages being transmitted on the bus have increased, so the bitrate have been upgrade to 250 kbps. For 2025 rocket, due to more complex avionics and payload, board ID would exceed 11-bit SID limition, so the 2025 rocket would use a 250 kbps CAN 2.0B(29 bit SID).
