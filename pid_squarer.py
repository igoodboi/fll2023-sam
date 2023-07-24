from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
from spike.operator import equal_to

# initalize
hub = PrimeHub()
# wheels = MotorPair('A', 'B')
lmotor = Motor('A')
rmotor = Motor('B')
wheels = MotorPair('A', 'B')
leftboi = ColorSensor('E')
rightboi = ColorSensor('F')
hub.light_matrix.show_image('DUCK')
target = 70


def line_square():
    count = 0
    while True:
        lsignal = leftboi.get_reflected_light() - target
        rsignal = rightboi.get_reflected_light() - target
        if abs(lsignal) + abs(rsignal) < 4 or count > 100:
            wheels.stop()
            break
        lspeed = gain(lsignal)
        rspeed = gain(rsignal)
        if lsignal < 3 and rsignal < 3:
            count += 1
            wheels.start_tank(lspeed // 3, rspeed // 3)
        else:
            wheels.start_tank(lspeed, rspeed)
    print('Done squaring with error = {} after {} tries'.format(abs(lsignal) + abs(rsignal), count))


def gain(signal):
    p = signal * pidk[0]
    # p is proportional feed back
    d = (signal - history[-1]) * pidk[2]
    history.append(signal)
    if len(history) > 100:
        history.pop(0)
    i = sum(history) * pidk[1]
    return -int(p + i - d)


pidk = [.5, .0, .06]
history = [0]
line_square()
