"""Exercise 6.8: Spell check."""

def spell_check(text: str, corrections: dict) -> str:
    """Return the corrected text for spelling errors according to a set of rules.

    :param text: The sentence to check for spelling.
    :param corrections: The dictionary of wrongly spelled words and their equivalent corrected version.
    :return: The correctly spelled sentence.
    """
    # TODO: Code has been removed from here. 

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
