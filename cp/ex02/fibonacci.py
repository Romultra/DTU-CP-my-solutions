"""Exercise 2.3: The Fibonacci sequence and recursion."""

def fibonacci_number(k):
    """Compute the :math:`k`'th Fibonacci number :math:`x_k`.

    The function use the recursive relationship :math:`x_{k+1} = x_k + x_{k-1}`, along with the initial conditions
    :math:`x_0 =0, x_1 = 1`, to complete the sequence up to :math:`k`.

    :param k: An integer
    :return:  The corresponding term :math:`x_k` of the Fibonacci sequence as an integer.
    """
    if k == 0:
        # TODO: 1 lines missing.
        raise NotImplementedError("Insert your solution and remove this error.")
    elif k == 1:
        # TODO: 1 lines missing.
        raise NotImplementedError("Insert your solution and remove this error.")
    else:
        # TODO: 1 lines missing.
        raise NotImplementedError("Fix this stuff")

if __name__ == "__main__":
    print("The term x_0 should be 0, you got:", fibonacci_number(0))
    print("The term x_1 should be 1, you got:", fibonacci_number(1))
    print("The term x_2 should be 1, you got:", fibonacci_number(1))
    print("The term x_6 should be 8, you got:", fibonacci_number(6))
