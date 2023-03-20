#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print("Disatance measurement In progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("waitting for 2s ")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.output(ECHO) == 0:
    pulse_start = time.time()

while GPIO.output(ECHO) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start 
distance = pulse_duration * 17150
distance = round( distance, 2)
print ("la distance est: " + str(distance))

GPIO.cleanup()

