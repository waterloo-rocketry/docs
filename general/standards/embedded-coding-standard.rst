Embedded (Firmware) Coding Standard
***********************************

Coding Style
============

Use snake case for variable and function name (snake_case)
100 character max per line
Use const and #define instead of magic number

Include Order
-------------
* C Standard Library (e.g. <stdint.h>)
* Platform specific system header (e.g. <xc.h>)
* Project local header file (e.g. "imu.h")

Include Guards
--------------

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
----------
Just use `team-wide clang-format config <https://github.com/waterloo-rocketry/rocketlib/blob/master/.clang-format>`_


