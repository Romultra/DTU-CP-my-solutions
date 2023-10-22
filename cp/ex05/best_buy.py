"""Exercise 5.11. Best Buy."""

def best_buy(prices: list, money: int, start_index: int, reverse: bool) -> int:
    """Return the number of items that can be bought with the given amount of money. The function should be able to handle arbitrary starting points and to run the list in reverse.
    
    :param prices: list of prices
    :param money: amount of money
    :param start_index: starting index in list
    :param reverse: boolean to indicate if list should be run in reverse
    :return: number of items that can be bought with the given amount of money
    """
    i = start_index
    counter = 0

    if reverse:
        direction = -1
    else:
        direction = 1

    while money-prices[i] >= 0 :
        counter += 1
        money = money-prices[i]
        if i == 0 and reverse:
            i = len(prices)-1
        elif i == len(prices)-1 and not reverse:
            i = 0
        else:
            i += direction
        
    return counter

print(best_buy([3, 2, 1, 3, 5], 10, 0, False))
print(best_buy([3, 2, 1, 3, 5], 15, 4, True))