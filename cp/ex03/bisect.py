"""Problems for the Bisection project in week 3."""
import math

def f(x : float) -> float:
    r"""Find the roots of this function.

    You should implement the function f(x) here.

    :param x: The value to evaluate the function in x
    :return: f(x)
    """
    return math.sin( 3*math.cos((x**2)/2))


def is_there_a_root(a : float, b : float) -> bool:
    """Return ``True`` if we are guaranteed there is a root of ``f`` in the interval :math:`[a, b]`.

    :param a: Lowest x-value to consider
    :param b: Highest x-value to consider
    :return: ``True`` if we are guaranteed there is a root otherwise ``False``.
    """
    if f(a) == 0 or f(b) == 0 or (f(a) < 0 and f(b) > 0) or (f(a) > 0 and f(b) < 0) : 
        return True
    else :
        return False

def bisect(xmin : float, xmax : float, delta : float) -> float:
    """Find a candidate root within ``xmin`` and ``xmax`` within the given tolerance.

    :param xmin: The minimum x-value to consider
    :param xmax: The maximum x-value to consider
    :param delta: The tolerance.
    :return: The first value :math:`x` which is within ``delta`` distance of a root according to the bisection algorithm
    """
    midpoint = (xmin+xmax)/2
    if not(is_there_a_root(xmin, xmax)) :
        return math.nan
    
    elif xmax - xmin <= 2*delta :
        return midpoint
    
    elif is_there_a_root(xmin, midpoint) :
        return bisect(xmin, midpoint, delta)
    
    else :
        return bisect(midpoint, xmax, delta)