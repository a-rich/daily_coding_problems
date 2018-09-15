def naive_profit(prices):
    max_profit = float('-inf')
    for i, price in enumerate(prices):
        if i == 0:
            continue

        for j, p in enumerate(prices[:i]):
            if price - p > max_profit:
                max_profit = price - p

    return max_profit

def opt_profit(prices):
    min_val = float('inf')
    max_profit = float('-inf')
    for price in prices:
        if price < min_val:
            min_val = price
        if price - min_val > max_profit:
            max_profit = price - min_val

    return max_profit

if __name__ == '__main__':
    prices = [9,11,8,5,7,10]
    assert opt_profit(prices) == 5
