import RPi.GPIO as GPIO
import div

def gpio_init(pin, frq, hex_color="#000000", dec_color=None):
    """This function initialisation the gpio functions.
    It take as parameters the 3 pins used for controlling the leds"""

    pwm = {}

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(pin["red"], GPIO.OUT)
    GPIO.setup(pin["green"], GPIO.OUT)
    GPIO.setup(pin["blue"], GPIO.OUT)

    # creation des signaux pwm
    pwm[1] = GPIO.PWM(pin["red"], frq)
    pwm[2] = GPIO.PWM(pin["green"], frq)
    pwm[3] = GPIO.PWM(pin["blue"], frq)

    # demarrage des signaux pwm
    if dec_color == None:
        dec_color = div.color_to_dict(hex_color)
    pwm[1].start(dec_color["red"]/2.55)
    pwm[2].start(dec_color["green"]/2.55)
    pwm[3].start(dec_color["blue"]/2.55)

    return pwm


def pwm_change_cycle(pwm, hex_color=None, dec_color=None):
    """This function change the pwm cycle.
    It take an (hexa)decimal value as parameter and the leds pins"""

    if (dec_color == None) and (hex_color == None):
        dec_color = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
    if dec_color == None:
        dec_color = div.color_to_dict(hex_color)
    pwm[1].ChangeDutyCycle(dec_color["red"]/2.55)
    pwm[2].ChangeDutyCycle(dec_color["green"]/2.55)
    pwm[3].ChangeDutyCycle(dec_color["blue"]/2.55)
