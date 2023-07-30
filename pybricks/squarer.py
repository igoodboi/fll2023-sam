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
default_turn_rate = -30
default_speed = -30


# it just defines the www
def touch_line():
    """
    this function just makes the code less clustered and crummy
    """
    while leftboi.reflection() >= target_reflection and rightboi.reflection() >= target_reflection:
        wheels.drive(default_speed * 1.5, 0)


# now the code looks better
# touch_line()
# we dont need it because here the line 35 touch_line()
while leftboi.reflection() >= target_reflection:
    wheels.drive(0, -default_turn_rate)
    touch_line()
while rightboi.reflection() >= target_reflection:
    wheels.drive(0, default_turn_rate)
    touch_line()
'''
we need two of the 
"while leftboi.reflection() >= target_reflection:
    wheels.drive(0, -default_turn_rate)
    touch_line()"
because we need account for left tilt, and right tilt
and for both scenarios
'''
