import RPi.GPIO as gpio
import time

class Motor:
    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        gpio.setmode(gpio.BOARD)
        # pwm pins pin1 pin2
        gpio.setup(self.pin1, gpio.OUT)
        gpio.setup(self.pin2, gpio.OUT)
        self.pwm1 = gpio.PWM(self.pin1, 100)
        self.pwm2 = gpio.PWM(self.pin2, 100)
        self.pwm1.start(0)
        self.pwm2.start(0)

    def forward(self, speed=100):
        self.pwm1.ChangeDutyCycle(speed)
        self.pwm2.ChangeDutyCycle(0)

    def backward(self, speed=100):
        self.pwm1.ChangeDutyCycle(0)
        self.pwm2.ChangeDutyCycle(speed)

    def stop(self):
        self.pwm1.ChangeDutyCycle(0)
        self.pwm2.ChangeDutyCycle(0)

    def cleanup(self):
        gpio.cleanup()

if __name__ == '__main__':
    motor = Motor(11, 13)
    motor.forward(100)
    time.sleep(2)
    motor.backward(100)
    time.sleep(2)
    motor.stop()
    motor.cleanup()

    