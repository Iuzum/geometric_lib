import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    """Тесты для triangle.py.

    Область тестирования:
    - валидные значения основания, высоты и сторон (>= 0);
    - крайние случаи: нулевые значения;
    - равносторонний треугольник;
    - типичные и дробные значения.

    Вне области тестирования:
    - отрицательные значения;
    - нечисловые значения (str, None);
    - проверка неравенства треугольника (a + b > c).
    """

    def test_zero_area_base(self):
        '''Площадь с нулевым основанием равна 0.'''
        self.assertEqual(area(0, 5), 0)

    def test_zero_area_height(self):
        '''Площадь с нулевой высотой равна 0.'''
        self.assertEqual(area(4, 0), 0)

    def test_area(self):
        '''Площадь с основанием 4 и высотой 5 равна 10.'''
        self.assertEqual(area(4, 5), 10)

    def test_float_area(self):
        '''Площадь с дробными значениями: 3.5 и 2 → 3.5.'''
        self.assertAlmostEqual(area(3.5, 2), 3.5)

    def test_zero_perimeter(self):
        '''Периметр с нулевыми сторонами равен 0.'''
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter(self):
        '''Периметр треугольника 3,4,5 равен 12.'''
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral(self):
        '''Периметр равностороннего треугольника со стороной 6 равен 18.'''
        self.assertEqual(perimeter(6, 6, 6), 18)

    def test_float_perimeter(self):
        '''Периметр с дробными сторонами: 1.5 + 2.5 + 3 = 7.'''
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3), 7.0)


if __name__ == '__main__':
    unittest.main()
