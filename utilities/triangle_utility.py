from two_dimension_objects.point import Point
from two_dimension_objects.line import Line
from two_dimension_objects.triangle import Triangle


class TriangleUtility:
    @staticmethod
    def get_point_from_two_line(line1: Line, line2: Line) -> Point:
        px = (line1.c*line2.b - line2.c*line1.b) / (line1.a*line2.b - line2.a*line1.b)
        py = (line1.a*line2.c - line2.a*line1.c) / (line1.a*line2.b - line2.a*line1.b)
        return Point(px, py)

    @staticmethod
    def get_triangle_from_three_lines(line1: Line, line2: Line, line3: Line) -> Triangle:
        if line1.a != 0 and line1.b != 0 and line3.a != 0 and line3.b != 0 and line2.a/line1.a != line2.b/line1.b and\
                line2.a/line3.a != line2.b/line3.b and line3.a/line1.a != line3.b/line1.b:
            point_a = TriangleUtility.get_point_from_two_line(line1, line2)
            point_b = TriangleUtility.get_point_from_two_line(line2, line3)
            point_c = TriangleUtility.get_point_from_two_line(line3, line1)
            return Triangle(point_a, point_b, point_c)
        else:
            raise RuntimeError('Not Triangle')

