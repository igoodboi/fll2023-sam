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
    while True:
        lsignal = leftboi.get_reflected_light() - target
        rsignal = rightboi.get_reflected_light() - target
        if leftboi.get_color() == 'black' == rightboi.get_color() and abs(lsignal-rsignal)<3:
            wheels.stop()
            break
        lspeed = gain(lsignal)
        rspeed = gain(rsignal)
        if lsignal < 10 and rsignal < 10:
            wheels.start_tank(lspeed // 4, rspeed // 4)
        else:
            wheels.start_tank(lspeed, rspeed)
    print('Done')

history = []
def gain(signal):
    p = int(-signal * .5)

    return p

line_square()