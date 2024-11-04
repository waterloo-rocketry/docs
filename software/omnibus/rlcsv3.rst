RLCS V3
=======

RLCS V3 stands for :doc:`Remote Launch Control System Version 3</electrical-gse/rlcs-v3/index>`. It was originally designed long before omnibus was a thing to remotely fill and launch the rocket. However, later in its life, it was modified to communicate its internal state and processes over omnibus to allow us to gain an understanding of it during operations procedures.

RLCS was modified to communicate its data over a USB port (in a very similar way to the source parsley). This data is then read by the RLCS source parsed using
parsley (the submodule parsley, used for parsing various types of binary data) and sent over the CAN bus.

RLCS uses parsley to convert the binary data it reads into a RLCS message. We prepend "W" and postpend "R" to the message to serve as a buffer between data.
We check that these bytes are correct along with the length of the message being correct to let us delinate between different messages. This logic is in `rlcs.py`.

The logic for communicating the state of the actuators is in `commander.py`, we only send a subset of the data parsed from the RLCS message currently.


(As a fun side note, the reason the file `rlcs_test.py` is empty is because we updated the rlcs source and that broke the tests and we just didn't fix it D: )
