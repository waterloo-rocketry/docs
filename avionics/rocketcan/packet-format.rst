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

+--------+---------+----------------------+
| Byte 0-1         | Byte 2-5             |
+========+=========+======================+
| 2 byte timestamp | BOARD_ERROR_BITFIELD |
+--------+---------+----------------------+

| **BOARD_ERROR_BITFIELD:** Board error code bitfield, see `board_error_bitfield`_

RESET_CMD (0x02)
=================
Command to reset boards

+--------+---------+----------------------+----------------------+
| Byte 0-1         | Byte 2               | Byte 3               |
+========+=========+======================+======================+
| 2 byte timestamp | TARGET_BOARD_TYPE_ID | TARGET_BOARD_INST_ID |
+--------+---------+----------------------+----------------------+

| **TARGET_BOARD_TYPE_ID:** Board Type ID of board to reset, set to 0 to reset all boards on bus
| **TARGET_BOARD_INST_ID:** Board Inst ID of board to reset, set to 0 to reset all board of specific type

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

+--------+---------+----------------------+----------------------+-----------+--------------+
| Byte 0-1         | Byte 2               | Byte 3               | Byte 4-5  | Byte 6-7     |
+========+=========+======================+======================+===========+==============+
| 2 byte timestamp | TARGET_BOARD_TYPE_ID | TARGET_BOARD_INST_ID | CONFIG_ID | CONFIG_VALUE |
+--------+---------+----------------------+----------------------+-----------+--------------+

| **TARGET_BOARD_TYPE_ID:** Board Type ID of target board, cannot be zero
| **TARGET_BOARD_INST_ID:** Board Inst ID of target board, set to 0 to set all board of specific type
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

+-------------+--------+---------+--------------------+---------------------+
| Metadata    | Byte 0-1         | Byte 2             | Byte 3              |
+=============+========+=========+====================+=====================+
| ACTUATOR_ID | 2 byte timestamp | ACTUATOR_CMD_STATE | ACTUATOR_CURR_STATE |
+-------------+--------+---------+--------------------+---------------------+

| **ACTUATOR_ID:** Acturator ID, see `actuator_id`_
| **ACTUATOR_CMD_STATE:** Actuator Commanded State, see `actuator_state`_
| **ACTUATOR_CURR_STATE:** Actuator Current State, see `actuator_state`_

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

SENSOR_2D_ANALOG24 (0x0C)
==========================
2-Dimensional 24-bit analog sensor value message

+-----------+--------+---------+----------+----------+
| Metadata  | Byte 0-1         | Byte 2-4 | Byte 5-7 |
+===========+========+=========+==========+==========+
| SENSOR_ID | 2 byte timestamp | VALUE_X  | VALUE_Y  |
+-----------+--------+---------+----------+----------+

| **SENSOR_ID:** 2 Dimensional sensor ID, see `dem_2d_sensor_id`_
| **VALUE_X:** Analog sensor value X
| **VALUE_Y:** Analog sensor value Y

SENSOR_3D_ANALOG16 (0x0D)
==========================
3-Dimensional 16-bit analog sensor value message

+-----------+--------+---------+----------+----------+----------+
| Metadata  | Byte 0-1         | Byte 2-3 | Byte 4-5 | Byte 6-7 |
+===========+========+=========+==========+==========+==========+
| SENSOR_ID | 2 byte timestamp | VALUE_X  | VALUE_Y  | VALUE_Z  |
+-----------+--------+---------+----------+----------+----------+

| **SENSOR_ID:** 3 Dimensional sensor ID, see `dem_3d_sensor_id`_
| **VALUE_X:** Analog sensor value X
| **VALUE_Y:** Analog sensor value Y
| **VALUE_Z:** Analog sensor value Z

GPS_TIMESTAMP (0x0E)
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

GPS_LATITUDE (0x0F)
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

GPS_LONGITUDE (0x10)
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

GPS_ALTITUDE (0x11)
====================
+--------+---------+----------+--------+
| Byte 0-1         | Byte 2-5 | Byte 6 |
+========+=========+==========+========+
| 2 byte timestamp | ALT      | DALT   |
+--------+---------+----------+--------+

| **ALT:** Altitude in ft
| **DALT:** No description

GPS_INFO (0x12)
================
+--------+---------+---------+---------+
| Byte 0-1         | Byte 2  | Byte 3  |
+========+=========+=========+=========+
| 2 byte timestamp | NUM_SAT | QUALITY |
+--------+---------+---------+---------+

| **NUM_SAT:** Number of satellite
| **QUALITY:** Quality

STREAM_STATUS (0x13)
=====================
+--------+---------+------------+----------+
| Byte 0-1         | Byte 2-4   | Byte 5-7 |
+========+=========+============+==========+
| 2 byte timestamp | TOTAL_SIZE | TX_SIZE  |
+--------+---------+------------+----------+

| **TOTAL_SIZE:** Total transfer size in bytes
| **TX_SIZE:** Transfered size in bytes

STREAM_DATA (0x14)
===================
+----------+--------+---------+----------+
| Metadata | Byte 0-1         | Byte 2-7 |
+==========+========+=========+==========+
| SEQ_ID   | 2 byte timestamp | DATA     |
+----------+--------+---------+----------+

| **SEQ_ID:** Sequence ID
| **DATA:** Data payload

STREAM_RETRY (0x15)
====================
TELEMETRY_INFO (0x16)
======================
+------------+--------+---------+--------+--------+
| Metadata   | Byte 0-1         | Byte 2 | Byte 3 |
+============+========+=========+========+========+
| CHANNEL_ID | 2 byte timestamp | LQI    | RSSI   |
+------------+--------+---------+--------+--------+

| **CHANNEL_ID:** Channel ID(Use LTT board instance ID)
| **LQI:** Link Quality Indicator
| **RSSI:** Received Signal Strength Indicator(2s complement signed)

TELEMETRY_STATE_SWITCH (0x17)
==============================
CANARD_FIRMWARE_ERROR (0x18)
=============================
+-----------+--------+---------+------------+----------+
| Metadata  | Byte 0-1         | Byte 2-5   | Byte 6   |
+===========+========+=========+============+==========+
| MODULE_ID | 2 byte timestamp | ERROR_CODE | SEVERITY |
+-----------+--------+---------+------------+----------+

| **MODULE_ID:** Module ID, see `canards_module_id`_
| **ERROR_CODE:** Error Code Bitfield, see `canards_module_error_bitfield`_
| **SEVERITY:** Severity, see `canards_health_severity`_

LEDS_ON (0x19)
===============
LEDS_OFF (0x20)
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
   * - IGNITION
     - Ignition Puck
     - 0x02
   * - ROCKET_UPPER_CHARGE_ENABLE
     - Rocket Upper Section Ground-side Charging Enable
     - 0x03
   * - ROCKET_INJECTOR_CHARGE_ENABLE
     - Rocket Injector Section Ground-side Charging Enable
     - 0x04
   * - 5V_RAIL_ROCKET
     - No Description
     - 0x05
   * - 12V_RAIL_ROCKET
     - No Description
     - 0x06
   * - TELEMETRY
     - No Description
     - 0x07
   * - CAMERA_SIDE_LOOKING_POWER
     - No Description
     - 0x08
   * - CAMERA_DOWN_LOOKING_POWER
     - No Description
     - 0x09
   * - CAMERA_RECOVERY_POWER
     - No Description
     - 0x0A
   * - CAMERA_SIDE_LOOKING_RECORD
     - No Description
     - 0x0B
   * - CAMERA_DOWN_LOOKING_RECORD
     - No Description
     - 0x0C
   * - CAMERA_RECOVERY_RECORD
     - No Description
     - 0x0D
   * - CANARD_PAD_FILTER
     - Switch Canard to Pad Filter when commanded ACT_STATE_ON
     - 0x0E
   * - CANARD_5V_OUTPUT
     - Enable Canard Board's 5V output to payload
     - 0x0F
   * - CANARD_LIPO_ON
     - Enable Canard board draw power from LiPo
     - 0x10
   * - SRAD_ALT_ESTIMATOR_INIT
     - Actuator command to start SRAD Altimeter state estimation
     - 0x11
   * - SRAD_ALT_GPS_RESET
     - Actuator command to reset GPS Receiver on SRAD Altimeter
     - 0x12
   * - CAMERA_CAPTURE
     - No Description
     - 0x13
   * - PAYLOAD_LOGGING_ENABLE
     - Payload Sensor Board Logging Enable Control
     - 0x14
   * - INJECTOR_BOARD_ACTUATOR_1
     - Injector board actuator channel 1
     - 0x15
   * - INJECTOR_BOARD_ACTUATOR_2
     - Injector board actuator channel 2
     - 0x16
   * - RLCS_RELAY_POWER
     - RLCS Relay Board Power Relay
     - 0x17
   * - RLCS_RELAY_SELECT
     - RLCS Relay Board Select Relay(Limit switch state feedback)
     - 0x18
   * - PAYLOAD_ACCEL_ARM
     - Payload accelerometer arming
     - 0x19
   * - PAYLOAD_PZT_ARM
     - Payload PZT phase biasing arming
     - 0x1A
   * - LOGGER_FLASH_ERASE
     - Erase logger board flash
     - 0x1B
   * - CANARD_FLASH_ERASE
     - Erase canard board flash
     - 0x1C
   * - CANARD_MOTOR_CALIBRATION
     - Start canard motor calibration routine
     - 0x1D
   * - LOGGER_SD_CLEAR
     - Clear logger board SD card
     - 0x1E
   * - CANARD_SD_CLEAR
     - Clear canard board SD card
     - 0x1F
   * - PAYLOAD_SD_CLEAR
     - Clear payload board SD card
     - 0x20

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
   * - ALTERNATE_BATT_VOLT
     - Secondary Battery Voltage in mV
     - 0x07
   * - BATT_CURR
     - Battery Current in mA
     - 0x08
   * - RADIO_CURR
     - Radio current in mA
     - 0x09
   * - GPS_CURR
     - GPS Receiver current in mA
     - 0x0A
   * - CAMERA_CURR
     - Camera current in mA
     - 0x0B
   * - LOCAL_RAIL_CURR
     - Local power rail (e.g. 3.3V) current in mA
     - 0x0C
   * - PT_CHANNEL_1
     - Pressure Transducer Channel 1
     - 0x0D
   * - PT_CHANNEL_2
     - Pressure Transducer Channel 2
     - 0x0E
   * - PT_CHANNEL_3
     - Pressure Transducer Channel 3
     - 0x0F
   * - PT_CHANNEL_4
     - Pressure Transducer Channel 4
     - 0x10
   * - PT_CHANNEL_5
     - Pressure Transducer Channel 5
     - 0x11
   * - PT_CHANNEL_6
     - Pressure Transducer Channel 6
     - 0x12
   * - PT_CHANNEL_7
     - Pressure Transducer Channel 7
     - 0x13
   * - PT_CHANNEL_8
     - Pressure Transducer Channel 8
     - 0x14
   * - PT_CHANNEL_9
     - Pressure Transducer Channel 9
     - 0x15
   * - PT_CHANNEL_10
     - Pressure Transducer Channel 10
     - 0x16
   * - HALL_CHANNEL_1
     - Hall-Effect Sensor Channel 1
     - 0x17
   * - HALL_CHANNEL_2
     - Hall-Effect Sensor Channel 2
     - 0x18
   * - HALL_CHANNEL_3
     - Hall-Effect Sensor Channel 3
     - 0x19
   * - RA_BATT_VOLT_1
     - No Description
     - 0x1A
   * - RA_BATT_VOLT_2
     - No Description
     - 0x1B
   * - RA_BATT_CURR_1
     - No Description
     - 0x1C
   * - RA_BATT_CURR_2
     - No Description
     - 0x1D
   * - RA_MAG_VOLT_1
     - No Description
     - 0x1E
   * - RA_MAG_VOLT_2
     - No Description
     - 0x1F
   * - FPS
     - Camera framerate
     - 0x20
   * - PAYLOAD_LIM_1
     - Payload Motor Board Limit Switch 1
     - 0x21
   * - PAYLOAD_LIM_2
     - Payload Motor Board Limit Switch 2
     - 0x22
   * - PAYLOAD_SERVO_DIRECTION
     - Payload Servo Direction
     - 0x23
   * - PAYLOAD_INFRARED
     - Payload Infrared Sensor Reading
     - 0x24
   * - INJECTOR_BOARD_TEMP_1
     - Injector board temperature channel 1
     - 0x25
   * - INJECTOR_BOARD_TEMP_2
     - Injector board temperature channel 2
     - 0x26
   * - INJECTOR_BOARD_TEMP_3
     - Injector board temperature channel 3
     - 0x27
   * - RLCS_RELAY_OUTPUT_VOLT_A
     - RLCS Relay Board channel A output voltage
     - 0x28
   * - RLCS_RELAY_OUTPUT_VOLT_B
     - RLCS Relay Board channel B output voltage
     - 0x29
   * - RLCS_RELAY_OUTPUT_CURR_A
     - RLCS Relay Board channel A output current
     - 0x2A
   * - RLCS_RELAY_OUTPUT_CURR_B
     - RLCS Relay Board channel B output current
     - 0x2B
   * - RLCS_RELAY_LIM_VOLT_A
     - RLCS Relay Board limit switch A voltage
     - 0x2C
   * - RLCS_RELAY_LIM_VOLT_B
     - RLCS Relay Board limit switch B voltage
     - 0x2D
   * - LOG_WRITTEN_SIZE
     - Number of bytes written to log file(reset to 0 when a new file is created)
     - 0x2E
   * - SD_LOG_FILE_NAME
     - SD Card log file name(the number part only)
     - 0x2F
   * - SD_USED
     - SD Card used space size, in MiB
     - 0x30
   * - SD_FREE
     - SD Card free space size, in MiB
     - 0x31
   * - FLASH_LOG_FILE_NAME
     - Flash log file name(the number part only)
     - 0x32
   * - FLASH_USED
     - Flash used space size, in MiB
     - 0x33
   * - FLASH_FREE
     - FLash free space size, in MiB
     - 0x34
   * - CANARD_CTRL_CMD_ANGLE
     - Canard Controller Commanded Angle
     - 0x35
   * - CANARD_CTRL_COEFF_LIFT
     - Canard Controller Coefficient of Lift
     - 0x36
   * - CANARD_MTI630_BARO_0
     - Canard MTI-630 Movella barometer reading 0
     - 0x37
   * - CANARD_MTI630_BARO_1
     - Canard MTI-630 Movella barometer reading 1
     - 0x38
   * - CANARD_MTI630_EST_ALT
     - Canard MTI-630 Movella Estimation altitude
     - 0x39
   * - CANARD_ADXRS649_GYRO
     - Canard ADXRS649 1-Axis Gyroscope angular velocity reading
     - 0x3A
   * - CANARD_SERVO_ANGLE
     - Canard Servo encoder angle reading
     - 0x3B
   * - CANARD_SERVO_CURR
     - Canard Servo current reading (in mA)
     - 0x3C
   * - CANARD_SERVO_TEMP
     - Canard Servo temperature reading (in Celcius)
     - 0x3D
   * - PAYLOAD_SENSOR_CURR_READING
     - Payload Sensor Current Reading
     - 0x3E
   * - ALTITUDE
     - Altitude in ft
     - 0x3F
   * - PAYLOAD_TEMP
     - Payload temperature
     - 0x40
   * - TC_0
     - TC 0
     - 0x41
   * - TC_1
     - TC 1
     - 0x42
   * - TC_2
     - TC 2
     - 0x43
   * - TC_3
     - TC 3
     - 0x44
   * - TC_4
     - TC 4
     - 0x45
   * - TC_5
     - TC 5
     - 0x46
   * - TC_6
     - TC 6
     - 0x47
   * - TC_7
     - TC 7
     - 0x48
   * - TC_8
     - TC 8
     - 0x49
   * - TC_9
     - TC 9
     - 0x4A
   * - TC_10
     - TC 10
     - 0x4B
   * - TC_11
     - TC 11
     - 0x4C
   * - TC_12
     - TC 12
     - 0x4D
   * - TC_13
     - TC 13
     - 0x4E
   * - TC_14
     - TC 14
     - 0x4F
   * - TC_15
     - TC 15
     - 0x50

dem_2d_sensor_id
================

2 Dimensional Sensor ID

.. list-table:: dem_2d_sensor_id Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - CANARD_NAV_VEL_ANGLE_VEL_X
     - Canard Navigation Velocity(X) and Angular Velocity(Y) on X-axis
     - 0x00
   * - CANARD_NAV_VEL_ANGLE_VEL_Y
     - Canard Navigation Velocity(X) and Angular Velocity(Y) on Y-axis
     - 0x01
   * - CANARD_NAV_VEL_ANGLE_VEL_Z
     - Canard Navigation Velocity(X) and Angular Velocity(Y) on Z-axis
     - 0x02
   * - CANARD_MS5611_BARO_TEMP
     - Canard MS5611 Barometer Pressure(X) and Temperature(Y) reading
     - 0x03
   * - CANARD_MTI630_EST_ORI_QW_QX
     - Canard MTI-630 Movella Estimation Orientation (Euler) - QW and QX demension
     - 0x04
   * - CANARD_MTI630_EST_ORI_QY_QZ
     - Canard MTI-630 Movella Estimation Orientation (Euler) - QY and QZ demension
     - 0x05

dem_3d_sensor_id
================

3 Dimensional Sensor ID

.. list-table:: dem_3d_sensor_id Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - CANARD_NAV_ORI_QX_QY_QZ
     - Canard Navigation Orientation QX, QY, QZ
     - 0x00
   * - CANARD_NAV_ORI_QW_ALT_VARNORM
     - Canard Navigation Orientation QW(X), Altitude(Y), Variance Norm(Z)
     - 0x01
   * - CANARD_LSM6DSV32X_ACCEL
     - Canard LSM6DSV32X 32G IMU Acceleration
     - 0x02
   * - CANARD_LSM6DSV32X_GYRO
     - Canard LSM6DSV32X 32G IMU Angular Velocity
     - 0x03
   * - CANARD_IIS2MDC_ACCEL
     - Canard IIS2MDC Compass Acceleration
     - 0x04
   * - CANARD_IIS2MDC_MAG
     - Canard IIS2MDC Magnetometer Reading
     - 0x05
   * - CANARD_MTI630_ACCEL
     - Canard MTI-630 Movella Acceleration
     - 0x06
   * - CANARD_MTI630_GYRO
     - Canard MTI-630 Movella Angular Velocity
     - 0x07
   * - CANARD_MTI630_MAG
     - Canard MTI-630 Movella Magnetometer Reading
     - 0x08
   * - RESERVED_0
     - Reserved 0
     - 0x09
   * - CANARD_MTI630_EST_ANGLE_VEL
     - Canard MTI-630 Movella Estimation Angular Velocity
     - 0x0A
   * - CANARD_MTI630_EST_VEL
     - Canard MTI-630 Movella Estimation Velocity
     - 0x0B
   * - CANARD_ADXL380_ACCEL
     - Canard ADXL380 Accelerometer Acceleration
     - 0x0C
   * - PAYLOAD_ACCEL_0
     - Payload Accelerometer 0
     - 0x0D
   * - PAYLOAD_ACCEL_1
     - Payload Accelerometer 1
     - 0x0E
   * - PAYLOAD_ACCEL_2
     - Payload Accelerometer 2
     - 0x0F
   * - PAYLOAD_ACCEL_3
     - Payload Accelerometer 3
     - 0x10
   * - PAYLOAD_ACCEL_4
     - Payload Accelerometer 4
     - 0x11
   * - PAYLOAD_ACCEL_5
     - Payload Accelerometer 5
     - 0x12
   * - PAYLOAD_ACCEL_6
     - Payload Accelerometer 6
     - 0x13
   * - PAYLOAD_ACCEL_7
     - Payload Accelerometer 7
     - 0x14

canards_health_severity
=======================

Canards Health Severity

.. list-table:: canards_health_severity Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - HEALTH_OK
     - No issues
     - 0x00
   * - HEALTH_ERROR
     - Something is wrong, but can still fly safely
     - 0x01
   * - HEALTH_FATAL
     - Unrecoverable failure, unsafe flight
     - 0x02

canards_module_id
=================

Canards Module ID

.. list-table:: canards_module_id Enum Values
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Description
     - ID
   * - ADC
     - No Description
     - 0x00
   * - ADXL380
     - No Description
     - 0x01
   * - ADXRS649
     - No Description
     - 0x02
   * - AK45
     - No Description
     - 0x03
   * - CAN_HANDLER
     - No Description
     - 0x04
   * - CONTROLLER
     - No Description
     - 0x05
   * - FLIGHT_PHASE
     - No Description
     - 0x06
   * - FSM
     - No Description
     - 0x07
   * - GPIO
     - No Description
     - 0x08
   * - I2C
     - No Description
     - 0x09
   * - IIS2MDC
     - No Description
     - 0x0A
   * - LOGGER
     - No Description
     - 0x0B
   * - LSM6DSV32X
     - No Description
     - 0x0C
   * - MOVELLA
     - No Description
     - 0x0D
   * - MS5611
     - No Description
     - 0x0E
   * - NAVIGATOR
     - No Description
     - 0x0F
   * - POWER_HANDLER
     - No Description
     - 0x10
   * - SD_CARD
     - No Description
     - 0x11
   * - SENSOR_HANDLER
     - No Description
     - 0x12
   * - TELEMETRY
     - No Description
     - 0x13
   * - TIMER
     - No Description
     - 0x14
   * - UART
     - No Description
     - 0x15

Bitfields Definition
*********************

board_error_bitfield
====================

Board error bitfield

.. list-table:: board_error_bitfield Bitfield bits
   :widths: 25 60 15
   :header-rows: 1

   * - Bitfield Name
     - Description
     - Offset
   * - 5V_OVER_CURR
     - No Description
     - 0x00
   * - 5V_OVER_VOLT
     - No Description
     - 0x01
   * - 5V_UNDER_VOLT
     - No Description
     - 0x02
   * - 12V_OVER_CURR
     - No Description
     - 0x03
   * - 12V_OVER_VOLT
     - No Description
     - 0x04
   * - 12V_UNDER_VOLT
     - No Description
     - 0x05
   * - BATT_OVER_CURR
     - No Description
     - 0x06
   * - BATT_OVER_VOLT
     - No Description
     - 0x07
   * - BATT_UNDER_VOLT
     - No Description
     - 0x08
   * - MOTOR_OVER_CURR
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
   * - 12V_EFUSE_FAULT
     - No Description
     - 0x0D
   * - 5V_EFUSE_FAULT
     - No Description
     - 0x0E
   * - PT_OUT_OF_RANGE
     - No Description
     - 0x0F
   * - CANARD_MODULE_FAILURE
     - Canard firmware application module error
     - 0x10
   * - LOCAL_RAIL_OVER_CURR
     - Local power rail (e.g. 3.3V) over current
     - 0x11
   * - CHARGE_RAIL_OVER_VOLT
     - Charge power rail over voltage
     - 0x12
   * - CHARGE_RAIL_OVER_CURR
     - Charge power rail over current
     - 0x13

canards_module_error_bitfield
=============================

Canards module_error bitfield

.. list-table:: canards_module_error_bitfield Bitfield bits
   :widths: 25 60 15
   :header-rows: 1

   * - Bitfield Name
     - Description
     - Offset
   * - BAT1_FAULT
     - Battery 1 fault
     - 0x00
   * - BAT2_FAULT
     - Battery 2 fault
     - 0x01
   * - DEVICE_FAULT
     - External device fault
     - 0x02
   * - FILE_SYSTEM
     - SD card or flash storage mount, read, or write operation failed
     - 0x03
   * - HARDWARE_FAIL
     - Hardware interface failed (GPIO, pin config, etc.)
     - 0x04
   * - LOW_POWER_MODE_WITH_EXT_5V_ON
     - Low-power mode active while external 5V is on
     - 0x05
   * - COMM_FAILURE
     - Communication protocol failure (I2C, SPI, UART, etc.)
     - 0x06
   * - CRC_FAILED
     - Integrity check failed
     - 0x07
   * - NO_DATA
     - Expected sensor data packet or control command frame is missing
     - 0x08
   * - RX_FAILURE
     - Error occurred during data reception on physical bus transceivers
     - 0x09
   * - TIMEOUT
     - Operation or sensor handshake exceeded its allocated time window
     - 0x0A
   * - TX_FAILURE
     - Transmit failure
     - 0x0B
   * - ERROR_STATE
     - FSM transitioned into an unhandled, invalid, or corrupted state
     - 0x0C
   * - FAILED_CALIBRATION
     - Calibration routine executed but failed
     - 0x0D
   * - NOT_CALIBRATED
     - Calibration did not execute
     - 0x0E
   * - LOOP_TIMING
     - Control loop period did not meet timing requirements
     - 0x0F
   * - NOT_INIT
     - Module, task, or driver was accessed before being initialized
     - 0x10
   * - OS
     - RTOS feature (queue, semaphore) failed
     - 0x11
   * - CODEGEN
     - Error occurred inside codegen
     - 0x12
   * - UNEXPECTED_EVENT
     - Attempted to trigger an illegal state transition event
     - 0x13
   * - INVALID_PARAM
     - Function argument passed with value outside of legal range
     - 0x14
   * - MATH
     - Floating-point exception, division by zero, or NaN in control algorithms
     - 0x15
   * - OUT_OF_BOUNDS
     - Data is out of range
     - 0x16
   * - OVERFLOW
     - Buffer, queue, or integer arithmetic register overflow
     - 0x17
   * - INTERNAL
     - General software assertion or unhandled catch-all logical exception
     - 0x18

