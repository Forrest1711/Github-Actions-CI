import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_subtract_1(self):
        self.assertEqual(example.subtract(1, 1), 0)

    def test_multiply_1(self):
        self.assertEqual(example.multiply(2, 3), 6)

    def test_divide_1(self):
        self.assertEqual(example.divide(6, 3), 2)

    def test_add_2(self):
        self.assertEqual(example.add(-31, 62), 31)

    def test_subtract(self):
        self.assertEqual(example.subtract(-13, -19), 6)


if __name__ == '__main__':
    unittest.main()
