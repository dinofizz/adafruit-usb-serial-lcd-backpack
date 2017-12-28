"""
The LcdBackpack class exposes the commands available on the Adafruit LCD USB/Serial Backpack via simple methods.

Author: Dino Fizzotti
Date: April 2017
License: BSD 3-clause "New" or "Revised" License

I used Adafruit's 'matrixtest.py' as a reference when writing this, and so I am including following:

(from https://github.com/adafruit/Adafruit-USB-Serial-RGB-Character-Backpack)

Test python sketch for Adafruit USB+Serial LCD backpack
---> http://www.adafruit.com/category/63_96

Adafruit invests time and resources providing this open source code, 
please support Adafruit and open-source hardware by purchasing products from Adafruit!

Written by Limor Fried/Ladyada  for Adafruit Industries.  
BSD license, check license.txt for more information
All text above must be included in any redistribution

"""

import serial
import sys


class LcdBackpack:
    """
    The LcdBackpack class exposes the commands available on the Adafruit LCD USB/Serial Backpack via simple methods.
    """
    GPIO_HIGH = 0x57
    GPIO_LOW = 0x56
    CURSOR_BACK = 0x4C
    CURSOR_FORWARD = 0x4D
    SET_CURSOR_HOME = 0x48
    SET_CURSOR_POSITION = 0x47
    SET_BRIGHTNESS = 0x99
    SET_CONTRAST = 0x50
    SET_SPLASH_SCREEN = 0x40
    DISPLAY_ON = 0x42
    DISPLAY_OFF = 0x46
    COMMAND_START = 0xFE
    CLEAR_DISPLAY = 0x58
    AUTOSCROLL_ON = 0x51
    AUTOSCROLL_OFF = 0x52
    UNDERLINE_CURSOR_ON = 0x4A
    UNDERLINE_CURSOR_OFF = 0x4B
    BLOCK_CURSOR_ON = 0x53
    BLOCK_CURSOR_OFF = 0x54
    BACKLIGHT_RGB = 0xD0
    LCD_SIZE = 0xD1

    def __init__(self, serial_device, baud_rate):
        self._baud_rate = baud_rate
        self._serial_device = serial_device
        self._ser = None

    def __del__(self):
        if self._ser.is_open:
            self._ser.close()
        self._ser = None

    def connect(self):
        """
        Connects to the serial port.
        """
        self._ser = serial.Serial(self._serial_device, self._baud_rate, timeout=1)

    def disconnect(self):
        """
        Closes the serial port connection.
        """
        self._ser.close()

    @property
    def connected(self):
        """
        Returns the state of the serial connection.
        :return: True if the serial port is open (connected), False otherwise.
        """
        return self._ser.is_open

    def display_on(self):
        """
        Switches the LCD backlight on.
        """
        self._write_command([LcdBackpack.DISPLAY_ON, 0])

    def display_off(self):
        """
        Switches the LCD backlight off.
        """
        self._write_command([LcdBackpack.DISPLAY_OFF])

    def set_brightness(self, brightness):
        """
        Sets the brightness of the LCD backlight.
        :param brightness: integer value from 0 - 255 
        """
        self._write_command([LcdBackpack.SET_BRIGHTNESS, brightness])

    def set_contrast(self, contrast):
        """
        Sets the contrast of the LCD character text.
        :param contrast: integer value from 0 - 255
        """
        self._write_command([LcdBackpack.SET_CONTRAST, contrast])

    def set_autoscroll(self, auto_scroll):
        """
        Sets the autoscrolling capability to the value provided.
        :param auto_scroll: true/false
        """
        if auto_scroll:
            self._write_command([LcdBackpack.AUTOSCROLL_ON])
        else:
            self._write_command([LcdBackpack.AUTOSCROLL_OFF])

    def set_cursor_position(self, column, row):
        """
        Moves the cursor to the provided position.
        :param column: integer value for column posititon starting from 1
        :param row: integer value for row position starting from 1
        """
        self._write_command([LcdBackpack.SET_CURSOR_POSITION, column, row])

    def set_cursor_home(self):
        """
        Moves the cursor to the "home" positon: column = 1, row = 1.
        """
        self._write_command([LcdBackpack.SET_CURSOR_HOME])

    def cursor_forward(self):
        """
        Moves the cursor forward one character.
        """
        self._write_command([LcdBackpack.CURSOR_FORWARD])

    def cursor_back(self):
        """
        Moves the cursor backward one character.
        """
        self._write_command([LcdBackpack.CURSOR_BACK])

    def set_underline_cursor(self, underline_cursor):
        """
        Enables/disables the underline cursor.
        :param underline_cursor: true/false
        """
        if underline_cursor:
            self._write_command([LcdBackpack.UNDERLINE_CURSOR_ON])
        else:
            self._write_command([LcdBackpack.UNDERLINE_CURSOR_OFF])

    def set_block_cursor(self, block_cursor):
        """
        Enables/disables the block cursor.
        :param block_cursor: 
        """
        if block_cursor:
            self._write_command([LcdBackpack.BLOCK_CURSOR_OFF])
        else:
            self._write_command([LcdBackpack.BLOCK_CURSOR_ON])

    def set_backlight_rgb(self, red, green, blue):
        """
        Sets the RGB LCD backlight to the colour provided by red, green and blue values.
        :param red: integer value 0 - 255
        :param green: integer value 0 - 255 
        :param blue: integer value 0 - 255
        """
        self._write_command([LcdBackpack.BACKLIGHT_RGB, red, green, blue])

    def set_backlight_red(self):
        """
        Sets the backlight of an RGB LCD display to be red. 
        """
        self.set_backlight_rgb(0xFF, 0, 0)

    def set_backlight_green(self):
        """
        Sets the backlight of an RGB LCD display to be green. 
        """
        self.set_backlight_rgb(0, 0xFF, 0)

    def set_backlight_blue(self):
        """
        Sets the backlight of an RGB LCD display to be blue. 
        """
        self.set_backlight_rgb(0, 0, 0xFF)

    def set_backlight_white(self):
        """
        Sets the backlight of an RGB LCD display to be white. 
        """
        self.set_backlight_rgb(0xFF, 0xFF, 0xFF)

    def set_lcd_size(self, columns, rows):
        """
        Sets the size of the LCD display (columns, rows).
        :param columns: the number of columns
        :param rows: the number of rows.
        """
        self._write_command([LcdBackpack.LCD_SIZE, columns, rows])

    def set_gpio_high(self, gpio):
        """
        Sets the given GPIO pin on the LCD back pack HIGH (5V).
        :param gpio: the GPIO pin to set HIGH (1 - 4) 
        """
        self._write_command([LcdBackpack.GPIO_HIGH, gpio])

    def set_gpio_low(self, gpio):
        """
        Sets the given GPIO pin on the LCD back pack LOW (5V).
        :param gpio: the GPIO pin to set LOW (1 - 4) 
        """
        self._write_command([LcdBackpack.GPIO_LOW, gpio])

    def clear(self):
        """
        Clears all the characters from the display.
        """
        self._write_command([LcdBackpack.CLEAR_DISPLAY])

    def write(self, string):
        """
        Writes the given text on the LCD display.
        :param string: the text to be written on the display. 
        """
        if self._ser is None or self._ser.closed:
            raise serial.SerialException('Not connected')

        self._ser.write(str.encode(string))

    def set_splash_screen(self, string, lcd_chars):
        """
        Sets the LCD splash screen. 
        :param string: the text to be displayed at LCD start up
        :param lcd_chars: the total characters of the LCD display
        """
        self._write_command(LcdBackpack.SET_SPLASH_SCREEN)
        self._ser.write('{{0: <{}}}'.format(lcd_chars).format(string).encode())


    def _write_command(self, command_list):
        """
        Writes the given command list to the LCD back pack.
        :param command_list: The commands to be written to the LCD back pack.
        """
        if self._ser is None or self._ser.closed:
            raise serial.SerialException('Not connected')

        command_list.insert(0, LcdBackpack.COMMAND_START)

        # there must be a better way of handling this!
        if sys.version_info[0] == 3:
            self._ser.write(bytes(command_list))
        else:
            for item in command_list:
                self._ser.write(chr(item))
