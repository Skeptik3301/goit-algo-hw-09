import time

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount = amount - coin * count
    
    return result


def find_min_coins(amount):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    
    last_coin = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    last_coin[i] = coin
    
    result = {}
    current = amount
    
    while current > 0:
        coin = last_coin[current]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current = current - coin
    
    return result


if __name__ == "__main__":
    test_amounts = [113, 1000, 5000]
    
    print("=" * 60)
    print("COIN CHANGE ALGORITHMS COMPARISON")
    print("=" * 60)
    
    for amount in test_amounts:
        print(f"\nAmount: {amount}")
        print("-" * 60)
        
        start_time = time.time()
        greedy_result = find_coins_greedy(amount)
        greedy_time = time.time() - start_time
        
        print(f"Greedy algorithm: {greedy_result}")
        print(f"Total coins: {sum(greedy_result.values())}")
        print(f"Execution time: {greedy_time:.6f} seconds")
        
        start_time = time.time()
        dp_result = find_min_coins(amount)
        dp_time = time.time() - start_time
        
        print(f"\nDynamic programming: {dp_result}")
        print(f"Total coins: {sum(dp_result.values())}")
        print(f"Execution time: {dp_time:.6f} seconds")
        
        print(f"\nTime difference: {abs(greedy_time - dp_time):.6f} seconds")
        print("=" * 60)