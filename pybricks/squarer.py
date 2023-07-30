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
bumper = ForceSensor(Port.D)

target_reflection = 50
default_turn_rate = -50
default_speed = -30


def touch_line():
    while leftboi.reflection() >= target_reflection and rightboi.reflection() >= target_reflection:
        wheels.drive(default_speed, 0)


touch_line()
while leftboi.reflection() >= target_reflection:
    wheels.drive(0, -default_turn_rate)
    touch_line()
while rightboi.reflection() >= target_reflection:
    wheels.drive(0, default_turn_rate)
    touch_line()
