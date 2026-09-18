import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    """Тесты для rectangle.py.

    Область тестирования:
    - валидные значения сторон (a, b >= 0);
    - крайние случаи: нулевые стороны, равные стороны (квадрат);
    - типичные и дробные значения;
    - регрессионный тест на исправленный баг в perimeter.

    Вне области тестирования:
    - отрицательные значения;
    - нечисловые значения (str, None).
    """

    def test_zero_area(self):
        '''Площадь с нулевой стороной равна 0.'''
        self.assertEqual(area(10, 0), 0)

    def test_zero_area_both(self):
        '''Площадь с обеими нулевыми сторонами равна 0.'''
        self.assertEqual(area(0, 0), 0)

    def test_square_area(self):
        '''Прямоугольник 10×10 — квадрат, площадь 100.'''
        self.assertEqual(area(10, 10), 100)

    def test_area(self):
        '''Площадь 3×4 равна 12.'''
        self.assertEqual(area(3, 4), 12)

    def test_float_area(self):
        '''Площадь 1.5×2 равна 3.0.'''
        self.assertAlmostEqual(area(1.5, 2), 3.0)

    def test_zero_perimeter(self):
        '''Периметр с нулевыми сторонами равен 0.'''
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter(self):
        '''Периметр 3×4 равен 14 — регрессионный тест.'''
        self.assertEqual(perimeter(3, 4), 14)

    def test_perimeter_square(self):
        '''Периметр 10×10 равен 40.'''
        self.assertEqual(perimeter(10, 10), 40)

    def test_float_perimeter(self):
        '''Периметр 1.5×2 равен 7.0.'''
        self.assertAlmostEqual(perimeter(1.5, 2), 7.0)


if __name__ == '__main__':
    unittest.main()
