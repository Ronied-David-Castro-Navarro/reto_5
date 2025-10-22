from .point import Point

class Line:
    def __init__(self, start_point, end_point):
        self.__start = start_point
        self.__end = end_point

    def length(self):
        return self.__start.distance_to(self.__end)
