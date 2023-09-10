"""
this is only for beta byricks
it has HEADING code!
*hub_imu = hub.imu.heading()*
https://beta.pybricks.com/
"""
ik = 0.01
pk = 1
delta = .3


def turn(angle, imu=None, drive_base=None):
    imu = imu or hub.imu
    drive_base = drive_base or wheels
    init_angle = imu.heading()
    target = angle + init_angle
    history = 0

    while True:
        measure = imu.heading()
        diff = target - measure
        if abs(diff) < delta:
            break
        history += diff
        print("{:+04.5}, {:+04.5}, {:+04.5}, {:+04.5}, {:+04.5}".format(init_angle, measure, target, history, diff))
        drive_base.turn(diff * pk + history * ik)


# while True:
# print(hub.imu.heading())
if __name__ == '__main__':
    from pybricks.hubs import PrimeHub
    from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
    from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
    from pybricks.robotics import DriveBase
    from pybricks.tools import wait, StopWatch

    hub = PrimeHub()
    # Initialize a motor on port A.
    drivingl = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
    drivingr = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
    wheels = DriveBase(left_motor=drivingl, right_motor=drivingr, wheel_diameter=56, axle_track=60)
    leftboi = ColorSensor(Port.C)
    rightboi = ColorSensor(Port.E)
    turn(90.00, hub.imu, wheels)
