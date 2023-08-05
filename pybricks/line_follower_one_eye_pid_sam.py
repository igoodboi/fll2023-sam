from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from umath import *
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
# Initialize a motor on port A.
lmotor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
rmotor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
wheels = DriveBase(left_motor=lmotor, right_motor=rmotor, wheel_diameter=56, axle_track=80)
eye = ColorSensor(Port.C)
eye.detectable_colors([Color.BLACK, Color.WHITE])
default_speed = 70
target = 70
p = 65
i = 0.0
d = 0.0


def start_tank(left_speed, right_speed):
    speed = (right_speed + left_speed) / 2
    turn_rate = (right_speed - left_speed) / 80
    wheels.drive(speed, turn_rate)


def gain(signal):
    error = signal - target
    diff = error * p

    return default_speed + diff, default_speed - diff


def line_follower():
    while True:
        signal = eye.reflection()
        lspeed, rspeed = gain(signal)
        start_tank(lspeed, rspeed)


line_follower()
