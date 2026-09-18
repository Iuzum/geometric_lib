import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    """Тесты для square.py.

    Область тестирования:
    - валидные значения стороны (a >= 0);
    - крайние случаи: a = 0, a = 1;
    - типичные и дробные значения.

    Вне области тестирования:
    - отрицательные значения;
    - нечисловые значения (str, None).
    """

    def test_zero_area(self):
        '''Площадь квадрата со стороной 0 равна 0.'''
        self.assertEqual(area(0), 0)

    def test_unit_area(self):
        '''Площадь квадрата со стороной 1 равна 1.'''
        self.assertEqual(area(1), 1)

    def test_area(self):
        '''Площадь квадрата со стороной 4 равна 16.'''
        self.assertEqual(area(4), 16)

    def test_float_area(self):
        '''Площадь квадрата со стороной 2.5 равна 6.25.'''
        self.assertAlmostEqual(area(2.5), 6.25)

    def test_zero_perimeter(self):
        '''Периметр квадрата со стороной 0 равен 0.'''
        self.assertEqual(perimeter(0), 0)

    def test_unit_perimeter(self):
        '''Периметр квадрата со стороной 1 равен 4.'''
        self.assertEqual(perimeter(1), 4)

    def test_perimeter(self):
        '''Периметр квадрата со стороной 4 равен 16.'''
        self.assertEqual(perimeter(4), 16)


if __name__ == '__main__':
    unittest.main()
