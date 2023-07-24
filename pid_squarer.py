from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
from spike.operator import equal_to
# initalize
hub = PrimeHub()
# wheels = MotorPair('A', 'B')
lmotor = Motor('A')
rmotor = Motor('B')
wheels = MotorPair('A', 'B')
leftboi = ColorSensor('E')
rightboi = ColorSensor('F')
hub.light_matrix.show_image('DUCK')
target = 60


def line_square():
    count = 0
    while True:
        lsignal = leftboi.get_reflected_light() - target
        rsignal = rightboi.get_reflected_light() - target
        if leftboi.get_color() == 'black' == rightboi.get_color() and  abs(lsignal-rsignal)<3 or count > 5:
            wheels.stop()
            break
        lspeed = gain(lsignal)
        rspeed = gain(rsignal)
        if lsignal < 10 and rsignal < 10:
            count += 1
            wheels.start_tank(lspeed // 3, rspeed // 3)
        else:
            wheels.start_tank(lspeed, rspeed)
    print('Done')


def gain(signal):
    p = signal * .5
    # p is proportional feed back
    d = (signal - history[-1]) * 0.
    # d = 0 cuz we dont need it
    history.append(signal)
    if len(history) > 10:
        history.pop(0)
    # print(len(history))
    i = sum(history) * 0.0
    # return -int(p + i + d)
    return -int(p)

history = [0]
line_square()