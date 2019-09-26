import gpio
import time

# testing. a implementer
async def fade(red_pwm, green_pwm, blue_pwm, jsn):
    gpio.pwm_change_cycle(red_pwm, green_pwm, blue_pwm, "#ffffff")

def flash(red_pwm, green_pwm, blue_pwm, jsn):
    while True:
        for color in jsn["colors"]:
            print("color : ", jsn["colors"][color])
            gpio.pwm_change_cycle(red_pwm, blue_pwm, green_pwm, jsn["colors"][color])
            time.sleep(int(jsn["config"]["speed"]))
