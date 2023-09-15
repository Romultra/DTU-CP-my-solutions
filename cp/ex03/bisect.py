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
    Compute f(x) here.
    # TODO: Code has been removed from here.


def is_there_a_root(a : float, b : float) -> bool:
    """Return ``True`` if we are guaranteed there is a root of ``f`` in the interval :math:`[a, b]`.

    :param a: Lowest x-value to consider
    :param b: Highest x-value to consider
    :return: ``True`` if we are guaranteed there is a root otherwise ``False``.
    """
    # TODO: Code has been removed from here. 

def bisect(xmin : float, xmax : float, delta : float) -> float:
    """Find a candidate root within ``xmin`` and ``xmax`` within the given tolerance.

    :param xmin: The minimum x-value to consider
    :param xmax: The maximum x-value to consider
    :param delta: The tolerance.
    :return: The first value :math:`x` which is within ``delta`` distance of a root according to the bisection algorithm
    """
    # TODO: Code has been removed from here. 

