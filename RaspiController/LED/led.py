import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button, RGBLED
from colorzero import color
from random import random as rand

class LedInterface(object):
    """ raspi gpio pins for LED """

    def __init__(self, red, green, blue):
        # reveive pin location
        self.red = red
        self.green = green
        self.blue = blue
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(red, GPIO.OUT)
        GPIO.setup(green, GPIO.OUT)
        GPIO.setup(blue, GPIO.OUT)
        self.led(False, False, False) # inti as off

    def led(self, boolred, boolgreen, boolblue):
        """ set led pins to value """
        GPIO.output(self.red, boolred)
        GPIO.output(self.green, boolgreen)
        GPIO.output(self.blue, boolblue)
