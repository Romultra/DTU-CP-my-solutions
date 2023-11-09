"""Exercise 7.7: Code shift."""

def code_shift(code : tuple, turn : tuple) -> tuple:
    """Return the updated code pattern.

    :param code: Tuple with the initial code in the lock
    :param turn: Tuple with the turn on each lock dial
    :return: Updated lock code.
    """
    code_list = []
    for i, move in enumerate(turn):
        if code[i] + turn[i] > 9:
            code_list.append(code[i] + turn[i] - 10)
        elif code[i] + turn[i] < 0:
            code_list.append( + turn[i] + 10)
        else:
            code_list.append(code[i] + turn[i])

    return (code_list[0], code_list[1], code_list[2], code_list[3])