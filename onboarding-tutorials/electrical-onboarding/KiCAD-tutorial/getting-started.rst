Getting Started
===============

Download
--------
First things first, if you have not already installed KiCad onto your computer, do so now. The download links can be found at `KiCAD.org <https://kicad-pcb.org/download/>`_. The program should run on pretty much any computer but do note that it will take up around 5GB of space on your drive. Note that this tutorial was written with KiCad version 6.0 in mind and later versions might have slightly changed functionality that may render this tutorial somewhat outdated.

Start-up
--------
Once KiCad is good to go, open it up. You should be met with a window similar to what is shown below. Note that there’s likely a few more things on my window compared to yours as I currently have an existing project open.

    .. image:: ../main-window.png

Let’s take a moment to go over the points of interest on this window. On the left side of the status bar at the bottom of the window, the directory that the KiCad project file is in will be displayed, or will be blank if no project is open. To the left, you can see the project files. We’ll go more into this later on, but for now know that the area will display all the important files and folders that are contained within the project, such as the board’s electrical schematics, PCB layout, and parts libraries. On the left toolbar, you have the usual buttons for things such as saving, loading, creating a new project, along with a few others.

Now, let’s get onto the interesting stuff: the nine large buttons that you see on the right side of the window.  Each of these buttons will take you to specific applications within KiCad. Let’s go over the first five buttons, as we will be using these tools in this tutorial:

    .. image:: ../button-meanings.png

Note that I mentioned a few other applications in the descriptions above, such as the Schematic Editor, Symbol Editor, and PCB Editor. “But wait, isn’t KiCad all I need to make cool boards?” you may ask. You see, KiCad is an Electronics Design Automation **Suite**, and its functionality is contained within several programs, most of which you will use going through in this tutorial.

Project Creation
----------------
Now that we have some understanding of the UI, let’s get started on building our board. First, we will need to create a new project. This can be done by going to **File > New Project...**, hitting the **Ctrl+N** hotkey, or simply just clicking on the **Create new blank project** icon on the toolbar. A file browser will open up, in which you can choose a location to create the KiCad project file. By default, a new folder with the project name will be created at the chosen location and the file itself will be within it.

Upon creation, you will notice that the project directory area has been updated and now contains a ``.kicad_pro`` file with a ``.kicad_pcb`` and ``.kicad_sch`` file within it. These are all the files you will need to create a PCB. We're not ready to start quite yet though, as we are missing a few custom component symbols and footprints that we will need for our board. To remedy this, we will be downloading and importing a few KiCad libraries.

Library Imports
---------------
We will be downloading some symbol libraries from the team’s GitHub to get the parts we need. Since this is not a GitHub tutorial (nag the software lead for this or something), I’ll go through the process quite quickly. If you’re Git-savvy and want to make this quick,  just clone Waterloo Rocketry’s electrical_tutorials repo found on the `Waterloo Rocketry Github <https://github.com/waterloo-rocketry/electrical_tutorials>`_. If you’re new to GitHub, don’t worry! While you will probably need to learn the technology at some point in the future, it’s quite easy to get what we currently need done. Simply navigate to the above link on your favorite browser and load the page. On the page, above the file list, click on the green **Code** button. From its drop-down, click on **Download ZIP** and a .zip file will download.

Inside the folder within the ``electrical_tutorials-master.zip`` file that you downloaded, you will find a few subfolders filled with tutorial files from various years including the one that you're currently doing. These files may come in handy if you get stuck and want to see the final product to help lead the way. Navigate to ``./2022_generic`` and copy the ``Tutorial_Footprints.pretty`` and ``Tutorial_Symbols.kicad_sym`` files into the project folder that you have created. The project directory should now look like what's below:

    .. image:: ../project-directory.png

There are two types of libraries in KiCad. Those that have the ``.kicad_sym`` extension contain symbols for electrical schematics, while libraries that have the ``.pretty`` extension contain component footprints and silkscreens to be used during the PCB design stage. The libraries that we copied contain some silkscreen Waterloo Rocketry logos and a footprint for a connector that we will need.

Let’s get this library hooked up to our project so we can actually use it as just moving it into the folder does nothing. Go back to KiCad and navigate to **Preferences > Manage Footprint Libraries…** You should be met with the Footprint Libraries window in which you can manage all your KiCad footprints. There are two tabs to this window: one for **Global Libraries**, footprint libraries that all your KiCad projects have access to, and **Project Specific Libraries**, libraries that can only be accessed by our current project. Switch to the Project **Specific Libraries** tab and click on the **Add Existing Library** to Table button. A file browser will open, choose the ``Tutorial_Footprints.pretty`` file that is in your project directory. If everything was done correctly then the library table should now look like what’s below:

    .. image:: ../footprint-libraries.png

Since the process for adding a symbol library and footprint library is exactly the same, you should now know not only how to import footprint libraries, but also symbol libraries. All you need to do is repeat what you have just done to add the symbol library, except select **Manage Symbol Libraries…** from the preferences drop-down and when selecting a file, select ``Tutorial_Symbols.kicad_sym``.

Now you should be all set up and ready to get started with using the powerful applications that KiCad contains. The next step is to create a custom schematic symbol for the PIC microcontroller that will be used in this design. Get started in the next section.