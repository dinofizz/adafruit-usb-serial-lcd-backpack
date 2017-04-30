from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lcdbackpack',
    version='1.0.0b1',
    description='A wrapper library to facilitate writing text and commands to the Adafruit USB / Serial LCD Backpack',
    url='https://github.com/dinofizz/adafruit-usb-serial-lcd-backpack',
    author='Dino Fizzotti',
    author_email='dino@dinofizzotti.com',
    license='BSD',
    packages=['lcdbackpack'],
    install_requires=[
        'pyserial',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Serial port device access',

        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='USB serial port LCD Adafruit'
)
