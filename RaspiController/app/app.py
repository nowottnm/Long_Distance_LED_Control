import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button, RGBLED
from colorzero import color
from random import random as rand
import RaspiController.message_parser.parser as parsers
import RaspiController.button.button as buttons
from RaspiController.LED.led import LedInterface
# from RaspiController.message_parser.parser import EmailInterface as emailparser
# from RaspiController.Raspi_Gpio.gpio import RaspiGPIO as raspi
import random
import json
import time


def rnd():
    return(random.random() > 0.5)


def main():
    config = json.load(open(('/home/pi/Desktop/raspi_config.json')))
    led_config = config['led_setup']
    connection_config = list(config['connection'].items())
    button_config = list(config['button'].items())
    led = LedInterface(**led_config)
    parser = getattr(parsers, connection_config[0])(**connection_config[1])
    button = getattr(buttons, button_config[0])(**button_config[1])
    rgb = parser.receive_message()
    start_time = time.time()
    while(True):
        try:
            if (time.time() - start_time) > 90:
                rgb_global = parser.receive_message()
                print("rgb in the cloud is: " + str(rgb_global))
                start_time = time.time()
                if rgb != rgb_global:
                    parser.send_message(rgb)
            if button.get_input():
                rgb = button.process_input(rgb)
            led.led(*rgb)
        except KeyboardInterrupt:
            GPIO.cleanup()
            exit(1)


if __name__ == "__main__":
    main()
