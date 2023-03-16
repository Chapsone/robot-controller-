#!/usr/bin/env python3
import gpiozero as gp
import time

ur_l = gp.DistanceSensor(23,24)
while True:
    dist = ur_l.distance
    print(dist)
    time.sleep(1)
