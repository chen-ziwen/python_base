# my_module/area.py

import math


def area_circle(r):
    """计算圆的面积

    :param r: 半径
    """
    return math.pi * r * r


def area_quadrilateral(a, b):
    """计算矩形的面积

    :param a: 长
    :param b: 宽
    """
    return a * b
