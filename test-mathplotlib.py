import matplotlib.pyplot as plt
from two_dimension_objects.triangle import Triangle
from two_dimension_objects.quadrilateral import Quadrilateral
from two_dimension_objects.point import Point
from two_dimension_objects.circle import Circle

p1 = Point(1, 2)
p2 = Point(2, 1)
p3 = Point(1, 1)
tri1 = Triangle(p1, p2, p3)

point1 = Point(1, 4)
point2 = Point(2, 3)
point3 = Point(3, 5)
point4 = Point(1, 6)
q1 = Quadrilateral(point1, point2, point3, point4)

r = 0.1
point5 = Point(2.75, 2)
cir1 = Circle(point5, r)
plt.Circle((point5.x, point5.y), r, color='red')

plt.plot(q1.get_x_seq(), q1.get_y_seq())
plt.plot(tri1.get_x_seq(), tri1.get_y_seq())
plt.text(q1.get_center().x, q1.get_center().y,  q1.get_area())
plt.text(tri1.get_center().x, tri1.get_center().y, tri1.get_area())
plt.ylabel('y axis')
plt.xlabel('x axis')
plt.show()




