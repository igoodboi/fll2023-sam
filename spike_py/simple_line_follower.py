# LEGO type:standard slot:0 autostart

from spike_py import PrimeHub, LightMatrix, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike_py.control import wait_for_seconds, wait_until, Timer
from math import *

# initalize
hub = PrimeHub()
wheels = MotorPair('B', 'A')
leftCSensor = ColorSensor('F')
rightCSensor = ColorSensor('E')
bumper = ForceSensor('D')

perimeter = pi * 56

# functions


def line_follower(speed):
    # if you see a black go start_tank.move(20,-20) until u see white

    while True:
        diff = deviation()
        wheels.start_tank(speed - diff, speed + diff)
        if bumper.is_pressed():
            wheels.stop()


def deviation():
    # when dieviate to the left, return value negative
    # when ddeviate to the right, return value positive
    leftLight = leftCSensor.get_reflected_light()
    rightLight = rightCSensor.get_reflected_light()
    diff = rightLight - leftLight
    return diff


# program
line_follower(speed=30)
