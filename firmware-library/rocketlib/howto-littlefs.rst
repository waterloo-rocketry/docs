***********************************
How-To: Read littlefs on a computer
***********************************

Windows
=======



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

Create a MBR partition table using your favourate tool on the SD card(Sometime the MBR is also called "msdos" in some Linux partition tool), note down partition device file name, e.g. /dev/sda1. Then run

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
