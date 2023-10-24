"""Exercise 5.3-5.4. Conditioned maximum."""

def conditioned_maximum(nums: list, threshold: float) -> float:
    """Return the maximum of a list of numbers, that is strictly smaller than the given threshold.
    
    :param nums: list of numbers
    :param threshold: limit for maximum value   
    :return: maximum of list thats smaller than the threshold
    """
    maximum = 0
    for num in nums:
        if num < threshold and num > maximum:
            maximum = num
    return maximum


def conditioned_maximum_name(nums: list, names: list, threshold: float) -> str:
    """Return the name of the maximum of a list of numbers, that is smaller than the given threshold.
    
    :param nums: list of numbers with animal heights.
    :param names: list of animal names
    :param threshold: limit for maximum value   
    :return: animal name with the corresponding maximum height, which is shorter than the threshold height.
    """
    maximum = 0
    for i, num in enumerate(nums):
        if num < threshold and num > maximum:
            maximum = num
            maximum_index = i

    return names[maximum_index]