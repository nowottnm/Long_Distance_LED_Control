import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button, RGBLED
from colorzero import color
from random import random as rand
from RaspiController.message_parser.parser import EmailInterface as emailparser
from RaspiController.Raspi_Gpio.gpio import RaspiGPIO as raspi
import json

def main():
    config = json.load(open(('~/Desktop/raspi_config.json')))
    hardware = config['gpio_setup']
    connection = config['connection']
    rpi = raspi(**hardware)
    mail = emailparser(**connection)
    while
