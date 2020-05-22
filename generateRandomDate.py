"""
Author : Ashutosh Kumar
Version : 1.0
Description : Generate Random Date Between a Given Range
Email : ashutoshkumardbms@gmail.com
"""

from random import randrange

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


from datetime import datetime, timedelta

d1 = datetime.strptime('1/1/2020 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('3/28/2020 11:59 PM', '%m/%d/%Y %I:%M %p')

print(random_date(d1, d2))
