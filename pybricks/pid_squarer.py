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
leftboi = ColorSensor(Port.E)
rightboi = ColorSensor(Port.F)

target = 60


def line_square():
    while True:
        lsignal = leftboi.reflection() - target
        rsignal = rightboi.reflection() - target
        lspeed = gain(lsignal)
        rspeed = gain(rsignal)
        # if lsignal < 0.1 * target and rightboi < 0.1 * target:
            # lmotor.run(lspeed / 3)
            # rmotor.run(rspeed / 3)
        # else:
        lmotor.run(lspeed)
        rmotor.run(rspeed)
        if abs(lsignal-rsignal)<10:
            wheels.stop


def gain(signal):
    return signal


line_square()
