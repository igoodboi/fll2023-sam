# LEGO type:standard slot:0 autostart

from spike_py import PrimeHub, LightMatrix, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike_py.control import wait_for_seconds, wait_until, Timer
from math import *

# initalize
hub = PrimeHub()
wheels = MotorPair('B', 'A')
wheel = Motor('B')
leftCSensor = ColorSensor('F')
rightCSensor = ColorSensor('E')
bumper = ForceSensor('D')
timer = Timer()

perimeter = 3.14159 * 56
print(perimeter)

# functions


def line_follower(time, speed, distance):
    # if you see a black go start_tank.move(20,-20) until u see white
    timer.reset()
    distance1 = 0
    while timer.now() < time and distance1 < distance:
        diff = deviation()
        wheels.start_tank(speed - diff, speed + diff)
        if bumper.is_pressed():
            break
        # degrees = wheel.get_degrees_counted()
        distance1 = speed * timer.now() * 0.5
        # print(timer.now())
    wheels.stop()


def deviation():
    # when dieviate to the left, return value negative
    # when ddeviate to the right, return value positive
    leftLight = leftCSensor.get_reflected_light()
    rightLight = rightCSensor.get_reflected_light()
    diff = rightLight - leftLight
    return diff


# program
line_follower(time = 800, speed=30, distance = 80)
