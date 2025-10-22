from shapes.point import Point
from shapes.rectangle import Rectangle
from shapes.square import Square

def main():
    p1 = Point(0, 0)
    p2 = Point(5, 5)

    rect = Rectangle(p1, p2)
    print("Rectangle area:", rect.compute_area())
    print("Rectangle perimeter:", rect.compute_perimeter())
    print("Is rectangle regular?", rect.is_it_regular())

    sq = Square(p1, p2)
    print("Square area:", sq.compute_area())
    print("Square perimeter:", sq.compute_perimeter())
    print("Is square regular?", sq.is_it_regular())

if __name__ == "__main__":
    main(
