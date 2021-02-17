import math
from two_dimension_objects.point import Point
from two_dimension_objects.line import Line
from two_dimension_objects.triangle import Triangle


class Distance:
    @staticmethod
    def get_distance_between_point(point1: Point, point2: Point) -> float:
        return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

    @staticmethod
    def get_distance_between_point_line(point1: Point, line: Line) -> float:
        return abs(line.a * point1.x + line.b * point1.y + line.c) / math.sqrt(point1.x ** 2 + point1.y ** 2)

    @staticmethod
    def distance_from_point_to_triangle(point: Point, triangle: Triangle) -> float:
        point_center = triangle.get_center()
        return math.sqrt((point.x - point_center.x) ** 2 + (point.y - point_center.y) ** 2)