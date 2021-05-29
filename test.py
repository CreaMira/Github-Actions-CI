import unittest
import example


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(example.sub(6, 5), 1)

    def test_mul(self):
        self.assertEqual(example.mul(3, 4), 12)

    def test_div(self):
        self.assertEqual(example.div(8, 4), 2)


if __name__ == '__main__':
    unittest.main()
