"""Exercise 5.5. short words."""

def short_words(words: str, max_len: int) -> str:
    """Return a string of words that are shorter than max_len.
    
    :param words: string of words
    :param max_len: maximum length of words 
    :return: string of words that are shorter than max_len
    """
    start_next_word = 0
    filtered_words = ''
    for i in range(len(words)):
        if words[i] == ' ':
            if len(words[start_next_word:i]) < max_len:
                filtered_words += words[start_next_word:i] + ' '
            start_next_word = i+1
        elif i == len(words)-1:
            if len(words[start_next_word:i+1]) < max_len:
                filtered_words += words[start_next_word:i+1] + ' '
    return filtered_words[:len(filtered_words)-1]