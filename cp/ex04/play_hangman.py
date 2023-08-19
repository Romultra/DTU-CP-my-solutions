"""Play a game of hangman by loading a random word."""
import random
import os

def load_words() -> list:
    """
    Return a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.

    :return: The available words as a list.
    """
    from cp.ex08.words import load_words
    wordlist = load_words(os.path.join(os.path.dirname(__file__), "files", "5000-words.txt")).split()
    return wordlist


def choose_word() -> str:
    """Select a word at random.

    :return: A randomly selected word, useful for playing hangman.
    """
    wordlist = load_words()
    return random.choice(wordlist)
