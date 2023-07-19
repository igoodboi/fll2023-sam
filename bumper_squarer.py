from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
from spike.operator import equal_to
hub = PrimeHub()
wheels = MotorPair('A', 'B')
leftboi = ColorSensor('F')
rightboi = ColorSensor('E')
hub.light_matrix.show_image('DUCK')

def squarer():
    return leftboi.get_color()=='black' or rightboi.get_color()=='black'
    
def line_square(speed):
    wheels.start(0, speed)
    wait_until(square)
    if leftboi.get_color()=='black':
        wheels.start_tank(-5,speed)
        wait_until(rightboi.get_color, equal_to,'black')
        wheels.stop()
    else:
        wheels.start_tank(speed,-5)
        wait_until(leftboi.get_color, equal_to,'black')
        wheels.stop()

line_square(10)