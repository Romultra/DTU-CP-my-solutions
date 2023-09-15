"""Exercise 3.7: Solar panel."""

def solar_panel(move : bool, swap : bool, hot : bool, empty : bool) -> str:
    """Print out whether it is a good idea to install solar panels on an object with the given properties.

    :param move: does the object move around?
    :param swap: does the object allow swapping or recharging battery?
    :param hot: is the object hot to the touch when it is running?
    :param empty: are there other empty places near the object?
    :return: Whether you should put solar panels on the object as a string.
    """
    if move and not(swap) and not(hot) :
        return 'maybe'
    
    elif move and not(swap) and (hot) :
        return 'haha, good luck'
    
    elif (move and swap)  or (not(move) and empty):
        return 'probably not'
    
    elif not(move) and not(empty) :
        return 'sure'