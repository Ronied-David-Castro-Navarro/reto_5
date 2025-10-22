
from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)
        self._name = "Square"

    def is_it_regular(self):
        return True  # Todos los cuadrados son regulares
