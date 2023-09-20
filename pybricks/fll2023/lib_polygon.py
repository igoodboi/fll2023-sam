from umath import *

from lib_move import move
from lib_turn import turn
from fll_robot import Robot


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
        maneuvers.append((turn_angle, distance, heading))
    return maneuvers


def route(point1, point2, heading=0, reverse=False):
    """
    Generate the routing parameters for a sequence of maneuvers, a turn plus a straight movement, that will ensure robot to traverse from point1 to point2.
    :param point1: starting point
    :param point2: ending point
    :param heading: starting heading direction (deg), follow pybricks orientation convention
    :param reverse: boolean. if True, revert else drive forward (default)
    :return: a tuple of (turn angle, straight distance, ending orientation)
    """
    displacement = [point2[0] - point1[0], point2[1] - point1[1]]
    polar_angle = atan2(displacement[1], displacement[0]) * 180 / pi
    radius = sqrt(pow(displacement[1], 2) + pow(displacement[0], 2))
    heading += 180 if reverse else 0
    mod_angle = principle(polar_angle - heading)
    distance = -radius if reverse else radius
    print('original heading={} new heading={} dist={} turn={}'.format(
        heading, polar_angle, radius, mod_angle))
    return mod_angle, distance, polar_angle


def poly(heading, vertices, robot: Robot, motion_type: int = 1, reverse: bool = False, speed=None):
    """
    Given a polygon (vertices), plan the trip and execute the plan to traverse the polygon edges in order.
    heading = the initial orientation of the robot used for determining the first maneuver.
    If reverse = True, revert the entire trip backward back to the origin.
    :param heading: initial heading direction (deg), follow pybricks orientation convention
    :param vertices: the ordered vertices of the polygon, as a list of 2d coordinates, such as [(x1, y1), (x2, y2) ...], with the starting position as the first element
    :param robot: the robot
    :param motion_type: the direction for all the maneuvers: move forward = 1, move backward = -1, freeze = 0 (turn only with no straight motion)
    :param reverse: reverse course at the end of the trip
    :param speed: specified speed for the whole trip. If unspecified (None), use system default
    :return: final heading (deg), follow pybricks orientation convention
    """

    def execute(maneuvers):
        for turn_angle, distance, _ in maneuvers:
            print(turn_angle, distance * motion_type)
            turn(robot, turn_angle)
            move(robot, distance_mm=distance * motion_type, speed=speed)

    base_maneuvers = trip_plan(vertices, heading)
    execute(base_maneuvers)
    if not reverse:
        return base_maneuvers[-1][-1]

    # reverse course
    reverse_maneuvers = base_maneuvers[::-1]
    execute(reverse_maneuvers)
    return reverse_maneuvers[-1][-1]


if __name__ == "__main__":
    bot = Robot()
    # heading = trip([0, 0], [100, 0], bot, heading=180, reverse=True)
    # bot.hub.imu.reset_heading(180)
    # heading = trip([0, -100], [0, 0], bot, heading=180)
    # heading = trip([510, 1000], [960, 0], bot, heading=0)
    # print(heading)
    # bot.hub.imu.reset_heading(180)
    # poly(0, [ [100, -100], [0, -100], [0, 0]], bot)
    # poly(0, [[0, 0], [100, 0], [100, -100], [0, -100], [0, 0]], bot, reverse=True)
    heading = poly(0, [[0, 940], [500, 940], [700, 250], [760, 100]], bot)
    heading = poly(heading, [[760, 100], [700, 250]], bot, reverse=True)
    heading = poly(heading, [[700, 250], [600, 0], [660, 0], [700, 250], [500, 940], [0, 940]], bot)
