from abc import ABC, abstractmethod
import imaplib
import email
import sys
from email.message import EmailMessage
from smtplib import SMTP_SSL, SMTP_SSL_PORT
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button, RGBLED
from colorzero import color
from random import random as rand
import time


class ButtonInterface(ABC):
    """ template for button, rgb info pull inteface """

    @abstractmethod
    def setup_gpio(self):
        """ setup the pins """
        pass

    @abstractmethod
    def get_input(self):
        """ check_for input """
        pass

    @abstractmethod
    def process_input(self,r,g,b):
        """ what to do with if button is pressed """
        pass

class TactileButton(ButtonInterface):
    """ single button interface, only one input pin """
    def __init__(self, input_pin):
        self._input_pin = input_pin

    def setup_gpio(self):
        """ set the to low input """
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def get_input(self):
        """ check if state high """
        return GPIO.input(self._input_pin) == 1

    def process_input(self, rgb):
        """ lock button while pressed, advance colours, modulo """
        while self.get_input():
            pass
        time.sleep(0.1)  # avoid noisy inputs
        # strategy is to binarize the number up to three places and advance by one
        # the binary strategy is stolen from https://stackoverflow.com/a/10411151
        num = (rgb[0] + rgb[1] << 1 + rgb[2] << 2 + 1) % 7 + 1
        binary = ("%03d" % int(bin(num)[2:]))[0]
        r = bool(binary[0])
        g = bool(binary[1])
        b = bool(binary[2])
        return [r, g, b]


class MatrixButton(ButtonInterface):
    """ Membrane matrix utton interface """
    states =[[False, False, False], #0
             [True, False, False],  #1
             [False, True, False],  #2
             [True,  True, False],  #3
             [False, False, True],  #4
             [True, False,True],    #5
             [False, True, True],   #6
             [True, True, True]]    #7
    def __init__(self, rows, colls, mapping):
        self._rows = rows
        self._colls = colls
        self._mapping = mapping
        self._action = mapping[0]  # just for init
        self._pressed = rows[0]  # just for init
        self.setup_gpio()
        
    def setup_gpio(self):
        """ set the to low input """
        for row in self._rows:
            GPIO.setup(row, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        for coll in self._colls:
            GPIO.setup(coll, GPIO.OUT)
            GPIO.output(coll, 1)

    def get_input(self):
        """check if state low on any row on any button """
        for coll in self._colls:
            GPIO.output(coll, 0)
            for row, maping in zip(self._rows, self._mapping):
                if GPIO.input(row) == 0:
                    self._action = maping
                    self._pressed = row
                    print("pressed {} {}".format(row, maping))
                    return(True)
            GPIO.output(coll, 1)
        return(False)

    def process_input(self, rgb):
        """ lock button while pressed, advance colours, modulo """
        while GPIO.input(self._pressed) == 0:
            pass
        time.sleep(0.1) 
        print((self._pressed, self._action))
        if self._action == 'off':
            num = 0
        if self._action == 'forward':
            num = rgb[0] + rgb[1] * 2 + rgb[2] * 4 
            print(num)
            num = abs((num + 1) % 8)
            print(num)
        if self._action == 'backward':
            num = rgb[0] + rgb[1] * 2 + rgb[2] * 4 
            num = abs((num - 1) % 8)
        binary = "%03d" % int(bin(num)[2:])
        r = bool(int(binary[0]))
        g = bool(int(binary[1]))
        b = bool(int(binary[2]))
        return self.states[num]
