********************************************************
How-To: Develop canlib and rocketlib
********************************************************

Note Linting and Formatting depends on clang-format and clang-tidy, :doc:`instructions to install those tools</standards-tutorials/firmware/clang-format-tidy>` .

Linting
=======

Linting is code quality static analysis, run with:

.. code-block::

   make lint

Formatting
==========

Formatting is for ensure code has consistant style, like white spaces, run with:

.. code-block::

   make format

Running unit test
=================

Unit tests actually tests code functionality, run with:

.. code-block::

   make run-test
