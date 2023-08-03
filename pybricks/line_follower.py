from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor, ColorSensor, ForceSensor
from pybricks.robotics import DriveBase
from umath import *

hub = PrimeHub()
# Initialize a motor on port A.
lmotor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
rmotor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
wheels = DriveBase(left_motor=lmotor, right_motor=rmotor, wheel_diameter=56, axle_track=80)
leftboi = ColorSensor(Port.F)
rightboi = ColorSensor(Port.E)
bumper = ForceSensor(Port.D)

len_hist = 10
history = [0]
p, i, d = 50, .0, 0
error_margin = 40
default_speed = 150


# perimeter = pi * 56

# functions
def start_tank(left_speed, right_speed):
    speed = (right_speed + left_speed) / 2
    turn_rate = (right_speed - left_speed) / 80
    wheels.drive(speed, turn_rate)


def gain(signal):
    error = signal
    history.append(error)
    if len(history) > len_hist:
        history.pop(0)
    diff = p * error + i * sum(history)
    slow_factor = exp(-pow(error / error_margin, 2))
    speed = default_speed * slow_factor
    return speed - diff, speed + diff


def line_follower():
    # if u see black go 'drive' until u see white
    while True:
        error = deviation()
        left_speed, right_speed = gain(error)
        start_tank(left_speed, right_speed)
        if bumper.touched():
            wheels.stop()


# when dieviated to left return value negative
# when dieviated to right return value positive
def deviation():
    leftlight = leftboi.reflection()
    rightlight = rightboi.reflection()
    diff = rightlight - leftlight
    return diff


# program
line_follower()
