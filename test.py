import unittest
from program import factorial

class Testfactorial(unittest.TestCase):
    def test_factorial1(self):
        result1 = factorial(9)
        self.assertEqual(result1, 362880)
    def test_factorial2(self):
        result2 = factorial(0)
        self.assertEqual(result2, 1)
    def test_factorial3(self):
        result3 = factorial(3)
        self.assertEqual(result3, 6)


if __name__ == '__main__':
    unittest.main()
