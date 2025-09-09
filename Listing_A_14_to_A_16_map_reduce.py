nums = [num for num in range(1, 101)]
nums_squared = map(lambda x: x**2, nums)
nums_squared.__next__()
nums_squared_list = list(nums_squared)

nums = [num for num in range(1, 101)]
nums_filtered = filter(lambda x: x%2 == 1, nums)
nums_filtered.__next__()
nums_filtered_list = list(nums_filtered)

# an example of map-reduce
from functools import reduce
nums = [num for num in range(1, 101)]
nums_squared = map(lambda x: x**2, nums)
nums_summation = reduce(lambda acc, nxt : acc + nxt, nums_squared)