import math
import unittest
from scalculator import sqrt, factorial, ln, power

class TestCalculator(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2.0)
        self.assertEqual(sqrt(25), 5.0)

    def test_factorial(self):
        self.assertEqual(factorial(5.0), 120)
        self.assertEqual(factorial(0.0), 1)

    def test_ln(self):
        self.assertAlmostEqual(ln(math.e), 1.0) # type: ignore
        self.assertEqual(ln(1), 0.0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8.0)
        self.assertEqual(power(5, -1), 0.2)

if __name__ == '__main__':
    unittest.main()