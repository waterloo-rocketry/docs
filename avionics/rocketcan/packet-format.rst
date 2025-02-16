Packet Format
#####################

**Note:** All multi-byte data field are big-endian

Message Packet Format Definition
********************************

GENERAL_BOARD_STATUS (0x001)
============================
Board status broadcast

+--------+---------+----------------------+--------------------+
| Byte 0 | Byte 1  |Byte 2-5              |Byte 6-7            |
+========+=========+======================+====================+
| 2 byte timestamp |GENERAL_ERROR_BITFIELD|BOARD_ERROR_BITFIELD|
+--------+---------+----------------------+--------------------+

| **GENERAL_ERROR_BITFIELD:** General error code bitfield, see `general_board_status`_
| **BOARD_ERROR_BITFIELD:** Board specific error code bitfield

RESET_CMD (0x002)
=================
Command to reset boards

+--------+---------+-------------+-------------+
| Byte 0 | Byte 1  |Byte 2       |Byte 3       |
+========+=========+=============+=============+
| 2 byte timestamp |BOARD_TYPE_ID|BOARD_INST_ID|
+--------+---------+-------------+-------------+

| **BOARD_TYPE_ID:** Board Type ID of board to reset, set to 0 to reset all boards on bus
| **BOARD_INST_ID:** Board Inst ID of board to reset, set to 0 to reset all board of specific type

DEBUG_RAW (0x003)
=================
6-bytes of raw data

+--------+---------+--------+
| Byte 0 | Byte 1  |Byte 2-7|
+========+=========+========+
| 2 byte timestamp |RAW_DATA|
+--------+---------+--------+

| **RAW_DATA:** Raw data, 6 bytes

CONFIG_SET (0x004)
==================
Set board specific configuration

+--------+---------+---------+------------+
| Byte 0 | Byte 1  |Byte 2-3 |Byte 4-7    |
+========+=========+=========+============+
| 2 byte timestamp |CONFIG_ID|CONFIG_VALUE|
+--------+---------+---------+------------+

| **CONFIG_ID:** Configuration ID, Board Specific
| **CONFIG_VALUE:** Configuration Value, Board and Config ID specific

CONFIG_STATUS (0x005)
=====================
Broadcast board specific configuration, for verify CONFIG_SET success

+--------+---------+---------+------------+
| Byte 0 | Byte 1  |Byte 2-3 |Byte 4-7    |
+========+=========+=========+============+
| 2 byte timestamp |CONFIG_ID|CONFIG_VALUE|
+--------+---------+---------+------------+

| **CONFIG_ID:** Configuration ID, Board Specific
| **CONFIG_VALUE:** Configuration Value, Board and Config ID specific

ACTUATOR_CMD (0x006)
====================
Set actuator commanded state

+--------+---------+-----------+--------------+
| Byte 0 | Byte 1  |Byte 2     |Byte 3        |
+========+=========+===========+==============+
| 2 byte timestamp |ACTUATOR_ID|ACTUATOR_STATE|
+--------+---------+-----------+--------------+

| **ACTUATOR_ID:** Acturator ID, see `actuator_id`_
| **ACTUATOR_STATE:** Actuator State, see `actuator_state`_

ACTUATOR_ANALOG_CMD (0x007)
===========================
Analog Actuator Command

+--------+---------+-----------+---------------------+
| Byte 0 | Byte 1  |Byte 2     |Byte 3-4             |
+========+=========+===========+=====================+
| 2 byte timestamp |ACTUATOR_ID|ACTUATOR_ANALOG_STATE|
+--------+---------+-----------+---------------------+

| **ACTUATOR_ID:** Acturator ID, see `actuator_id`_
| **ACTUATOR_ANALOG_STATE:** Actuator State (16 bit analog, Board/Actuator specific)

ACTUATOR_STATUS (0x008)
=======================
Actuator Status Message

+--------+---------+-----------+-------------------+------------------+
| Byte 0 | Byte 1  |Byte 2     |Byte 3             |Byte 4            |
+========+=========+===========+===================+==================+
| 2 byte timestamp |ACTUATOR_ID|ACTUATOR_CURR_STATE|ACTUATOR_REQ_STATE|
+--------+---------+-----------+-------------------+------------------+

| **ACTUATOR_ID:** Acturator ID, see `actuator_id`_
| **ACTUATOR_CURR_STATE:** Actuator Current State, see `actuator_state`_
| **ACTUATOR_REQ_STATE:** Actuator Requested State, see `actuator_state`_

ALT_ARM_CMD (0x009)
===================
Command to arm altimeter

+--------+---------+------+-------------+
| Byte 0 | Byte 1  |Byte 2|Byte 3       |
+========+=========+======+=============+
| 2 byte timestamp |ALT_ID|ALT_ARM_STATE|
+--------+---------+------+-------------+

| **ALT_ID:** Altimeter ID, see `altimeter_id`_
| **ALT_ARM_STATE:** Altimeter set arm state, see `alt_arm_state`_

ALT_ARM_STATUS (0x00A)
======================
Altimeter Arm Status

+--------+---------+------+-------------+--------+--------+
| Byte 0 | Byte 1  |Byte 2|Byte 3       |Byte 4-5|Byte 6-7|
+========+=========+======+=============+========+========+
| 2 byte timestamp |ALT_ID|ALT_ARM_STATE|DROGUE_V|MAIN_V  |
+--------+---------+------+-------------+--------+--------+

| **ALT_ID:** Altimeter ID, see `altimeter_id`_
| **ALT_ARM_STATE:** Altimeter current arm state, see `alt_arm_state`_
| **DROGUE_V:** Drogue Pyro Voltage
| **MAIN_V:** Main Pyro Voltage

SENSOR_TEMP (0x00B)
===================
Temperature Sensor

+--------+---------+---------------+--------+
| Byte 0 | Byte 1  |Byte 2         |Byte 3-6|
+========+=========+===============+========+
| 2 byte timestamp |TEMP_SENSOR_NUM|TEMP    |
+--------+---------+---------------+--------+

| **TEMP_SENSOR_NUM:** Tempterature sensor ID
| **TEMP:** Temperature

SENSOR_ALTITUDE (0x00C)
=======================
Altitude sensor message(exclude GPS with have a specific message)

+--------+---------+--------+
| Byte 0 | Byte 1  |Byte 2-5|
+========+=========+========+
| 2 byte timestamp |ALT     |
+--------+---------+--------+

| **ALT:** Altitude in ft

SENSOR_IMU_X (0x00D)
====================
+--------+---------+------+------------+---------------+
| Byte 0 | Byte 1  |Byte 2|Byte 3-4    |Byte 5-6       |
+========+=========+======+============+===============+
| 2 byte timestamp |IMU_ID|LINEAR_ACCEL|ANGULAR_VELOITY|
+--------+---------+------+------------+---------------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **LINEAR_ACCEL:** Linear Acceleration on X axis
| **ANGULAR_VELOITY:** Angular Velocity around X axis

SENSOR_IMU_Y (0x00E)
====================
+--------+---------+------+------------+---------------+
| Byte 0 | Byte 1  |Byte 2|Byte 3-4    |Byte 5-6       |
+========+=========+======+============+===============+
| 2 byte timestamp |IMU_ID|LINEAR_ACCEL|ANGULAR_VELOITY|
+--------+---------+------+------------+---------------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **LINEAR_ACCEL:** Linear Acceleration on Y axis
| **ANGULAR_VELOITY:** Angular Velocity around Y axis

SENSOR_IMU_Z (0x00F)
====================
+--------+---------+------+------------+---------------+
| Byte 0 | Byte 1  |Byte 2|Byte 3-4    |Byte 5-6       |
+========+=========+======+============+===============+
| 2 byte timestamp |IMU_ID|LINEAR_ACCEL|ANGULAR_VELOITY|
+--------+---------+------+------------+---------------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **LINEAR_ACCEL:** Linear Acceleration on Z axis
| **ANGULAR_VELOITY:** Angular Velocity around Z axis

SENSOR_MAG_X (0x010)
====================
+--------+---------+------+--------+
| Byte 0 | Byte 1  |Byte 2|Byte 3-4|
+========+=========+======+========+
| 2 byte timestamp |IMU_ID|MAG     |
+--------+---------+------+--------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **MAG:** magnetometer X value

SENSOR_MAG_Y (0x011)
====================
+--------+---------+------+--------+
| Byte 0 | Byte 1  |Byte 2|Byte 3-4|
+========+=========+======+========+
| 2 byte timestamp |IMU_ID|MAG     |
+--------+---------+------+--------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **MAG:** magnetometer Y value

SENSOR_MAG_Z (0x012)
====================
+--------+---------+------+--------+
| Byte 0 | Byte 1  |Byte 2|Byte 3-4|
+========+=========+======+========+
| 2 byte timestamp |IMU_ID|MAG     |
+--------+---------+------+--------+

| **IMU_ID:** IMU Unique Indentifier, see `imu_id`_
| **MAG:** magnetometer Z value

SENSOR_ANALOG (0x013)
=====================
+--------+---------+---------+--------+
| Byte 0 | Byte 1  |Byte 2   |Byte 3-4|
+========+=========+=========+========+
| 2 byte timestamp |SENSOR_ID|VALUE   |
+--------+---------+---------+--------+

| **SENSOR_ID:** Sensor ID, see `analog_sensor_id`_
| **VALUE:** Analog sensor value

GPS_TIMESTAMP (0x014)
=====================
+--------+---------+---------+-----------+-----------+------------+
| Byte 0 | Byte 1  |Byte 2   |Byte 3     |Byte 4     |Byte 5      |
+========+=========+=========+===========+===========+============+
| 2 byte timestamp |UTC_HOURS|UTC_MINUTES|UTC_SECONDS|UTC_DSECONDS|
+--------+---------+---------+-----------+-----------+------------+

| **UTC_HOURS:** Hour
| **UTC_MINUTES:** Minutes
| **UTC_SECONDS:** Seconds
| **UTC_DSECONDS:** Decisecond

GPS_LATITUDE (0x015)
====================
+--------+---------+-------+-------+----------+------+
| Byte 0 | Byte 1  |Byte 2 |Byte 3 |Byte 4-5  |Byte 6|
+========+=========+=======+=======+==========+======+
| 2 byte timestamp |DEGREES|MINUTES|DMINUTES_H|DIR_NS|
+--------+---------+-------+-------+----------+------+

| **DEGREES:** Degrees
| **MINUTES:** Minutes
| **DMINUTES_H:** No description
| **DIR_NS:** North/South

GPS_LONGITUDE (0x016)
=====================
+--------+---------+-------+-------+----------+------+
| Byte 0 | Byte 1  |Byte 2 |Byte 3 |Byte 4-5  |Byte 6|
+========+=========+=======+=======+==========+======+
| 2 byte timestamp |DEGREES|MINUTES|DMINUTES_H|DIR_EW|
+--------+---------+-------+-------+----------+------+

| **DEGREES:** Degrees
| **MINUTES:** Minutes
| **DMINUTES_H:** No description
| **DIR_EW:** East/West

GPS_ALTITUDE (0x017)
====================
+--------+---------+--------+------+
| Byte 0 | Byte 1  |Byte 2-5|Byte 2|
+========+=========+========+======+
| 2 byte timestamp |ALT     |DALT  |
+--------+---------+--------+------+

| **ALT:** Altitude in ft
| **DALT:** No description

GPS_INFO (0x018)
================
+--------+---------+-------+-------+
| Byte 0 | Byte 1  |Byte 2 |Byte 3 |
+========+=========+=======+=======+
| 2 byte timestamp |NUM_SAT|QUALITY|
+--------+---------+-------+-------+

| **NUM_SAT:** Number of satellite
| **QUALITY:** Quality

STATE_EST_DATA (0x019)
======================
+--------+---------+------------+--------+
| Byte 0 | Byte 1  |Byte 2      |Byte 3-6|
+========+=========+============+========+
| 2 byte timestamp |STATE_EST_ID|DATA    |
+--------+---------+------------+--------+

| **STATE_EST_ID:** State ID, see `state_est_id`_
| **DATA:** State data

LEDS_ON (0x01A)
===============
LEDS_OFF (0x01B)
================
Enums Definition
****************

general_board_status
====================

General board status bitfield

.. list-table:: general_board_status Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - NOMINAL
     - No Description
     - 0x00
   * - 5V_OVER_CURRENT
     - No Description
     - 0x01
   * - 5V_OVER_VOLTAGE
     - No Description
     - 0x02
   * - 5V_UNDER_VOLTAGE
     - No Description
     - 0x04
   * - 12V_OVER_CURRENT
     - No Description
     - 0x08
   * - 12V_OVER_VOLTAGE
     - No Description
     - 0x10
   * - 12V_UNDER_VOLTAGE
     - No Description
     - 0x20
   * - IO_ERROR
     - No Description
     - 0x40
   * - FS_ERROR
     - No Description
     - 0x80

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
   * - CHARGE_ENABLE
     - Ground side charging board charging enable
     - 0x02
   * - 5V_RAIL_ROCKET
     - No Description
     - 0x03
   * - 5V_RAIL_PAYLOAD
     - No Description
     - 0x04
   * - TELEMETRY
     - No Description
     - 0x05
   * - CAMERA_INJ_A
     - No Description
     - 0x06
   * - CAMERA_INJ_B
     - No Description
     - 0x07
   * - CAMERA_VENT_A
     - No Description
     - 0x08
   * - CAMERA_VENT_B
     - No Description
     - 0x09
   * - CAMERA_VENT_C
     - No Description
     - 0x0A
   * - CAMERA_VENT_D
     - No Description
     - 0x0B
   * - CAMERA_RECOVERY
     - No Description
     - 0x0C
   * - PROC_ESTIMATOR_INIT
     - Actuator command to start processor board state estimation
     - 0x0D
   * - CANARD_ENABLE
     - Power on Canard motor control board servo
     - 0x0E
   * - CANARD_ANGLE
     - Canard Angle Command (from Processor board to Motor Control board)
     - 0x0F

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
     - Raven4 Altimeter (COTS)
     - 0x00
   * - STRATOLOGGER
     - StratoLoggerCF Altimeter (COTS)
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

imu_id
======

IMU Unique Indentifier

.. list-table:: imu_id Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - PROC_POLULU_ALTIMU10
     - Polulo AltIMU-10 Connected to Processor Board
     - 0x00
   * - PROC_MOVELLA_MTI630
     - Movella MTI-630 Connected to Processor Board
     - 0x01
   * - PROC_ST
     - ST LSM6DSO32 Soldered on Processor Board
     - 0x02
   * - SRAD_ALT_POLULU_ALTIMU10
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
   * - PRESSURE_OX
     - Oxidizer Tank pressure in psi
     - 0x09
   * - PRESSURE_FUEL
     - Fuel Tank pressure in psi
     - 0x0A
   * - PRESSURE_CC
     - Combustion Chamber pressure in psi
     - 0x0B
   * - BARO_PRESSURE
     - Barometer pressure measurement
     - 0x0C
   * - BARO_TEMP
     - Barometer temperature measurement
     - 0x0D
   * - RA_BATT_VOLT_1
     - No Description
     - 0x0E
   * - RA_BATT_VOLT_2
     - No Description
     - 0x0F
   * - RA_BATT_CURR_1
     - No Description
     - 0x10
   * - RA_BATT_CURR_2
     - No Description
     - 0x11
   * - RA_MAG_VOLT_1
     - No Description
     - 0x12
   * - RA_MAG_VOLT_2
     - No Description
     - 0x13
   * - FPS
     - Camera framerate
     - 0x14
   * - CANARD_ENCODER_1
     - No Description
     - 0x15
   * - CANARD_ENCODER_2
     - No Description
     - 0x16
   * - PROC_FLIGHT_PHASE_STATUS
     - No Description
     - 0x17

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

