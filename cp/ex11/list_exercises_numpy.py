"""Exercise 11.5: Revisit lists."""
import numpy as np
def avg(data: np.ndarray) -> float:
    """Return the average of an array.
    
    :param data: The array to average.
    :return: The average of the array.
    """
    return np.mean(data)

def conditional_max(data: np.ndarray, threshold: float) -> float:
    """Return the maximum value in the array that is smaller than the threshold.

    :param data: The array to search.
    :param threshold: The threshold to compare against.
    :return: The maximum value in the array that is smaller than the threshold.
    """
    return np.max(data[data<threshold])

def vector_add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Add two vectors together.

    :param a: The first vector.
    :param b: The second vector.
    :return: The sum of the two vectors.
    """
    return a+b

def count_multiples(data: np.ndarray, divisor: int) -> int:
    """Count the number of multiples of a number in an array.

    :param data: The array to search.
    :param divisor: The number to check for multiples of.
    :return: The number of multiples of the divisor in the array.
    """
    return data[data%divisor==0].shape[0]

def return_multiples(data, divisor):
    """Return the multiples of a number in an array.

    :param data: The array to search.
    :param divisor: The number to check for multiples of.
    :return: The multiples of the divisor in the array.
    """
    return data[data%divisor==0]