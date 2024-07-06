Omnibus - Overview
==================

Omnibus is a unified data processing and visualization platform designed to be used during and after operations procedures.
It is built upon zeromq, which itself is a thin abstraction over sockets. As a result, it is capable of processing data from various
sources accross a network. It also boasts a dashboard used during operations to visualize data.

Architecture
------------

When using omnibus, the programs are usually running.
1. A source, which provides data
2. A sink, which consumes it
3. Omnibus's core library, which connects the two

There are numerous sources and sinks, each of which has its own subsection.

The core library is built ontop of `zeromq <https://zeromq.org/>`, which is a thin abstraction ontop of web sockets.


Core Library
------------

The core library is found in the `omnibus` folder of the repository. It contains the code which is
used to communicated between the various sources and sinks. It is designed to work accross a Local
Area Network so that our operations team can recieve data from the various computers stationed
accross the launch site.

Omnibus.py
~~~~~~~~~~

Omnibus.py provides a few core classes. `Message` and subclasses of `OmnibusCommunicator`.
Omnibus Communicator is a super class of the two most important classes in Omnibus; `Sender` and `Receiver`.


Message
~~~~~~~

This class has three fields. `Channel`; the channel the message was sent on, `Timestamp`; the time the message
was sent and `Payload`; the contents of the message. It is worth noting that this class is designed to be
turned into a sequence of bytes to be sent over the Socket. This process is described in the “Sender” section.


Sender
~~~~~~

This class is used by sources to send information over omnibus. Most sources include these lines, which include
Sender in a project and make use of it.

...code-block:: python

    from omnibus import Sender

    sender = Sender()
    CHANNEL = "Your Channel" # omnibus channel

    ...

    sender.send(CHANNEL, data)


This class has two methods, `Sender.send_message(self, message)`, which accepts a Message type and sends it over
the channel message.channel. To simplify this process slightly, the method `Sender.send(self, CHANNEL, data)` simply
accepts a channel and a payload and constructs a message type to provide send message.

Receiver
~~~~~~~~

Receiver is the complement to Sender. Its purpose is to receive messages sent over omnibus. Here is an example of its use.

...code-block:: python

    from omnibus import Receiver

    channel = "" # Receiver channel
    receiver = Receiver(channel)

    while True:
        data = receiver.recv()
        ...

The methods on receiver correspond to the ones on sender. Note, both `Receiver.recv_message(self, timeout=None)` and `Receiver.recv(self, timeout=None)`
listen to a channel for timeout milliseconds until a message is received. If one is found, it stops and returns it, else it fails. If the timeout is set
to None, then the Receiver will wait until it receives a message.

An important note is that the receiver does not only listen on the channel it is initialized with. It listens to all channel’s whose
name has its channel has a prefix. An example is illuminating.

Say we define `rec = Receiver("a")`, then rec will listen to messages sent on channels `"a"`, `"abcd"` or `"actuator board"`. However, it would not listen to
messages sent over `"b"`. A nice result of this feature is that if you want to listen to all messages sent over omnibus, you can initialize your receiver
on the channel `""`.


This is largely a hold over from the ZMQ library.
