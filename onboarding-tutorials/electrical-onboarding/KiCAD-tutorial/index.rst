KiCAD Tutorial
=================

This is a very basic introduction to KiCAD using the Fall 2022 tutorial (which is based off the Fall 2020 tutorial). You
will learn basic schematic design as well as PCB layout techniques.

 .. note:: This tutorial is being revised and a new tutorial board is in the works for 2025

Prerequisites
-------------
- Very basic understanding of circuitry concepts (voltage, current, resistance) and components (resistors, capacitors, IC's)

Introduction
------------
In this tutorial, we will be taking a deep dive into Waterloo Rocketry’s Electrical Design Automation Software of choice, **KiCad**. We will be covering all the steps that you will need to go through to design a board from scratch, from drawing the electrical schematics to laying out the PCB design. There is a lot to cover, and I highly recommend that you get through this tutorial in multiple steps and take breaks in between to digest what you’ve learned. I’ve put a lot more information on here than the base knowledge that you would need to build a board in this program, such as background information about the PCB design process and helpful shortcuts, but I hope that the extra content will allow you to get up and going much more quickly. If you just want to get things done, I’ve written this tutorial in a way that is easily skimmable, with key words bolded throughout.
The board you will be creating in this tutorial is a simple programmable PCB powered by a PIC microcontroller. It is equipped with a buzzer, two LEDs, a switch, a potentiometer, and a programming header. Power will be supplied through a screw terminal. Additionally, the board is compact enough to be used as a keychain – a hole exists on the board just for that purpose. Here’s the reference board, created by our benevolent electrical overlord `Jack Christensen`, that we will be using to help guide the creation process:
    .. image:: ../tutorial-board.png
