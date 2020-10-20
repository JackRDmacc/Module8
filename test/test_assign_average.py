import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_a(self):
        self.assertEqual(assign_average.switch_average('A'), 'You entered an A!')

    def test_b(self):
        self.assertEqual(assign_average.switch_average('B'), 'You entered a B!')

    def test_c(self):
        self.assertEqual(assign_average.switch_average('C'), 'You entered a C!')

    def test_d(self):
        self.assertEqual(assign_average.switch_average('D'), 'You entered a D!')

    def test_f(self):
        self.assertEqual(assign_average.switch_average('F'), 'You entered an F!')

    def test_non_key(self):
        self.assertEqual(assign_average.switch_average('Z'), 'This is not a valid Grade')


if __name__ == '__main__':
    unittest.main()
