import datetime


def gen_secs():
    """
    Generator function for seconds (0-59).

    Yields
    ------
    int
        The next second in the range 0-59.
    """
    for sec in range(60):
        yield sec


def gen_minutes():
    """
    Generator function for minutes (0-59).

    Yields
    ------
    int
        The next minute in the range 0-59.
    """
    for min in range(60):
        yield min


def gen_hours():
    """
    Generator function for hours (0-23).

    Yields
    ------
    int
        The next hour in the range 0-23.
    """
    for h in range(24):
        yield h


def gen_time():
    """
    Generator function for time in the format "hh:mm:ss".

    Yields
    ------
    str
        The next time string in the format "hh:mm:ss".
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)


def gen_years(start=datetime.datetime.now().year):
    """
    Generator function for years starting from a given year.

    Parameters
    ----------
    start : int, optional
        The starting year (default is the current year).

    Yields
    ------
    int
        The next year starting from the given start year.
    """
    year = start
    while True:
        yield year
        year += 1


def gen_months():
    """
    Generator function for months (1-12).

    Yields
    ------
    int
        The next month in the range 1-12.
    """
    for month in range(1, 13):
        yield month


def is_leap_year(year):
    """
    Function to check if a year is a leap year.

    Parameters
    ----------
    year : int
        The year to check.

    Returns
    -------
    bool
        True if the year is a leap year, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def gen_days(month, leap_year=True):
    """
    Generator function for days in a given month, considering leap years.

    Parameters
    ----------
    month : int
        The month for which to generate days.
    leap_year : bool, optional
        Whether the year is a leap year (default is True).

    Yields
    ------
    int
        The next day in the given month.
    """
    days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    for day in range(1, days_in_month[month] + 1):
        yield day


def gen_date():
    """
    Generator function for full date in the format "dd/mm/yyyy hh:mm:ss".

    Yields
    ------
    str
        The next date string in the format "dd/mm/yyyy hh:mm:ss".
    """
    for year in gen_years():
        for month in gen_months():
            leap_year = is_leap_year(year)
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)


# Example usage of the gen_date generator
date_gen = gen_date()
iteration_count = 0

while True:
    date = next(date_gen)
    iteration_count += 1
    if iteration_count % 1000000 == 0:
        print(date)