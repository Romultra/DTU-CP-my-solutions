"""Exercise 5.2. Average of lists."""

def calculate_average(nums: list) -> float:
    """Return the average of a list of numbers.
    
    :param nums: list of numbers
    :return: average of list
    """
    sum=0
    for i in nums:
        sum = sum + i
    
    return sum/len(nums)

print(calculate_average([2,4,2,4]))