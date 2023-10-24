"""Exercise 5.7. Vector additon."""

def vector_add(v: list, w: list) -> list:
    """Add two vectors.
    
    :param v: vector 1 (list of numbers)
    :param w: vector 2 (list of numbers, same length as v)
    :return: sum of v and w (list of number)
    """
    return [v[0]+w[0], v[1]+w[1], v[2]+w[2]]
