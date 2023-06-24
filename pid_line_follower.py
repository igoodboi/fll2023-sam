# LEGO type:standard slot:0 autostart

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

# initalize
hub = PrimeHub()
wheels = MotorPair('B', 'A')
leftCSensor = ColorSensor('F')
rightCSensor = ColorSensor('E')
bumper = ForceSensor('D')

perimeter = pi * 56


# functions
def deviation():
    # when dieviate to the left, return value negative
    # when ddeviate to the right, return value positive
    leftLight = leftCSensor.get_reflected_light()
    rightLight = rightCSensor.get_reflected_light()
    diff = rightLight - leftLight
    return diff


history = [0]


def gain(signal):
    p = signal * 0.2
    d = (signal - history[-1]) * 0.0
    history.append(signal)
    if len(history) > 5:
        history.pop(0)
    # print(len(history))
    i = sum(history) * 0.15
    return int(p + i + d)


def line_follower(speed):
    # if you see a black go start_tank.move(20,-20) until u see white
    while True:
        signal = deviation()
        diff = gain(signal)
        wheels.start_tank(speed - diff, speed + diff)
        if bumper.is_pressed():
            wheels.stop()


# program
line_follower(speed=30)
