#!/usr/bin/env python3

import simplejson
import effects
import json
import multiprocessing
import gpio
import time


task = {}
oldjsn = None

while True:
    # recuperation du fichier json
    jsn = json.get_json("http://web/color.json")

    try:
        if jsn != oldjsn:
            if oldjsn != None:
                while len(jsn) < len(oldjsn):
                    task[len(oldjsn)].terminate()
                    task.pop(len(jsn))

                    for pingroup in jsn:
                        if jsn[pingroup] != oldjsn[pingroup]:
                            task[int(pingroup)].terminate()
                            task[int(pingroup)] = multiprocessing.Process(target=effects.strip, args=(jsn[pingroup],))
                            task[int(pingroup)].start()
            else:
                for pingroup in jsn:
                    task[int(pingroup)] = multiprocessing.Process(target=effects.strip, args=(jsn[pingroup],))
                    task[int(pingroup)].start()

        jsn = oldjsn

    except Exception as e:
        print("error", e)
        for tsk in task:
            task[tsk].terminate()
        for pingroup in jsn:
            gpio.gpio_init(jsn[pingroup])

    time.sleep(2)
