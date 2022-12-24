import RPi.GPIO as gpio
import time
from motor import Motor as motor

# 11,12  13,15,  21,23,  29,31,  33,35,  37,40  
class drive:
    def __init__(self, pins: list = [40,37,  35,33,  29,31,  12,11,  15,13,  21,23]):
        self.motor1 = motor(pins[0], pins[1])
        self.motor2 = motor(pins[2], pins[3])
        self.motor3 = motor(pins[4], pins[5])
        self.motor4 = motor(pins[6], pins[7])
        self.motor5 = motor(pins[8], pins[9])
        self.motor6 = motor(pins[10], pins[11])

    def forward(self, speed=100):
        self.motor1.forward(speed)
        self.motor2.forward(speed)
        self.motor3.forward(speed)
        self.motor4.forward(speed)
        self.motor5.forward(speed)
        self.motor6.forward(speed)

    def backward(self, speed=100):
        self.motor1.backward(speed)
        self.motor2.backward(speed)
        self.motor3.backward(speed)
        self.motor4.backward(speed)
        self.motor5.backward(speed)
        self.motor6.backward(speed)

    def stop(self):
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()
        self.motor5.stop()
        self.motor6.stop()

    def cleanup(self):
        self.motor1.cleanup()
        self.motor2.cleanup()
        self.motor3.cleanup()
        self.motor4.cleanup()
        self.motor5.cleanup()
        self.motor6.cleanup()

    def turn_left(self):
        self.motor1.forward(50)
        self.motor2.forward(50)
        self.motor3.forward(50)
        self.motor4.forward(0)
        self.motor5.forward(0)
        self.motor6.forward(0)

    def turn_right(self):
        self.motor1.forward(0)
        self.motor2.forward(0)
        self.motor3.forward(0)
        self.motor4.forward(50)
        self.motor5.forward(50)
        self.motor6.forward(50)

    def adjust_left(self):
        self.motor1.forward(90)
        self.motor2.forward(90)
        self.motor3.forward(90)
        self.motor4.forward(100)
        self.motor5.forward(100)
        self.motor6.forward(100)

    def adjust_right(self):
        self.motor1.forward(100)
        self.motor2.forward(100)
        self.motor3.forward(100)
        self.motor4.forward(90)
        self.motor5.forward(90)
        self.motor6.forward(90)


if __name__ == '__main__':
    drive = drive()
    drive.forward(100)
    time.sleep(2)
    drive.backward(100)
    time.sleep(2)
    drive.stop()
    time.sleep(2)
    drive.turn_left()
    time.sleep(2)
    drive.turn_right()
    time.sleep(2)
    drive.stop()
    drive.cleanup()
