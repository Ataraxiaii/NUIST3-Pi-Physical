# work with the Raspberry Pi's GPIO pins 
import RPi.GPIO as GPIO
# import the Time library
import time
#tell the program which naming convention is to be used
GPIO.setmode(GPIO.BCM)
# disable GPIO warnings
GPIO.setwarnings(False)
# set GPIO18 as output
GPIO.setup(18,GPIO.OUT)
# indicate LED activation
print("LED on")
# turn LED on
GPIO.output(18,GPIO.HIGH)
# pause for 1 second
time.sleep(1)
# indicate LED deactivation
print("LED off")
# turn the LED off
GPIO.output(18,GPIO.LOW)

