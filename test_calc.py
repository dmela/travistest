import calc
import unittest

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-4, -5), -9)
        self.assertEqual(calc.add(-4, 5), 1)

    def test_substract(self):
        self.assertEqual(calc.substract(100, 50), 50)
        self.assertEqual(calc.substract(-40, -50), 10)
        self.assertEqual(calc.substract(-40, 50), -90)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-4, -5), 20)
        self.assertEqual(calc.multiply(-4, 5), -20)

    def test_division(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-4, -2), 2)
        self.assertEqual(calc.divide(-100, 50), -2)
        self.assertEqual(calc.divide(100, 50), 2)


if __name__ == '__main__':
    unittest.main()
