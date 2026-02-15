IMU Handler
===========

Assignee: Shiman

Purpose
-------
Handle IMU acquisition, validity/redundancy checks, failure detection, and provide validated inputs to the estimator.

Selected Requirements (examples)
--------------------------------
- FIRM-LLR-IMU-002: Sampling jitter < 5% of estimator period (tests TBD).
- FIRM-LLR-IMU-004: Validate acceleration magnitude vs. expected flight envelope.
- FIRM-LLR-IMU-005: Reject IMU data inconsistent with rigid-body dynamics.
- FIRM-LLR-IMU-012: One-way state transitions in flight if a sensor fails.
- FIRM-LLR-IMU-020: Each state transition emits a CAN message.
- FIRM-LLR-IMU-021: IMU acquisition uses DMA.
- FIRM-LLR-IMU-022: Data transfer does not block estimator execution.

Flow
----
1. Initialize (poll all IMUs to confirm initialization).
2. Read raw data.
3. Validate/correct; log health state.
4. Publish to estimator at its rate; log status to CAN each loop.

Changes for 2026
----------------
- Measure/log sampling jitter; assert in debug builds if desired.
- Switch acquisition to DMA; ensure frequency alignment with estimator.
- Implement physics validity checks (accel bounds, angular accel plausibility).
- Track and log per-sensor states.
