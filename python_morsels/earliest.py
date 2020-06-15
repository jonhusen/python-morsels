"""
I want you to write a function that takes two strings representing dates
and returns the string that represents the earliest point in time.
The strings are in the US-specific MM/DD/YYYY format... just to make things
harder. Note that the month, year, and day will always be represented
by 2, 4, and 2 digits respectively.

Your function should work like this:

>>> get_earliest("01/27/1832", "01/27/1756")
"01/27/1756"
>>> get_earliest("02/29/1972", "12/21/1946")
"12/21/1946"
>>> get_earliest("02/24/1946", "03/21/1946")
"02/24/1946"
>>> get_earliest("06/21/1958", "06/24/1958")
"06/21/1958"

There's a catch though. Your exercise should work with invalid month
and date combinations. What I mean by that is that dates like 02/40/2006
should be supported. By that I mean 02/40/2006 is before 03/01/2006 but
after 02/30/2006 (dates don't roll over at all). I'm adding this requirement
so you can't rely on Python's datetime module.

Bonus
If you complete the main exercise, there's also a bonus for you to attempt:
allow the function to accept any number of arguments and return the earliest
date string of all provided.

So if you complete the bonus, this should work:

>>> get_earliest("02/24/1946", "01/29/1946", "03/29/1945")
"03/29/1945"
"""


def get_earliest(*args):
    """Takes US-format dates as strings and returns the earliest

    Args:
        *args: Tuple of dates of arbitrary length

    Returns: Earliest date as a string

    """
    # Original implementation
    # dates = [tuple(arg.split("/")) for arg in args]
    # earliest = dates[0]
    # for date in dates:
    #     m1, d1, y1 = earliest
    #     m2, d2, y2 = date
    #     if y1 < y2:
    #         continue
    #     elif y1 == y2:
    #         if m1 < m2:
    #             continue
    #         elif m1 == m2:
    #             if d1 < d2:
    #                 continue
    #     earliest = date
    # return "/".join(earliest)

    # PM solution
    def date_key(date):
        (m, d, y) = date.split("/")
        return (y, m, d)
    return min(args, key=date_key)
