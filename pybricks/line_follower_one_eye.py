from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from umath import *
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
# Initialize a motor on port A.
lmotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
rmotor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
wheels = DriveBase(left_motor=lmotor, right_motor=rmotor, wheel_diameter=56, axle_track=80)
eye = ColorSensor(Port.C)
eye.detectable_colors([Color.BLACK, Color.WHITE])

goal = 60
lowest = 20
default_speed = 150
error_margin = 10
p, i, d = 50, .0, 0

len_hist = 10
history = [goal]


def rectify(error):
    pass


def gain(signal):
    error = signal - goal
    history.append(error)
    if len(history) > len_hist:
        history.pop(0)
    diff = p * error + i * sum(history)
    speed = default_speed * exp(-pow(error / error_margin, 2))
    return speed - diff, speed + diff


def start_tank(left_speed, right_speed):
    speed = (right_speed + left_speed) / 2
    turn_rate = (right_speed - left_speed) / 80
    # print(left_speed, right_speed, speed, turn_rate)
    wheels.drive(speed, turn_rate)


def line_follower():
    # if u see black go 'drive' until u see white
    while True:
        c = eye.color()
        r = eye.reflection()
        history.append(r)
        if len(history) > 50:
            history.pop(0)
        signal = eye.reflection()
        left_speed, right_speed = gain(signal)
        start_tank(left_speed, right_speed)


# program
line_follower()
