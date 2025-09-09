def knapsack_with_repeat(weights, values, capacity):
    n = len(weights)
    dp = [0 for i in range(capacity + 1)]
    for b in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= b:
                dp[b] = max(dp[b], values[i] + dp[b -weights[i]])
    return dp[capacity]

def knapsack_repeat_2D(weights, values, capacity):
    n = len(weights)
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(1, capacity + 1):
            if weights[i - 1] > b:
                dp[i][b] = dp[i-1][b]
            else:
                dp[i][b] = max(dp[i-1][b], dp[i][b - weights[i-1]] + values[i-1])
    return dp[n][capacity]

if __name__ == "__main__":                         
    weights = [16, 14, 10, 5]
    values = [16, 12, 8, 1]
    B = 24
    print (knapsack_with_repeat(weights, values, B)) 
    print (knapsack_repeat_2D(weights, values, B)) 