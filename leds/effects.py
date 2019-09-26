import gpio
import time

def fixe(pin, color, frq):
    pwm = gpio.gpio_init(pin, frq)
    gpio.pwm_change_cycle(pwm, color)

async def fade(pin, old_color, new_color):
    # while
    pass

def flash(pin, jsn):
    pwm = gpio.gpio_init(pin, jsn["config"]["frequence"])
    while True:
        for color in jsn["colors"]:
            gpio.pwm_change_cycle(pwm, jsn["colors"][color])
            time.sleep(int(jsn["config"]["speed"]))
