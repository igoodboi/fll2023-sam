from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from umath import *
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
lmotor = Motor(Port.C, positive_direction=Direction.CLOCKWISE)
rmotor = Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
wheels = DriveBase(left_motor=lmotor, right_motor=rmotor, wheel_diameter=56, axle_track=80)
eye = ColorSensor(Port.A)
eye.detectable_colors([Color.BLACK, Color.WHITE])
clock = StopWatch()
margin = 1000
slow_tingy = 70
default_speed = 70
target = 70
p = 65


def start_tank(left_speed, right_speed):
    speed = (right_speed + left_speed) / 2
    turn_rate = (right_speed - left_speed) / 80
    wheels.drive(speed, turn_rate)


def gain(signal):
    error = signal - target
    diff = error * p
    if diff < -margin or diff > margin:
        speed = slow_tingy
    else:
        speed = default_speed
    return speed + diff, speed - diff


def line_follower(distance, time):
    while wheels.distance() < distance and clock.time() < time:
        signal = eye.reflection()
        lspeed, rspeed = gain(signal)
        start_tank(lspeed, rspeed)
    wheels.stop()


line_follower(300000, time=50000)
