"""Exercise 3.5: Compare numbers."""

def compare_numbers(first_number:int, second_number:int) -> str:
    """Return a string based on which number has the greatest numerical value.

    :param first_number: first number.
    :param second_number: second number.
    :return: string stating which number is the greatest.
    """
    if first_number > second_number :
        greater_number = "first"
    else :
        greater_number = "second"
    
    return f"The {greater_number} number has the greatest numerical value"

print(compare_numbers(5,2))     # Output : 'The first number has the greatest numerical value'