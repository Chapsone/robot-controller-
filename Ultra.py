#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG1 = 23
ECHO1 = 24
TRIG2 = 14
ECHO2 = 15

print("Disatance measurement In progress")

GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)

GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)

GPIO.output(TRIG1, False)
GPIO.output(TRIG2, False)
print("waitting for 0.5s ")
time.sleep(0.5)

def distances():

    GPIO.output(TRIG1, True)
    time.sleep(0.00001)
    GPIO.output(TRIG1, False)

    while GPIO.input(ECHO1) == 0:
        pulse_start_1 = time.time()

    while GPIO.input(ECHO1) == 1:
        pulse_end_1 = time.time()

    pulse_duration_1 = pulse_end_1 - pulse_start_1 
    distance_1 = pulse_duration_1 * 17150
    distance_1 = round( distance_1, 2)

    GPIO.output(TRIG2, True)
    time.sleep(0.00001)
    GPIO.output(TRIG2, False)

    while GPIO.input(ECHO2) == 0:
        pulse_start_2 = time.time()

    while GPIO.input(ECHO2) == 1:
        pulse_end_2 = time.time()

    pulse_duration_2 = pulse_end_2 - pulse_start_2 
    distance_2 = pulse_duration_2 * 17150
    distance_2 = round( distance_2, 2)

    print ("la distance est: " + str(distance_1))
    print ("la distance est: " + str(distance_2))
    return(distance_1,distance_2)

dist1,dist2 = distances()
print ("la distance est11: " + str(dist1))
print ("la distance est22: " + str(dist2))
GPIO.cleanup()


