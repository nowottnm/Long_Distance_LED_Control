import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button, RGBLED
from colorzero import color
from random import random as rand
GPIO.cleanup()
GPIO_N = 8
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.output(36, GPIO.LOW)
GPIO.output(38, GPIO.LOW)
GPIO.output(40, GPIO.LOW)
GPIO.setup(GPIO_N, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # pin 10 to input, init low
button_message = "Button was pushed"
#GPIO.cleanup()
#led = RGBLED(red=36, green=38, blue=40)
#button = Button(8)
while True:
	if GPIO.input(GPIO_N) == GPIO.HIGH:
		print(button_message)
		GPIO.output(36, GPIO.HIGH)
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(40, GPIO.HIGH)
		sleep(1500)
		#led.color=(0,0,0)

