"""Problems for the Bisection project in week 3."""
import math

def f(x : float) -> float:
    r"""Find the roots of this function.

    You should implement the function :math:`f(x)` here. It is defined as:

    .. math::

        f(x) = \sin(3\cos(\frac{1}{2} x^2))


    :param x: The value to evaluate the function in :math:`x`
    :return: :math:`f(x)`.
    """
    # TODO: 1 lines missing.
    raise NotImplementedError("Compute f(x) here.")
    return y


def is_there_a_root(a : float, b : float) -> bool:
    """Return ``True`` if we are guaranteed there is a root of ``f`` in the interval :math:`[a, b]`.

    :param a: Lowest x-value to consider
    :param b: Highest x-value to consider
    :return: ``True`` if we are guaranteed there is a root otherwise ``False``.
    """
    # TODO: 1 lines missing.
    raise NotImplementedError("Compute the condition here")
    return has_root

def bisect(xmin : float, xmax : float, delta : float) -> float:
    """Find a candidate root within ``xmin`` and ``xmax`` within the given tolerance.

    :param xmin: The minimum x-value to consider
    :param xmax: The maximum x-value to consider
    :param delta: The tolerance.
    :return: The first value :math:`x` which is within ``delta`` distance of a root according to the bisection algorithm
    """
    # TODO: 6 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")



if __name__ == "__main__":
    print("Are we guaranteed there is a zero within the interval [1, 3]?", is_there_a_root(1, 3), "(this should be True)")
    print("Are we guaranteed there is a zero within the interval [1, 3.5]?", is_there_a_root(1, 3.5), "(this should be False)")

    print("Find a zero within tolerance 0.1 in the interval [1, 2]")
    print(bisect(1, 2, 0.1))
    print("Same, but with a tolerance of 0.5")
    print(bisect(1, 2, 0.1))

    print("Should return math.nan")
    print(bisect(1, 3.5, 0.1))
