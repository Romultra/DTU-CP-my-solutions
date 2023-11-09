"""Exercise 7.4: Returning multiple values."""


def returning_multiple_values(values: list, threshold: int) -> tuple:
    """Return a tuple containing a list of all elements in the list that are greater than the threshold and the minimum of the values.

    :param values: A list of integers.
    :param threshold: An integer.
    :return: A tuple containing the a list of elements that are greater than the threshold and the minimum of values
    """
    new_values = []
    min_value = values[0]
    for value in values:
        if value > threshold:
            new_values.append(value)
        if value < min_value:
            min_value = value
    
    return (new_values, min_value)