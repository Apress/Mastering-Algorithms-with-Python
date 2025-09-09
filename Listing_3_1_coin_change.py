def coin_change(coins, amount):
    num_coins = 0
    coins.sort()
    max_coin_index = len(coins) - 1
    while amount:
        while True:
            if coins[max_coin_index] > amount:
                max_coin_index -= 1
            else:
                break 
        amount -= coins[max_coin_index]
        num_coins += 1
    return num_coins

if __name__ == "__main__":
    coins = [1,2,5,10,20,50,100,1000]
    amount_1 = 70
    amount_2 = 122
    amount_3 = 2035
    assert(coin_change(coins, amount_1) == 2)
    assert(coin_change(coins, amount_2) == 3)
    assert(coin_change(coins, amount_3) == 5)