BigRedBee GPS Tracker
=======================
We use BigRedBee's `High Altitude 70cm 100mw GPS/APRS Transmitter <https://shop.bigredbee.com/collections/vhf-uhf-transmitters/products/high-altitude-70cm-100mw-gps-aprs-transmitter>`_

Configuration
-------------
BRB's documents and programs can be downloaded from https://shop.bigredbee.com/pages/documentation-and-programming-utilities. We need the `70cm and 2meter APRS Transmitter utility <https://cdn.shopify.com/s/files/1/0062/3919/1158/files/BeeLineGPS.066a_1.zip?10068239033136361787>`_. The `User Guide <https://cdn.shopify.com/s/files/1/0062/3919/1158/files/beelineGPS_19.pdf?17310379549075783602>`_ has more detail on the device configuration.

Essentially, you start the configuration utility on the computer and connect the radio transmitter to the computer using its ICSP to USB adapter. Power up the board, select the correct COM port, and click the “Read” button before the board enters charging mode, change the configurations in the utility, then click the “Write” button.

(Their program kinda sucks)

Right now we’re using 431.000 MHz to transmit the packets.

The setup was tested with the following configurations:
Last Tested Conguration

explaination


Getting Software

The setup uses Dire Wolf as software TNC to decode audio input, and APRSISCE/32 to display the position on the map.

    Get direwolf from https://github.com/wb2osz/direwolf/releases/tag/1.6



Extract the zip somewhere (on the team laptop I put it on Desktop)

Get APRSISCE/32 from http://aprsisce.wikidot.com/downloads



    Extract the exe in zip into an empty folder (on the team laptop I put it in Desktop\APRSIS32)

Running Software

    Connect the FT-4X tranceiver to microphone jack using an aux line.

        If the computer only has TRRS combo jack (like the team laptop), use a splitter cable to split out TRS microphone line and connect using that.

        If the computer doesn’t appear to be receiving audio with splitter cable, try unplug the aux line from the splitter first, plug the splitter into the computer, then plug the aux line back to the splitter.

    Turn on the tranceiver and set the frequency to 431.000MHz (or whatever frequency the transmitter is configured to).

    Start direwolf.exe

        If the transmitter is on and has a fix, it should send a packet every 5 seconds. Direwolf should  be able to decode them and print them out.

        If there are warnings about signal level, adjust the volume of the tranceiver.

    Run APRSIS32.exe

        When starting the program for the first time, it’ll asking for a call sign. We’re not using it to transmit anything so it should be fine to put anything (like NOCALLL).

        Once the program is started, uncheck these options:

            Uncheck Enable → APRS-IS Enabled - we don’t need to send the position to the internet

            Uncheck Enable → Beaconing Enabled - doesn’t really matter since we’re only receiving packets, but unchecking it reduces useless messages in the program.

        Go to Configure → Ports → New Port
        Type: AGW
        Name: direwolf

        In the next popup
        Select TCP/IP
        IP or DNS: 127.0.0.1
        Port: 8000
        Uncheck everything else

        Once the port is added, check Enables → Ports → direwolf

        If everything is working properly, the position of the APRS transmitter should now be shown on the map
