"""Exercise 2.2: Round a number to the next nearest thousand."""
import math

def next_thousand(a:int):
    """Round a number to the next nearest thousand and print.

    :param a: the number to be rounded.
    """
    a = a/1000
    a = math.ceil(a)
    a = a*1000
    print(a)

next_thousand(43400)    # Output : 44000
next_thousand(9999)     # Output : 10000