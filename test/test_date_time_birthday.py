import unittest
import datetime
from more_fun_with_collections import date_time_birthday


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        birthday = datetime.datetime(2020, 6, 19)
        self.assertEqual(date_time_birthday.half_birthday(birthday), datetime.datetime(2020, 12, 19))


if __name__ == '__main__':
    unittest.main()
