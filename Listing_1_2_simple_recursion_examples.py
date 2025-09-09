def sum_n_integers(n):
    """Given input n, sum all nonnegative integers up to n
    """
    if n == 0 or n == 1:
        return n 
    return sum_n_integers(n - 1) + n 

def sum_arr_v1(nums):
    if len(nums) == 1:
        return nums[0]
    return nums[0] + sum_arr_v1(nums[1:])

def sum_arr_v2(nums):
    if len(nums) == 1:
        return nums[-1]
    return nums[-1] + sum_arr_v2(nums[:-1])

if __name__ == "__main__":
    assert sum_n_integers(5) == 15
    assert sum_arr_v1([1,2,3,4,5]) == 15
    assert sum_arr_v2([1,2,3,4,5]) == 15
