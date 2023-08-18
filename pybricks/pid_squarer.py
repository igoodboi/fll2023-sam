from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
# Initialize a motor on port A.
lmotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
rmotor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
wheels = DriveBase(left_motor=lmotor, right_motor=rmotor, wheel_diameter=56, axle_track=80)
leftboi = ColorSensor(Port.F)
rightboi = ColorSensor(Port.E)

target = 30
speed = 20

def start_tank(left_speed, right_speed):
    speed = (right_speed + left_speed) / 2
    turn_rate = (right_speed - left_speed) / 80
    wheels.drive(speed, turn_rate)


def line_square():
    count = 0
    while True:
        lsignal = leftboi.reflection() - target
        rsignal = rightboi.reflection() - target
        if abs(lsignal) + abs(rsignal) < 4 :
            print('Done squaring with error = {} after {} tries'.format(abs(lsignal) + abs(rsignal), count))
            wheels.stop()
            break
        lspeed, rspeed = gain(lsignal, rsignal)
        if abs(lsignal) < 10 or abs(rsignal) < 10:
            print('slowly tanking at {}, {}'.format(lspeed, rspeed))
            count += 1
            start_tank(lspeed // 3, rspeed // 3)
        else:
            print('tanking at {}, {}'.format(lspeed, rspeed))
            start_tank(lspeed, rspeed)


def gain(lsignal, rsignal):
    pl,pr = lsignal * pidk[0], rsignal * pidk[0]
    # p is proportional feed back
    dl,dr = (lsignal - history[0][-1]) * pidk[2], (rsignal - history[1][-1]) * pidk[2]
    history[0].append(lsignal)
    history[1].append(rsignal)
    if len(history[0]) > 100:
        history[0].pop(0)
        history[1].pop(0)
    il,ir = sum(history[0]) * pidk[1],sum(history[1]) * pidk[1]
    return int(pl + il - dl),int(pr + ir - dr)


pidk = [1, .0, .0]
history = [[0],[0]]
line_square()
