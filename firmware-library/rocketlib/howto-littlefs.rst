***********************************
How-To: Read littlefs on a computer
***********************************

Windows
=======

We will use littlefs-FUSE inside WSL to mount the LittleFS filesystem.

See `here <https://learn.microsoft.com/en-us/windows/wsl/install>`_ for instructions on installing WSL. 

Rebuild WSL with USB mass storage device support
------------------------------------------------
Unfortunately WSL does not have a USB mass storage device driver by default so we'll have to rebuild the WSL kernel with this feature enabled.
Follow `this guide <https://www.tomshardware.com/how-to/access-linux-ext4-partitions-in-windows>`_ to do so, including installing ``usbipd``.
This can take a while!

Some notes:

* You shouldn't actually need ``sudo`` for many of the commands in the linked tutorial, including steps 9-11, 17, and 19.
* Make sure the source directory where you clone, configure, and build the kernel is in a WSL rather than a mounted Windows directory
  to avoid errors caused by the Windows filesystem's case-insensitivity.
* When enabling `USB Mass Storage support` using ``make menuconfig``, you may find it depends on some other features
  to also be included as built-in. You can press ``H`` with `USB Mass Storage support` selected to view these dependencies and
  press ``/`` to find where to enable them. 

Attach USB device using usbipd
----------------------------------
If you haven't already, install usbipd using `these instructions <https://github.com/dorssel/usbipd-win/blob/master/README.md>`_.

Once your SD card is plugged in using a USB adapter, first share the device by running the following inside Windows
(not WSL) with admin privileges:

.. code-block::

   usbipd --help
   usbipd list
   usbipd bind --busid=<BUSID>

Sharing a device survives reboots.

Then attach the device (doesn't require admin):

.. code-block::

   usbipd attach --wsl --busid=<BUSID>

Attaching a device doesn't survive reboots or unplugging and replugging.

Now back in WSL you should see the SD card mounted under something like ``/mnt/sdd`` (or ``sde``, etc.).

littlefs-FUSE install and usage
-------------------------------

From here, you should be able to follow the instructions in the :ref:`Linux section <howto-littlefs-linux>` inside WSL to
install libfuse-dev and littlefs-FUSE, create an MBR partition table on the mounted SD card, then format and
mount the filesystem.

MacOS
=====

One time setup
--------------

Install `macFUSE <https://macfuse.github.io>`_ (use a stable release). The installer enables a system extension; after install, confirm **macFUSE** appears under System Settings and allow it if prompted. You may need to restart once.

Clone and build the macOS littlefs-FUSE driver. The upstream ``littlefs-fuse`` project does not support macOS; use this fork instead:

.. code-block::

   git clone --recursive https://github.com/SAT-oO/littlefs-rw.git
   cd littlefs-rw/littlefs-fuse-macos
   make

You should see an ``lfs`` binary in ``littlefs-fuse-macos/``.

If you already cloned without ``--recursive``:

.. code-block::

   git submodule update --init --recursive

Reading from USB
----------------

Use a stick that is already formatted with LittleFS (for example, one used with rocketlib firmware). No ``block_size`` or ``block_count`` flags are needed—the driver reads them from the device.

Identify the raw device:

.. code-block::

   diskutil list

Note the path (for example ``/dev/disk4``). Replace ``diskX`` below with your disk index.

Unmount any macOS volume on the stick so the raw device is free:

.. code-block::

   diskutil unmountDisk /dev/diskX

From ``littlefs-fuse-macos/``, start the FUSE driver and leave this terminal open:

.. code-block::

   mkdir -p ../littlefs-mount
   sudo ./lfs -o allow_other,defer_permissions /dev/diskX ../littlefs-mount

In a second terminal (from the ``littlefs-rw`` project root), read files:

.. code-block::

   ls littlefs-mount
   cat littlefs-mount/config.txt

Unmounting
----------

Stop the ``lfs`` process in the first terminal with ``Ctrl+C``, then:

.. code-block::

   umount ../littlefs-mount
   diskutil eject /dev/diskX

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
