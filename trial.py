from two_dimension_objects.point import Point
from utilities.triangle_utility import TriangleUtility
from two_dimension_objects.triangle import Triangle
from two_dimension_objects.line import Line
from two_dimension_objects.point import Point
from two_dimension_objects.distance import Distance
from two_dimension_objects.quadrilateral import Quadrilateral

p1 = Point(1, -2)
p2 = Point(2, 1)
p3 = Point(-1, 4)
p4 = Point(1, 1)
t1 = Triangle(p1, p2, p3)
print(t1.get_center())
dis = Distance()
print(dis.distance_from_point_to_triangle(p1, t1))

Q1 = Quadrilateral(p1, p2, p3, p4)
print(Q1.get_center())

