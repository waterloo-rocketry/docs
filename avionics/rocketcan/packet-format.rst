Packet Format
#####################

**Note:** All multi-byte data field are big-endian

Message Packet Format Definition
********************************

UNDEFINED (0x00)
=================
Undefined message, do not use

GENERAL_BOARD_STATUS (0x01)
============================
Board status broadcast

+--------+---------+------------------------+----------------------+
| Byte 0-1         | Byte 2-5               | Byte 6-7             |
+========+=========+========================+======================+
| 2 byte timestamp | GENERAL_ERROR_BITFIELD | BOARD_ERROR_BITFIELD |
+--------+---------+------------------------+----------------------+

| **GENERAL_ERROR_BITFIELD:** General error code bitfield, see `general_board_status`_
| **BOARD_ERROR_BITFIELD:** Board specific error code bitfield, see `board_specific_status`_

RESET_CMD (0x02)
=================
Command to reset boards

+--------+---------+---------------+---------------+
| Byte 0-1         | Byte 2        | Byte 3        |
+========+=========+===============+===============+
| 2 byte timestamp | BOARD_TYPE_ID | BOARD_INST_ID |
+--------+---------+---------------+---------------+

| **BOARD_TYPE_ID:** Board Type ID of board to reset, set to 0 to reset all boards on bus
| **BOARD_INST_ID:** Board Inst ID of board to reset, set to 0 to reset all board of specific type

DEBUG_RAW (0x03)
=================
6-bytes of raw data

+--------+---------+----------+
| Byte 0-1         | Byte 2-7 |
+========+=========+==========+
| 2 byte timestamp | RAW_DATA |
+--------+---------+----------+

| **RAW_DATA:** Raw data, 6 bytes

CONFIG_SET (0x04)
==================
Set board specific configuration

+--------+---------+---------------+---------------+-----------+--------------+
| Byte 0-1         | Byte 2        | Byte 3        | Byte 4-5  | Byte 6-7     |
+========+=========+===============+===============+===========+==============+
| 2 byte timestamp | BOARD_TYPE_ID | BOARD_INST_ID | CONFIG_ID | CONFIG_VALUE |
+--------+---------+---------------+---------------+-----------+--------------+

| **BOARD_TYPE_ID:** Board Type ID of target board, cannot be zero
| **BOARD_INST_ID:** Board Inst ID of target board, set to 0 to set all board of specific type
| **CONFIG_ID:** Configuration ID, Board Specific
| **CONFIG_VALUE:** Configuration Value, Board and Config ID specific

CONFIG_STATUS (0x05)
=====================
Broadcast board specific configuration, for verify CONFIG_SET success

+--------+---------+-----------+--------------+
| Byte 0-1         | Byte 2-3  | Byte 4-5     |
+========+=========+===========+==============+
| 2 byte timestamp | CONFIG_ID | CONFIG_VALUE |
+--------+---------+-----------+--------------+

| **CONFIG_ID:** Configuration ID, Board Specific
| **CONFIG_VALUE:** Configuration Value, Board and Config ID specific

ACTUATOR_CMD (0x06)
====================
Set actuator commanded state

+-------------+--------+---------+--------------------+
| Metadata    | Byte 0-1         | Byte 2             |
+=============+========+=========+====================+
| ACTUATOR_ID | 2 byte timestamp | ACTUATOR_CMD_STATE |
+-------------+--------+---------+--------------------+

| **ACTUATOR_ID:** Acturator ID, see `actuator_id`_
| **ACTUATOR_CMD_STATE:** Actuator Commanded State, see `actuator_state`_

ACTUATOR_STATUS (0x07)
=======================
Actuator Status Message

+-------------+--------+---------+---------------------+--------------------+
| Metadata    | Byte 0-1         | Byte 2              | Byte 3             |
+=============+========+=========+=====================+====================+
| ACTUATOR_ID | 2 byte timestamp | ACTUATOR_CURR_STATE | ACTUATOR_CMD_STATE |
+-------------+--------+---------+---------------------+--------------------+

| **ACTUATOR_ID:** Acturator ID, see `actuator_id`_
| **ACTUATOR_CURR_STATE:** Actuator Current State, see `actuator_state`_
| **ACTUATOR_CMD_STATE:** Actuator Commanded State, see `actuator_state`_

ALT_ARM_CMD (0x08)
===================
Command to arm altimeter

+----------+--------+---------+---------------+
| Metadata | Byte 0-1         | Byte 2        |
+==========+========+=========+===============+
| ALT_ID   | 2 byte timestamp | ALT_ARM_STATE |
+----------+--------+---------+---------------+

| **ALT_ID:** Altimeter ID, see `altimeter_id`_
| **ALT_ARM_STATE:** Altimeter set arm state, see `alt_arm_state`_

ALT_ARM_STATUS (0x09)
======================
Altimeter Arm Status

+----------+--------+---------+---------------+----------+----------+
| Metadata | Byte 0-1         | Byte 2        | Byte 3-4 | Byte 5-6 |
+==========+========+=========+===============+==========+==========+
| ALT_ID   | 2 byte timestamp | ALT_ARM_STATE | DROGUE_V | MAIN_V   |
+----------+--------+---------+---------------+----------+----------+

| **ALT_ID:** Altimeter ID, see `altimeter_id`_
| **ALT_ARM_STATE:** Altimeter current arm state, see `alt_arm_state`_
| **DROGUE_V:** Drogue Pyro Voltage
| **MAIN_V:** Main Pyro Voltage

SENSOR_ANALOG16 (0x0A)
=======================
16-bits analog sensor

+-----------+--------+---------+----------+
| Metadata  | Byte 0-1         | Byte 2-3 |
+===========+========+=========+==========+
| SENSOR_ID | 2 byte timestamp | VALUE    |
+-----------+--------+---------+----------+

| **SENSOR_ID:** Sensor ID, see `analog_sensor_id`_
| **VALUE:** Analog sensor value

SENSOR_ANALOG32 (0x0B)
=======================
32-bits analog sensor

+-----------+--------+---------+----------+
| Metadata  | Byte 0-1         | Byte 2-5 |
+===========+========+=========+==========+
| SENSOR_ID | 2 byte timestamp | VALUE    |
+-----------+--------+---------+----------+

| **SENSOR_ID:** Sensor ID, see `analog_sensor_id`_
| **VALUE:** Analog sensor value

SENSOR_DEM_ANALOG16 (0x0C)
===========================
3-Dimensional 16-bit analog sensor value message

+---------------+--------+---------+----------+----------+----------+
| Metadata      | Byte 0-1         | Byte 2-3 | Byte 4-5 | Byte 6-7 |
+===============+========+=========+==========+==========+==========+
| DEM_SENSOR_ID | 2 byte timestamp | VALUE_X  | VALUE_Y  | VALUE_Z  |
+---------------+--------+---------+----------+----------+----------+

| **DEM_SENSOR_ID:** 3-Dimensional sensor ID, see `dem_sensor_id`_
| **VALUE_X:** Analog sensor value X
| **VALUE_Y:** Analog sensor value Y
| **VALUE_Z:** Analog sensor value Z

GPS_TIMESTAMP (0x0D)
=====================
+--------+---------+-----------+-------------+-------------+--------------+
| Byte 0-1         | Byte 2    | Byte 3      | Byte 4      | Byte 5       |
+========+=========+===========+=============+=============+==============+
| 2 byte timestamp | UTC_HOURS | UTC_MINUTES | UTC_SECONDS | UTC_DSECONDS |
+--------+---------+-----------+-------------+-------------+--------------+

| **UTC_HOURS:** Hour
| **UTC_MINUTES:** Minutes
| **UTC_SECONDS:** Seconds
| **UTC_DSECONDS:** Decisecond

GPS_LATITUDE (0x0E)
====================
+--------+---------+---------+---------+------------+--------+
| Byte 0-1         | Byte 2  | Byte 3  | Byte 4-5   | Byte 6 |
+========+=========+=========+=========+============+========+
| 2 byte timestamp | DEGREES | MINUTES | DMINUTES_H | DIR_NS |
+--------+---------+---------+---------+------------+--------+

| **DEGREES:** Degrees
| **MINUTES:** Minutes
| **DMINUTES_H:** No description
| **DIR_NS:** North/South

GPS_LONGITUDE (0x0F)
=====================
+--------+---------+---------+---------+------------+--------+
| Byte 0-1         | Byte 2  | Byte 3  | Byte 4-5   | Byte 6 |
+========+=========+=========+=========+============+========+
| 2 byte timestamp | DEGREES | MINUTES | DMINUTES_H | DIR_EW |
+--------+---------+---------+---------+------------+--------+

| **DEGREES:** Degrees
| **MINUTES:** Minutes
| **DMINUTES_H:** No description
| **DIR_EW:** East/West

GPS_ALTITUDE (0x10)
====================
+--------+---------+----------+--------+
| Byte 0-1         | Byte 2-5 | Byte 6 |
+========+=========+==========+========+
| 2 byte timestamp | ALT      | DALT   |
+--------+---------+----------+--------+

| **ALT:** Altitude in ft
| **DALT:** No description

GPS_INFO (0x11)
================
+--------+---------+---------+---------+
| Byte 0-1         | Byte 2  | Byte 3  |
+========+=========+=========+=========+
| 2 byte timestamp | NUM_SAT | QUALITY |
+--------+---------+---------+---------+

| **NUM_SAT:** Number of satellite
| **QUALITY:** Quality

STREAM_STATUS (0x12)
=====================
+--------+---------+------------+----------+
| Byte 0-1         | Byte 2-4   | Byte 5-7 |
+========+=========+============+==========+
| 2 byte timestamp | TOTAL_SIZE | TX_SIZE  |
+--------+---------+------------+----------+

| **TOTAL_SIZE:** Total transfer size in bytes
| **TX_SIZE:** Transfered size in bytes

STREAM_DATA (0x13)
===================
+----------+--------+---------+----------+
| Metadata | Byte 0-1         | Byte 2-7 |
+==========+========+=========+==========+
| SEQ_ID   | 2 byte timestamp | DATA     |
+----------+--------+---------+----------+

| **SEQ_ID:** Sequence ID
| **DATA:** Data payload

STREAM_RETRY (0x14)
====================
LEDS_ON (0x15)
===============
LEDS_OFF (0x16)
================
Enums Definition
****************

actuator_id
===========

Actuator ID for Actuator Command and Status Messages

.. list-table:: actuator_id Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - OX_INJECTOR_VALVE
     - Oxidizer Injector Valve, for hall-effect sensor state feedback and Canard activation
     - 0x00
   * - FUEL_INJECTOR_VALVE
     - Oxidizer Injector Valve, for hall-effect sensor state feedback
     - 0x01
   * - ROCKET_CHARGE_ENABLE
     - Rocket Ground-side Charging Enable
     - 0x02
   * - PAYLOAD_CHARGE_ENABLE
     - Payload Ground-side Charging Enable
     - 0x03
   * - 5V_RAIL_ROCKET
     - No Description
     - 0x04
   * - 5V_RAIL_PAYLOAD
     - No Description
     - 0x05
   * - 12V_RAIL_ROCKET
     - No Description
     - 0x06
   * - TELEMETRY
     - No Description
     - 0x07
   * - CAMERA_SIDE_LOOKING
     - No Description
     - 0x08
   * - CAMERA_DOWN_LOOKING
     - No Description
     - 0x09
   * - CAMERA_RECOVERY
     - No Description
     - 0x0A
   * - PROC_ESTIMATOR_INIT
     - Actuator command to start processor board state estimation
     - 0x0B
   * - SRAD_ALT_ESTIMATOR_INIT
     - Actuator command to start SRAD Altimeter state estimation
     - 0x0C
   * - SRAD_ALT_GPS_RESET
     - Actuator command to reset GPS Receiver on SRAD Altimeter
     - 0x0D
   * - CAMERA_CAPTURE
     - No Description
     - 0x0E
   * - PAYLOAD_LOGGING_ENABLE
     - Payload Sensor Board Logging Enable Control
     - 0x0F
   * - THESEUS_ACTUATOR_1
     - Theseus board actuator channel 1
     - 0x10
   * - THESEUS_ACTUATOR_2
     - Theseus board actuator channel 2
     - 0x11
   * - RLCS_RELAY_POWER
     - RLCS Relay Board Power Relay
     - 0x12
   * - RLCS_RELAY_SELECT
     - RLCS Relay Board Select Relay(Limit switch state feedback)
     - 0x13

actuator_state
==============

Actuator State

.. list-table:: actuator_state Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - ON
     - Actuator is in ON state, or Open
     - 0x00
   * - OFF
     - Actuator is in OFF state, or Close
     - 0x01
   * - UNK
     - Unknown state, for example when ball valve is turning
     - 0x02
   * - ILLEGAL
     - Illegal state, for example when limit switch of both state being triggered
     - 0x03

altimeter_id
============

Altimeter ID for uniquely indentify each altimeter

.. list-table:: altimeter_id Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - RAVEN
     - Raven4 Altimeter
     - 0x00
   * - STRATOLOGGER
     - StratoLoggerCF
     - 0x01
   * - SRAD
     - SRAD Altimeter
     - 0x02

alt_arm_state
=============

Altimiter Arm State

.. list-table:: alt_arm_state Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - DISARMED
     - Disarmed
     - 0x00
   * - ARMED
     - Armed
     - 0x01

analog_sensor_id
================

Sensor ID for Sensor Messages

.. list-table:: analog_sensor_id Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - 5V_VOLT
     - Voltage of 5V rail in mV
     - 0x00
   * - 5V_CURR
     - Current of 5V rail in mA
     - 0x01
   * - 12V_VOLT
     - Voltage of 12V rail in mV
     - 0x02
   * - 12V_CURR
     - Current of 12V rail in mA
     - 0x03
   * - CHARGE_VOLT
     - LiPo charging voltage in mV
     - 0x04
   * - CHARGE_CURR
     - LiPo charging current in mA
     - 0x05
   * - BATT_VOLT
     - Battery Voltage in mV
     - 0x06
   * - BATT_CURR
     - Battery Current in mA
     - 0x07
   * - RADIO_CURR
     - Radio current in mA
     - 0x08
   * - GPS_CURR
     - GPS Receiver current in mA
     - 0x09
   * - LOCAL_CURR
     - Local voltage rail (e.g. 3.3V) current in mA
     - 0x0A
   * - PT_CHANNEL_1
     - Pressure Transducer Channel 1, J3 on Injector Sensor Hub
     - 0x0B
   * - PT_CHANNEL_2
     - Pressure Transducer Channel 2, J4 on Injector Sensor Hub
     - 0x0C
   * - PT_CHANNEL_3
     - Pressure Transducer Channel 3, J6 on Injector Sensor Hub
     - 0x0D
   * - PT_CHANNEL_4
     - Pressure Transducer Channel 4, J8 on Injector Sensor Hub
     - 0x0E
   * - PT_CHANNEL_5
     - Pressure Transducer Channel 5, J10 on Injector Sensor Hub
     - 0x0F
   * - HALL_CHANNEL_1
     - Hall-Effect Sensor Channel 1, J7 on Injector Sensor Hub
     - 0x10
   * - HALL_CHANNEL_2
     - Hall-Effect Sensor Channel 2, J5 on Injector Sensor Hub
     - 0x11
   * - HALL_CHANNEL_3
     - Hall-Effect Sensor Channel 3, J9 on Injector Sensor Hub
     - 0x12
   * - RA_BATT_VOLT_1
     - No Description
     - 0x13
   * - RA_BATT_VOLT_2
     - No Description
     - 0x14
   * - RA_BATT_CURR_1
     - No Description
     - 0x15
   * - RA_BATT_CURR_2
     - No Description
     - 0x16
   * - RA_MAG_VOLT_1
     - No Description
     - 0x17
   * - RA_MAG_VOLT_2
     - No Description
     - 0x18
   * - FPS
     - Camera framerate
     - 0x19
   * - PAYLOAD_LIM_1
     - Payload Motor Board Limit Switch 1
     - 0x1A
   * - PAYLOAD_LIM_2
     - Payload Motor Board Limit Switch 2
     - 0x1B
   * - PAYLOAD_SERVO_DIRECTION
     - Payload Servo Direction
     - 0x1C
   * - PAYLOAD_INFRARED
     - Payload Infrared Sensor Reading
     - 0x1D
   * - THESEUS_TEMP_1
     - Theseus board temperature channel 1
     - 0x1E
   * - THESEUS_TEMP_2
     - Theseus board temperature channel 2
     - 0x1F
   * - THESEUS_TEMP_3
     - Theseus board temperature channel 3
     - 0x20
   * - RLCS_RELAY_OUTPUT_VOLT_A
     - RLCS Relay Board channel A output voltage
     - 0x21
   * - RLCS_RELAY_OUTPUT_VOLT_B
     - RLCS Relay Board channel B output voltage
     - 0x22
   * - RLCS_RELAY_OUTPUT_CURR_A
     - RLCS Relay Board channel A output current
     - 0x23
   * - RLCS_RELAY_OUTPUT_CURR_B
     - RLCS Relay Board channel B output current
     - 0x24
   * - RLCS_RELAY_LIM_VOLT_A
     - RLCS Relay Board limit switch A voltage
     - 0x25
   * - RLCS_RELAY_LIM_VOLT_B
     - RLCS Relay Board limit switch B voltage
     - 0x26
   * - LOG_WRITTEN_SIZE
     - Number of bytes written to log file(reset to 0 when a new file is created)
     - 0x27
   * - SD_LOG_FILE_NAME
     - SD Card log file name(the number part only)
     - 0x28
   * - SD_USED
     - SD Card used space size, in MiB
     - 0x29
   * - SD_FREE
     - SD Card free space size, in MiB
     - 0x2A
   * - FLASH_LOG_FILE_NAME
     - Flash log file name(the number part only)
     - 0x2B
   * - FLASH_USED
     - Flash used space size, in MiB
     - 0x2C
   * - FLASH_FREE
     - FLash free space size, in MiB
     - 0x2D
   * - CANARD_CTRL_CMD_ANGLE
     - No Description
     - 0x2E
   * - CANARD_CTRL_COEFF_LIFT
     - No Description
     - 0x2F
   * - CANARD_MS5611_BARO
     - No Description
     - 0x30
   * - CANARD_MS5611_TEMP
     - No Description
     - 0x31
   * - CANARD_MTI630_BARO_0
     - No Description
     - 0x32
   * - CANARD_MTI630_BARO_1
     - No Description
     - 0x33
   * - CANARD_MTI630_EST_ALT
     - No Description
     - 0x34
   * - CANARD_ADXRS649_GYRO
     - No Description
     - 0x35
   * - CANARD_SERVO_ANGLE
     - No Description
     - 0x36
   * - CANARD_SERVO_CURR
     - No Description
     - 0x37
   * - CANARD_SERVO_TEMP
     - No Description
     - 0x38

dem_sensor_id
=============

3-Dimensional SENSOR_ID

.. list-table:: dem_sensor_id Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - CANARD_NAV_ORIENTATION_QUAT_QX_QY_QZ
     - Canard Navigation Orientation QX, QY, QZ
     - 0x00
   * - CANARD_NAV_ORIENTATION_QUAT_QW_ALT_VARNORM
     - Canard Navigation Orientation QW, Altitude, Variance Norm
     - 0x01
   * - CANARD_NAV_ANGLE_VEL
     - No Description
     - 0x02
   * - CANARD_NAV_VEL
     - No Description
     - 0x03
   * - CANARD_LSM6DSV32X_ACCEL
     - No Description
     - 0x04
   * - CANARD_LSM6DSV32X_GYRO
     - No Description
     - 0x05
   * - CANARD_LSM303AGR_ACCEL
     - No Description
     - 0x06
   * - CANARD_LSM303AGR_MAG
     - No Description
     - 0x07
   * - CANARD_MTI630_ACCEL
     - No Description
     - 0x08
   * - CANARD_MTI630_GYRO
     - No Description
     - 0x09
   * - CANARD_MTI630_MAG
     - No Description
     - 0x0A
   * - CANARD_MTI630_EST_ORIENTATION
     - No Description
     - 0x0B
   * - CANARD_MTI630_EST_ANGLE_VEL
     - No Description
     - 0x0C
   * - CANARD_MTI630_EST_VEL
     - No Description
     - 0x0D
   * - CANARD_ADXL380_ACCEL
     - No Description
     - 0x0E

Bitfields Definition
*********************

general_board_status
====================

General board status bitfield

.. list-table:: general_board_status Bitfield bits
   :widths: 25 60 15
   :header-rows: 1

   * - Bitfield Name
     - Description
     - Offset
   * - 5V_OVER_CURRENT
     - No Description
     - 0x00
   * - 5V_OVER_VOLTAGE
     - No Description
     - 0x01
   * - 5V_UNDER_VOLTAGE
     - No Description
     - 0x02
   * - 12V_OVER_CURRENT
     - No Description
     - 0x03
   * - 12V_OVER_VOLTAGE
     - No Description
     - 0x04
   * - 12V_UNDER_VOLTAGE
     - No Description
     - 0x05
   * - BATT_OVER_CURRENT
     - No Description
     - 0x06
   * - BATT_OVER_VOLTAGE
     - No Description
     - 0x07
   * - BATT_UNDER_VOLTAGE
     - No Description
     - 0x08
   * - MOTOR_OVER_CURRENT
     - No Description
     - 0x09
   * - IO_ERROR
     - No Description
     - 0x0A
   * - FS_ERROR
     - No Description
     - 0x0B
   * - WATCHDOG_TIMEOUT
     - No Description
     - 0x0C

board_specific_status
=====================

Board specific status bitfield

.. list-table:: board_specific_status Bitfield bits
   :widths: 25 60 15
   :header-rows: 1

   * - Bitfield Name
     - Description
     - Offset
   * - 12V_EFUSE_FAULT
     - No Description
     - 0x00
   * - 5V_EFUSE_FAULT
     - No Description
     - 0x01
   * - PT_OUT_OF_RANGE
     - No Description
     - 0x02

