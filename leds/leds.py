#!/usr/bin/env python3

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

                if jsn["0"]["config"]["mode"] == "fixe":
                    pwm = gpio.gpio_init(jsn["0"], hex_color=jsn["colors"]["0"])
                elif jsn["0"]["config"]["mode"] == "fade":
                    task = multiprocessing.Process(target=effects.fade_loop, args=(jsn["0"],))
                elif jsn["0"]["config"]["mode"] == "flash":
                    task = multiprocessing.Process(target=effects.flash, args=(jsn["0"],))
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
            pwm = gpio.gpio_init(jsn["0"], hex_color="#000000")
        oldjsn = jsn
        time.sleep(2)

main()
