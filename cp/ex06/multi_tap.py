"""Exercise 6.9: Multi-tap."""

def multi_tap(keys : list, times : list) -> str:
    """Return the string corresponding to the multi-tap key presses.

    :param keys: The list of keys pressed.
    :param times: The list of times of when the keys were pressed.
    :return: The string corresponding to the key presses.
    """

    text=''
    keypad_dict = {0: [' '],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z']}
    i=0
    while i < len(keys):
        t=0
        
        if (i==len(keys)-1):
            text+=keypad_dict[keys[i]][0]
            i+=1
        elif keys[i]==keys[i+1] and times[i+1]-times[i]>0.5:
            text+=keypad_dict[keys[i]][0]
            i+=1
        else:
            while (keys[i]==keys[i+1] and times[i+1]-times[i]<0.5):
                t+=1      
                i+=1 
                if (i==len(keys)-1):
                    break
            text+=keypad_dict[keys[i]][t]
            i+=1
    return text
    



if __name__ == "__main__":
    keys = [7, 7, 7, 7, 6, 6, 6]
    times = [0, 0.7, 0.8, 0.9, 1, 1.1, 1.2]
    print(multi_tap(keys, times), '==', 'PRO')
