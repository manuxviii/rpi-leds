import gpio
import time
import div

def fade(pwm, old_color, new_color):
    """fade from a color to another"""

    old_color = div.color_to_dict(old_color)
    new_color = div.color_to_dict(new_color)

    i = 0
    steps = 500
    while i < steps:
        old_color = {
            "red": (old_color["red"] + (new_color["red"] - old_color["red"]) / steps),
            "green": (old_color["green"] + (new_color["green"] - old_color["green"]) / steps),
            "blue": (old_color["blue"] + (new_color["blue"] - old_color["blue"]) / steps)
        }
        gpio.pwm_change_cycle(pwm, dec_color=old_color)
        time.sleep(0.005)
        i += 1
        # TODO: reglage timer par utilisateur

def fade_loop(pin, jsn, old_color="#000000"):
    """fade between all color sets in jsn["colors"]"""

    pwm = gpio.gpio_init(pin, jsn["config"]["frequence"])

    while True:
        i = 0
        while i < len(jsn["colors"]):
            color = div.is_random(jsn["colors"][str(i)])
            fade(pwm, old_color, color)
            old_color = color
            i += 1

def flash(pin, jsn):
    """switch abruptely between all color in jsn[frequence]"""
    pwm = gpio.gpio_init(pin, jsn["config"]["frequence"])
    while True:
        for color in jsn["colors"]:
            gpio.pwm_change_cycle(pwm, div.is_random(jsn["colors"][color]))
            time.sleep(int(jsn["config"]["speed"]))
