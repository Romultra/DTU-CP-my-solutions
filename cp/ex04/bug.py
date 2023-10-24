"""Exercise 4.4-4.5: Let the world know you have written your last bug."""

def last_bug():
    """Write a nice message enclosed by lines and pipes that clearly indicate you have written your last bug.

    The function should print out the following three lines in the console:

    .. code-block:: console

        ------------------------------
        | I have written my last bug |
        ------------------------------
    """
    print('------------------------------')
    print('| I have written my last bug |')
    print('------------------------------')


def nice_sign(msg : str):
    """Print the input string as a nice sign by enclosing it with pipes.

    Note that the input message can vary in length.

    .. code-block:: console

        ---------------
        | {input msg} |
        ---------------

    :param msg: The message to enclose.
    """
    print('-'*(4+len(msg)))
    print(f'| {msg} |')
    print('-'*(4+len(msg)))


if __name__ == "__main__":
    # here you can try out your functions
    last_bug()  # Done with the bugs
    nice_sign("Hello world")
