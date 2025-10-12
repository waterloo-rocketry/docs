*********************************
Setup clang-format and clang-tidy
*********************************

Introduction
============
*clang-format* is a tool for formatting source code of C-like languages including C, C++ and Java, it support user defined syntax rules. It's part of the LLVM compiler toolchain suite.

*clang-tidy* is a C/C++ `source code linting tool <https://en.wikipedia.org/wiki/Lint_(software)>`_, it checks for common coding errors.

On Waterloo Rocketry, we used those tools to format C firmware code and to enforce team C syntax rule. This tutorial is based on assumption that you have git bash setup in case of you are on Windows, because the shell(bash) is required for running shell scripts. We are currently using clang-format/tidy version 21.

Install clang-format and clang-tidy on Debian/Ubuntu Linux
==========================================================
Open a terminal and run `sudo apt install -y clang-format-21 clang-tidy-21`

Install clang-format and clang-tidy on Windows
==============================================
Go to `LLVM  GitHub release page <https://github.com/llvm/llvm-project/releases/>`_ , download latest LLVM 21 Windows release `LLVM-21.x.x-win64.exe`, run this installer.
In the LLVM install page, select "Add LLVM to the system PATH for all users", and select a location that you would like to install LLVM, and wait for installation to finish.

Install clang-format and clang-tidy on MacOS
============================================
Open a terminal and run `brew install clang-format@21`

Test the clang-format and clang-tidy installation
=================================================
Go to shell and type `clang-format --version`, the output should be `clang-format Version 21.x.x`, Which `x` is the minor version number. Type `clang-tidy --version`, the output should be `LLVM Version 21.x.x`, Which `x` is the minor version number. 

Running clang-format on a CAN firmware repository
=================================================
For PIC18 projects: Assuming the *rocketlib* git submodule is added to the root of the `cansw_*` git repository, run `./rocketlib/scripts/format-cansw.sh` to format code.
