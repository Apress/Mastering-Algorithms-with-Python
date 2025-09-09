def prefix_sum_naive(arr):
    prefix_sum = []
    for i in range(len(arr)):
        local_sum = 0
        for j in range(i+1):
            local_sum += arr[j]
        prefix_sum.append(local_sum) 
    return prefix_sum

def prefix_sum_dp(arr):
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    return prefix_sum 

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print (prefix_sum_naive(arr))
    print (prefix_sum_dp(arr))