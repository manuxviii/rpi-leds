import RPi.GPIO as GPIO

def gpio_init(pin, frq, color="#000000"):
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

    # demarrage des signaux pwm. leds eteintes
    pwm[1].start(int(color[1:3])/2.55)
    pwm[2].start(int(color[3:5])/2.55)
    pwm[3].start(int(color[5:7])/2.55)

    return pwm


def pwm_change_cycle(pwm, color):
    """This function change the pwm cycle.
    It take an hexadecimal value as parameter and the leds pins"""

    pwm[1].ChangeDutyCycle(int(color[1:3], 16)/2.55)
    pwm[2].ChangeDutyCycle(int(color[3:5], 16)/2.55)
    pwm[3].ChangeDutyCycle(int(color[5:7], 16)/2.55)
