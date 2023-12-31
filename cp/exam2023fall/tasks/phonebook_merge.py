"""Task 8: Phonebook merge."""

def phonebook_merge(phonebook: dict, second_phonebook:dict):
    """Modify phonebook by adding new content from second_phonebook.

    :param phonebook: Dictionary with names and list of phone numbers.
    :param second_phonebook: Dictionary with names and list of phone numbers.
    """
    for name in second_phonebook:
        if name not in phonebook:
            phonebook[name] = second_phonebook[name]
        else:
            for num in second_phonebook[name]:
                if num not in phonebook[name]:
                    phonebook[name].append(num)

if __name__ == '__main__':
    phonebook = {'Liv': ['55511112', '18777890'] , 
                 'Mads': ['27274445', '48533336'],
                 'Steve': ['45455555', '25455525']} 
    second_phonebook = {'Anna': ['89577772'] , 
                        'Steve': ['25257755', '25455525'],
                        'Mads': ['48533336', '27274445']}
    phonebook_merge(phonebook, second_phonebook)
    for name in phonebook:
        print(name, phonebook[name])
