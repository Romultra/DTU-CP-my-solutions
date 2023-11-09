"""Exercise 7.4: Color Hue."""

def rgb_to_hue(RGB: tuple) -> float:
    """Return the hue given RGB values.

    :param RGB: Tuple containing  three RGB values.
    :return: Hue in degrees.
    """
    max_value = RGB[0]
    max_name = 0
    min_value = RGB[0]
    
    for i, value in enumerate(RGB):
        if value > max_value:
            max_value = value
            max_name  = i
        if value < min_value:
            min_value = value
    
    delta = max_value - min_value

    if max_name == 0:
        H = 60 * (RGB[1] - RGB[2])/delta
    elif max_name == 1:
        H = 120 + 60 * (RGB[2] - RGB[0])/delta
    else:
        H = 240 + 60 * (RGB[0] - RGB[1])/delta

    if H < 0:
        H = H + 360
    
    return H