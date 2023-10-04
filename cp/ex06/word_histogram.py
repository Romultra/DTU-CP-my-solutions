"""Exercise 6.3-6.4."""

def word_histogram(lines : list) -> list:
    """Return the word count histogram from the input lines.

    :param lines: The lines that are analyzed for word count.
    :return: The histogram of word occurrences.
    """
    # TODO: Code has been removed from here. 
    
def extract_keyword(lines : str, ignore_list : list) -> dict:
    """Return the five most frequent words that are not on the ignore list and their occurrences.

    :param lines: The sentence to extract keywords from.
    :param ignore_list: The words that should ignored.
    :return: The five most frequent words in the sentence as keys with their count as values.
    """
    # TODO: Code has been removed from here. 


if __name__ == "__main__":
    # here you can try out your functions
    print(word_histogram('I think therefore I am.'))

    # Ignore list of common words
    ignore_list = [
    'a', 'an', 'the', 'above', 'across', 'against', 'along', 'among', 'around',
    'at', 'before', 'behind', 'below', 'beneath', 'beside', 'between', 'by',
    'down', 'from', 'in', 'into', 'near', 'of', 'off', 'on', 'to', 'toward',
    'under', 'upon', 'with', 'within','function', 'for', 'and', 'nor', 'but', 'or', 'yet', 'so']

    # Example usage:
    lines = [    "Write the function word_histogram, which takes as argument a list containing lines of a text.",    "The function should ... ... ... ... ... make a histogram of words that occur in the text."]

    keywords_result = extract_keyword(lines, ignore_list)

    # Print the 5 most occurring keywords
    print(keywords_result)
