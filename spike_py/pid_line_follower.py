# LEGO type:standard slot:0 autostart

from spike_py import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike_py.control import wait_for_seconds, wait_until, Timer
from math import *

# initalize
hub = PrimeHub()
wheels = MotorPair('B', 'A')
left_wheel = Motor('B')
right_wheel = Motor('A')
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
    # p is proportional feed back
    d = (signal - history[-1]) * 0.0
    # d = 0 cuz we dont need it
    history.append(signal)
    if len(history) > 5:
        history.pop(0)
    # print(len(history))
    i = sum(history) * 0.15
    return int(p + i + d)
# gain factor 3 o' em

def manuver():
    left_speed = left_wheel.get_speed()
    left_wheel.run_to_position(180, speed=left_speed)
    right_speed = right_wheel.get_speed()
    right_wheel.run_to_position(180, speed=right_speed)
    wheels.move_tank(180, 'degrees', left_speed, -right_speed)

def line_follower(speed):
    # if you see a black go start_tank.move(20,-20) until u see white
    while True:
        signal = deviation()
        diff = gain(signal)
        wheels.start_tank(speed - diff, speed + diff)
        if bumper.is_pressed():
            manuver()


# program
line_follower(speed=40)