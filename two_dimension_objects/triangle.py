from typing import List
from two_dimension_objects.point import Point


class Triangle:
    point1: Point
    point2: Point
    point3: Point

    def __init__(self, point1: Point, point2: Point, point3: Point):
        if Triangle.triangle_verification(point1, point2, point3):
            self.point1 = point1
            self.point2 = point2
            self.point3 = point3
        else:
            raise RuntimeError('Not Triangle')

    def __str__(self):
        return str(self.point1) + ',' + ' ' + str(self.point2) + ',' + ' ' + str(self.point3)

    @staticmethod
    def triangle_verification(point1: Point, point2: Point, point3: Point) -> bool:
        n1 = point2.x - point1.x
        n2 = point3.x - point2.x
        d1 = point2.y - point1.y
        d2 = point3.y - point2.y
        if d1 != 0 and d2 != 0 and n2 / n1 == d2 / d1:
            return False
        else:
            return True

    def get_center(self) -> Point:
        m = (self.point1.x + self.point2.x + self.point3.x) / 3
        n = (self.point1.y + self.point2.y + self.point3.y) / 3
        return Point(m, n)

    def get_area(self) -> float:
        return round((1 / 2 * (
            abs((self.point2.x - self.point1.x) * (self.point3.y - self.point1.y) - (self.point3.x - self.point1.x) *
                (self.point2.y - self.point1.y)))), 2)

    def get_x_seq(self) -> List:
        x_seq = [self.point1.x, self.point2.x, self.point3.x, self.point1.x]
        return x_seq

    def get_y_seq(self) -> List:
        y_seq = [self.point1.y, self.point2.y, self.point3.y, self.point1.y]
        return y_seq



