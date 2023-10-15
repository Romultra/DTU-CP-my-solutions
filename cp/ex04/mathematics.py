"""Exercise 4.1 and 4.2."""
import math

def square_root(a : float) -> float:
    r"""Compute the square root, see section 7.5 in Think Python.

    :param a: A number to compute the square root of.
    :return: :math:`\sqrt{a}`.
    """
    y=a
    x=y+1
    while abs(y-x) > 0.0000001:
        x = y
        y = (x+(a/x))/2
    return y

def ramanujan() -> float:
    r"""Compute the Ramanujan approximation of :math:`\pi` using a sufficient number of terms.

    :return: A high-quality approximation of :math:`\pi` as a ``float``.
    """
    sum = 0
    pi = 0
    k = 0
    while True:
        if abs(pi - math.pi ) < 0.0000001 :
            return pi
        
        sum = sum + math.factorial(4*k) * (1103+26390*k) /(math.factorial(k)**4 * 396**(4*k) )

        pi = abs(1/(((2*2**0.5)/9801) * sum))

        k += 1

if __name__ == "__main__":
    # here you can try out your functions
    print("approximate pi", ramanujan())
    print("square root of 2 is", square_root(144))
