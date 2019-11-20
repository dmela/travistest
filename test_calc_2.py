import calc
import unittest

class TestCalc(unittest.TestCase):

    def test_substract(self):
        self.assertEqual(calc.substract(20, 10), 0) # This test will fail

if __name__ == '__main__':
    unittest.main()
