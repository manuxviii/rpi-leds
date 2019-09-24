#!/usr/bin/env python3

PIN_RED = 17
PIN_GREEN = 22
PIN_BLUE = 27
FREQUENCE = 100

import json
import RPi.GPIO as GPIO
from time import sleep

old_color = ""

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)
GPIO.setup(PIN_BLUE, GPIO.OUT)

red_pwm = GPIO.PWM(PIN_RED, FREQUENCE)
green_pwm = GPIO.PWM(PIN_GREEN, FREQUENCE)
blue_pwm = GPIO.PWM(PIN_BLUE, FREQUENCE)

red_pwm.start(250/2.55)
green_pwm.start(250/2.55)
blue_pwm.start(250/2.55)

while True:
    color = json.get_json()

    if color != old_color:
        red_pwm.ChangeDutyCycle(int(color[1:3], 16)/2.55)
        green_pwm.ChangeDutyCycle(int(color[3:5], 16)/2.55)
        blue_pwm.ChangeDutyCycle(int(color[5:7], 16)/2.55)

        old_color = color

    sleep(1)
