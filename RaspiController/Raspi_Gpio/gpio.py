import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button, RGBLED
from colorzero import color
from random import random as rand

class RaspiGPIO(object):
    """ raspi gpio pin """

    def __init__(self, button, red, green, blue):
        # reveive pin location
        self.button = button
        self.red = red
        self.green = green
        self.blue = blue
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(red, GPIO.OUT)
        GPIO.setup(green, GPIO.OUT)
        GPIO.setup(blue, GPIO.OUT)
        self.led(False, False, False) # inti as off
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def led(self, boolred, boolgreen, boolblue):
        """ set led pins to value """
        GPIO.output(self.red, boolred)
        GPIO.output(self.green, boolgreen)
        GPIO.output(self.blue, boolblue)

    def button(self):
        """ get button state """
        return(GPIO.input(self.button) == GPIO.HIGH)
