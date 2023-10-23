"""Exercise 4.10-4.11."""

def common_prefix(word1 : str, word2 : str) -> str:
    """
    Return the longest string so that both ``word1``, and ``word2`` begin with that string.

    :param word1: First word
    :param word2: Second word
    :return: The longest common prefix.
    """
    i = 0
    while word1[i] == word2[i] and i<len(word1) and i<len(word2):
        i+=1
    
    return word1[0:i]

def common_prefix3(word1 : str, word2 : str, word3 : str) -> str:
    """
    Return the longest string so that both ``word1``, ``word2``, and ``word3`` begin with that string.

    :param word1: First word
    :param word2: Second word
    :param word3: Third word
    :return: The longest common prefix.
    """
    i = 0
    while word1[i] == word2[i] == word3[i] and i<len(word1) and i<len(word2) and i<len(word3):
        i+=1
    
    return word1[0:i]


if __name__ == "__main__":
    # here you can try out your functions
    print("The longest Common Prefix is :", common_prefix("egregious", "egg"))
    print("The longest Common Prefix is :", common_prefix3("egg", "egregious", "eggplant"))
