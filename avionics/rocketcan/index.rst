===================
How does RocketCAN?
===================
    a beginner's guide to canlib & co

    ========================
    How does CAN in general?
    ========================
        Honestly the best resource is wikipedia: https://en.wikipedia.org/wiki/CAN_bus

        The most important thing to understand is the message format and how arbitration works. Each CAN message is composed of a bunch of different fields. The most important are:
            -  SID (arbitration identifier). CAN is a multi-master bus - any board can try to send something on the bus at any time, and there may be collisions. Arbitration is the mechanism for deciding which message has priority.
            - control (data length). Basic CAN supports 0-8 bytes of data. Each message needs to specify its data length.
            - data. The stuff you want to send. This can be formatted however the heck you want, but the team has a standard data format that all boards are expected to agree on.
            - ACK. This is not under your control - this is "set" by other boards on the bus that listen to the incoming message. As part of the CAN protocol, other units on the bus check the validity of incoming messages. If the message is valid, they will assert ACK. If the transmitting board does not receive an ACK, it will abort the rest of the message and the transmission is considered unsuccessful.
                - NOTE: this means that in order to successfully send a CAN message, you need at least one listener on the bus (e.g. usb debug).

![[Pasted image 20220626070137.png]]

        I really don't think I can explain arbitration better than this 'wiki section'_:
            - The CAN specifications use the terms "dominant" bits and "recessive" bits, where dominant is a logical 0 (actively driven to a voltage by the transmitter) and recessive is a logical 1 (passively returned to a voltage by a resistor). The idle state is represented by the recessive level (Logical 1). If one node transmits a dominant bit and another node transmits a recessive bit then there is a collision and the dominant bit "wins". This means there is no delay to the higher-priority message, and the node transmitting the lower priority message automatically attempts to re-transmit six bit clocks after the end of the dominant message. This makes CAN very suitable as a real-time prioritized communications system.

            - The exact voltages for a logical 0 or 1 depend on the physical layer used, but the basic principle of CAN requires that each node listen to the data on the CAN network including the transmitting node(s) itself (themselves). If a logical 1 is transmitted by all transmitting nodes at the same time, then a logical 1 is seen by all of the nodes, including both the transmitting node(s) and receiving node(s). If a logical 0 is transmitted by all transmitting node(s) at the same time, then a logical 0 is seen by all nodes. If a logical 0 is being transmitted by one or more nodes, and a logical 1 is being transmitted by one or more nodes, then a logical 0 is seen by all nodes including the node(s) transmitting the logical 1. When a node transmits a logical 1 but sees a logical 0, it realizes that there is a contention and it quits transmitting. By using this process, any node that transmits a logical 1 when another node transmits a logical 0 "drops out" or loses the arbitration. A node that loses arbitration re-queues its message for later transmission and the CAN frame bit-stream continues without error until only one node is left transmitting. This means that the node that transmits the first 1 loses arbitration. Since the 11 (or 29 for CAN 2.0B) bit identifier is transmitted by all nodes at the start of the CAN frame, the node with the lowest identifier transmits more zeros at the start of the frame, and that is the node that wins the arbitration or has the highest priority.

        What this means is that you can define a heirarchy of which messages are most important (e.g. valve control messages can be prioritized over sensor data). **Note: you cannot have two different units transmit the same SID at the same time - this is invalid.** To get around this, every message we send on rocketCAN is has an SID composed of the "message type" and the board ID (which should be uniquely programmed per board).

---

    ==================
    Architecture stuff
    ==================

        ===================
        Why does RocketCAN?
        ===================
            The reasoning behind rocketCAN is pretty well documented in various presentations, reports, etc:
                - 'Original presentation'_
                - 'Podium session presentation'_
                - 'Podium session abstract'
                - 'Spicy slack thread'_

            The story (again) is that in 2018 we had remotely actuated valves on the rocket for the first time (injector and vent). The bare minimum here was to have 1) a radio and 2) something to control the valve. In reality there was a bunch of other stuff we wanted so the total functionality ended up consisting of:
                - a radio
                - valve driving circuitry
                - sensors (pressure, accel, gyro, temperature...)
                - SD card logging

            Basically it was giant, we ran into a bunch of issues with it, and whenever something broke we either had to fix it right there, or swap the entire board which was painful and expensive. The hugeness was also a problem.

            Behold its monolithic glory (fun fact, that's a windshield wiper motor that draws up to 10 A):
![[Pasted image 20220626064851.png]]

        ============================================
        The system architecture as it originally was
        ============================================
            Alex's note: This is super out of date at this point. Yall have changed a lot, so someone really needs to make an updated version of this.

            The main idea is that radio gets messages from RLCS client-side (relayed by tower-side), and sends instructions onto the CAN bus. Every board listens to the bus and acts on those messages. Other boards also broadcast their status and other data (such as valve status) over the bus; this gets relayed back to ops by radio.
![[Pasted image 20220626062917.png]]

            @Team: please document your existing setup! A lot of people have complained that this knowledge is limited to a couple of people, and there's nothing they can reference for onboarding.

---

    ===========
    Canhw stuff
    ===========
        To onboard a board onto rocketCAN, it needs to have:
            - CAN module (internal or external)
                - this is the module that handles message buffers, filtering, etc.
                - The PIC18F26K83 has an internal CAN module that you can program directly by writing to the PIC's internal registers.
                - The MCP2515 is an external module that you control over SPI
                - The CAN module outputs its data over a pair of lines called CANTX/CANRX, which go to the transceiver
            - CAN transceiver
                - this is connected to the physical bus and responsible for actually spitting data out over CANH/CANL
            - current sensing (not a CAN requirement, but a team requirement)
                - if a board is connected to the shared 12V (or whatever it is now) rail, then it needs to report its current consumption over the bus

        How things are connected with an internal module
```C
-------------------                 -----------
|                 |                 |         |
| microcontroller |<---- CANTX ---->| MCP2562 |<--- CANH --->
|                 |<---- CANRX ---->|         |<--- CANL ---> ... the rest of the bus
-------------------                 -----------
```

How things are connected with an external module
```C
-------------------            -------------                 -----------
|                 |--- CS_L -->|           |                 |         |
| microcontroller |--- SCLK -->|  MCP2515  |<---- CANTX ---->| MCP2562 |<--- CANH --->
|                 |<-- MISO ---|           |<---- CANRX ---->|         |<--- CANL ---> ... the rest of the bus
|                 |--- MOSI -->|           |                 -----------
-------------------            -------------
```
---

    ============
    Canlib Stuff
    ============

        =====================================
        How does canlib? General organization
        =====================================

            Canlib github: https://github.com/waterloo-rocketry/canlib
            Cansw example github: https://github.com/waterloo-rocketry/cansw_injector

            Canlib is a common library used by all our boards using rocketCAN. It provides:
            - a list of message types and their format (`message_types.h`)
            - a set of utility functions to build and parse these messages (`can_common.h`)
            - low-level CAN drivers (currently available for 3 platforms - see README for details)
            - misc utilities
                - timing parameter generator (not actually a generator...)
                - timer functions for pic microcontrollers

            Other software projects include canlib as a submodule. Make sure that the canlib version checked out by each cansw project is in sync, to avoid differences in message format.

            Canlib can be extended to any microcontroller with a CAN submodule - you will just need to write the low-level CAN driver layer for your particular platform. The higher layers (can_common and message_types) are agnostic to the driver implementation.

        ============================
        Message types and board SIDs
        ============================

            CAN 2.0 supports 11 bit SIDs. Each SID is made up of the message type (upper bits) and the board id (lower bits, prevents collisions). From `message_types.h`:
            ```
            * Message SIDs are 11 bit unique identifiers.
            * Bottom 5 bits: IDs that are unique to the board sending the message
            * Top 6 bits: message types. The message types defined here therefore
            * have the bottom 5 bits set to 0.
            *
            * MESSAGE_SID = MESSAGE_TYPE | BOARD_UNIQUE_ID
            ```
            When defining a new message type or board id, make sure that the bits for each don't overlap. Since the bottom 5 bits of each message type must be 0, the minimum increment between message types is 0x20 (ie. 0b100000). Beyond that you can do whatever you want with the message type.

            Board ids don't matter much - we didn't bother with a hierarchy there. They are just there to prevent collisions.

        ==========================================
        Basics: adding new message types to canlib
        ==========================================

            Relevant files:
            - message_types.h
            - can_common.h
            - can_common.c
            - unit_tests.c
            - build_can_message.h/c

            1. Choose a message type ID for your new type. Add it to the list of message types in message_types.h
            2. Figure out the format for your message. Add this format to the giant comment in message_types.h. Your payload must be at most 8 bytes for CAN 2.0A.
            ```cpp
            /*
            * General message type format (from spreadsheet):
            * (Version 0.7.0)
            *                  byte 0      byte 1      byte 2      byte 3                byte 4         byte 5             byte 6          byte 7
            * GENERAL_CMD:     TSTAMP_MS_H TSTAMP_MS_M TSTAMP_MS_L COMMAND_TYPE          None           None               None            None
            * ACTUATOR_CMD:    TSTAMP_MS_H TSTAMP_MS_M TSTAMP_MS_L ACTUATOR_ID           ACTUATOR_STATE None               None            None
            * ALT_ARM_CMD:     TSTAMP_MS_H TSTAMP_MS_M TSTAMP_MS_L ALT_ARM_STATE & #     None           None               None            None
            // <-- add your format here -->
            ```
            3. Add functions to build and parse your new message to can_common.h and can_common.c. This is the only place where raw CAN messages are parsed - all other code should use the functions defined here. Example: `build_gps_lon_msg(...)` and  `get_gps_lon(...)`.
                1. This file is thoroughly commented and is a good reference for figuring out what parsing functions are available to you.
                2. When you add your own functions, make sure to add a descriptive comment for each as well.
            4. Write tests for your new format functions
                1. add your tests to `build_can_message.c` - make sure to also add them to the test execute function at the bottom of the file (`test_build_can_message()`).
                2. These tests can be run both locally on your machine, or on a microcontroller. Locally is easier.

        ============================
        Basics: general driver setup
        ============================

            To set up a CAN driver, you need these things:
            1. a general interrupt service handler(ISR) for your main code (this is what gets called whenever ANY* interrupt is triggered). Within this handler, it is up to you to determine whether you have received an interrupt from CAN (based on an interrupt flag), and then call `can_handle_interrupt()` or the equivalent.
                1. `can_handle_interrupt()` is responsible for the low-level details of reading the RX buffer on the micro, etc.
            2. a CAN message handler function. This will be called by `can_handle_interrupt` once a message is received.
                1. This is responsible for deciding what to do with incoming messages.
            3. timing parameters
                1. see `can_timing_t` in can.h
                2. there's a utility function to populate these parameters based on your clock speed. Note that it isn't really a calculator, just a collection of previously used timing params.
                3. See section 34.8 in the PIC18F26K83 datasheet for how these are used.

            \* logger (DSPIC) is an exception to this - it has vectored interrupts. The Pic18F series has support for high/low priority interrupts but we don't use this feature since don't have a lot of interrupts.

            **PIC18F code example**
            ```cpp
            int main() {
                // do stuff ...

                // Enable global interrupts - needed for our interrupt handler to run
                INTCON0bits.GIE = 1;

                // set up CAN module
                can_timing_t can_setup;
                can_generate_timing_params(_XTAL_FREQ, &can_setup);

                can_init(&can_setup, can_msg_handler); // can_msg_handler is a function pointer. The function is defined below.
                // do more stuff
            }

            // blah blah blah

            // Interrupt handler. For PICs, interrupt handlers are always "static void interrupt <name>(void)"
            // This function will get called whenever any interrupt is triggered.
            // In this handler, we check the various flags we're interested in to find what we need to do.
            // The various flags are spelled out in the datasheet.

            // PIR = periheral interrupt register. They range from PIR0 to PIR9
            // PIE = peripheral interrupt enable
            // see register definitions starting on page 127 of PIC18F26K83 datasheet
            static void interrupt interrupt_handler() {
                // we've received a CAN related interrupt
                if (PIR5) {
                    can_handle_interrupt(); // clears PIR5 internally
                }

                // Timer0 has overflowed - update millis() function
                // This happens approximately every 500us
                if (PIE3bits.TMR0IE == 1 && PIR3bits.TMR0IF == 1) {
                    timer0_handle_interrupt();
                    PIR3bits.TMR0IF = 0;
                }
            }

            // Example message handler - ignore everything except LEDS ON/OFF
            // This is called from within can_handle_interrupt()
            static void can_msg_handler(can_msg_t *msg) {
                uint16_t msg_type = get_message_type(msg); // get_message_type() is part of can_common
                switch (msg_type) {
                    case MSG_LEDS_ON:
                        RED_LED_ON();
                        BLUE_LED_ON();
                        WHITE_LED_ON();
                        break;

                    case MSG_LEDS_OFF:
                        RED_LED_OFF();
                        BLUE_LED_OFF();
                        WHITE_LED_OFF();
                        break;

                    // all the other ones - do nothing
                    default:
                        break;
                }
            }

            ```


        ===================================
        Basics: PIC18F CAN driver specifics
        ===================================

            In addition to the above, you need to properly set up the CAN TX and RX GPIO before you set up the driver. These lines are what the PIC18F uses to communicate with the CAN transceiver (MCP2562), which ultimately drives the CANH and CANL lines on the bus.

            Since this GPIO can be remapped, it is not done inside the `pic18f26k83` can_init function. It must be set up externally. How to do this is described in `pic18f26k83/pic18f26k83_can.h`. Check the datasheet for specifics. **Note: not all pins can be mapped as CAN. Check the datasheet before routing a PCB.**
            ```
            /*
            * Initialize the CAN driver on a PI18fC26fk83. Note that this function
            * DOES NOT setup the inputs and outputs from the CAN module to the
            * output pins, application code must do that. In order to do that,
            * CANRXPPS must be set to the proper pin value for the CANRX pin, and
            * ___PPS must be set to 0x33 to mark it as outputting from the CAN
            * module. In addition, TRIS and ANSEL registers for whatever pin
            * is being used must be set to the right values.
            */
            void can_init(const can_timing_t *timing,
                        void (*receive_callback)(const can_msg_t *message));
            ```

            Your complete intialization might then look something like this. This example is from the old injector board:
            ```cpp
            // somewhere in main()

                // Enable global interrupts
                INTCON0bits.GIE = 1;

                // Set up CAN TX
                TRISC0 = 0;     // set up as output
                RC0PPS = 0x33;  // peripheral pin select: see section 34.1 and table 17-2

                // Set up CAN RX
                TRISC1 = 1;     // set as input
                ANSELC1 = 0;    // disable analog in (pins are analog by default)
                CANRXPPS = 0x11; // peripheral pin select: see section 34.1 and table 17-1

                // set up CAN module
                can_timing_t can_setup;
                can_generate_timing_params(_XTAL_FREQ, &can_setup);

                can_init(&can_setup, can_msg_handler);
            ```

            (Tip: it's useful to include accessible test points for CAN TX and RX so you can debug your GPIO config during bringup)

        ====================================
        Basics: MCP2515 CAN driver specifics
        ====================================

            The MCP2515 is a standalone CAN module that can be used with microcontrollers that do not have their own internal one. The main micro can communicate with it over SPI.

            The driver setup is pretty much identical to the PIC18F driver, except the function names are a little different, and you need to provide the SPI read/write functions to the driver. You also need to set up the SPI GPIO. The interface looks like this:
            ```cpp
            void mcp_can_init(can_timing_t *can_params,
                            uint8_t (*spi_read_fcn)(void),        // function pointer for "read"
                            void (*spi_write_fcn)(uint8_t data),  // function pointer for "write"
                            void (*cs_drive_fcn)(uint8_t state)); // function pointer for "chip select"
            void mcp_can_send(can_msg_t *msg);
            bool mcp_can_send_rdy(void);
            bool mcp_can_receive(can_msg_t *msg);
            ```
            Internally, the mcp2515 driver will call these SPI functions to communicate with the MCP2515. They are not hardcoded inside the driver itself, so that the driver can be used with different micros/pin configurations.

            Notably, mcp2515 does not have a `can_handle_interrupt` function. This is because the MCP2515 hardware has a dedicated INT line that can be triggered upon message reception. At that point we can just call `mcp_can_receive` to extract the message over SPI (note: don't do this in your ISR itself).

            **small code example**
            ```cpp
            #include "spi.h" // or whatever you're using

            int main() {
                spi_init();

                //initialize the CAN module
                can_timing_t can_setup;
                can_generate_timing_params(_XTAL_FREQ, &can_setup);

                // cs_drive is expected to be a function that drives some hardcoded pin
                // you could make this more flexible if you wanted but we decided it didn't matter that much
                mcp_can_init(&can_setup, spi_read, spi_write, cs_drive);
            }

            // e.g.
            void cs_drive(uint8_t state)
            {
                if (state) {
                    LATC |= (1 << 3);
                } else {
                    LATC &= ~(1 << 3);
                }
            }
            ```

            (Tip: here I like to have test points for the CANTX/RX lines AND the SPI lines. A logic analyzer - or an oscilloscope in a pinch - is enormously useful for debugging this connection)

        =======================================================
        Basics: setting up the ringbuffer and sending a message
        =======================================================

            - queue the message now and yeet it later
            - this is independent of which CAN driver you are using!!
            - you can have multiple!!
            - TODO ALEX

        ============================
        Adding new drivers to canlib
        ============================

            To add a new driver, you need to provide an interface for:
            - `init`
                - set timing
                - set CAN mode (legacy vs extended)
                - set rx/tx interrupts
                - set up filters and masks (currently we do not do filtering and allow all messages through. This is a topic for another time...)
                - anything else your new micro wants (read the datasheet TM)
            - `can_send`
                - self-explanatory, write to TX buffer and initiate a transaction
            - `can_send_rdy`
                - check current status (i.e. are we ready to send a new message)
            - `can_handle_interrupt` or other receive function

            The pic18f26k83 CAN driver is a good reference - it's pretty readable and also has comments almost everywhere explaining what it's doing. Of course, your new platform will behave somewhat differently, so you'll have tospend some time with the datasheet ;)

---

    ==========================
    Other useful documentation
    ==========================

        - intro to function pointers: https://www.cprogramming.com/tutorial/function-pointers.html
            - function pointers are useful as passing functions as parameters to other functions
        - intro to git submodules: https://git-scm.com/book/en/v2/Git-Tools-Submodules
        - PIC18F datasheet: http://ww1.microchip.com/downloads/en/DeviceDoc/40001943A.pdf
        - MCP2515 datasheet
        - TI "how to debug can" whitepaper: https://www.ti.com/lit/an/slyt529/slyt529.pdf?ts=1656202344705
            - this is a good one to read thoroughly!
        - Generic electrical onboarding slack post: https://waterloorocketry.slack.com/archives/C07MX0QDS/p1548901868070500


        _wiki section: https://en.wikipedia.org/wiki/CAN_bus#Data_transmission
        _Original presentation: https://docs.google.com/presentation/d/1lY-6Jb7F9jVUYJ2JZXEdMu1GOq21mpF8pozzrxEguzs/edit?usp=sharing
        _Podium session presentation: https://drive.google.com/file/d/1fRxTF7ohCUvl9OJgpzXgkvUX4kHPzG_L/view?usp=sharing
        _Podium session abstract: https://docs.google.com/document/d/1AnKkN07KEadL46xrn5BsaJCLON5rAeupkaKTvWgShUA/edit
        _Spicy slack thread: https://waterloorocketry.slack.com/archives/C07MX0QDS/p1620432775473100
