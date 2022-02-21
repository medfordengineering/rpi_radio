# Sample code to demonstrate Encoder class.  Prints the value every 5 seconds, and also whenever it changes.

import subprocess
import time
import RPi.GPIO as GPIO
from encoder import Encoder

def valueChanged(value, direction):
	print("* New value: {}, Direction: {}".format(value, direction))
	sts = subprocess.Popen("mpc play " + str(value), shell=True).wait()

def volumeChanged(value, direction):
	print("* New volume: {}, Direction: {}".format(value, direction))
	sts = subprocess.Popen("mpc volume " + str(value), shell=True).wait()

GPIO.setmode(GPIO.BCM)

e1 = Encoder(17, 18, valueChanged)
e2 = Encoder(27, 22, volumeChanged)

try:
    while True:
        time.sleep(5)
        print("Value is {}".format(e1.getValue()))
except Exception:
    pass

GPIO.cleanup()



