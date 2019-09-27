import RPi.GPIO as GPIO
import div

def gpio_init(pin, frq, hex_color="#000000", dec_color=None):
    """This function initialisation the gpio functions.
    It take as parameters the 3 pins used for controlling the leds"""

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(pin["red"], GPIO.OUT)
    GPIO.setup(pin["green"], GPIO.OUT)
    GPIO.setup(pin["blue"], GPIO.OUT)

    # creation des signaux pwm
    pwm = {
        "red": GPIO.PWM(pin["red"], frq),
        "green": GPIO.PWM(pin["green"], frq),
        "blue": GPIO.PWM(pin["blue"], frq)
    }

    # demarrage des signaux pwm
    if dec_color == None:
        dec_color = div.color_to_dict(hex_color)
    pwm["red"].start(dec_color["red"]/2.55)
    pwm["green"].start(dec_color["green"]/2.55)
    pwm["blue"].start(dec_color["blue"]/2.55)

    return pwm


def pwm_change_cycle(pwm, hex_color=None, dec_color=None):
    """This function change the pwm cycle.
    It take an (hexa)decimal value as parameter and the leds pins
    If no color is pass, a random color will be set"""

    if (dec_color == None) and (hex_color == None):
        dec_color = div.random_color()
    if dec_color == None:
        dec_color = div.color_to_dict(hex_color)
    pwm["red"].ChangeDutyCycle(dec_color["red"]/2.55)
    pwm["green"].ChangeDutyCycle(dec_color["green"]/2.55)
    pwm["blue"].ChangeDutyCycle(dec_color["blue"]/2.55)
