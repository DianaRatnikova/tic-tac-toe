

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Для возможности сравнивать объекты классов
    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.x == other.x and
                    self.y == other.y)
    def show_point(self):
        print("(", self.x, ", ",  self.y, ")")


class Player:
    def __init__(self, role, list_point=[]):
        self.role = role
        self.list_point = []

    def add_point(self, point):
        self.list_point.append(point)

    def show_player(self):
        print(self.role)
        for num, p in enumerate(self.list_point):
            print(num, ". ", end = '')
            p.show_point()
