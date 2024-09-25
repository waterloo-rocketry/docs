RLCS V3 Towerside
=================

.. toctree::
   :maxdepth: 2
   :caption: Boards

   towerside-power-board.rst
   towerside-relay-board.rst
   tank-heating-relay-board.rst

Introduction
------------
Towerside is more complicated because it needs to handle the high current draw of motorized valves. It is made up of a set of identical Relay boards connected over an I2C bus to a master Arduino Mega.

The various I2C boards in Towerside are connected over an I2C bus in a daisy-chain configuration. In addition to the two I2C wires SDA and SCL, there is a regulated 5 V line, an unregulated 12 V line, and a ground line. The 5 V line drives the various microcontrollers on the boards and the 12 V line is used to drive the relays on I2C Relay board. The I2C Relay boards additionally have a secondary daisy-chained power connection which uses low-gauge wire and is used exclusively to drive the actuators. This ensures that the high current draw of the actuators does not cause brownouts on the MCU power lines.

The main purpose of the Towerside Power Board is to supply 5V power to the Arduino, and provide power output, UART screw terminal for communication to Client-side, and keylock switch connector and JST I2C connector. The seven segment display on the board displays the current status of each motorized valve ang ignition, with binary each bit represent a valve or ignition coil.

The main purpose of the RLCS Relay board is to operate the motorized valves that control the flow of oxidizer into the rocket during fill operations. Each Relay board is connected to one motorized valve. Relay board also detects the states of limit switches built into the valves, which are activated whenever the motor shaft arrives at a fully closed or fully open state. These limit switches indicate the current position of the motor shaft; this information is provided to human operators at mission control so that the operators are continually aware of the current position of every motorized valve in the system. Accurate tracking of the states of each of the launch control devices is critical for safety. In addition to operating motorized valves, the Relay board can also apply an electric current to an ignition coil to ignite the engine.
The typical ignition current is approximately 5 A. The Relay board is equipped with a current-sense amplifier which continually measures the current sunk through whatever actuator or coil is connected. These measurements are reported to the human operators at mission control so that the operators are aware of the current flowing to the motors and ignition coils. Thus, if any of these electrical devices are malfunctioning, the human operators can easily identify the faulty component and take appropriate action.

Relay board uses a pair of relays to control actuation direction and power to the actuator independently. This requires two actions to be taken in order to actuate a valve or fire an ignition coil (where the coil is wired to the normally open contacts of the direction relay).

System Safety
-------------
he entire system is designed to prevent unintended actuation of valves and fail safely. Both Clientside and Towerside have keyed-alike arming and disarming switches respectively, both of which retain the key when turned. This means that whenever the tower is approached the key is removed from Client Side, disarming it, and then inserted into Towerside, also disarming it. In this configuration it is physically impossible to arm Clientside while personnel are at the tower since the key is also physically with them, and even if a fault caused either Clientside or Towerside to unintentionally arm the other half would still be disarmed.

Within Towerside, two relays are required to actuate in order to trigger any action. The relays are wired in series such that one provides power to the actuator and the second determines which direction the actuator should move in. The plumbing system is also set up such that if any individual actuator fails the system can still be safely vented. Clientside and Towerside continually send command and sensor data messages to each other. This means that if either one unexpectedly fails, or the radio link between them drops, both can detect this by noticing silence on the line. If Towerside does not hear from Clientside for 10 seconds, it will automatically set all actuators to a predefined ‘safe state’ that is baked into its firmware. This means opening all vent valves and closing or de-energizing all others in order to make the system safely approachable by personnel. Clientside will also report any silence of at least 3 seconds to the operator, which could indicate a flakey radio connection or an issue with Towerside.

Towerside Board I2C Communication Protocol
------------------------------------------

Relay Board
```````````
The two relay is controled by I2C write one byte

+-------------+--------+--------+-------+
| Bits        | 7-2    | 1      | 0     |
+=============+========+========+=======+
| Description | Unused | Select | Power |
+-------------+--------+--------+-------+

The limit switch and current are reported by I2C read

+------+----------------+
| Byte | Description    |
+======+================+
|  0   | | Limit switch |
|      | | 0 - Unknown  |
|      | | 1 - Open     |
|      | | 2 - Close    |
+------+----------------+
| 1    | Primary ADC-L  |
+------+----------------+
| 2    | Primary ADC-H  |
+------+----------------+
| 3    | Second ADC-L   |
+------+----------------+
| 4    | Second ADC-H   |
+------+----------------+

Tank Heating Board
``````````````````
The the relay is controled by I2C write one byte

+-------------+--------+--------+
| Bits        | 7-1    | 0      |
+=============+========+========+
| Description | Unused | ON/OFF |
+-------------+--------+--------+

The voltages and current are reported by I2C read

+------+-------------------+
| Byte | Description       |
+======+===================+
| 0    | Thermistor ADC-L  |
+------+-------------------+
| 1    | Thermistor ADC-H  |
+------+-------------------+
| 2    | Current ADC-L     |
+------+-------------------+
| 3    | Current ADC-H     |
+------+-------------------+
| 4    | 24V PWR IN ADC-L  |
+------+-------------------+
| 5    | 24V PWR IN ADC-H  |
+------+-------------------+
| 6    | Kelvin Low ADC-L  |
+------+-------------------+
| 7    | Kelvin Low ADC-H  |
+------+-------------------+
| 8    | Kelvin High ADC-L |
+------+-------------------+
| 9    | Kelvin High ADC-H |
+------+-------------------+
