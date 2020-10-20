import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_a(self):
        self.assertEqual(assign_average.switch_average('A'), 'a')

    def test_b(self):
        self.assertEqual(assign_average.switch_average('B'), 'b')

    def test_c(self):
        self.assertEqual(assign_average.switch_average('C'), 'c')

    def test_d(self):
        self.assertEqual(assign_average.switch_average('D'), 'd')

    def test_e(self):
        self.assertEqual(assign_average.switch_average('E'), 'e')

    def test_non_key(self):
        self.assertEqual(assign_average.switch_average('F'), 'not found')


if __name__ == '__main__':
    unittest.main()
