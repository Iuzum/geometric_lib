import math


def area(r):
    '''Принимает радиус r (int/float), возвращает площадь круга.
    Пример вызова: area(5) -> 78.53981633974483'''
    return math.pi * r * r

def perimeter(r):
    '''Принимает радиус r (int/float), возвращает длину окружности.
    Пример вызова: perimeter(5) -> 31.41592653589793'''
    return 2 * math.pi * r

