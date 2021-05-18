# Standard Library
from math import cos, pi, sin


def obj_func_q1(x, y):
    assert isinstance(x, (int, float))
    assert isinstance(y, (int, float))
    assert -0.5 <= x <= 1.5
    assert -0.5 <= y <= 1.5

    x = round(x, 3)
    y = round(y, 3)

    return 80 - x ** 2 - y ** 2 + 10 * cos(2 * pi * x) + 10 * sin(2 * pi * y)
