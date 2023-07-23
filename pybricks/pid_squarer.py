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
leftboi =  ColorSensor(Port.F)
rightboi = ColorSensor(Port.E)

target = 80
def sensed_color():
    return leftboi.reflection()<target or rightboi.reflection()<target

def color_equal():
    return abs(leftboi.reflection() - rightboi.reflection())<3
def wait_until(condition):
    while not condition():
        pass
def line_square(speed):
    # step1 we want to move to the target, once we hit the target we stop, isint it
    wheels.drive(speed,0)
    wait_until(sensed_color)
    wheels.stop()
    # step2 we want to move the other wheel so that it is squared to the line using pid controls system
    pid_squar()
def pid_squar():
    pass
def gain(signal):
    p = [signal]
    pass








    print(leftboi.color())
    print(rightboi.color())
    #
    if leftboi.color()==Color.NONE:
        wheels.drive(0,5)
        wait_until(color_equal)
        wheels.stop()
    else:
        wheels.drive(0,-5)
        wait_until(color_equal)
        wheels.stop()
        l1 = leftboi.reflection()
        r1 = rightboi.reflection()
        wheels.drive(5,0)
        wait(1000)
        wheels.stop()
        l2 = leftboi.reflection()
        r2 = rightboi.reflection()
        wheels.drive(-5,0)
        wait(1000)
        wheels.stop()
        diff = (l1-l2)-(r1-r2)
        print(diff)
        if diff<2:
            wheels.stop()
        else:
            wheels.drive(0,diff)
            wait(1000)
            wheels.stop()
line_square(100)
print('doyee')
