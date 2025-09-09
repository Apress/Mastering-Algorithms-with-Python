def knapsack_no_repeat(weights, values, capacity):
    n = len(weights)
    V = [[0 for i in range(capacity + 1)] for j in range(n + 1)]
 
    for i in range(1, n + 1):
        for c in range(1, capacity + 1):
            if weights[i - 1] > c:
                V[i][c] = V[i-1][c]
            else:
	            V[i][c] = max(V[i-1][c], V[i-1][c - weights[i-1]] + values[i-1])
	 
    return V[n][capacity]

if __name__ == "__main__":                         
    weights = [16, 14, 10, 5]
    values = [16, 12, 8, 1]
    C = 24
    print (knapsack_no_repeat(weights, values, C))