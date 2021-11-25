import unittest
from program import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fib1(self):
        result1 = fibonacci(9)
        self.assertEqual(result1, 30)
    def test_fib2(self):
        result2 = fibonacci(0)
        self.assertEqual(result2, 0)
    def test_fib3(self):
        result3 = fibonacci(20)
        self.assertEqual(result3, 6765)


if __name__ == '__main__':
    unittest.main()
