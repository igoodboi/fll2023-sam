from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
# Initialize a motor on port A.
lmotor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
rmotor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
wheels = DriveBase(left_motor=lmotor, right_motor=rmotor, wheel_diameter=56, axle_track=80)
eye = ColorSensor(Port.C)
eye.detectable_colors([Color.BLACK, Color.WHITE])
goal = 40
default_speed = -100


def start_tank(left_speed, right_speed):
    speed = (right_speed + left_speed) / 2
    turn_rate = (right_speed - left_speed) / 80
    wheels.drive(speed, turn_rate)
    pass


gain = 70


def line_follower(speed):
    # if u see black go 'drive' until u see white

    while True:
        c = eye.color()
        r = eye.reflection()
        if c == Color.WHITE and r > 80:
            wheels.drive(-10, 10)
            wait(100)
        elif c == Color.BLACK and r < 20:
            wheels.drive(-10, -10)
            wait(100)

        diff = deviation() * gain
        start_tank(speed - diff, speed + diff)


# when dieviated to left return value negative
# when dieviated to right return value positive
def deviation():
    leftlight = eye.reflection()
    return leftlight - goal


# program
line_follower(speed=default_speed)
