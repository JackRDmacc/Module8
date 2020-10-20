import unittest
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertEqual(dict_membership.in_dict({'A': 90, 'B': 80, 'C': 70, 'D': 60}, 'A'), True)

    def test_in_dict_false(self):
        self.assertEqual(dict_membership.in_dict({'A': 90, 'B': 80, 'C': 70, 'D': 60}, 'F'), False)


if __name__ == '__main__':
    unittest.main()
