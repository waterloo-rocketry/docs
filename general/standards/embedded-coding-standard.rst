Embedded (Firmware) Coding Standard
######################################

Coding Style
*************

Use snake case for variable and function name (snake_case)
100 character max per line
Use const and #define instead of magic numbers

Include Order
===============
* C Standard Library (e.g. <stdint.h>)
* Platform specific system header (e.g. <xc.h>)
* Project local header file (e.g. "imu.h")

Include Guards
===============

For most firmware:

.. code-block:: c

	#ifndef _FILENAME_H
	#define _FILENAME_H

	/* Your code here */
	
	#endif

For firmware libraries:

.. code-block:: c

	#ifndef _LIBRARY_FILENAME_H
	#define _LIBRARY_FILENAME_H

	/* Your code here */
	
	#endif
	
Formatting
===============
Just use `team-wide clang-format config <https://github.com/waterloo-rocketry/rocketlib/blob/master/.clang-format>`_

Embedded Coding Standard
***************************
All firmware projects should adopt the `BARR Embedded C Coding Standard <https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard>`_.

    A C coding standard is a set of rules for source code that is adopted by a team of programmers working together on a project, such as the design of an embedded system.
    
    Barr Group's Embedded C Coding Standard was developed to minimize bugs in firmware by focusing on practical rules that keep bugs out--while also improving the maintainability and portability of embedded software

The goal of adopting this standard team-wide is to improve firmware consistency and reliability as a team. 

Enforcement
=============
The BARR standard indicates how each rule should be enforced - by static code analysis, code reviews, etc.

It is the responsibility of any team member reviewing code to be aware of this standard and make
a best effort to enforce the rules.

Static analysis is WIP (as of nov 2024). Likely will be using clang-tidy.

Style rules are enforced by the team-wide clang-format.

Rationale
==========
A number of other embedded coding standards were considered, including MISRA, JPL, and CERT.
BARR was chosen due to its open availability, and having a general focus appropriate for all our projects.
MISRA is overkill for most of our projects, while CERT focuses on IoT projects.

Rocketlib
**********
Rocketlib aims to standarize common modules for team-wide use.
All firmware projects should add rocketlib as a submodule and use the modules it provides
where appropriate (avoid reinventing the wheel).

Safe function usage
===================
Safe C function that explicitly set output buffer size should be used, to prevent buffer overflow, for example :code:`snprintf` should be used over :code:`sprintf`, .

Error Handling
===============
All functions that have a possibility of failing should return a `rocketlib status code <https://github.com/waterloo-rocketry/rocketlib/blob/799ca8196b572062380c05ed9bdea1c1a9be4da1/include/common.h#L12>`_ unless the function is blatently trivial.
The status code must reflect the outcome of the function's execution.

Accordingly, callers should not ignore status codes returned by functions. Status codes should be read and handled appropriately.

Example:

.. code-block:: c

    w_status_t res = W_SUCCESS; // Initialize status

    res |= i2c_init(); // Capture status code into res

    uint8_t value = 0; // Return status code by passing the output value as a parameter instead
    res |= calculate_something(&value); // Capture status code, and receive output value into the parameter

    // In this example we don't care about specific failures, only success or not success
    if (res == W_SUCCESS) {
        // Celebrate success
    } else {
        // Something failed!
    }
