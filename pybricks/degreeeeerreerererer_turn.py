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
lmotor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
rmotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
wheels = DriveBase(left_motor=lmotor, right_motor=rmotor, wheel_diameter=56, axle_track=60)
leftboi = ColorSensor(Port.F)
rightboi = ColorSensor(Port.E)
ik = 0.01
pk = 1
def turn(angle):
    init_angle = hub.imu.heading()
    target = angle + init_angle
    history = 0

    while True:
        hub_imu = hub.imu.heading()
        diff = hub_imu - target
        history += diff
        print(init_angle, hub_imu, target, history, diff)
        if diff < 0:
            wheels.turn(diff * pk + history * ik)
            # wheels.turn(-10)
        else:
            break

# while True:
    # print(hub.imu.heading())
turn(90)