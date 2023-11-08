"""Exercise 8.8: Guessing the language of a text."""

def frequency_letter(filename: str, letter: str) -> float:
    """Calculate the frequency of a letter in a text file.
    
    This function takes a text file and a letter as input and calculates the frequency of
    the letter in the text file in percent.
    
    :param filename: A string representing the name of the text file.
    :param letter: A string representing the letter to be searched for.
    :return: A float representing the frequency of the letter in the text file in percent.
    """
    with open(filename, 'r') as file:
        text = file.read()
        text = text.replace(' ', '')
        text = text.replace('.', '')
        text = text.replace(',', '')
        text = text.replace('?', '')
        text = text.replace('!', '')
        num_of_letter = text.count(letter)
        return num_of_letter * 100 / len(text)

def language_guess(filename: str) -> str:
    """Guess the language of a text file.

    This function takes a text file as input and guesses the language of the text file
    based on the frequency of the letters 'a' and 'e' in the text file.

    :param filename: A string representing the name of the text file.
    :return: A string representing the guessed language.
    """
    frequency_a = frequency_letter(filename, 'a')
    frequency_e = frequency_letter(filename, 'e')

    print(frequency_a)
    print(frequency_e)

    if 7.2 <= frequency_a <= 9.2 and 11.7 <= frequency_e <= 13.7:
        return 'English'

    elif 5.5 <= frequency_a <= 7.5 and 14.4 <= frequency_e <= 17.3:
        return 'German'
    
    elif 6.6 <= frequency_a <= 8.6 and 13.7 <= frequency_e <= 15.7:
        return 'French'
    
    else:
        return 'Unknown'