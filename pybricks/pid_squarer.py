from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
# Initialize a motor on port A.
lmotor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
rmotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
wheels = DriveBase(left_motor=lmotor, right_motor=rmotor, wheel_diameter=56, axle_track=60)
leftboi = ColorSensor(Port.F)
rightboi = ColorSensor(Port.E)

target = 80


def line_square():
    while True:
        lsignal = leftboi.reflection() - target
        lspeed = gain(lsignal)
        rsignal = rightboi.reflection() - target
        lmotor.run(lspeed)
        rspeed = gain(rsignal)
        rmotor.run(rspeed)


def gain(signal):
    return signal


line_square()
