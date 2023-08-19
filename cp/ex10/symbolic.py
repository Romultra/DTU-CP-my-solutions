"""Project work for week 10: A do-it-yourself sympy."""
import math


class Expression: 
    """A mathematical expression. Can represent a constant `1`, a symbol such as `x`, or a function such as `sin(x)`."""

    def evaluate(self, substitutions : dict) -> float: 
        """Evaluate the expression and return a floating-point number.

        The input argument is a dictionary which is used to evaluate all symbols. E.g. if ``substitutions = {'x': 3}``,
        this means all instances of the symbolic expression ``x`` will be replaced by ``3``.

        :param substitutions: A dictionary of substitutions. The keys are strings, and the values are numbers.
        :return: A floating-point number this expression has been evaluated to.
        """
        return 0 

    def differentiate(self, variable : str) -> 'Expression': 
        r"""Differentiate the expression with respect to the variable, specified as e.g. ``"x"``.

        Note that if this expression is a function of other variables, we must use the chain-rule to recursively
        differentiate the other expressions. e.g. :math:`\sin(f(x))' = \cos(f(x))f'(x)`.

        :param variable: The variable we differentiate with respect to (example: ``"x"``)
        :return: A class that inherits from ``Expression`` which corresponds to the derivative with respect to the given variable.
        """
        return Expression()  

    def __str__(self) -> str:  
        """Provide a string representation of the expression. The function is called automatically by ``print``.

        :return: A string representation of this expression.
        """
        return "Remember to implement the __str__()-function."  

# TODO: Code has been removed from here. 

if __name__ == "__main__":
    # construct some symbolic expressions
    c1 = Constant(2)
    c2 = Constant(3)
    v = Variable('x')

    # construct expression (2 * x + 3)
    expr1 = Addition(Multiplication(c1, v), c2)

    print(expr1)
    print(expr1.differentiate("x"))

    # let's evaluate this expression for x = 4
    print(expr1.evaluate( {'x': 4}  ))  # prints 11

    # let's differentiate this expression with respect to x
    # it should be (2 * 1 + 0) = 2
    diff_expr1 = expr1.differentiate('x')

    # evaluate the derivative at x = 4
    print(diff_expr1.evaluate( {'x': 2}  ))  # prints 2


    # construct another expression (x ^ 3)
    expr2 = Sin(v) #  Constant(3))

    # let's evaluate this expression for x = 2
    print(expr2.evaluate( {'x': 2} ))  # prints 8
    print(expr2)
    # let's differentiate this expression with respect to x
    # it should be 3 * x ^ 2 which equals 3 * 2 ^ 2 = 12 at x = 2
    diff_expr2 = expr2.differentiate('x')
    print(diff_expr2)

    print( Sin(Cos(Cos(v))).differentiate('y') )


    # evaluate the derivative at x = 2
    print(diff_expr2.evaluate({'x': 2}))  # prints 12


# Doctor
# Person
# Patient
