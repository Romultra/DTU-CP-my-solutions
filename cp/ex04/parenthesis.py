"""Exercise 4.6-4.9."""
def matching(expression :str) -> bool:
    """Tell if the parenthesis match in a mathematical expression.

    For instance, the parenthesis match in ``"3x(y-1)(3y+(x-1))"`` but not in ``"3x(y-4))"``

    :param expression: An expression containing zero or more parenthesis.
    :return: ``True`` if the number of open/close parenthesis match, otherwise ``False``
    """
    count = 0
    for char in expression:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
    if count == 0:
        return True
    else:
        return False

def find_innermost_part(s : str) -> str:
    """Find the innermost part of a mathematical expression.

    The innermost part is a substring enclosed in parenthessis but not containing parenthesis.
    For instance, given ``"3(x+(4-y^2))"``, then ``"4-y^2"`` is an inner-most part.
    The parenthesis can be assumed to match.

    :param s: The mathematical expression as a ``str``
    :return: The innermost part as a ``str``
    """
    count = 0
    best_count = 0
    best_pos = -1
    best_pos_end = len(s)
    for i, char in enumerate(s):
        if char == '(':
            count += 1
            if count > best_count:
                best_count = count
                best_pos = i
        elif char == ')':
            if best_count == count:
                best_pos_end = i
            count -= 1
    
    return s[best_pos+1:best_pos_end]


def find_index_of_equality(expression : str) -> int:
    """Find an index ``i`` which split the expression into two balanced parts.

    Given an expression containing opening and closing parenthesis, for instance ``"(()())"``, this function should
    return an index ``i``, such that when the string is split at ``i``, the
    number of opening parenthesis ``(`` in the left-hand part equal the number of closing parenthesis ``)`` in the
    right-hand part. For instance, if ``i=2``, the expression is split into the right, left hand parts:

    - ``"(()"``
    - ``"())"``

    In this case the left-hand part contains ``2`` opening parenthesis and the right-hand part ``2`` closing parenthesis so ``i`` is the right index.
    Similarly, for ``"()"``, the answer would be ``1``.

    :param expression: An expression only consisting of opening and closing parenthesis.
    :return: The index ``i`` as an int.
    """
    for i in range(len(expression)):
        if expression[:i].count('(') == expression[i:].count(')'):
            return i

def print_the_dialogue(s : str):
    """Print all dialogue in a manuscript.

    Given a manuscript (as a ``str``), this function will find all lines of dialogue to the console, one line of
    dialogue per printed line. Dialogue is enclosed by double ticks, i.e. this ``str`` contains two pieces of dialogue:
    ``"''My dear Mr. Bennet,'' said his lady to him one day, ''have you heard that Netherfield Park is let at last?''"``

    :param s: The manuscript as a ``str``.
    """
    dialogue_list=[]
    previous_char=''
    previous_pos = 0
    count = 0
    for i, char in enumerate(s):
        if char == previous_char == '\'':
            count += 1
            pos = i+1
            if previous_pos != 0 and count%2 == 0:
                dialogue_list.append(s[previous_pos:pos-2])
            previous_pos = pos
        previous_char = char

    for dialogue in dialogue_list:
        print(dialogue)



if __name__ == "__main__":
    # here you can try out your functions
    print("Does the parenthesis match?", matching("2x(x+2)"))
    print("Does the parenthesis match?", matching("2x(x+(2-y)^2)"))
    print("Does the parenthesis match?", matching("4x"))

    print("Does the parenthesis match?", matching("2x(x+2"))
    print("Does the parenthesis match?", matching("2x)(x"))
    print("Does the parenthesis match?", matching("4x()(()))"))

    print('y+x', find_innermost_part('(y+x)'))
    print('x-1', find_innermost_part('3x(y+(x-1))'))
    print('y+2', find_innermost_part('3x((y+2)y+x)'))

    s = "(())))("

    print("Index of equality for", s, "is", find_index_of_equality(s))
    dialogue = "He said: ''How are you old wife''? She answered, perplexed, ''I am not your wife''"
    print_the_dialogue(dialogue)
