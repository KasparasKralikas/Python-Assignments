import unittest
import doctest
import math

from is_finite import is_finite

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite('./doctest.txt'))
    return tests

class TestIsInfiteMethod(unittest.TestCase):

    def test_given_positive_integer_returns_true(self):
        result = is_finite(15)
        self.assertEqual(result, True)

    def test_given_nan_returns_false(self):
        result = is_finite(math.nan)
        self.assertEqual(result, False)

    def test_given_infinity_returns_false(self):
        result = is_finite(float('inf'))
        self.assertEqual(result, False)

    def test_given_negative_float_returns_true(self):
        result = is_finite(-9.99)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
