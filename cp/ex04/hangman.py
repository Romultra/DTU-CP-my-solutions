"""Exercise 4.12-4.16."""

def is_word_guessed(secret_word : str, letters_guessed : str) -> bool:
    """Determine if the word has been guessed.

    :param secret_word: The word to guess
    :param letters_guessed: A ``str`` containing the letters that have currently been guessed
    :return: True if and only if all letters in ``secret_word`` have been guessed.
    """
    for char in secret_word:
        if char not in letters_guessed:
            return False

    return True

def get_available_letters(letters_guessed : str) -> str:
    """
    Return the letters which are available, i.e. have not been guessed so far.

    The input string represents the letters the user have guessed, and the output should then be the lower-case
    letters which are not contained in that string. The function is used to show the user which
    letters are available in each round.

    :param letters_guessed: A `str` representing the letters the user has already guessed
    :return: A `str` containing the letters the user has not guessed at yet.
    """
    available_letter = 'abcdefghijklmnopqrstuvwxyz'
    for letter in letters_guessed:
        available_letter = available_letter.replace(letter, '')
    return available_letter

def get_guessed_word(secret_word : str, letters_guessed : str) -> str:
    """Format the secret word for the user by removing letters that have not been guessed yet.

    Given a list of the available letters, the function will replace the letters in the secret word with `'_ '`
    (i.e., a lower-case followed by a space). For instance, if the secret word is ``"cat"``, and the
    available letters are ``"ct"``, then the function should return ``"c_ t"``.

    :param secret_word: A ``str``, the word the user is guessing
    :param letters_guessed:  A ``str`` containing which letters have been guessed so far
    :return: A ``str``, comprised of letters, underscores (_), and spaces that represents which letters in secret_word have been guessed so far.
    """
    guessed_word = secret_word
    for letter in secret_word:
        if letter not in letters_guessed:
            guessed_word = guessed_word.replace(letter, '_ ')
    return guessed_word
            

def hangman(secret_word : str, guesses : int):
    """
    Play an interactive game of Hangman.

    This function should launch an interactive game of Hangman. The details of the game is defined in the
    project description available online, and should be read carefully.

    * The game should first display how many letters are in the secret word. You should start by generating this output.
    * Before each round, the user should see how many guesses that are left and which letters are not yet used
    * In each round, the user is prompted to input a letter. Use the ``input('..')`` function for this.
    * The user is given feedback based on whether the letter is in the word or not. The program also performs error handling.
    * The game terminates when the user win, has exceeded the number of guesses, or if the user makes an illegal input.
      in this case the user is shown a score.

    :param secret_word: The secret word to guess, for instance ``"cow"``
    :param guesses: The number of available guesses, for instance ``6``
    """
    print(f'Hangman! To save Bob, you must guess a {len(secret_word)} letter word within {guesses} attempts.')
    max_guesses = guesses
    letters_guessed = ''
    lost = False
    while guesses > 0:
        old_guessed_word = get_guessed_word(secret_word, letters_guessed)

        print('----')
        print(f'You have {guesses} guesses left.')
        user_input = input(f'The available letters are: {get_available_letters(letters_guessed)}. Guess a letter and press enter:')
        for char in user_input:
            if char not in get_available_letters(letters_guessed) and char != '':
                print('Game over :-(. Your score is 0 points.')
                lost = True
        if lost:
            break

        letters_guessed = letters_guessed + user_input
        guesses -= 1

        if is_word_guessed(secret_word, letters_guessed) == True:
            print(f'Success! You guessed \'{secret_word}\' in {max_guesses-guesses} tries.')
            print(f'Your score is {len(secret_word)*guesses}')
            break
        
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if guessed_word != old_guessed_word:
            print(f'Good guess: {guessed_word}')
        else:
            print(f'Oh no: {guessed_word}')

        if guesses == 0:
            print('Game over :-(. Your score is 0 points.')
        

        


if __name__ == "__main__":
    # here you can try out your functions
    print("This should return True: ", is_word_guessed("dog", "tdohg"))
    print("This should return False: ", is_word_guessed("dog", "dthk"))

    print("This should be 'c_ w': ", get_guessed_word('cow', 'kcwt'))

    print("Available letters when we have tried 'abcdefghijk'; this should be about half the alphabet: ", get_available_letters('abcdefghijk'))

    print("Lets launch hangman. Try the inputs in the exercise description and see if you get the same")
    hangman("doggy", guesses=8)
