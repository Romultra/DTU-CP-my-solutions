"""Exercise 6.7: Sentiment analysis."""

def sentiment_analysis(text: str) -> int:
    """Return the sentence sentiment score, according to the rules of words scoring, as described in the text above.

    :param text: The sentence to check for sentiment scoring.
    :return: The total sentiment scoring of the sentence.
    """
    score  = {'horrible': -5, 'awful': -5, 'bad': -4, 'terrible': -4, 'mediocre': -2, 'lousy': -3, 'poor': -3,
    'unfair': -1, 'average': 0, 'wonderful': +2, 'beautiful': +3, 'good': +3,'fantastic': +4,
    'excellent': +4, 'superb': +4, 'amazing': +4, 'great': +4, 'best': +5, 'brilliant': +5}

    points = 0
    for i in range(len(text)):
        if text[i:i+3] == 'but':
            start_index = i+3
    
    for key in score:
        if key in text[start_index:]:
            points += score[key]
    
    return points

if __name__ == "__main__":
    # here you can try out your functions
    text='I think the food was excellent and great, but the service was horrible '
    print(sentiment_analysis(text))
