import datetime as dt
import random
from functools import cached_property

from data import LOCATIONS, DATE_LOOKUP


class Date:
    def __init__(self, year, month, day, location=None, is_gregorian=True):
        self.year = year  # Year 0 is 1 BCE
        self.month = month
        self.day = day
        self.location = location
        self.is_gregorian = is_gregorian

    def __str__(self):
        result = self._date.strftime("%d. %B ")
        if self.year < 1:
            result += f"{abs(year) + 1} BCE"
        else:
            result += str(abs(self.year))
        if self.location:
            result += f" in {self.location}"
        return result

    @cached_property
    def _date(self):
        return dt.date(self.year if self.year > 0 else abs(self.year) + 1, self.month, self.day)

    @cached_property
    def is_leap_year(self):
        return is_leap_year(self.year, self.is_gregorian)

    @cached_property
    def weekday(self):
        """Monday is 0, Sunday is 6"""
        # we could use .weekday() plus an adjustment value down to the year 0, but
        # not before that, so let's just use the stupid table, I guess
        total = 0
        centuries = int(self.year / 100)
        years = self.year % 100
        if self.is_gregorian:
            total += DATE_LOOKUP["centuries_gregorian"][centuries % 4]
        else:
            total += DATE_LOOKUP["centuries_julian"][centuries % 7]
        total += DATE_LOOKUP["years"][years]
        if self.is_leap_year:
            total += DATE_LOOKUP["months_leap"][self.month]
        else:
            total += DATE_LOOKUP["months"][self.month]
        total += self.day
        return DATE_LOOKUP["weekday"][total % 7]

    @cached_property
    def weekday_string(self):
        return [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ][self.weekday]


def get_random_date():
    """
    You'd think that grabbing a random date is easy, wouldn't you?

    First off, a qualifier: Picking a random /European/ date.
    This excludes non-European calendars, and calendar reforms
    in the colonies, because I can't be arsed to learn those.

    We're starting by picking a year and a month at random, because
    those always exist, thank fuck. Now, we can't pick a random
    day next, because the available days depend on the calendar
    in use, which, between 1582 and 1924, depends on the location.
    So we pick a location, and then we can make sure that
    a) we're not using leap days that did not exist, and b)
    that our random date did actually occur.

    I'm tempted to add a mode where "Trick question, this date did
    not occur" is a valid answer.

    Some of this is imprecise, because I can't be arsed to make
    sure countries are only included when they actually existed.
    """
    year = random.randrange(-44, dt.date.today().year + 200)
    month = random.randrange(1, 13)
    day = None
    location = None

    if (1582, 10) <= (year, month) <= (1924, 10):
        # uhhhm, where are we
        location = random.choice(list(LOCATIONS.keys()))
        julian_end, gregorian_start = LOCATIONS[location]

        if (year, month) < (julian_end[0], julian_end[1]):  # easy
            is_gregorian = False
        elif (year, month) > (gregorian_start[0], gregorian_start[1]):  # easy
            is_gregorian = True
        else:  # aw man
            if (
                year == julian_end[0] and month == julian_end[1]
            ):  # Biased towards Julian calendar, wooo
                is_gregorian = False
                day = random.randrange(1, julian_end[2] + 1)
            else:
                is_gregorian = True
                day = (
                    gregorian_start[2]
                    if gregorian_start[2] > 28
                    else random.randrange(gregorian_start[2], 29)
                )  # nothing to see here
    else:
        is_gregorian = year > 1800  # things could be so simple

    if not day:
        day = get_random_day(year, month, is_gregorian=is_gregorian)

    return Date(
        year=year, month=month, day=day, location=location, is_gregorian=is_gregorian
    )


def is_leap_year(year, is_gregorian):
    if is_gregorian:
        try:
            dt.date(year, 2, 29)
            return True
        except ValueError:
            return False
    return year % 4 == 0


def get_random_day(month, year, is_gregorian):
    if month != 2:  # We should be so lucky
        max_days = 30 if month in (4, 6, 9, 11) else 31
    else:
        max_days = 29 if is_leap_year(year, is_gregorian) else 28
    return random.randrange(1, max_days + 1)


def main():
    date = get_random_date()
    print(date)


if __name__ == "__main__":
    main()
