import calc
import unittest

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-4, -5), -9)
        self.assertEqual(calc.add(-4, 5), 1)


if __name__ == '__main__':
    unittest.main()
