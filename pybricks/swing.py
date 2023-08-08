from pybricks.geometry import Axis
from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
lmotor = Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
rmotor = Motor(Port.C, positive_direction=Direction.CLOCKWISE)
wheels = DriveBase(left_motor=lmotor, right_motor=rmotor, wheel_diameter=56, axle_track=80)

distance = 20
default_speed = 1000
wheels.settings(straight_speed=default_speed, straight_acceleration=default_speed)
delta_angle = 5
delta_speed = 5


def swing():
    while True:
        omega = hub.imu.angular_velocity(Axis.X)
        _, tilt = hub.imu.tilt()
        angle = lmotor.angle()
        phi = tilt - angle
        # print('{omega:+04.0f}, {tilt:+04.0f}, {angle:+04.0f}'.format(omega=omega, tilt=tilt, angle=phi))
        if abs(omega) < delta_speed:
            sign = -1 if phi < 0 else 1
            wheels.straight(sign * distance)
        elif abs(phi) < delta_angle:
            sign = -1 if omega < 0 else 1
            wheels.straight(sign * distance)


swing()
