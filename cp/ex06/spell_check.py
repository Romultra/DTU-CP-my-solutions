"""Exercise 6.8: Spell check."""

def spell_check(text: str, corrections: dict) -> str:
    """Return the corrected text for spelling errors according to a set of rules.

    :param text: The sentence to check for spelling.
    :param corrections: The dictionary of wrongly spelled words and their equivalent corrected version.
    :return: The correctly spelled sentence.
    """
    start_next_word = 0
    list_word = []
    new_sentence = ''
    for i in range(len(text)):
        if text[i] == ' ':
            list_word.append(text[start_next_word:i])
            start_next_word = i+1
        elif text[i] == ',' or text[i] == '.':
            list_word.append(text[start_next_word:i])
            if i == len(text)-1:
                list_word.append(text[i])
            else:
                start_next_word = i
        elif i == len(text)-1:
            list_word.append(text[start_next_word:i+1])
    
    for i in range(len(list_word)):
        for key in corrections.keys():
            if list_word[i] == key:
                list_word[i] = corrections[key]
                break
    
    for i, word in enumerate(list_word):
        if word == ',' or word == '.':
            new_sentence = new_sentence + word
        elif i==0:
            new_sentence = new_sentence + word
        else:
            new_sentence = new_sentence + ' ' + word
    
    return new_sentence



if __name__ == "__main__":
    # here you can try out your functions
    corrections = {
    'apsolute': 'absolute',
    'teh': 'the',
    'acess': 'access', 
    'occured': 'occurred',
    'exampel': 'example'
    }
    text = "The apsolute acsess to teh data occured in this exampel."

    print(spell_check(text, corrections))
