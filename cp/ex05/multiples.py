"""Exercise 5.8.-5-9. Count multiples."""

def count_multiples(numbers: list, m: int)  -> int:
    """Count the number of numbers that are divisible by m.
    
    :param numbers: list of numbers
    :param m: number to divide by
    :return: number of numbers that are divisible by m
    """
    count = 0
    for num in numbers:
        if num % m == 0:
            count+=1
    return count

def multiples_list(numbers: list, m: int)  -> list:
    """Make a list with all numbers from a list that are divisible by m.
    
    :param numbers: list of numbers
    :param m: number to divide by
    :return: list of numbers that are divisible by m
    """
    num_list = []
    for num in numbers:
        if num % m == 0:
            num_list.append(num)
    return num_list