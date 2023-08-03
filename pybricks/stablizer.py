from pybricks.geometry import Axis
from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

hub = PrimeHub()
lmotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
rmotor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
wheels = DriveBase(left_motor=lmotor, right_motor=rmotor, wheel_diameter=56, axle_track=80)


class PID(object):
    def __init__(self):
        self.pid_gains = [50, .0, 0]
        self.maxlen = 100
        self.history = [0]
        self.history_sum = 0

    def get_response(self, signal):
        p = self.pid_gains[0] * signal
        history_diff = signal - self.history[-1]
        d = self.pid_gains[2] * history_diff
        self.history_sum += history_diff
        i = self.pid_gains[1] * self.history_sum
        self.history.append(signal)
        if len(self.history) > self.maxlen:
            self.history.pop(0)

        # print('p = ' + str(p))
        # print('i = ' + str(i))
        # print('d = ' + str(d))
        return p + i + d


def stabilizer():
    pid = PID()
    while True:
        a = hub.imu.angular_velocity(Axis.X)
        speed = pid.get_response(a)
        wheels.drive(speed, 0)


stabilizer()
