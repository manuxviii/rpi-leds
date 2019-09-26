#!/usr/bin/env python3

PIN_RED = 17
PIN_GREEN = 22
PIN_BLUE = 27
FREQUENCE = 100

import simplejson
import effects
import asyncio
import json
import multiprocessing
import gpio
import RPi.GPIO as GPIO
from time import sleep

async def main():
    task = None
    oldjsn = None

    # initialisation du gpio
    gpio.gpio_init(PIN_RED, PIN_GREEN, PIN_BLUE)

    # creation des signaux pwm
    red_pwm = GPIO.PWM(PIN_RED, FREQUENCE)
    green_pwm = GPIO.PWM(PIN_GREEN, FREQUENCE)
    blue_pwm = GPIO.PWM(PIN_BLUE, FREQUENCE)

    # demarrage des signaux pwm. leds eteintes
    red_pwm.start(250/2.55)
    green_pwm.start(250/2.55)
    blue_pwm.start(250/2.55)

    while True:
        # recuperation du fichier json
        jsn = json.get_json("http://web/color.json")

        try:
            # si la couleur change, on update
            if jsn != oldjsn:
                # si une tache est en cours, on la supprime
                if task != None:
                    task.terminate()

                if jsn["config"]["mode"] == "fixe":
                    gpio.pwm_change_cycle(red_pwm, green_pwm, blue_pwm, jsn["colors"]["0"])
                    task = None
                elif jsn["config"]["mode"] == "fade":
                    task = asyncio.create_task(effects.fade(red_pwm, green_pwm, blue_pwm, jsn))
                elif jsn["config"]["mode"] == "flash":
                    # task = asyncio.Task(effects.flash(red_pwm, green_pwm, blue_pwm, jsn))
                    task = multiprocessing.Process(target=effects.flash, args=(red_pwm, green_pwm, blue_pwm, jsn,))
                    task.start()
                else:
                    raise("error")
        except Exception as e:
            print("error")
            print(e)
            task = None
            gpio.pwm_change_cycle(red_pwm, green_pwm, blue_pwm, "#000000")

        oldjsn = jsn
        sleep(2)

asyncio.run(main())
