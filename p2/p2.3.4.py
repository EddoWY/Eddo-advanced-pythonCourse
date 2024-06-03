"""
_x - x coordinate
_y - y coordinate
_red - a value between 0 and 255
_green - a value between 0 and 255
_blue - a value between 0 and 255
"""


class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        average = (self._red + self._green + self._blue) // 3
        self._red = average
        self._green = average
        self._blue = average

    def __repr__(self):
        return f"Pixel(x={self._x}, y={self._y}, red={self._red}, green={self._green}, blue={self._blue})"

    def print_pixel_info(self):
        color_info = f"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue})"
        color_names = {"Red": self._red, "Green": self._green, "Blue": self._blue}
        non_zero_colors = [k for k, v in color_names.items() if v > 50]

        if non_zero_colors and len(non_zero_colors) == 1:
            color_info += f" {non_zero_colors[0]}"

        print(color_info)


if __name__ == '__main__':
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()
