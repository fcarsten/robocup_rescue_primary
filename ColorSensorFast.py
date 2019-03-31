import sys
from ev3fast import ColorSensor

class ColorSensorFast(ColorSensor):
    def log(self, text):
        print(text, file=sys.stderr)

    def __init__(self, port):
        super().__init__(port)
        self.max_green = 300
        self.max_red = 300
        self.max_blue = 300

    def calibrate_white(self):
        rgb = self.raw
        self.log("Fast Raw color: {}".format(rgb))
        self.max_red = rgb[0]
        self.max_green = rgb[1]
        self.max_blue = rgb[2]

    @property
    def rgb(self):
        """
        Same as raw() but RGB values are scaled to 0-255
        """
        (red, green, blue) = self.raw

        return (min(int((red * 255) / self.max_red), 255),
                min(int((green * 255) / self.max_green), 255),
                min(int((blue * 255) / self.max_blue), 255))


