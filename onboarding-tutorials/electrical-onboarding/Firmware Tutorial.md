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
    > **Tip**: You can find this in KiCad. Typically when writing firmware it will be much easier to read things like part numbers and pinouts from the schematic as opposed to the PCB. Open up the schematic now and leave it open, we’ll need it later.

4. Select the version of XC8 that you have installed.

5. Give the project a name and hit the browse button to find a place to store it. Leave encoding alone.
    > **Tip**: Unless you check “Use project location as the project folder”, MPLAB will create a new folder (with the project’s name) and put it inside the location you selected. This can be fine, it just depends on what you want.

6. We now have a very barebones project. As you can see from the file browser on the left, there isn’t even a main.c!

## Power on, one
1. The first sign of life on any board is a heartbeat. Specifically, a blinking LED heartbeat. Let’s do that.

2. Add a `main.c` by adding a new file (File → New File) and under the “Microchip Embedded / XC8 Compiler” folder selecting `main.c`. Make sure to set the file name to `main`.

3. With PIC microcontrollers, we control everything by reading from and writing to special named registers. These registers do everything from turning on and off output pins to configuring complicated peripherals like a CAN bus.
Let's blink the red LED, which we can see on the schematic is connected to pin `RA1/ICSPCLK`. First, we need to tell the PIC that we want to use that pin (referred to as `RA1`) as a digital output. We do that by writing to the `TRISA1` register inside our main function:

```c
TRISA1 = 0; // Set A1 to be an output
```
Now that the pin is set as an output, we can turn the LED on or off by writing a 1 or a 0 to the `LATA1` register. Try to make a while loop that will blink the LED on and off forever!
> **Tip**: An easy way of adding a delay is to busyloop. Try using a for loop that does nothing 1000 times as a delay.

4. Lastly, we need to insert a magic line that unfortunately is necessary for everything to work. Put the following above your main function:

```c
#pragma config FOSC = INTOSC
```
This tells the PIC that it should use its internal oscillator as its clock, which is how it knows when to run the next instruction in your code. For some godforsaken reason the default is to use an external oscillator, which, as you may have noticed, doesn’t exist on the tutorial board.

5. Now, time to test your code! Please call someone who knows how to program PICs over, there are just too many things that can go wrong here to explain them all in this guide.

## Read the Datasheet

1. Congratulations on your first PIC program! Now, lets dive a little deeper and explain how I came up with the magic registers you needed to set to make that work.

2. Starting with the schematic, recall that the LED is connected to the pin labeled `RA1/ICSPCLK`. The `/` means the pin has two functions, it is both `RA1` (the normal name for it) and `ICSPCLK` (a special pin used to program the PIC). Since `ICSPCLK` is only used for programming, we can ignore it and just treat the pin as `RA1`.  
   Let’s break down what `RA1` means. The `R` can be ignored, it just differentiates this pin from something like a power pin (`VDD` or `VSS`). The `A1` means that this is pin 1 of port A. When we start to deal with PICs that have more pins, there will be more ports (typically A, B and C), each of which has (typically 8) numbered pins. Now, how do we control this pin?

3. To learn how to do this, we will need to turn to ***The Datasheet***. To find it, go to the product page for the specific PIC we are using (in this case [here](https://www.microchip.com/en-us/product/PIC12F1501)) and click the “Download Data Sheet” link. ***The Datasheet*** is a very long document that details every bit of functionality on the PIC. If there is something you want to know, it is almost certainly somewhere in ***The Datasheet***. In our case, somewhere is chapter 11.0, “IO Ports” (page 95).

4. Now, unfortunately the writing of ***The Datasheet*** isn’t the most beginner friendly. However, on the first page we can see that they call the `LATx` registers “output latch” and talk about writing to them, so we can guess that setting `LATx` is how we control digital outputs.  
   **Tip:** The lowercase `x` is a common pattern to notice in PIC datasheets, it means that you should substitute something (a pin number for example) into the name.

5. If we keep reading the first page we get some more general overview and important warnings (which we will need later) and come to a nice diagram which confirms our guess about writing to `LATx` (or in fact to `PORTx`) being how we get data from the “Data bus” into the “Data Register”. We can also see that there is a buffer labeled `TRISx` between the “Data Register” and the “I/O Pin”, this is a good clue. Continuing to read we can skip the next page about alternate pin function and our assumptions are confirmed by the first paragraph on page 97! “Clearing a TRISA bit (= 0) will make the corresponding PORTA pin an output.” This gives us everything we needed earlier: setting the pin to an output by setting `TRISA1` to 0 and controlling the pin’s valve by setting `LATA1`.

6. Now, you might wonder how I knew to substitute `A1` into `TRISx` and `LATx`. If you scroll down to the next page in ***The Datasheet*** you will get to the “Register Definitions” section. You will find a register definitions section after every section in ***The Datasheet***, and it tells you every single bit of every single register associated with that section. Taking a look at “Register 11-3: TRISA” we can see that each bit in the register (corresponding to a specific pin) is labeled, and explained below. We can then refer to those labels in our code, like we just did.

7. Remember how we saw that we could have written to `PORTx` instead of `LATx`? Use the register definitions and make you code also blink the green LED, this time via the `PORTA` register. Upload your code to the board to test it.

## Yo, fuck ANSEL

1. Now let’s try to turn an LED on and off in response to the button! We’ve already got the LED control sorted, so all we need to do is to figure out how to read the digital value of the button pin! If you feel confident, ***The Datasheet*** sections we just went over contain all the information you need to get this working. However, there are a few subtle tripping points I’ll point out below.

2. Right off the bat, we need to know which register we should be reading from. Read through the first page of section 11 and try to figure it out.  
> **Hint:** What’s the difference between reading from `LATx` and `PORTx`?

3. Go ahead and code up your solution based on the register you found above. I’ll spoil the surprise a bit and let you know that it won’t work yet, but its good to have something we can tweak and test with.

4. Now it’s time to debug! Let’s start by using a multimeter to probe the voltage on the pin, to make sure it’s not a hardware issue (as it too often is :( ). This is where pulling up the PCB in KiCad can be helpful - if you have both the schematic and the PCB open and you click on something on the schematic it will select it for you in the PCB! This is very helpful for finding where to probe.  
 > **Tip:** Remember to be very careful not to short two pins together when probing. Feel free to call someone over to help you figure out the multimeter and how best to probe.

5. Now, you should find that when you press and release the button, the voltage on the pin doesn’t change! First of all make sure you are using the multimeter correctly by probing something you know is +3V3 (eg the +3V3 pad on `C1` or `R2`), and once you’ve confirmed that, think about why you’re not reading something different when the button is pressed.

6. Take a look at the schematic. You’ll notice that the button merely connects the pin to ground when pressed, and when released the pin isn’t actually connected to anything! This is called “floating”, and if you try to read the value of a floating pin you will get a random value that depends on things like electromagnetic interference and the specific internals of the PIC. To fix this, we would typically add a pull-up resistor between the pin and +3V3. As it turns out, I didn’t need to include one on this board because the PIC has its own internal pull-ups that we can enable! Unfortunately the only info on the internal pull-ups is a brief mention in the first page and the corresponding register definition! Go ahead and give enabling the pull-up a try, remember to look at the bit description and notes in the register definition. If you’ve done it correctly you should now see the pin go to +3V3 when the button is released.

7. So now we’ve fixed the “hardware” issue (which was really still a software issue), but why is it still not working? For this, I point you to the last paragraph in section 11.0 and all of section 11.3.3. For some godforsaken reason the PIC designers thought it would be a good idea for *ANSEL to be enabled by default*, and you just read about what that does. If your code does not work after fixing this last issue, call someone over to give you a hand.
