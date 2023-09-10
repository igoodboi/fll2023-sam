from spike_py import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike_py.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
wheels = MotorPair('B', 'A')

class PID():
    def __init__(self):
        self.pid_gains = [1, .0, 0]
        self.maxlen = 10
        self.history = [0]
        self.history_sum = 0
    def get_response(self, diff):
        p = self.pid_gains[0] * diff
        history_diff = diff - self.history[-1]
        d = self.pid_gains[2] * history_diff
        self.history_sum += history_diff
        i = self.pid_gains[1] * self.history_sum
        self.history.append(diff)
        if len(self.history) > self.maxlen:
            self.history.pop(0)

        print('p = ' + str(p))
        print('i = ' + str(i))
        print('d = ' + str(d))
        return p + i + d

def stabilizer():
    init_roll = hub.motion_sensor.get_roll_angle()
    print('init_roll=' + str(init_roll))
    pid = PID()
    while True:
        roll = hub.motion_sensor.get_roll_angle()
        motion = pid.get_response(roll - init_roll)
        # wheels.move(motion, 'cm', speed=90)
        wheels.move(motion, unit='cm', speed=int(80 * abs(motion)))

stabilizer()
