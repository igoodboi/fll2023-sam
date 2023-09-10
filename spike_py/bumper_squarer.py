from spike_py import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike_py.control import wait_for_seconds, wait_until, Timer
from math import *
from spike_py.operator import equal_to
# initalize
hub = PrimeHub()
wheels = MotorPair('A', 'B')
leftboi = ColorSensor('F')
rightboi = ColorSensor('E')
hub.light_matrix.show_image('DUCK')

def sensed_color():
    return leftboi.get_reflected_light()<80 or rightboi.get_reflected_light()<80

def color_equal():
    return abs(leftboi.get_reflected_light() - rightboi.get_reflected_light())<3

def line_square(speed):
    wheels.start(0, speed)
    wait_until(sensed_color)
    if leftboi.get_color()=='black':
        wheels.start_tank(speed,5)
        wait_until(color_equal)
        wheels.stop()
    else:
        wheels.start_tank(5,0)
        wait_until(color_equal)
        wheels.stop()
    l1 = leftboi.get_reflected_light()
    r1 = rightboi.get_reflected_light()
    wheels.start(0,5)
    wait_for_seconds(2)
    wheels.stop()
    l2 = leftboi.get_reflected_light()
    r2 = rightboi.get_reflected_light()
    wheels.start(0,-5)
    wait_for_seconds(2)
    wheels.stop()
    if (l1 - l2) * (r1 - r2)>0:
        wheels.stop()
    else:
        wheels.move_tank(5,'cm',-10,10)

line_square(-10)
