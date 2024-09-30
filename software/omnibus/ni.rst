NI source
=========

Omnibus was originally created to work with the Data Acquisition (DAQ) system. The Ni source is the one that is designed to
work with it. The heart of the DAQ briefcase is the National Instruments (Ni) box. This is what converts the values received
from the electronic sensors to digital values. The python library used to interface with this box can be found here.

`NI-DAQmx Python documentation <https://nidaqmx-python.readthedocs.io/en/latest/>`_

In order to run this source, you will need to download this software onto your computer.

`NI-DAQmx <https://www.ni.com/en-ca/support/downloads/drivers/download.ni-daqmx.html#460239>`_

It is worth noting that for windows this is straight forward, however, we do not know how to install this on either Mac or
Linux, but we will soon.

Specific instructions on using DAQ with omnibus can be found in the electrical documentation.


.. note::
   There is another source called "fakeni" which is meant to expose the same interface as ni, but without actually reading
   any data from hardware.
