"""Exercise 3.10: Ackermann's function."""

def ackermann(m:int, n:int):
    """Compute the Ackermann's function :math:`A(m, n)`.

    Your implementation should use recursion and not loops.

    :param m: the variable m.
    :param n: the variable n.
    :return: the computed value :math:`A(m,n)`.
    """
    if m == 0 :
        return n+1
    
    elif m > 0 and n == 0 :
        return ackermann(m-1, 1)
    
    elif m > 0 and n > 0 :
        return ackermann(m-1, ackermann(m, n-1))