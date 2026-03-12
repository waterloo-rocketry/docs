***********************************
How-To: Read littlefs on a computer
***********************************

Windows
=======



MacOS
=====



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
