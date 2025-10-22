from .shape import Shape
from .line import Line

class Rectangle(Shape):
    def __init__(self, point1, point2):
        super().__init__()
        self.__point1 = point1
        self.__point2 = point2
        self.__width = abs(point2.get_x() - point1.get_x())
        self.__height = abs(point2.get_y() - point1.get_y())

    def get_width(self):
        return self.__width

    def set_width(self, w):
        if w > 0:
            self.__width = w

    def get_height(self):
        return self.__height

    def set_height(self, h):
        if h > 0:
            self.__height = h

    def compute_area(self):
        return self.__width * self.__height

    def compute_perimeter(self):
        return 2 * (self.__width + self.__height)

    def compute_inner_angles(self):
        return [90, 90, 90, 90]

    def is_it_regular(self):
        return self.__width == self.__height
