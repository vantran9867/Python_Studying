import math
import numpy as np
from typing import List
from two_dimension_objects.point import Point
from two_dimension_objects.triangle import Triangle
from two_dimension_objects.distance import Distance


class Quadrilateral:
    point1: Point
    point2: Point
    point3: Point
    point4: Point

    def __init__(self, point1: Point, point2: Point, point3: Point, point4: Point):
        if Quadrilateral.quadrilateral_verification(point1, point2, point3, point4):
            self.point1 = point1
            self.point2 = point2
            self.point3 = point3
            self.point4 = point4
        else:
            raise RuntimeError('Not Quadrilateral')

    def __str__(self):
        return str(self.point1) + ',' + ' ' + str(self.point2) + ',' + ' ' + str(self.point3) + ',' + ' ' + \
               str(self.point3)

    @staticmethod
    def quadrilateral_verification(point1: Point, point2: Point, point3: Point, point4: Point) -> bool:
        if Triangle.triangle_verification(point1, point2, point3) and \
                Triangle.triangle_verification(point1, point3, point4) and \
                Triangle.triangle_verification(point2, point3, point4) and \
                Triangle.triangle_verification(point1, point3, point4):
            return True
        else:
            return False

    def get_center(self) -> Point:
        m = (self.point1.x + self.point2.x + self.point3.x + self.point4.x) / 4
        n = (self.point1.y + self.point2.y + self.point3.y + self.point4.y) / 4
        return Point(m, n)

    def get_area(self) -> float:
        tri_a = Triangle(self.point1, self.point2, self.point3)
        tri_b = Triangle(self.point3, self.point4, self.point1)
        return tri_a.get_area() + tri_b.get_area()

    def get_x_seq(self) -> List:
        x_seq = [self.point1.x, self.point2.x, self.point3.x, self.point4.x, self.point1.x]
        return x_seq

    def get_y_seq(self) -> List:
        y_seq = [self.point1.y, self.point2.y, self.point3.y, self.point4.y, self.point1.y]
        return y_seq








