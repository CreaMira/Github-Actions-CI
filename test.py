import unittest
import example


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(example.add(1, 2), 3)


    def test_mul(self):
        self.assertEqual(example.mul(3, 4), 12)


if __name__ == '__main__':
    unittest.main()
