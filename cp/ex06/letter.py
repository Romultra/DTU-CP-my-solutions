"""Exercise 6.2: Letter histogram."""

def letter_histogram(input_string : str) -> dict:
    """Return the histogram of letter occurrences.
    
    :param input_string: The word based on which the letter histogram is calculated.
    :return: The alphabet characters as keys with their corresponding occurrences as values.
    """
    letter_dict = {
        'a' : 0,
        'b' : 0,
        'c' : 0,
        'd' : 0,
        'e' : 0,
        'f' : 0,
        'g' : 0,
        'h' : 0,
        'i' : 0,
        'j' : 0,
        'k' : 0,
        'l' : 0,
        'm' : 0,
        'n' : 0,
        'o' : 0,
        'p' : 0,
        'q' : 0,
        'r' : 0,
        's' : 0,
        't' : 0,
        'u' : 0,
        'v' : 0,
        'w' : 0,
        'x' : 0,
        'y' : 0,
        'z' : 0,
    }

    for char in input_string:
        if char.lower() in letter_dict.keys():
            letter_dict[char.lower()] += 1
    return letter_dict


if __name__ == "__main__":
    # here you can try out your functions
    print("What is the letter histogram of the word banana?",  letter_histogram('banana'))
