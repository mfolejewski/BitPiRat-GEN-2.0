import RPi.GPIO as GPIO
from time import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
GPIO.output(13, GPIO.LOW)

GPIO.output(22, GPIO.HIGH)
sleep(1)
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.HIGH)
sleep(1)
GPIO.output(27, GPIO.LOW)


for x in range(5000):
	GPIO.output(13, GPIO.HIGH)
	sleep(0.00005)
	GPIO.output(13, GPIO.LOW)
	sleep(0.00005)

GPIO.output(13, GPIO.LOW)