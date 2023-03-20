#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

LED_PIN = 23
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(LED_PIN, GPIO.LOW)
time.sleep(0.5)

GPIO.cleanup()
