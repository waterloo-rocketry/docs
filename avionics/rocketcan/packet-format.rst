Packet Format
#####################

**Note:** All multi-byte data field are big-endian

Message Packet Format Definition
********************************

GENERAL_BOARD_STATUS (0x001)
============================
Board status broadcast

+--------+---------+------------------------+----------------------+
| Byte 0 | Byte 1  | Byte 2-5               | Byte 6-7             |
+========+=========+========================+======================+
| 2 byte timestamp | GENERAL_ERROR_BITFIELD | BOARD_ERROR_BITFIELD |
+--------+---------+------------------------+----------------------+

| **GENERAL_ERROR_BITFIELD:** General error code bitfield, see `general_board_status`_
| **BOARD_ERROR_BITFIELD:** Board specific error code bitfield, see `board_specific_status`_

RESET_CMD (0x002)
=================
Command to reset boards

+--------+---------+---------------+---------------+
| Byte 0 | Byte 1  | Byte 2        | Byte 3        |
+========+=========+===============+===============+
| 2 byte timestamp | BOARD_TYPE_ID | BOARD_INST_ID |
+--------+---------+---------------+---------------+

| **BOARD_TYPE_ID:** Board Type ID of board to reset, set to 0 to reset all boards on bus
| **BOARD_INST_ID:** Board Inst ID of board to reset, set to 0 to reset all board of specific type

DEBUG_RAW (0x003)
=================
6-bytes of raw data

+--------+---------+----------+
| Byte 0 | Byte 1  | Byte 2-7 |
+========+=========+==========+
| 2 byte timestamp | RAW_DATA |
+--------+---------+----------+

| **RAW_DATA:** Raw data, 6 bytes

CONFIG_SET (0x004)
==================
Set board specific configuration

+--------+---------+---------------+---------------+-----------+--------------+
| Byte 0 | Byte 1  | Byte 2        | Byte 3        | Byte 4-5  | Byte 6-7     |
+========+=========+===============+===============+===========+==============+
| 2 byte timestamp | BOARD_TYPE_ID | BOARD_INST_ID | CONFIG_ID | CONFIG_VALUE |
+--------+---------+---------------+---------------+-----------+--------------+

| **BOARD_TYPE_ID:** Board Type ID of target board, cannot be zero
| **BOARD_INST_ID:** Board Inst ID of target board, set to 0 to set all board of specific type
| **CONFIG_ID:** Configuration ID, Board Specific
| **CONFIG_VALUE:** Configuration Value, Board and Config ID specific

CONFIG_STATUS (0x005)
=====================
Broadcast board specific configuration, for verify CONFIG_SET success

+--------+---------+-----------+--------------+
| Byte 0 | Byte 1  | Byte 2-3  | Byte 4-5     |
+========+=========+===========+==============+
| 2 byte timestamp | CONFIG_ID | CONFIG_VALUE |
+--------+---------+-----------+--------------+

| **CONFIG_ID:** Configuration ID, Board Specific
| **CONFIG_VALUE:** Configuration Value, Board and Config ID specific

ACTUATOR_CMD (0x006)
====================
Set actuator commanded state

+--------+---------+-------------+--------------------+
| Byte 0 | Byte 1  | Byte 2      | Byte 3             |
+========+=========+=============+====================+
| 2 byte timestamp | ACTUATOR_ID | ACTUATOR_CMD_STATE |
+--------+---------+-------------+--------------------+

| **ACTUATOR_ID:** Acturator ID, see `actuator_id`_
| **ACTUATOR_CMD_STATE:** Actuator Commanded State, see `actuator_state`_

ACTUATOR_ANALOG_CMD (0x007)
===========================
Analog Actuator Command

+--------+---------+-------------+---------------------------+
| Byte 0 | Byte 1  | Byte 2      | Byte 3-4                  |
+========+=========+=============+===========================+
| 2 byte timestamp | ACTUATOR_ID | ACTUATOR_ANALOG_CMD_STATE |
+--------+---------+-------------+---------------------------+

| **ACTUATOR_ID:** Acturator ID, see `actuator_id`_
| **ACTUATOR_ANALOG_CMD_STATE:** Actuator Analog Commanded State (16 bit analog, Definition Board/Actuator specific)

ACTUATOR_STATUS (0x008)
=======================
Actuator Status Message

+--------+---------+-------------+---------------------+--------------------+
| Byte 0 | Byte 1  | Byte 2      | Byte 3              | Byte 4             |
+========+=========+=============+=====================+====================+
| 2 byte timestamp | ACTUATOR_ID | ACTUATOR_CURR_STATE | ACTUATOR_CMD_STATE |
+--------+---------+-------------+---------------------+--------------------+

| **ACTUATOR_ID:** Acturator ID, see `actuator_id`_
| **ACTUATOR_CURR_STATE:** Actuator Current State, see `actuator_state`_
| **ACTUATOR_CMD_STATE:** Actuator Commanded State, see `actuator_state`_

ALT_ARM_CMD (0x009)
===================
Command to arm altimeter

+--------+---------+--------+---------------+
| Byte 0 | Byte 1  | Byte 2 | Byte 3        |
+========+=========+========+===============+
| 2 byte timestamp | ALT_ID | ALT_ARM_STATE |
+--------+---------+--------+---------------+

| **ALT_ID:** Altimeter ID, see `altimeter_id`_
| **ALT_ARM_STATE:** Altimeter set arm state, see `alt_arm_state`_

ALT_ARM_STATUS (0x00A)
======================
Altimeter Arm Status

+--------+---------+--------+---------------+----------+----------+
| Byte 0 | Byte 1  | Byte 2 | Byte 3        | Byte 4-5 | Byte 6-7 |
+========+=========+========+===============+==========+==========+
| 2 byte timestamp | ALT_ID | ALT_ARM_STATE | DROGUE_V | MAIN_V   |
+--------+---------+--------+---------------+----------+----------+

| **ALT_ID:** Altimeter ID, see `altimeter_id`_
| **ALT_ARM_STATE:** Altimeter current arm state, see `alt_arm_state`_
| **DROGUE_V:** Drogue Pyro Voltage
| **MAIN_V:** Main Pyro Voltage

SENSOR_TEMP (0x00B)
===================
Temperature Sensor

+--------+---------+----------------+----------+
| Byte 0 | Byte 1  | Byte 2         | Byte 3-6 |
+========+=========+================+==========+
| 2 byte timestamp | TEMP_SENSOR_ID | TEMP     |
+--------+---------+----------------+----------+

| **TEMP_SENSOR_ID:** Tempterature sensor ID
| **TEMP:** Temperature

SENSOR_ALTITUDE (0x00C)
=======================
Altimeter altitude sensor message(exclude GPS with have a specific message)

+--------+---------+----------+--------+
| Byte 0 | Byte 1  | Byte 2-5 | Byte 2 |
+========+=========+==========+========+
| 2 byte timestamp | ALT      | APOGEE |
+--------+---------+----------+--------+

| **ALT:** Altitude in ft
| **APOGEE:** Apogee detection status, see `apogee_state`_

SENSOR_IMU_X (0x00D)
====================
+--------+---------+--------+--------------+------------------+
| Byte 0 | Byte 1  | Byte 2 | Byte 3-4     | Byte 5-6         |
+========+=========+========+==============+==================+
| 2 byte timestamp | IMU_ID | LINEAR_ACCEL | ANGULAR_VELOCITY |
+--------+---------+--------+--------------+------------------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **LINEAR_ACCEL:** Linear Acceleration on X axis
| **ANGULAR_VELOCITY:** Angular Velocity around X axis

SENSOR_IMU_Y (0x00E)
====================
+--------+---------+--------+--------------+------------------+
| Byte 0 | Byte 1  | Byte 2 | Byte 3-4     | Byte 5-6         |
+========+=========+========+==============+==================+
| 2 byte timestamp | IMU_ID | LINEAR_ACCEL | ANGULAR_VELOCITY |
+--------+---------+--------+--------------+------------------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **LINEAR_ACCEL:** Linear Acceleration on Y axis
| **ANGULAR_VELOCITY:** Angular Velocity around Y axis

SENSOR_IMU_Z (0x00F)
====================
+--------+---------+--------+--------------+------------------+
| Byte 0 | Byte 1  | Byte 2 | Byte 3-4     | Byte 5-6         |
+========+=========+========+==============+==================+
| 2 byte timestamp | IMU_ID | LINEAR_ACCEL | ANGULAR_VELOCITY |
+--------+---------+--------+--------------+------------------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **LINEAR_ACCEL:** Linear Acceleration on Z axis
| **ANGULAR_VELOCITY:** Angular Velocity around Z axis

SENSOR_MAG_X (0x010)
====================
+--------+---------+--------+----------+
| Byte 0 | Byte 1  | Byte 2 | Byte 3-4 |
+========+=========+========+==========+
| 2 byte timestamp | IMU_ID | MAG      |
+--------+---------+--------+----------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **MAG:** magnetometer X value

SENSOR_MAG_Y (0x011)
====================
+--------+---------+--------+----------+
| Byte 0 | Byte 1  | Byte 2 | Byte 3-4 |
+========+=========+========+==========+
| 2 byte timestamp | IMU_ID | MAG      |
+--------+---------+--------+----------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **MAG:** magnetometer Y value

SENSOR_MAG_Z (0x012)
====================
+--------+---------+--------+----------+
| Byte 0 | Byte 1  | Byte 2 | Byte 3-4 |
+========+=========+========+==========+
| 2 byte timestamp | IMU_ID | MAG      |
+--------+---------+--------+----------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **MAG:** magnetometer Z value

SENSOR_BARO (0x013)
===================
+--------+---------+--------+----------+----------+
| Byte 0 | Byte 1  | Byte 2 | Byte 3-5 | Byte 6-7 |
+========+=========+========+==========+==========+
| 2 byte timestamp | IMU_ID | PRESSURE | TEMP     |
+--------+---------+--------+----------+----------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **PRESSURE:** barometer pressure reading, raw value
| **TEMP:** barometer temperature reading, raw value

SENSOR_ANALOG (0x014)
=====================
+--------+---------+-----------+----------+
| Byte 0 | Byte 1  | Byte 2    | Byte 3-4 |
+========+=========+===========+==========+
| 2 byte timestamp | SENSOR_ID | VALUE    |
+--------+---------+-----------+----------+

| **SENSOR_ID:** Sensor ID, see `analog_sensor_id`_
| **VALUE:** Analog sensor value

GPS_TIMESTAMP (0x015)
=====================
+--------+---------+-----------+-------------+-------------+--------------+
| Byte 0 | Byte 1  | Byte 2    | Byte 3      | Byte 4      | Byte 5       |
+========+=========+===========+=============+=============+==============+
| 2 byte timestamp | UTC_HOURS | UTC_MINUTES | UTC_SECONDS | UTC_DSECONDS |
+--------+---------+-----------+-------------+-------------+--------------+

| **UTC_HOURS:** Hour
| **UTC_MINUTES:** Minutes
| **UTC_SECONDS:** Seconds
| **UTC_DSECONDS:** Decisecond

GPS_LATITUDE (0x016)
====================
+--------+---------+---------+---------+------------+--------+
| Byte 0 | Byte 1  | Byte 2  | Byte 3  | Byte 4-5   | Byte 6 |
+========+=========+=========+=========+============+========+
| 2 byte timestamp | DEGREES | MINUTES | DMINUTES_H | DIR_NS |
+--------+---------+---------+---------+------------+--------+

| **DEGREES:** Degrees
| **MINUTES:** Minutes
| **DMINUTES_H:** No description
| **DIR_NS:** North/South

GPS_LONGITUDE (0x017)
=====================
+--------+---------+---------+---------+------------+--------+
| Byte 0 | Byte 1  | Byte 2  | Byte 3  | Byte 4-5   | Byte 6 |
+========+=========+=========+=========+============+========+
| 2 byte timestamp | DEGREES | MINUTES | DMINUTES_H | DIR_EW |
+--------+---------+---------+---------+------------+--------+

| **DEGREES:** Degrees
| **MINUTES:** Minutes
| **DMINUTES_H:** No description
| **DIR_EW:** East/West

GPS_ALTITUDE (0x018)
====================
+--------+---------+----------+--------+
| Byte 0 | Byte 1  | Byte 2-5 | Byte 2 |
+========+=========+==========+========+
| 2 byte timestamp | ALT      | DALT   |
+--------+---------+----------+--------+

| **ALT:** Altitude in ft
| **DALT:** No description

GPS_INFO (0x019)
================
+--------+---------+---------+---------+
| Byte 0 | Byte 1  | Byte 2  | Byte 3  |
+========+=========+=========+=========+
| 2 byte timestamp | NUM_SAT | QUALITY |
+--------+---------+---------+---------+

| **NUM_SAT:** Number of satellite
| **QUALITY:** Quality

STATE_EST_DATA (0x01A)
======================
+--------+---------+--------------+----------+
| Byte 0 | Byte 1  | Byte 2       | Byte 3-6 |
+========+=========+==============+==========+
| 2 byte timestamp | STATE_EST_ID | DATA     |
+--------+---------+--------------+----------+

| **STATE_EST_ID:** State ID, see `state_est_id`_
| **DATA:** State data (IEEE 754 floating point)

LEDS_ON (0x01B)
===============
LEDS_OFF (0x01C)
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
   * - 12V_RAIL_PAYLOAD
     - No Description
     - 0x07
   * - TELEMETRY
     - No Description
     - 0x08
   * - CAMERA_CANARD_A
     - No Description
     - 0x09
   * - CAMERA_CANARD_B
     - No Description
     - 0x0A
   * - CAMERA_RECOVERY
     - No Description
     - 0x0B
   * - CAMERA_PAYLOAD
     - No Description
     - 0x0C
   * - PROC_ESTIMATOR_INIT
     - Actuator command to start processor board state estimation
     - 0x0D
   * - SRAD_ALT_ESTIMATOR_INIT
     - Actuator command to start SRAD Altimeter state estimation
     - 0x0E
   * - SRAD_ALT_GPS_RESET
     - Actuator command to reset GPS Receiver on SRAD Altimeter
     - 0x0F
   * - CANARD_ENABLE
     - Power on Canard motor control board servo
     - 0x10
   * - CANARD_ANGLE
     - Canard Angle Command (from Processor board to Motor Control board)
     - 0x11
   * - PAYLOAD_MOTOR_ENABLE
     - Payload Servo Motor Power Control
     - 0x12
   * - PAYLOAD_LOGGING_ENABLE
     - Payload Sensor Board Logging Enable Control
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
   * - ROCKET_RAVEN
     - Raven4 Altimeter on Rocket (COTS)
     - 0x00
   * - ROCKET_STRATOLOGGER
     - StratoLoggerCF Altimeter on Rocket (COTS)
     - 0x01
   * - ROCKET_SRAD
     - SRAD Altimeter on Rocket
     - 0x02
   * - PAYLOAD_RAVEN
     - Raven4 Altimeter on Payload (COTS)
     - 0x03
   * - PAYLOAD_STRATOLOGGER
     - StratoLoggerCF Altimeter on Payload (COTS)
     - 0x04

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

imu_id
======

IMU Unique Indentifier

.. list-table:: imu_id Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - PROC_ALTIMU10
     - Polulo AltIMU-10 Connected to Processor Board
     - 0x00
   * - PROC_MTI630
     - Movella MTI-630 Connected to Processor Board
     - 0x01
   * - PROC_LSM6DSO32
     - ST LSM6DSO32 Soldered on Processor Board
     - 0x02
   * - SRAD_ALT_ALTIMU10
     - Polulo AltIMU-10 Connected to SRAD Altimeter
     - 0x03

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
   * - MOTOR_CURR
     - Motor current in mA
     - 0x08
   * - RADIO_CURR
     - Radio current in mA
     - 0x09
   * - GPS_CURR
     - GPS Receiver current in mA
     - 0x0A
   * - LOCAL_CURR
     - Local voltage rail (e.g. 3.3V) current in mA
     - 0x0B
   * - PT_CHANNEL_0
     - Pressure Transducer Channel 0, J3 on Injector Sensor Hub
     - 0x0C
   * - PT_CHANNEL_1
     - Pressure Transducer Channel 1, J4 on Injector Sensor Hub
     - 0x0D
   * - PT_CHANNEL_2
     - Pressure Transducer Channel 2, J6 on Injector Sensor Hub
     - 0x0E
   * - PT_CHANNEL_3
     - Pressure Transducer Channel 3, J8 on Injector Sensor Hub
     - 0x0F
   * - PT_CHANNEL_4
     - Pressure Transducer Channel 4, J10 on Injector Sensor Hub
     - 0x10
   * - HALL_CHANNEL_0
     - Hall-Effect Sensor Channel 0, J7 on Injector Sensor Hub
     - 0x11
   * - BARO_PRESSURE
     - Barometer pressure measurement
     - 0x12
   * - BARO_TEMP
     - Barometer temperature measurement
     - 0x13
   * - RA_BATT_VOLT_1
     - No Description
     - 0x14
   * - RA_BATT_VOLT_2
     - No Description
     - 0x15
   * - RA_BATT_CURR_1
     - No Description
     - 0x16
   * - RA_BATT_CURR_2
     - No Description
     - 0x17
   * - RA_MAG_VOLT_1
     - No Description
     - 0x18
   * - RA_MAG_VOLT_2
     - No Description
     - 0x19
   * - FPS
     - Camera framerate
     - 0x1A
   * - CANARD_ENCODER_1
     - No Description
     - 0x1B
   * - CANARD_ENCODER_2
     - No Description
     - 0x1C
   * - PROC_FLIGHT_PHASE_STATUS
     - No Description
     - 0x1D
   * - PAYLOAD_LIM_1
     - Payload Motor Board Limit Switch 1
     - 0x1E
   * - PAYLOAD_LIM_2
     - Payload Motor Board Limit Switch 2
     - 0x1F
   * - PAYLOAD_SERVO_DIRECTION
     - Payload Servo Direction
     - 0x20
   * - PAYLOAD_INFRARED
     - Payload Infrared Sensor Reading
     - 0x21
   * - HALL_CHANNEL_1
     - Hall-Effect Sensor Channel 1, J5 on Injector Sensor Hub
     - 0x22
   * - HALL_CHANNEL_2
     - Hall-Effect Sensor Channel 2, J9 on Injector Sensor Hub
     - 0x23

state_est_id
============

State Estimation data field indentifier

.. list-table:: state_est_id Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - ATT_Q0
     - No Description
     - 0x00
   * - ATT_Q1
     - No Description
     - 0x01
   * - ATT_Q2
     - No Description
     - 0x02
   * - ATT_Q3
     - No Description
     - 0x03
   * - RATE_WX
     - No Description
     - 0x04
   * - RATE_WY
     - No Description
     - 0x05
   * - RATE_WZ
     - No Description
     - 0x06
   * - VEL_VX
     - No Description
     - 0x07
   * - VEL_VY
     - No Description
     - 0x08
   * - VEL_VZ
     - No Description
     - 0x09
   * - ALT
     - No Description
     - 0x0A
   * - COEFF_CL
     - No Description
     - 0x0B
   * - CANARD_ANGLE
     - No Description
     - 0x0C

apogee_state
============

Apogee detection state

.. list-table:: apogee_state Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - UNKNOWN
     - No Description
     - 0x00
   * - NOT_REACHED
     - No Description
     - 0x01
   * - REACHED
     - No Description
     - 0x02

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

