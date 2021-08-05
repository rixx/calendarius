import datetime as dt
import random


"""
The AMAZING source for all these locations and their date skipping
shenanigans is https://norbyhus.dk/calendar.php
You can find my parsing code in ./data.py
💌 Historians 💌
"""
LOCATIONS = {  # Location: last Julian date, first Gregorian date
    # "Bulgaria": (( 1915, 10, 31), ( 1915, 11, 14)),  # has two dates, confusing
    # "Greece": (( 1923, 2, 15), ( 1923, 3, 1))  # has two dates, confusing
    # "Lithuania": ((1915, 11, 15), (1915, 11, 29)),  # adopted in 1584, reverted in 1800 under Russian administration
    # "Luxemburg": ((1582, 12, 14), (1582, 12, 25)),  # has two dates, confusing
    # Romania outside Transylvania has four different dates between 1864 and 1920 depending on source and religion
    # Serbia has three dates, 1878, 1919, 1923, excluding
    # "Sweden": ((1753, 2, 17), (1753, 3, 1)),  # Excluding for their incredibly fucked up period from 1700-1753
    # "Finland": ((1753, 2, 17), (1753, 3, 1)),  # Excluded as part of Sweden (later Russian occupation did NOT actually fuck with their calendar)
    # Turkey excluded because they only adopted the Julian calendar in 1789
    # "Groningen, Netherlands": ((1583, 2, 28), (1583, 3, 11)), flopped back in 1594
    "Salzburg, Austria": ((1583, 10, 5), (1583, 10, 16)),
    "Kärnten (Carinthia), Austria": ((1583, 12, 14), (1583, 12, 25)),  # Short advent
    "Steiermark, Austria": ((1583, 12, 14), (1583, 12, 25)),  # Short advent
    "Brabant, Belgium": ((1582, 12, 21), (1583, 1, 1)),  # NO CHRISTMAS?!
    "Flanders, Belgium": ((1582, 12, 21), (1583, 1, 1)),  # NO CHRISTMAS?!
    "Liege (Lüttich), Belgium": ((1583, 2, 10), (1583, 2, 21)),
    "Croatia": ((1923, 9, 30), (1923, 10, 14)),
    "Bohemia (Böhmen), Czech Republic": ((1584, 1, 6), (1584, 1, 17)),
    "Moravia (Mähren), Czech Republic": ((1584, 1, 6), (1584, 1, 17)),
    "Denmark": ((1700, 2, 18), (1700, 3, 1)),
    "Norway": ((1700, 2, 18), (1700, 3, 1)),
    "England": ((1752, 9, 2), (1752, 9, 14)),
    "Estonia": ((1918, 1, 31), (1918, 2, 14)),
    "Lorraine (Lothringen), France": ((1582, 12, 9), (1582, 12, 20)),
    "Alsace (Elsass), France": ((1583, 10, 13), (1583, 10, 24)),
    "Strasbourg, France": ((1682, 2, 5), (1682, 2, 16)),
    "Færø Islands, Denmark": (
        (1700, 11, 16),
        (1700, 11, 28),
    ),  # Part of Denmark, but late
    "Augsburg, Germany": ((1583, 2, 13), (1583, 2, 24)),
    "Trier, Germany": ((1583, 10, 4), (1583, 10, 15)),
    "Bavaria (Bayern), Germany": ((1583, 10, 5), (1583, 10, 16)),
    "Breisgau, Germany": ((1583, 10, 13), (1583, 10, 24)),
    "Duchy of Jülich, Germany": ((1583, 11, 2), (1583, 11, 13)),
    "Köln (Cologne), Germany": ((1583, 11, 3), (1583, 11, 14)),
    "Aachen, Germany": ((1583, 11, 3), (1583, 11, 14)),
    "Würzburg, Germany": ((1583, 11, 4), (1583, 11, 15)),
    "Mainz (Mayence), Germany": ((1583, 11, 11), (1583, 11, 22)),
    "Baden, Germany": ((1583, 11, 16), (1583, 11, 27)),
    "Münster, Germany": ((1583, 11, 17), (1583, 11, 28)),
    "Cleve, Germany": ((1583, 11, 17), (1583, 11, 28)),
    "Silesia (Schlesien)": ((1584, 1, 12), (1584, 1, 23)),
    "Lausitz (Lusatia), Germany": ((1584, 1, 12), (1584, 1, 23)),
    "Westfalen (Westphalia), Germany": ((1584, 7, 1), (1584, 7, 12)),
    "Paderborn, Germany": ((1585, 6, 16), (1585, 6, 27)),
    "Neuburg a. d. Donau (Pfalz-Neuburg), Germany": ((1615, 12, 13), (1615, 12, 24)),
    "Hildesheim, Germany": ((1631, 3, 15), (1631, 3, 26)),
    "Minden, Germany": ((1668, 2, 1), (1668, 2, 12)),
    "Stuttgart, Germany": ((1700, 2, 18), (1700, 3, 1)),  # example protestant locations
    "Nuremberg, Germany": ((1700, 2, 18), (1700, 3, 1)),  # example protestant locations
    "Berlin, Germany": ((1700, 2, 18), (1700, 3, 1)),  # example protestant locations
    "Darmstadt, Germany": ((1700, 2, 18), (1700, 3, 1)),  # example protestant locations
    "Erfurt, Germany": ((1700, 2, 18), (1700, 3, 1)),  # example protestant locations
    "Leipzig, Germany": ((1700, 2, 18), (1700, 3, 1)),  # example protestant locations
    "Lüneburg, Germany": ((1700, 2, 18), (1700, 3, 1)),  # example protestant locations
    "Hamburg, Germany": ((1700, 2, 18), (1700, 3, 1)),  # example protestant locations
    "Rostock, Germany": ((1700, 2, 18), (1700, 3, 1)),  # example protestant locations
    "Hungary": ((1584, 1, 22), (1584, 2, 2)),
    "Iceland": ((1700, 11, 16), (1700, 11, 28)),
    "Ireland": ((1752, 9, 2), (1752, 9, 14)),
    "Italy": (
        (1582, 10, 4),
        (1582, 10, 15),
    ),  # ignoring the Florentine and Pisan calendars
    "Latvia": ((1918, 2, 1), (1918, 2, 1)),  # … once it existed
    "Artois": ((1582, 12, 14), (1582, 12, 25)),
    "Antwerp, Netherlands": ((1582, 12, 20), (1582, 12, 31)),
    "Limburg": ((1582, 12, 21), (1583, 1, 1)),  # Netherlands, then
    "Arnhem, Netherlands": ((1700, 6, 30), (1700, 7, 12)),  # Gelderland
    "Utrecht, Netherlands": ((1700, 11, 30), (1700, 12, 12)),
    "Friesland, Netherlands": ((1700, 12, 31), (1701, 1, 12)),
    "Poland": ((1582, 10, 4), (1582, 10, 15)),
    "Duchy of Prussia (Preußen)": ((1610, 8, 22), (1610, 9, 2)),
    "Portugal": ((1582, 10, 4), (1582, 10, 15)),
    "Transylvania (Siebenbürgen/Erdely), Romania": ((1590, 12, 14), (1590, 12, 25)),
    "Russia": ((1918, 1, 31), (1918, 2, 14)),
    "Scotland": ((1752, 9, 2), (1752, 9, 14)),
    "Slovakia": ((1584, 1, 22), (1584, 2, 2)),  # as part of Hungary tbh
    "Spain": ((1582, 10, 4), (1582, 10, 15)),
    "Lucerne (Luzern), Switzerland:": ((1584, 1, 11), (1584, 1, 22)),
    "Uri, Switzerland:": ((1584, 1, 11), (1584, 1, 22)),
    "Zürich, Switzerland:": ((1700, 12, 31), (1701, 1, 12)),
    "Bern, Switzerland:": ((1700, 12, 31), (1701, 1, 12)),
    "Geneva, Switzerland:": ((1700, 12, 31), (1701, 1, 12)),
}


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
    year = random.randrange(-45, dt.date.today().year + 200)
    month = random.randrange(1, 13)
    day = None
    location = None
    year = 1600

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

    return {
        "year": year,
        "month": month,
        "day": day,
        "location": location,
        "is_gregorian": is_gregorian,
    }


def get_random_day(month, year, is_gregorian):
    if month != 2:  # We should be so lucky
        max_days = 30 if month in (4, 6, 9, 11) else 31
    elif not is_gregorian:
        max_days = 29 if year % 4 == 0 else 28
    else:  # sigh
        try:
            dt.date(year, 2, 29)
            max_days = 29
        except ValueError:
            max_days = 28
    return random.randrange(1, max_days + 1)


def main():
    date = get_random_date()
    print(date)


if __name__ == "__main__":
    main()
