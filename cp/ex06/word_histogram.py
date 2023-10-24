"""Exercise 6.3-6.4."""

def word_histogram(lines : list) -> dict:
    """Return the word count histogram from the input lines.

    :param lines: The lines that are analyzed for word count.
    :return: The histogram of word occurrences.
    """
    start_next_word = 0
    dict_word = {}
    for i in range(len(lines)):
        print(lines[i])
        lines[i] = lines[i].replace(',', '')
        lines[i] = lines[i].replace('.', '')
        print(lines[i])
        for j, char in enumerate(lines[i]):
            lines[i] = lines[i][:j] + char.lower() + lines[i][j+1:]
            if char == ' ':
                if j == 0:
                    start_next_word = j+1
                elif lines[i][start_next_word:j] not in dict_word.keys():
                    dict_word[lines[i][start_next_word:j]] = 1
                    start_next_word = j+1
                else:
                    dict_word[lines[i][start_next_word:j]] += 1
                    start_next_word = j+1

            elif j == len(lines[i])-1:
                if lines[i][start_next_word:j+1] not in dict_word.keys():
                    dict_word[lines[i][start_next_word:j+1]] = 1
                else:
                    dict_word[lines[i][start_next_word:j+1]] += 1
        start_next_word = 0
    return dict_word
    
def extract_keyword(lines : str, ignore_list : list) -> dict:
    """Return the five most frequent words that are not on the ignore list and their occurrences.

    :param lines: The sentence to extract keywords from.
    :param ignore_list: The words that should ignored.
    :return: The five most frequent words in the sentence as keys with their count as values.
    """
    highest = ''
    dict_most_freq_words = {}
    word_histo = word_histogram(lines)
    for i in range(5):
        for key in word_histo:
            if key not in ignore_list:
                if highest == '':
                    highest = key
                elif word_histo[key] > word_histo[highest]:
                    highest = key
        dict_most_freq_words[highest] = word_histo[highest]
        ignore_list.append(highest)
        highest = ''

    return dict_most_freq_words           



if __name__ == "__main__":
    # here you can try out your functions
    lines = ['This is the first sentence of text for you', 'This is the second sentence of text', 'This is for you']
    print("word_histogram")
    print(word_histogram(lines))
    print(word_histogram(["Write the function word histogram."," which takes as argument a list containing lines of a text."]))

    # Ignore list of common words
    ignore_list = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'is', 'have', 'I']

    # Print the 5 most occurring keywords
    print("extract_keywords")
    print(extract_keyword(lines, ignore_list))

    
