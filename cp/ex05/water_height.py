"""Exercise 5.10. Water height."""

def water_height(h0: int, r: list) -> int:
    """Calculate the water height after multiple days of rain.

    :param: h0: initial height of the water
    :param: r: list of rain showers
    :return: height of water after days of rain 
    """
    for showers in r:
        h0 += showers - 2
        if h0 < 0:
            h0 = 0
    return h0
