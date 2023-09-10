"""
this is only for beta byricks
it has HEADING code!
*hub_imu = hub.imu.heading()*
https://beta.pybricks.com/
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
# Initialize a motor on port A.
drivingl = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
drivingr = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
attachtl = Motor(Port.D, positive_direction=Direction.CLOCKWISE)
attacthr = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
wheels = DriveBase(left_motor=drivingl, right_motor=drivingr, wheel_diameter=56, axle_track=60)
leftboi = ColorSensor(Port.E)
rightboi = ColorSensor(Port.C)
imu = hub.imu

default_speed = 400
swing_angle=-190

def reached_destination():
    return rightboi.color() == Color.RED and leftboi.color() == Color.WHITE

while not reached_destination():
    wheels.drive(90,0)
wheels.stop()
attachtl.run_angle(default_speed, swing_angle)
attachtl.run_angle(default_speed,-swing_angle)
# motorl.reset_angle()
# a = motorl.angle()
# while True:
#     if a != motorl.angle():
#         print(a)
#         a = motorl.angle()

wheels.straight(-400)


wheels.stop()
