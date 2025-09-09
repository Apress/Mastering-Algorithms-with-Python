def max_sum_subarray(arr):
    sum_arr = [0] * len(arr)
    sum_arr[0] = arr[0]
    for i in range(1, len(arr)):
        sum_arr[i] = arr[i] + max(sum_arr[i-1], 0)
    return max(sum_arr)

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print (max_sum_subarray(arr))