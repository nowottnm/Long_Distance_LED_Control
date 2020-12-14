import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button, RGBLED
from colorzero import color
from random import random as rand
from RaspiController.message_parser.parser import EmailInterface as emailparser
from RaspiController.Raspi_Gpio.gpio import RaspiGPIO as raspi
import random
import json

def rnd():
    return(random.random() > 0.5)

def main():
    config = json.load(open(('~/Desktop/raspi_config.json')))
    hardware = config['gpio_setup']
    connection = config['connection']
    rpi = raspi(**hardware)
    mail = emailparser(**connection)
    rgb = [True, True, True]# init white
    def button_callback(channel):
        mail.send_message([rnd(), rnd(), rnd()])
    GPIO.add_event_detect(rpi.button, GPIO.RISING,callback=button_callback)
    while(True):
        rgb_new = mail.receive_message()
        if rgb_new:
            rgb = rgb_new
        rpi.led(rgb)
        sleep(60)
