Remote Launch Control System (RLCS)
===================================

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
| Bits        | 7-1    | 1      |
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

.. toctree::
   :maxdepth: 2
   :caption: Boards

   towerside-power-board.rst
   towerside-relay-board.rst
   clientside-board.rst
