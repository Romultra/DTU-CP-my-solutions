"""Exercise 3.9: Exponential function."""

def exponential(x : float, n : int) -> float:
    """Compute the exponential :math:`x^n` using recursion.

    First focus on the case where :math:`n=0`, then :math:`n > 0` and finally :math:`n < 0`.

    :param x: the base number :math:`x`.
    :param n: the power :math:`n`.
    :return: the computed value.
    """
    if n == 0 :
        return 1
    
    elif n < 0 :
        return 1/exponential(x,-n)
    
    else :
        return x*exponential(x, n-1)