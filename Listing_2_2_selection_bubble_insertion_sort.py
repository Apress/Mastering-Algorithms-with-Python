def selection_sort(nums):
    def find_min_index(arr):
        min_idx = None  
        min_val = float("inf")
        for idx, num in enumerate(arr):
            if num < min_val:
                min_idx, min_val = idx, num 
        return min_idx, min_val

    i = 0
    while i < len(nums):
        min_idx, min_val = find_min_index(nums[i:])
        if nums[i] > min_val:
            nums[i], nums[min_idx + i] = nums[min_idx + i], nums[i]
        i += 1
    return nums 

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i 
        while j > 0:
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums 

if __name__ == "__main__":
    unsorted_arr_1 = [5, -1, 0, 3, 2]
    sorted_arr_1 = selection_sort(unsorted_arr_1)
    print (sorted_arr_1)

    unsorted_arr_2 = [5, -1, 0, 3, 2]
    bubble_sort(unsorted_arr_2)
    print (unsorted_arr_2)

    unsorted_arr_3 = [5, -1, 0, 3, 2]
    insertion_sort(unsorted_arr_3)
    print (unsorted_arr_3)
