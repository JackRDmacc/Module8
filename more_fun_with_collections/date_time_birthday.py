"""Jack Reser
This program calculates a half-birthday
10/19/20"""

import datetime
import dateutil
from dateutil.relativedelta import relativedelta


def half_birthday(my_b_day):
    my_b_day = my_b_day.date()
    my_half_b_day = my_b_day + relativedelta(months=6)

    return my_half_b_day
