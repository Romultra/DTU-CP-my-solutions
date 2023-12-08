"""Task 4: Punctuation ratio."""

def punctuation_ratio(text: str) -> float:
    """Return punctuation ratio.

    :param text: A string with some text.
    :return: Ratio of ` and ` preceded by comma against ` and ` not preceded by comma.
    """
    and_count = 0
    comma_count = 0
    for i, char in enumerate(text):
        print
        if text[i+1:i+6] == ' and ':
            if char !=',':
                and_count += 1

            else:
                comma_count += 1
        
        if i == len(text)-6:
            break
    if and_count == 0:
        return 0
    return comma_count/and_count

    
if __name__ == '__main__':
    text = ("Sara and Emma like to travel, bike, and hike, and when they are " +
            "traveling they always take their bikes, hiking shoes, and sleeping bags. " +
            "Last year, Sarah and Emma traveled to Italy, France, and Spain. And that " +
            "was fun, and, according to Sara and Emma, very expensive!")
    print(punctuation_ratio(text))
