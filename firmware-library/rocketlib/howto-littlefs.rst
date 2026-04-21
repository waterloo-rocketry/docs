***********************************
How-To: Read littlefs on a computer
***********************************

Windows
=======

We will use littlefs-FUSE inside WSL to mount the LittleFS filesystem.

Rebuild WSL with USB mass storage device support
------------------------------------------------
Unfortunately WSL does not have a USB mass storage device driver by default so we'll have to rebuild the WSL kernel with this feature enabled.
Follow `this guide <https://www.tomshardware.com/how-to/access-linux-ext4-partitions-in-windows>`_, to do so, including installing ``usbipd``.
This can take a while!

Some notes:

* Make sure the source directory where you clone, configure, and build the kernel is in a WSL rather than a mounted Windows directory
  to avoid errors caused by the Windows filesystem's case-insensitivity.
* When enabling `USB Mass Storage support` using ``sudo make menuconfig``, you may find it depends on some other features
  to also be included as built-in. You can press ``H`` with `USB Mass Storage support` selected to view these dependencies and
  press ``/`` to find where to enable them. 

Attach USB device using usbipd
----------------------------------
Once your SD card is plugged in using a USB adapter, first share the device by running the following with admin privileges:

.. code-block::

   usbipd --help
   usbipd list
   usbipd bind --busid=<BUSID>

Sharing a device survives reboots.

Then attach the device (doesn't require admin):

.. code-block::

   usbipd attach --wsl --busid=<BUSID>

Attaching a device doesn't survive reboots or unplugging and replugging.

Now in WSL you should see the SD card mounted under something like ``/mnt/sde`` (or ``sdd``, etc.).

littlefs-FUSE install and usage
-------------------------------

From here, you should be able to follow the instructions in the :ref:`Linux section <howto-littlefs-linux>` inside WSL to
install libfuse-dev and littlefs-FUSE, create an MBR partition table on the mounted SD card, then format and
mount the filesystem.

MacOS
=====



.. _howto-littlefs-linux:

Linux
=====

One time setup
--------------

Install dependency on Debian/Ubuntu

.. code-block::

   sudo apt install libfuse-dev

Clone and build littlefs-FUSE

.. code-block::

   git clone --depth=1 https://github.com/littlefs-project/littlefs-fuse.git
   cd littlefs-fuse
   make -j20
   sudo cp lfs /usr/local/bin
   cd ..
   rm -rf littlefs-fuse

Formatting the SD card
----------------------

.. caution::

   This will erase everything on the SD card

Create a MBR partition table using your favourite tool on the SD card (Sometime the MBR is also called "msdos" in some Linux partition tool).
For our firmware to identify it correctly, the partition type must be ``0x83`` (Linux filesystem). Note down partition device file name, e.g. /dev/sda1. Then run

.. code-block::

   sudo lfs --format /dev/sda1

Mounting the file system
------------------------

.. code-block::

   sudo mkdir -p /mnt/logger
   sudo lfs -o allow_other /dev/sda1 /mnt/logger

.. tip::

   The "-o allow_other" allows non root user to access the filesystem

Unmounting the file system
--------------------------

.. code-block::

   sudo umount /mnt/logger
