#!/usr/bin/env python3
from time import sleep
from robot_fast import Robot
import sys

robot = Robot()

robot.speak('Starting')
# Press left to calibrate, right to go straight to program

# robot.touch_sensor.wait_for_pressed()

robot.calibrate_colour_sensors()

normal_speed = 10
slow_speed = 5
stop_speed = 0

def rescue_main_loop():
    while not robot.touch_sensor.is_pressed:
        left_colour = robot.get_left_color()
        right_colour = robot.get_right_color()

        robot.log("left: ({}), right: ({})".format(left_colour, right_colour))

        if left_colour == Robot.GREEN and right_colour == Robot.GREEN:
            do_rescue()
            return
        elif left_colour == Robot.GREEN:
            turn_left()
        elif right_colour == Robot.GREEN:
            turn_right()
        elif left_colour == Robot.WHITE and right_colour == Robot.WHITE:
            robot.move_tank(normal_speed, normal_speed)
            robot.set_leds("BLACK", "BLACK")
        elif left_colour == Robot.BLACK and right_colour == Robot.WHITE:
            robot.move_tank(normal_speed, stop_speed)
            robot.set_leds("AMBER", "BLACK")
        elif left_colour == Robot.WHITE and right_colour == Robot.BLACK:
            robot.move_tank(stop_speed, normal_speed)
            robot.set_leds("BLACK", "AMBER")
        else:
            robot.move_tank(slow_speed, slow_speed)
            robot.set_leds("AMBER", "AMBER")

def turn_right():
    robot.move_tank(slow_speed, slow_speed)
    while True:
        color = robot.get_right_color()
        if color == Robot.WHITE:
            return
        elif color == Robot.GREEN:
            robot.move_tank(slow_speed, slow_speed)
            robot.set_leds("BLACK", "GREEN")
        elif color == Robot.BLACK:
            robot.stop()
#            robot.move_tank_degrees(-slow_speed, slow_speed, 10)
            robot.set_leds("AMBER", "GREEN")
            robot.do_right_turn(slow_speed)

def turn_left():
    robot.move_tank(slow_speed, slow_speed)
    while True:
        color = robot.get_left_color()
        if color == Robot.WHITE:
            return
        elif color == Robot.GREEN:
            robot.move_tank(slow_speed, slow_speed)
            robot.set_leds("GREEN", "BLACK")
        elif color == Robot.BLACK:
            robot.stop()
#            robot.move_tank_degrees(slow_speed, -slow_speed, 10)
            robot.set_leds("GREEN", "AMBER")
            robot.do_left_turn(slow_speed)

def do_rescue():
    robot.off()
    robot.speak('Exiting rescue program!')

rescue_main_loop()
robot.off()
# sleep(2)

# while not robot.touch_sensor.is_pressed:
#     robot.log_colour()

robot.speak('Bye!')

