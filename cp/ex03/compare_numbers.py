"""Exercise 3.5: Compare numbers."""

def compare_numbers(first_number:int, second_number:int) -> str:
    """Return a string based on which number has the greatest numerical value.

    :param first_number: first number.
    :param second_number: second number.
    :return: string stating which number is the greatest.
    """
    if first_number > second_number :
        return "the first number is greater"
    elif first_number < second_number :
        return "the second number is greater"
    else :
        return 'the numbers are equal'