import RPi.GPIO as GPIO
from time import sleep

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# Disable Warnings
GPIO.setwarnings(False)

# Set relay pins as output
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

#Matikan dulu
GPIO.output(12, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(20, GPIO.LOW)
GPIO.output(21, GPIO.LOW)   


try:
    while (True):
        
        # Turn all relays ON
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
        # Sleep for 5 seconds
        # sleep(5) 
        # Turn all relays OFF
except KeyboardInterrupt:
# catches the ctrl-c command, breaks the loop above 
# and turns the relays off
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)   
    #Sleep for 5 seconds
    # sleep(5)