import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    # area tests
    def test_area_zero(self):
        self.assertEqual(area(0, 10), 0.0)
        self.assertEqual(area(10, 0), 0.0)
        self.assertEqual(area(0, 0), 0.0)

    def test_area_positive_integers(self):
        self.assertEqual(area(3, 5), 15.0)

    def test_area_floats(self):
        self.assertAlmostEqual(area(2.5, 4.2), 10.5)

    def test_area_large_numbers(self):
        self.assertEqual(area(10**6, 2), float(2 * 10**6))

    def test_area_negative_raises(self):
        with self.assertRaises(ValueError):
            area(-1, 5)
        with self.assertRaises(ValueError):
            area(5, -1)

    def test_area_invalid_type_raises(self):
        with self.assertRaises(TypeError):
            area("a", 5)
        with self.assertRaises(TypeError):
            area(5, None)

    # perimeter tests
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 10), 20.0)
        self.assertEqual(perimeter(0, 0), 0.0)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 5), 16.0)

    def test_perimeter_floats(self):
        self.assertAlmostEqual(perimeter(2.5, 4.5), 14.0)

    def test_perimeter_negative_raises(self):
        with self.assertRaises(ValueError):
            perimeter(-2, 3)

    def test_perimeter_invalid_type_raises(self):
        with self.assertRaises(TypeError):
            perimeter([1,2], 3)

if __name__ == "__main__":
    unittest.main()