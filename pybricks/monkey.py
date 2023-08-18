from pybricks.geometry import Axis
from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

hub = PrimeHub()
lmotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
rmotor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
wheels = DriveBase(left_motor=lmotor, right_motor=rmotor, wheel_diameter=56, axle_track=80)
imu = hub.imu
while True:
    print(imu.tilt())
