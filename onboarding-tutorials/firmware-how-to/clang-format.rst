Setup Clang Format
==================

Introduction
------------
*clang-format* is a tool for formatting source code of C-like languages including C, C++ and Java, it support user defined syntax rules. It's part of the LLVM compiler toolchain suite. On Waterloo Rocketry, we used this tool for format C firmware code, to enforce team C syntax rule. This tutorial is based on assumption that you have git bash setup in case of you are on Windows, because the shell(bash) is required for running shell scripts. We are currently using clang-format version 19.

Install Clang-format on Debian/Ubuntu Linux
-------------------------------------------
Open a terminal and run `sudo apt install clang-format-19`.

Install Clang-format on Windows
-------------------------------
Go to `LLVM  GitHub release page <https://github.com/llvm/llvm-project/releases/>`_ , download latest LLVM 19 Windows release `LLVM-19.x.x-win64.exe`, run this installer.
In the LLVM install page, select "Add LLVM to the system PATH for all users", and select a location that you would like to install LLVM, and wait for installation to finish.

Install Clang-format on MacOS
-----------------------------
Coming soon

Test the Clang-format installation
----------------------------------
Go to shell and type `clang-format --version`, the output should be `clang-format Version 19.x.x`, Which `x` is the minor version number.

Running clang-format on a CAN firmware repository
-------------------------------------------------
For PIC18 projects: Assuming the *rocketlib* git submodule is added to the root of the `cansw_*` git repository, run `./rocketlib/scripts/format-cansw.sh` to format code.
