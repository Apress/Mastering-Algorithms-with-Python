def quick_sort(arr):
    length = len(arr)
    if length == 1 or length == 0:
        return arr 
    pivot_num = arr[0]
    left_part = [num for num in arr[1:] if num <= pivot_num]
    print ("left part -->", left_part)
    right_part = [num for num in arr[1:] if num > pivot_num]
    print ("right part -->", right_part)
    sorted_arr = quick_sort(left_part) + [pivot_num] + quick_sort(right_part)
    print ("merge sorted arr -->", sorted_arr)
    return sorted_arr 

if __name__ == "__main__":
    unsorted_arr = [5, -1, 0, 3, 2]
    sorted_arr = quick_sort(unsorted_arr)
    print (sorted_arr)

