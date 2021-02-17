from two_dimension_objects.point import Point


class Circle:
    point1: Point
    r: float

    def __init__(self, point1: Point, r: float):
        self.point1 = point1
        self.r = r

    def __str__(self):
        return '(' + 'x' + ' ' + '-' + ' ' + str(self.point1.x) + ')' + '**2' + ' ' + '+' + ' ' + '(' + 'y' + ' ' + '-'\
               + ' ' + str(self.point1.y) + ')' + '**2' + ' ' + '=' + ' ' + str((self.r**2))

    def get_area(self) -> float:
        return round((self.r ** 2) * 3.14, 2)


