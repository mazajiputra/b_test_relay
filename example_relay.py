#!/usr/bin/python
import RPi.GPIO as GPIO 
from time import sleep 
Relay1_GPIO = 12
Relay2_GPIO = 16 
Relay3_GPIO = 20
Relay4_GPIO = 21
GPIO.output(Relay1_GPIO, GPIO.LOW)  
GPIO.output(Relay2_GPIO, GPIO.LOW) 
GPIO.output(Relay3_GPIO, GPIO.LOW)  
GPIO.output(Relay4_GPIO, GPIO.LOW)  
sleep(1) 