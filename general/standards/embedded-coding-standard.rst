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

Secure Coding Standard
**********************

We use ????? coding standard

Errors Handling
===============
All functions that have a possibility of failing should return a `rocketlib status code <https://github.com/waterloo-rocketry/rocketlib/blob/799ca8196b572062380c05ed9bdea1c1a9be4da1/include/common.h#L12>`_ unless the function is blatently trivial.
The status code must reflect the outcome of the function's execution.

Accordingly, callers should not ignore status codes returned by functions. Status codes should be read and handled appropriately.

Example:

.. code-block:: c

    w_status_t res = W_SUCCESS;             // Initialize status

    res |= i2c_init();                      // Capture status code into res

    uint8_t value = 0;                      // Return status code by passing the output value as a parameter instead
    res |= calculate_something(&value);     // Capture status code, and receive output value into the parameter

    // In this example we don't care about specific failures, only success or not success
    if (res == W_SUCCESS) {
        // Celebrate success
    } else {
        // Something failed!
    }
