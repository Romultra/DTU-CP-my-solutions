"""Task 6: Collatz conjecture."""

def collatz_conjecture(n: int) -> int:
    """Return the number of steps to reach 1 in the Collatz conjecture.
    
    :param n: A positive integer, the starting number.
    :return: A positive integer, the number of steps.
    """
    steps = 0
    while n != 1:
        if n%2 == 0:
            n = n/2
        elif n%2 != 0:
            n = 3*n+1
        steps += 1
    return steps
    
if __name__ == '__main__':
    print(collatz_conjecture(3))
