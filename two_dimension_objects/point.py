class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + ' ' + str(self.y) + ')'
