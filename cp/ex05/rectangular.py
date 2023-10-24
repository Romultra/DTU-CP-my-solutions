"""Exercise 5.6. Rectangular list."""

def is_rectangular(nested_list: list) -> bool:
    """Check if a list is rectangular.
    
    :param nested_list: nested list
    :return: True if list is rectangular, False otherwise
    """
    previous_list_len = -1
    for list_ in nested_list:
        if previous_list_len != len(list_) and previous_list_len != -1:
            return False
        previous_list_len = len(list_)
    return True