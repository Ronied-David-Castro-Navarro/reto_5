
from .shape import Shape
from .point import Point

class Rectangle(Shape):
    def __init__(self, p1: Point, p2: Point):
        super().__init__("Rectangle")
        self._p1 = p1
        self._p2 = p2

    def compute_area(self):
        width = abs(self._p2.get_x() - self._p1.get_x())
        height = abs(self._p2.get_y() - self._p1.get_y())
        return width * height

    def compute_perimeter(self):
        width = abs(self._p2.get_x() - self._p1.get_x())
        height = abs(self._p2.get_y() - self._p1.get_y())
        return 2 * (width + height)

    def compute_inner_angles(self):
        return [90, 90, 90, 90]

    def is_it_regular(self):
        width = abs(self._p2.get_x() - self._p1.get_x())
        height = abs(self._p2.get_y() - self._p1.get_y())
        return width == height
