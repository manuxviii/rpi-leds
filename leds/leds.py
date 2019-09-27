#!/usr/bin/env python3

PIN = {
    "red": 17,
    "green": 22,
    "blue": 27
}

import simplejson
import effects
import json
import multiprocessing
import gpio
import time

def main():
    task = None
    oldjsn = None
    pwm = None

    while True:
        # recuperation du fichier json
        jsn = json.get_json("http://web/color.json")

        try:
            # si la couleur change, on update
            if jsn != oldjsn:
                # si une tache est en cours, on la supprime
                if task != None:
                    task.terminate()
                    task = None
                elif pwm != None:
                    for entry in pwm:
                        pwm[entry].stop()
                    pwm = None

                if jsn["config"]["mode"] == "fixe":
                    pwm = gpio.gpio_init(PIN, jsn["config"]["frequence"], hex_color=jsn["colors"]["0"])
                elif jsn["config"]["mode"] == "fade":
                    task = multiprocessing.Process(target=effects.fade_loop, args=(PIN, jsn))
                elif jsn["config"]["mode"] == "flash":
                    task = multiprocessing.Process(target=effects.flash, args=(PIN, jsn))
                else:
                    raise EnvironmentError

                if task != None:
                    task.start()

        except Exception as e:
            print("error")
            print(e)
            if task != None:
                task.terminate()
                task = None
            pwm = gpio.gpio_init(PIN, jsn["config"]["frequence"], hex_color="#000000")
        oldjsn = jsn
        time.sleep(2)

main()
