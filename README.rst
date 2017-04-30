Python Library for Adafruit USB / Serial LCD Backpack
=======================

This library is a simple wrapper intended to help send text and commands to the Adafruit USB / Serial LCD Backpack.

Adafruit product link: https://www.adafruit.com/product/782
Adafruit product tutorial: https://learn.adafruit.com/usb-plus-serial-backpack/overview

The commands suported are those listed here: https://learn.adafruit.com/usb-plus-serial-backpack/command-reference

...with the exception of those relating to saving, storing and using custom characters.

Installation
===

.. code:: bash

    $ pip install lcdbackpack


Example usage
===

.. code:: bash

    Python 3.6.1 (default, Mar 27 2017, 00:27:06)
    [GCC 6.3.1 20170306] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from lcdbackpack import LcdBackpack
    >>> lcdbackpack = LcdBackpack('/dev/ttyACM0', 115200)
    >>> lcdbackpack.connect()
    >>> lcdbackpack.clear()
    >>> lcdbackpack.write("Hello World!")
    >>> lcdbackpack.disconnect()

