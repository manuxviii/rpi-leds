import RPi.GPIO as GPIO

def gpio_init(pin_red, pin_green, pin_blue):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(pin_red, GPIO.OUT)
    GPIO.setup(pin_green, GPIO.OUT)
    GPIO.setup(pin_blue, GPIO.OUT)

def pwm_change_cycle(red_pwm, green_pwm, blue_pwm, color):
    red_pwm.ChangeDutyCycle(int(color[1:3], 16)/2.55)
    green_pwm.ChangeDutyCycle(int(color[3:5], 16)/2.55)
    blue_pwm.ChangeDutyCycle(int(color[5:7], 16)/2.55)
