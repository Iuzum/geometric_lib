import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    """Тесты для circle.py.

    Область тестирования:
    - валидные значения радиуса (r >= 0);
    - крайние случаи: r = 0, r = 1;
    - типичные значения.

    Вне области тестирования:
    - отрицательные значения (не входят в контракт функции);
    - нечисловые значения (str, None).
    """

    def test_zero_area(self):
        '''Площадь круга радиуса 0 равна 0.'''
        self.assertEqual(area(0), 0)

    def test_unit_area(self):
        '''Площадь круга радиуса 1 примерно равна π.'''
        self.assertAlmostEqual(area(1), 3.141592653589793)

    def test_area(self):
        '''Площадь круга радиуса 5 ≈ 78.53981633974483.'''
        self.assertAlmostEqual(area(5), 78.53981633974483)

    def test_zero_perimeter(self):
        '''Длина окружности радиуса 0 равна 0.'''
        self.assertEqual(perimeter(0), 0)

    def test_unit_perimeter(self):
        '''Длина окружности радиуса 1 ≈ 2π.'''
        self.assertAlmostEqual(perimeter(1), 6.283185307179586)

    def test_perimeter(self):
        '''Длина окружности радиуса 5 ≈ 31.41592653589793.'''
        self.assertAlmostEqual(perimeter(5), 31.41592653589793)


if __name__ == '__main__':
    unittest.main()
