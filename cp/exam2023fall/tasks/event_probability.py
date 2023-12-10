"""Task 1: Event probability."""

def event_probability(T: int, n: int) -> float:
    """Return the event probability.

    :param T: A positive integer, the return period.
    :param n: A positive integer, the time period.
    :return: The probability that an event with return period T will occur in the time period. 
    """
    return 1 - (1-(1/T))**n


if __name__ == '__main__':
    print(event_probability(100, 25))
