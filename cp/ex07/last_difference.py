"""Exercise 7.3: Last difference."""

def last_difference(a : tuple, b : tuple) -> float:
    """Return the difference between last elements regardless of length.

    :param a: The first tuple.
    :param b: The second tuple.
    :return: The difference between the last elements of the two tuples.
    """
    return a[len(a)-1] - b[len(b)-1]