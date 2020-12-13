import RPi.GPIO as GPIO
from time import sleep
GPIO_N = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_N, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # pin 10 to input, init low
button_message = "Button was pushed"
import pdb; pdb.set_trace()
while True:
    if GPIO.input(GPIO_N) == GPIO.HIGH:
        print(button_message)
        #sleep(5)
        exit(0)
    print(GPIO.input(GPIO_N))

