"""A handful of python programming examples."""
# Example 1
print("Hello world")

# Example 2
print("hello")
print("world")

a = 2
b = 3
c = 1
x = 3
y = a*x**2 + b * x + c

# Example 3
def second_poly(x):
    """Compute a first order polynomial.

    :param x: Input value :math:`x`
    :return: :math:`y = 2x + 4`
    """
    return 2 * x + 4

# example 4
def say_hello(name):
    """Print out "Hello {name}.

    :param name: The name to say hello to
    """
    print("Hello " + name)
