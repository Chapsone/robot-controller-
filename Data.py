#!/usr/bin/env python3
import numpy as np

from gpiozero import AngularServo
import time 
servo1 = AngularServo(20, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo2 = AngularServo(21, min_pulse_width=0.0006, max_pulse_width=0.0023)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
TRIG1 = 23
ECHO1 = 24
TRIG2 = 14
ECHO2 = 15

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

    return(distance_1,distance_2)

def servo(s1,s2):
    servo1.angle = s1
    servo2.angle = s2

def main():
    s1 = 0
    s2 = 90

    servo(s1, s2)
    dist1,dist2 = distances()

    print("angle1: " + str(s1) + " , distance1: " + str(dist1) )
    print("angle2: " + str(s2) + " , distance1: " + str(dist2) )

if __name__=='__main__':
    main() 




