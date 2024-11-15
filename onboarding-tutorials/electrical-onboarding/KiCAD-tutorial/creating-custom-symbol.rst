Creating a Custom Symbol
========================

In this tutorial, we’ll be covering most of the processes that you’ll be going through to create a board. This of course, includes creating a schematic symbol from scratch. While KiCad’s libraries contain hundreds of common schematic symbols, you can’t expect the symbol for every single obscure microcontroller to be included. For instance, we will have to create the symbol for the PIC12LF1501 microcontroller that is used for this board. Doing this will require a bit of work with component datasheets, so expect to learn a thing or two about reading them on top of learning KiCad.

Creating a Library
------------------
In order to create our custom schematic symbol, we will first need to create a new library to store it in. Back in the KiCad main window, open the Symbol Editor by clicking on its button or by hitting **Ctrl+L**. It will take a bit to load the symbols libraries but once completed you will be in the Symbol Editor application. To create a new library, go to **File > New Library…** You will then be presented with a pop-up that will prompt you to choose the library table to add it to. Choose **Project**, as we only want this library to be project wide. Select the location to create the library at, preferably in your project directory, and give it a helpful name, such as ``My_Tutorial_Symbols``. You will now be back at the Symbol Editor window. Newly-created libraries will automatically be added to the current project. To verify that your library has been properly added, search for it in the Libraries list on the left. If you don't have this list, click on the **Toggle search** tree button on the left toolbar and it should show up.

Creating the Symbol
-------------------
Okay, now that our new library is set up, let’s get to symbol creation. As mentioned before, we will be creating the schematic symbol for the PIC12(L)F1501 8-Pin Microcontroller. To start off, open up this component’s datasheet, which you can find at: https://ww1.microchip.com/downloads/en/DeviceDoc/40001615C.pdf

A datasheet is a document that contains all the information that you’d likely ever need on the characteristics and performance of an electronic component. This is evident in the fact that the document we just opened is 292 pages long. Don’t worry, we’re only here for just a few of these pages. Flip (or scroll, I guess) to page three of the document, the section labelled **Pin Diagrams**. Pin diagrams are simply schematics that give the locations and functions of each of the pins on the microcontroller. We will be copying this into our editor to get the symbol we need. If it helps, I’ve put the diagram that we’ll be working with below:

    .. image:: ../pin-diagram.png

Let’s start creating this back in the Symbol Editor. Select the library that you have just created from the list on the left to create the new symbol under that library then click on the **Create a new Symbol** button on the top toolbar. When prompted, give the symbol a name of “PIC12LF1501”. Leave everything else as it is, although note the input for the **Default reference designator**. A **ref**\erence **des**\ignator is the identifier for a component on a schematic or PCB. It usually consists of letters that indicate the component class followed by a number. Here you can see that the refdes letter is ‘U’, which is used for integrated circuits such as microcontrollers.

Once you click **OK**, two overlapping text labels should appear in the creation area. To make our UI a bit less cluttered, now might be a good time to hide the library list by clicking on the **Toggle search tree** button on the left. Move the text labels around by hovering your mouse over them and hitting the **M** key. A **Clarify Selection** context menu may pop up prompting you to select the specific item that you want to move. Move the labels wherever you want for now, as we will pretty things up later.

To begin, let’s create the rectangle that will be the “body” of the symbol. On the right toolbar, click on the **Add a rectangle** button and create it by clicking on the points to be the top-left corner and bottom-right corners of the box. The box shouldn’t be too big or small. On the bottom of the window you should see the current X and Y coordinates of your cursor. Use that info to create a box that is approximately 20mm x 15mm. You can ensure that the units that your coordinate system is using are millimeters by clicking on the **Use millimeters** button on the left toolbar. If you want to move the box that you have created, you can do so by hovering your mouse over an edge of the box and pressing **M** to move it around. To resize the box, you can click on the edge of the box and drag the handles on the corners. To make the box stick out from the background, let’s add a fill color to it. Do this by hovering your mouse over an edge of the box and pressing **E** to open the edit menu. From here, change the **Fill Style** to **Fill with body background color**. Modify your rectangle and move your labels around until you have something that looks like what’s below. Make sure that the center of the box is (0, 0) as indicated by it being centered with the two blue axis lines.

    .. image:: ../blank-symbol.png

Now that the body has been created, let’s get to creating the pins. From the right toolbar, click on the **Add a pin** button. Now, whenever you click somewhere on the diagram you will begin the pin creation process. You can exit this tool at anytime by pressing **Esc** or clicking the **Select item(s)** button on the right toolbar. Let’s start by creating Pin 1, found on the top-left of our pin diagram. The pin is labelled VDD, so we’ll make it just that. Click somewhere on the drawing area and the **Pin Properties** window will pop up. Edit the pin name, pin number, electrical type, and orientation so it matches with what’s below:

    .. image:: ../pin-properties.png

Click OK and you will be able to choose where to put the pin. Put it roughly where it is on the datasheet, with the right end of the line connected to the border of the box. Move the label if desired. Now, onto the rest of the pins. To make it easier on you, there’s a table below that specifies the properties you will need to set for all the pins. Also, here’s a reminder to save often.

To make the schematic a bit cleaner, the positions of a few pins have been switched compared to the datasheet. Here’s what your symbol should look like at the end:

    .. image:: ../schematic-symbol.png

    .. image:: ../schematic-symbol-pins.png

    .. note:: Note: You can add a bar over text by putting a tilde in front and wrapping it in curly braces (e.g. `~{MCLR}`)

And we’re done! Hopefully, you now have a decent grasp on how to create custom symbols in KiCad. That wasn’t too bad, right? Unfortunately, we won’t be covering how to create custom component footprints in this tutorial – they’re made from scratch a lot less frequently than symbols are due to how standardized component dimensions are – but this process is very similar to that too. If you’d like to, mess around with the Footprint Editor yourself and see what you can do. For now, save your symbol and close the Schematic Editor.

Now that we have all the schematic symbols that we’ll need to draw a schematic, we can finally get to doing just that in the next section.
