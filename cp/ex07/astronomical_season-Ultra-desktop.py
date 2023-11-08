"""Exercise 7.9: Astronomical season."""

def astronomical_season(date :  tuple) -> str:
    """Return the astronomical season of the given date.

    :param date: Tuple with the given date.
    :return: String with astronomical season
    """
    month_name_to_month_number = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    day_number = date[0]
    month_number = month_name_to_month_number[date[1]]

    if 3 < month_number < 6 or (month_number == 3 and day_number >= 20) or (month_number == 6 and day_number <= 20):
        return 'spring'
    
    if 6 < month_number < 9 or (month_number == 6 and day_number >= 21) or (month_number == 9 and day_number <= 22):
        return 'summer'
    
    if 9 < month_number < 12 or (month_number == 9 and day_number >= 23) or (month_number == 12 and day_number <= 20):
        return 'autumn'
    
    if month_number < 3 or (month_number == 12 and day_number >= 21) or (month_number == 3 and day_number <= 19):
        return 'winter'