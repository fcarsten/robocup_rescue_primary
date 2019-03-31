from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import TouchSensor
from ColorSensorFast import ColorSensorFast as ColorSensor
from ev3dev2.button import Button
from time import sleep
import sys

import os

class Robot:

    GREEN = 'green'
    BLACK = 'black'
    WHITE = 'white'
    SILVER = 'silver'

    # left_white = (240, 243,245)
    # right_white = (250, 245, 253)

    # left_black = (31, 36, 30)
    # right_black = (30, 40, 31)

    # left_green = (52, 135, 70)
    # right_green = (50, 137, 73)

    # left_colours = [left_white, left_green, left_black]
    # right_colours = [right_white, right_green, right_black]

    def rgb_to_color(self, rgb):
        if rgb[0] > 150:
            return Robot.WHITE
        else:
            if rgb[1] - rgb[0] > 50:
                return Robot.GREEN
            else:
                return Robot.BLACK

    def do_right_turn(self, speed):
        self.move_tank_degrees(0,speed,180)

    def do_left_turn(self, speed):
        self.move_tank_degrees(speed,0,180)

    def __init__(self):
        os.system('setfont Lat15-TerminusBold14')

        self.left_motor = LargeMotor(OUTPUT_B)
        self.left_motor.stop_action = 'hold'

        self.right_motor = LargeMotor(OUTPUT_C)
        self.right_motor.stop_action = 'hold'

        self.touch_sensor = TouchSensor()

        self.leds = Leds()

        self.color_sensor_left = ColorSensor('in1')

        self.color_sensor_right = ColorSensor('in4')

        self.sound = Sound()

        self.button = Button()

        self.tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)


    def move_tank(self, left_speed, right_speed):
        self.tank_drive.on(left_speed, right_speed)

    def move_tank_degrees(self, left_speed, right_speed, degrees):
        self.tank_drive.on_for_degrees(left_speed, right_speed, degrees)

    def stop(self):
        self.tank_drive.off()

    def off(self):
        self.stop()

    def is_touch_pressed(self):
        return self.touch_sensor.is_pressed

    def log(self, text):
        print(text, file=sys.stderr)

    def calibrate_colour_sensors(self):
        self.leds.set_color("LEFT", "RED")
        self.leds.set_color("RIGHT", "RED")
        sleep(2.0)

        self.color_sensor_right.calibrate_white()
        self.color_sensor_left.calibrate_white()
        self.leds.set_color("LEFT", "GREEN")
        self.leds.set_color("RIGHT", "GREEN")

    def speak(self, text):
        self.sound.speak(text)

    def set_leds(self, left, right):
        self.leds.set_color("LEFT", left)
        self.leds.set_color("RIGHT", right)

    def left_button_pressed(self):
        return self.button.left

    def right_button_pressed(self):
        return self.button.right

    def get_left_color(self):
        rgb = self.color_sensor_left.rgb
        return self.rgb_to_color(rgb)

    def get_right_color(self):
        rgb = self.color_sensor_right.rgb
        return self.rgb_to_color(rgb)

    def log_colour(self):
        rgb_left = self.color_sensor_left.rgb
        rgb_right = self.color_sensor_right.rgb
        self.log("Left: {}, Right:{}".format(rgb_left, rgb_right))


