import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button, RGBLED
from colorzero import color
from random import random as rand
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)
row = [31, 33, 35]
coll =[37]
for i in range(len(row)):
	GPIO.setup(row[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
for j in range(len(coll)):
	GPIO.setup(coll[j], GPIO.OUT)
	GPIO.output(coll[j],1)
button_message = "Button was pushed"
#GPIO.cleanup()
#led = RGBLED(red=36, green=38, blue=40)
#button = Button(8)
while True:
	try:
		for j in coll:
			GPIO.output(j,0)
			for i in row:
				if GPIO.input(i)==0:
					print((i,j))
			GPIO.output(j,1)
	except Exception as e:
		print(e)
		GPIO.cleanup()
		exit(1)


