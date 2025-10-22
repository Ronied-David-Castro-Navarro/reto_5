
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self._name = name  
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    @abstractmethod
    def compute_area(self):
        pass

    @abstractmethod
    def compute_perimeter(self):
        pass

    @abstractmethod
    def compute_inner_angles(self):
        pass

    @abstractmethod
    def is_it_regular(self):
        pass
