Setup Clang Format
==================

Introduction
------------
*clang-format* is a tool for formatting source code of C-like languages including C, C++ and Java, it support user defined syntax rules. It's part of the LLVM compiler toolchain suite. On Waterloo Rocketry, we used this tool for format C firmware code, to enforce team C syntax rule. This tutorial is based on assumption that you have git bash setup in case of you are on Windows, because the shell(bash) is required for running shell scripts. We are currently using clang-format version 17.

Install Clang-format on Debian/Ubuntu Linux
-------------------------------------------
Open a terminal and run `sudo apt install clang-format-17`.

Install Clang-format on Windows
-------------------------------
Go to `LLVM 17.0.6 GitHub release page <https://github.com/llvm/llvm-project/releases/tag/llvmorg-17.0.6>`_ , download `LLVM-17.0.6-win64.exe`, run this installer.
In the LLVM install page, select "Add LLVM to the system PATH for all users", and select a location that you would like to install LLVM, and wait for installation to finish.

Install Clang-format on MacOS
-----------------------------
Coming soon

Test the Clang-format installation
----------------------------------
Go to shell and type `clang-format-17 --version`, the output should be `clang-format Version 17.x.x`, Which `x` is the minor version number.

Running clang-format on a CAN firmware repository
-------------------------------------------------
Assuming the *rocketlib* git submodule is added to the root of the `cansw_*` git repository, run `cd rocketlib/scripts` to change current directory to the rocketlib scripts directory, then run `./format.sh` to format firmware code. Then all cansw and rocketlib code should be formatted, but not mcc_generated_files and canlib.
