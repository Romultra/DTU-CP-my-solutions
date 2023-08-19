"""Project work for week 9, classes I."""
import math

class Sin:
    """A class that represents the sinus-function, i.e. sin(x) where x can be any expression."""


class Cos:
    """A class that represents the cosine-function, i.e. cos(x) where x can be any expression."""


class Variable:
    """A class that represents a (named) variable such as ``x``, ``y``, ``x2``, etc."""


def make_symbol(symbol : str) -> Variable: 
    """Create a new Variable object with the given name.

    If ``v = make_symbol(x)`` then ``v.symbol`` should be the string ``"x"``.

    :param symbol: The symbol this variable represents, e.g. ``"x"``.
    :return: A new variable object.
    """
    # TODO: 2 lines missing.
    raise NotImplementedError("Implement function body")
    return v

def sine(arg : object) -> Sin: 
    """Create a new Sin object. The object will represent sin(arg).

    In other words, if we let ``s = sine(arg), then s.arg should be equal to ``arg``. In our case,
    ``arg`` can be either a ``Variable``, or an object such as ``Sin``.

    :param arg: The argument to sin.
    :return: An object representing ``sin(arg)``.
    """
    # TODO: 2 lines missing.
    raise NotImplementedError("Implement function body")
    return s

def cosine(arg : object) -> Cos: 
    """Create a new Cos object. The object will represent cos(arg).

    In other words, if we let ``s = cosine(arg), then s.arg should be equal to ``arg``. In our case,
    ``arg`` can be either a ``Variable``, or an object such as ``Cos``.

    :param arg: The argument to cos.
    :return: An object representing ``cos(arg)``.
    """
    # TODO: 2 lines missing.
    raise NotImplementedError("Implement function body")
    return s

def format_expression(expression : object) -> str:
    """Format the given expression and return it as a string.

    The expression is an object either of class Variable, Sin or Cos. The function should format it as a ``str``.

    :param expression: An object to format.
    :return: A string representation such as ``"cos(x)"`` or ``"sin(cos(y))"``.
    """
    # TODO: 6 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")


if __name__ == "__main__":
    exp = sine(cosine(sine(sine(make_symbol('x')))))
    print( format_expression(exp) )
    # print(format_expression(exp), "evaluated in x=0 is", evaluate(exp, 0) )
    pass

    from sympy import sin, cos, symbols, evaluate, Symbol
    evaluate_expression = sin.evalf  # Get the evaluation-function. Ignore the right-hand side for now.
    print_expression = sin.__str__   # Get the formatting-function. Ignore the right-hand side for now.

    x = symbols('x') # Define a symbol
    y = sin(cos(x))
    print_expression(y)
    evaluate_expression(y, subs={'x': 0})

    y = sin(x)
    isinstance(y, sin) # It is an instance of the sin-class
    from sympy import Symbol
    y.args
    isinstance(y.args[0], Symbol)
    y.args[0] == x
