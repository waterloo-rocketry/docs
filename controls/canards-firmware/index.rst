****************
Canards Firmware
****************

.. toctree::
   :maxdepth: 2

   development.rst
   modules/index

Prerequisite / Corequisite Reading
==================================

This page collects the links referenced at the top of the design document.

- Project proposals: `Controls <https://drive.google.com/drive/u/0/folders/19gl8aURkmgG0Qm3f0aXJBbHZXBfEQqw5>`_
- Top-level controls requirements: `2026 Controls Requirements <https://docs.google.com/spreadsheets/d/1JLKeAksTf0xKj0QCYFTEEwu3voSvOGnbUyV6GcdOs_8/edit?usp=drive_link>`_
- Firmware requirements: `2026 Controls Firmware Requirements <https://docs.google.com/spreadsheets/d/1B3ySHuVDmd2GWt3BVV5CLqYwFB5VyxrsIBiqm5Tm4xc/edit?usp=drive_link>`_
- Architecture diagram: `Firmware architecture (draw.io) <https://drive.google.com/file/d/1RLQA_6f2_7usm5ytfW0u7gmsRUmp29gt/view?usp=drive_link>`_

Useful resources for developers
--------------------------------
- `Firmware practical coding advice (processor board) <https://docs.google.com/document/d/1_ezajd09ty_aAKcIjkUv2QdzlUp1-3-NICnz4yqtmKI/edit#heading=h.cve18e50n4on>`_

Historical context (Canards 2025)
---------------------------------
- `Processor Board Firmware Design (2025) <https://docs.google.com/document/d/1OokvdQ8c74xzt_znfmBUrUzJ5vtqvndMz0l9xxN98dY/edit>`_
- `2025 – Canards Drive <https://drive.google.com/drive/u/0/folders/1iuZNrTtR7TAryeRXcraWjmycB-5Mf-rT>`_

Background
==========

Canards 2025 worked decently considering it was our first time flying canards (see retrospective). Unfortunately, some quality was sacrificed just to make it work. With fewer new features in 2026, we can strengthen the foundation for future controls projects. The one major change is merging the two 2025 boards into a single board.

Goals
=====

1. **Iterate** on the 2025 project to implement the new features required to make the Canard board work (peripheral control, controller, and estimator implementations).
2. **Improve development processes** (clearer requirements and FMEA usage, easier unit testing, etc.).
3. **Improve modules** from last year where possible (e.g., timing optimization).

Requirements
============

We loosely follow a DO-178C–style hierarchy. Team-wide requirements inform
`2026 Rocket Requirements <https://docs.google.com/spreadsheets/d/1t7zfE7QHRDbFQc56IHl4r6ZE58SATR9Tcd604797iHM/edit?usp=sharing>`_,
which in turn derive the
`2026 Controls Requirements <https://docs.google.com/spreadsheets/d/1JLKeAksTf0xKj0QCYFTEEwu3voSvOGnbUyV6GcdOs_8/edit#gid=0>`_
and the
`2026 Controls Firmware Requirements <https://docs.google.com/spreadsheets/d/1B3ySHuVDmd2GWt3BVV5CLqYwFB5VyxrsIBiqm5Tm4xc/edit#gid=1762808058>`_.

Scope
=====

Covers all firmware that runs on the Canard board. Testing procedures are out of scope (though testable interfaces are in scope). Algorithm design for controller/estimator is separate; this document focuses on the embedded C implementation.

System Overview
===============

The firmware runs on FreeRTOS. In this design, a *task* refers to a FreeRTOS task.

Modules and Layering
--------------------
- High-level architecture: `draw.io diagram <https://drive.google.com/file/d/1RLQA_6f2_7usm5ytfW0u7gmsRUmp29gt/view?usp=drivesdk>`_.
- Modules are organized in layers; each module should interact only with peers in its layer and modules in lower layers to abstract hardware and enable testing.
- Components are the internal building blocks of modules (e.g., tasks, small libraries).
- Note: Consider allowing device drivers (e.g., IMU) to own protocol usage (I²C/SPI/UART) to avoid overly generalized peripheral layers.

Interfaces and Interactions
---------------------------
- Public interfaces are the functions exposed in each module’s ``.h``. Inter-module interactions are the focus; internal static helpers are excluded.
- Logger and CAN provide public interfaces intended to be callable by multiple modules.

Data Flow
---------
- Visualize where inputs enter, how they are processed, and how outputs are produced. (Add diagram/link.)

Tasks and Timing
----------------
- Define a timing diagram to satisfy controller/estimator loop deadlines and clarify concurrency and data handoff.

DTEG (Design, Test & Evaluation Guide)
--------------------------------------
- The system must only actuate when permitted. The Flight Phase module determines safe actuation windows with redundancy; Controller and Motor Control must respect those windows.

Design Parameters
-----------------
- Centralize runtime constants (e.g., burn time, expected board current draw) in a single authoritative source (link to parameters sheet TBD).
  
Data Collection
===============

.. raw:: html

   <iframe src="https://docs.google.com/spreadsheets/d/1isjiDjAHeaFbIcemxMDZfsfbDFZSkMUr7OAtPzHfreU/edit?gid=0#gid=0" height="800px" width="100%"/>
