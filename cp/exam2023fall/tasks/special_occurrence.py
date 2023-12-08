"""Task 3: Special occurrence."""

def special_occurrence(sequence: list) -> int:
    """Find first special occurrence.

    :param sequence: A list of positive integers with 0 or more elements.
    :return: The index of the first 5 followed by two numbers where exactly one is 7.
    """
    for i, num in enumerate(sequence):
        if num == 5 and ( (sequence[i+1] == 7 and sequence[i+2] != 7) or (sequence[i+1] != 7 and sequence[i+2] == 7) ):
            return i
        
        if i == len(sequence)-3:
            return -1

if __name__ == '__main__':
    print(special_occurrence([2, 8, 11, 3, 12, 5, 7, 7, 11, 3, 12, 5, 2, 7, 5, 7, 2, 6]))
