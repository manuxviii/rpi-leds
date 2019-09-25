import gpio
import asyncio

async def fade(red_pwm, green_pwm, blue_pwm, jsn):
    gpio.pwm_change_cycle(red_pwm, green_pwm, blue_pwm, "#ffffff")
    pass

async def flash(jsn):
    pass
