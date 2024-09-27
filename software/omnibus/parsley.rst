Parsley
=======

Background Information
----------------------

The nervous system of our avionic is our CAN (Controller Area Network) bus. All of the boards within our rocket are connected
to this central data bus so that they can communicate. You can think about the bus as allowing boards to send 1's and 0's to every
other board attached on the bus. Each board recieves these bits and decides what to do with them (if anything).

In order to make use of this bus, we have written up a standard communication protocol aggreed upon by all of the boards on our rocket.
This protocol is called `canlib <https://github.com/waterloo-rocketry/canlib>`_ and sees data packaged into messages known as "CAN messages".
Canlib provides utilities for developers to convert can messages into binary data and send them over the bus.

A wire leaves our rocket (through our electrical disonnect) and connects the CAN bus to a board inside our DAQ (data aquisition) box called "DAQ can support".
This board then recieves the raw binary data and sends it through a USB port to the DAQ computer (and old framework laptop which we mutalated and slapped inside
the DAQ box).

After this, parsley (this program!) reads the raw binary data coming in through the USB port and reconstructs the CAN messages. It then sends them over the
omnibus for various sinks to use.

(It is worth noting that the stack I just described is only one of the places parsley is used. It is also used to interface with live telemtry and in some other places)


The Parsley Source
------------------

The code is divided into two subsections to deal with perform these tasks
#. Reading data from the USB port, and communicating with omnibus
#. Parsing binary data into CAN messages

The code used to solve the second of these problems has been extracted out of omnibus into its own submodule. Confusingly, this submodule is
also known as `parsley <https://github.com/waterloo-rocketry/parsley>`_. This piece of code is amazingly well documented and written thanks
to the wonderful Micheal. As a result, I will not be explaining it here. If you have questions about it, go to the github repo linked above.

Before we dig into the code, I explain the options

* port
    * When reading data from a USB port, you need to specify which USB port you are actually reading. there are a few options for figuring this out.
      If you are on windows, you can open your device manager. Scroll until you find something called "COM ports" or something similar. Upon expanding that, you will
      see a few options that are something like `COM 5`, `COM 7` etc. One of them is the port you want, just try all the options until one of them works.
      If you are on linux, the port will be a file path. Specifically, it will be of the from `/dev/tty0`, `dev/tty1`, etc. `This article <https://www.cyberciti.biz/faq/find-out-linux-serial-ports-with-setserial/>`_
      will help you figure out which specific one you want to use.
* baud
    * baud refers to speed at which data is transfered over the USB port you are using. For 99% of applications, the default value should be fine. If it isn't, godspeed soilder,
      godspeed
* fake
    * We occasionally need to test other systems without having access to a running CAN bus. As a result, you can use this option to make parlsey spit out fake data for testing reasons
* format
    * The parlsey source prints out all the data it recieves so that it can be viewed live. This is very useful for doing things like debugging a PCB. Format specifies the
      format you want the data printed in. Notice one of the options (telemtry) causes a few other behaviour changes since it is meant for parsing data from our live telemetry
      system, which has a different data format and requirements.
* solo
    * If you want to run this source without connecting to an instance of omnibus (again, very useful for debugging individual boards), you can specify this option

Serial Communicators
~~~~~~~~~~~~~~~~~~~~

There are two classes which do something like serial communication. `SerialCommunicator` and `FakeSerialCommunicator`. Serial Communicator is meant to abstract away the process
of reading from the USB port. Fake Serial Communicator is a version of Serial Communicator which exposes the same methods, but dosen't actually read any data. This is for the
fake option described above.


Communication Over the Omnibus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Despite the simple description of parsley I gave above, there are actually quite a few non-trivial things parsley is doing.

#. The first and most obvious is sending all the CAN messages it recieves over the omnibus. The channel parsley uses for this is `SEND_CHANNEL`, usually set to
   CAN/parsley
#. The parsley source also sends "health check" messages over the omnibus so we know how many instances of parsley are running (specifically so we can get their ID's, which
   are used for the purpose described below). It does this over the `HEARTBEAT_CHANNEL` set to "Parsley/Health"
#. Sometimes, we want to send commands from the operations dashboard (its a sink, explained elsewhere) to parsley so that it can send those message back to the CAN bus.
   As a result, parsley is actually both a source *and* a sink. To make this work, parsley listens to a channel called `RECEIVE_CHANNEL`. (usually "CAN/commands", but
   telemtry uses "telemtry/CAN/commands"). There is a fair amount of logic built into parsley to deal with the fact that we sometimes want to send different instances
   of parsley. Each instance of parsley has a `sender_id` which we use to send commands to specific instances of parsley.



