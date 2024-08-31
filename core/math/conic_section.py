from math import sin, cos, tan, pi, radians, degrees, asin, acos, atan

def polar_to_orth(r: float, c: float) -> tuple[float, float]:
    """
    Converts polar coordinate to orthology coordinate.

    :param r: Radius.
    :param c: Degree in radian.
    """
    return r * cos(c), r * sin(c)

def orth_to_polar(x: float, y: float) -> tuple[float, float]:
    """
    Converts orthology coordinate to polar coordinate.

    :param x: X Coordinate.
    :param y: Y Coordinate.
    """
    return (x ** 2 + y ** 2) ** 0.5, atan(y / x)

class Circle():
    pass

class Eillpse():
    pass

class Parabola():
    pass

class Hyperbola():
    pass

