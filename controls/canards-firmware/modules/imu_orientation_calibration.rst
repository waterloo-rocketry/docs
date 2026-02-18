IMU Orientation Calibration
===========================

Goal
----
Align all IMUs to a common board/rocket frame to correct for mounting misalignment.

Procedure (Sketch)
------------------
1. Use a machined square baseplate with orthogonal faces.
2. Mount the board and sensors carefully.
3. Place the assembly on a precisely horizontal table.
4. Collect accel data with low-pass filtering; when flat, only the vertical axis should read ~9.81 m/s²; others ~0.
5. Repeat for all orthogonal faces.
6. Compute per-sensor rotation matrices.
7. Store calibration constants in on-board flash and archive externally.
8. Recalibrate whenever sensors/board are moved or replaced.

References
----------
- `ArduPilot: Accelerometer calibration <https://ardupilot.org/copter/docs/common-accelerometer-calibration.html>`_
