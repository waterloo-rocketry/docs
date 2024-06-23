# Firmware Tutorial

## Prerequisites
- An assembled copy of the 2022 electrical tutorial board.
  > Note: Due to supply chain issues we had to go with a different microcontroller than was originally intended so the potentiometer isn’t usable for analog input without doing some complex bodges. Thus, it is optional for the purposes of this tutorial.

- A basic understanding of KiCad.
- The KiCad files for the 2022 tutorial board.
- A basic understanding of C.

## Required Software
We use the MPLAB X IDE and the XC8 and XC16 compilers from Microchip. Having a recent (3.8+) version of Python installed is also useful, but won’t be necessary for this tutorial.

## MPLAB is Awful
1. So, let’s use it to create a project! First, open the MPLAB IDE and create a project (File → New Project).

2. Leave the default of Microchip Embedded Standalone Project.

3. Under “Device”, input the name of the microcontroller we are writing this code for. Leave “Tool” as “No Tool” for now.
    > Tip: You can find this in KiCad. Typically when writing firmware it will be much easier to read things like part numbers and pinouts from the schematic as opposed to the PCB. Open up the schematic now and leave it open, we’ll need it later.

4. Select the version of XC8 that you have installed.

5. Give the project a name and hit the browse button to find a place to store it. Leave encoding alone.
    > Tip: Unless you check “Use project location as the project folder”, MPLAB will create a new folder (with the project’s name) and put it inside the location you selected. This can be fine, it just depends on what you want.

6. We now have a very barebones project. As you can see from the file browser on the left, there isn’t even a main.c!

## Power on, one
1. The first sign of life on any board is a heartbeat. Specifically, a blinking LED heartbeat. Let’s do that.

2. Add a `main.c` by adding a new file (File → New File) and under the “Microchip Embedded / XC8 Compiler” folder selecting `main.c`. Make sure to set the file name to `main`.
