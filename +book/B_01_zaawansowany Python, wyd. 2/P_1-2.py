# implementacja __repre__ __abs__ __add__ __mul__ __bool__


import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # nowa instancja obiektu klasy Vector
    # żaden operand nie jest modyfikowany
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # nowa instancja obiektu klasy Vector
    # tu można mnożyć Vector przez scalar, scalar przez Vector już nie --> __rmul__
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # __repr__ jest wywoływany przez wbudowaną funkcję repr() w celu otrzymania reprezentacji tekstowej obiektu do inspecji
    # __


# v1 = Vector(2, 4)
# v2 = Vector(2, 1)

# print(v1 + v2)
# Vector(4, 5)

v = Vector(3, 4)
print(abs(v))
# 5.0

print(repr(v))
# Vector(3, 4)
# <__main__.Vector object at 0x10f5a0c10>