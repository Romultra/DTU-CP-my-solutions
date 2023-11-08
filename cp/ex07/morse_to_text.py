"""Exercise 7.8: Morse code."""

def morse_to_text(morse_code : str) -> str:
    """Return the extracted message from its Morse code.

    :param morse_code: String with the initial message encoded in Morse. 
    :return: The decoded message.
    """
    # Morse code dictionary mapping Morse code symbols to letters
    morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'
    }
    message = ''
    morse_code = morse_code.split('  ')
    for word in morse_code:
        if ' ' in word:
            letter_in_word = word.split(' ')
            for letter in letter_in_word:
                message += morse_code_dict[letter]
            message += ' '
        else:
            message += morse_code_dict[word] + ' '
        
    return message[:len(message)-1]