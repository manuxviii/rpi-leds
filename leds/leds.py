#!/usr/bin/env python3

PIN_RED = 17
PIN_GREEN = 22
PIN_BLUE = 27
FREQUENCE = 100

import simplejson
import json
import gpio
import RPi.GPIO as GPIO
from time import sleep

old_color = ""

gpio.gpio_init(PIN_RED, PIN_GREEN, PIN_BLUE)

red_pwm = GPIO.PWM(PIN_RED, FREQUENCE)
green_pwm = GPIO.PWM(PIN_GREEN, FREQUENCE)
blue_pwm = GPIO.PWM(PIN_BLUE, FREQUENCE)

red_pwm.start(250/2.55)
green_pwm.start(250/2.55)
blue_pwm.start(250/2.55)

while True:
    colors = json.get_json()

    if colors["favcolor"] != old_color:
        gpio.pwm_change_cycle(red_pwm, green_pwm, blue_pwm, colors["favcolor"])

        old_color = colors["favcolor"]

    sleep(1)
