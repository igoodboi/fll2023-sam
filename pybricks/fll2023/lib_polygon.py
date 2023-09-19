from umath import *

from fll_robot import Robot
from lib_move import move
from lib_turn import turn


def principle(angle):
    """
    Given an angle (degree), calculate the principle angle in the range (-180, 180]
    :param angle: any angle in degree
    :return: the principle angle corresponding to the input in the range (-180, 180]
    """
    return (angle + 180) % 360 - 180


# map size 2 m x 112 cm. let the 112 cm side be x; 2 m side be y
def trip_plan(vertices, heading=0):
    """
    Given a polygon vertices and initial heading, generate the trip plan (a sequence of maneuvers)
    :param vertices:
    :param heading:
    :return:
    """
    maneuvers = []
    for i in range(1, len(vertices)):
        turn_angle, distance, heading = route(vertices[i - 1], vertices[i], heading)
        maneuvers.append((turn_angle, distance))
    return maneuvers


def route(point1, point2, heading=0):
    """
    Generate the routing parameters for a sequence of maneuvers, a turn plus a straight movement, that will ensure robot to traverse from point1 to point2.
    :param point1: starting point
    :param point2: ending point
    :param heading: starting heading direction (deg), follow pybricks orientation convention
    :return: a tuple of (turn angle, straight distance, ending orientation)
    """
    displacement = [point2[0] - point1[0], point2[1] - point1[1]]
    polar_angle = atan2(displacement[1], displacement[0]) * 180 / pi
    radius = sqrt(pow(displacement[1], 2) + pow(displacement[0], 2))
    mod_angle = principle(polar_angle - heading)
    print('original heading={} new heading={} dist={} turn={}'.format(
        heading, polar_angle, radius, mod_angle))
    return mod_angle, radius, polar_angle


def poly(heading, vertices, robot: Robot, reverse: bool = False, speed=None):
    '''
    Given a polygon (vertices), plan the trip and execute the plan to traverse the polygon edges in order.
    heading = the initial orientation of the robot used for determining the first manuver.
    If reverse = True, revert the entire trip backward back to the origin.
    '''
    maneuvers = trip_plan(vertices, heading)
    for turn_angle, distance in maneuvers:
        print(turn_angle, distance)
        turn(robot, turn_angle)
        move(robot, distance_mm=distance, speed=speed)
        # [TODO] there seems to be a bug in the IMU that if I uncomment the following line, the last turn of
        # [TODO] poly(0, [[0, 0], [100, 0], [100, -100], [0, -100], [0, 0]], bot)
        # [TODO] will be funky
        # robot.hub.imu.reset_heading(heading)
    if not reverse:
        return
    # reverse course
    for turn_angle, distance in maneuvers[::-1]:
        print(-turn_angle, -distance)
        move(robot, distance_mm=-distance, speed=speed)
        turn(robot, -turn_angle)


def main():
    bot = Robot()
    # heading = trip([0, 0], [100, 0], bot, heading=180, reverse=True)
    # bot.hub.imu.reset_heading(180)
    # heading = trip([0, -100], [0, 0], bot, heading=180)
    # heading = trip([510, 1000], [960, 0], bot, heading=0)
    # print(heading)
    # bot.hub.imu.reset_heading(180)
    # poly(0, [ [100, -100], [0, -100], [0, 0]], bot)
    poly(0, [[0, 940], [500, 940], [750, 250], [800, 180]], bot, reverse=True)
    # poly(0, [[0, 0], [100, 0], [100, -100], [0, -100], [0, 0]], bot, reverse=True)


if __name__ == "__main__":
    main()
