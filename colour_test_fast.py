#!/usr/bin/env python3
from time import sleep
from robot_fast import Robot
import sys

robot = Robot()

robot.speak('Starting now')

robot.calibrate_colour_sensors()

normal_speed = 20

def main_loop():
    measurements = []
    counter = 1
    robot.move_tank(normal_speed, normal_speed)
    while not robot.touch_sensor.is_pressed:
        left_colour = robot.get_left_color()
        right_colour = robot.get_right_color()
        measurements.append((counter, left_colour, right_colour))
        counter = counter+1

    with open('colours_fast.csv', 'w+') as file:
        for c,l,r in measurements:
            file.write("{},{},{}\n".format(c,l,r))

main_loop()
robot.off()

robot.speak('Done!')

