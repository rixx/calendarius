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
    "Lucerne (Luzern), Switzerland": ((1584, 1, 11), (1584, 1, 22)),
    "Uri, Switzerland": ((1584, 1, 11), (1584, 1, 22)),
    "Zürich, Switzerland": ((1700, 12, 31), (1701, 1, 12)),
    "Bern, Switzerland": ((1700, 12, 31), (1701, 1, 12)),
    "Geneva, Switzerland": ((1700, 12, 31), (1701, 1, 12)),
}


# The date lookup is entirely taken from Wikipedia
# https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Complete_table:_Julian_and_Gregorian_calendars
# Tested to work correctly with:
# - current date
# - Thursday, 4 October 1582 (is_gregorian=False)
# - Friday, 15 October 1582 (is_gregorian=True)
DATE_LOOKUP = {
    "centuries_gregorian": {0: 0, 1: 5, 2: 3, 3: 1},
    "centuries_julian": {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0, 6: 6},
    "years": {},
    "months": {
        1: 0,
        2: 3,
        3: 3,
        4: 6,
        5: 1,
        6: 4,
        7: 6,
        8: 2,
        9: 5,
        10: 0,
        11: 3,
        12: 5,
    },
    "months_leap": {
        1: 6,
        2: 2,
        3: 3,
        4: 6,
        5: 1,
        6: 4,
        7: 6,
        8: 2,
        9: 5,
        10: 0,
        11: 3,
        12: 5,
    },
    "weekday": {0: 5, 1: 6, 2: 0, 3: 1, 4: 2, 5: 3, 6: 4},
}
reverse_year_lookup = {
    0: [0, 6, 17, 23, 28, 34, 45, 51, 56, 62, 73, 79, 84, 90],
    1: [1, 7, 12, 18, 29, 35, 40, 46, 57, 63, 68, 74, 85, 91, 96],
    2: [2, 13, 19, 24, 30, 41, 47, 52, 58, 69, 75, 80, 86, 97],
    3: [3, 8, 14, 25, 31, 36, 42, 53, 59, 64, 70, 81, 87, 92, 98],
    4: [9, 15, 20, 26, 37, 43, 48, 54, 65, 71, 76, 82, 93, 99],
    5: [4, 10, 21, 27, 32, 38, 49, 55, 60, 66, 77, 83, 88, 94],
    6: [5, 11, 16, 22, 33, 39, 44, 50, 61, 67, 72, 78, 89, 95],
}
for key, values in reverse_year_lookup.items():
    for value in values:
        DATE_LOOKUP["years"][value] = key
