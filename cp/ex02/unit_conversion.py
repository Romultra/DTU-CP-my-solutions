"""Exercise: Convert length in foot and inch to centimeter."""
import math

def unit_conversion(foot:int, inch:int):
    """Convert length in foot and inch to centimeter.

    :param foot: foot portion of the length in imperical unit.
    :param inch: inch portion of the length in imperical unit.
    """
    length_cm = round(foot*30.48 + inch*2.54)
    print(f'{foot} ft {inch} in is equal to {length_cm} cm.')

unit_conversion(7, 5)     # Output : '7 ft 5 in is equal to 226 cm.'
