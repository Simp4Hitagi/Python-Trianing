import unittest
from main import add, subtract, division, multiply

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, -1), 0)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(1, 5), 0.2)

        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            division(5, 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
