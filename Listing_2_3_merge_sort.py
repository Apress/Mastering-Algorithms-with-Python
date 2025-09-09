def merge_lists(l1, l2):
    res = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
            
    res += l1[i:]
    res += l2[j:]
        
    return res

def merge_sort(arr):
    length = len(arr)
    if length == 1 or length == 0:
        return arr 
    mid_point_idx = length // 2
    left_part = merge_sort(arr[:mid_point_idx])
    print ("left part -->", left_part)
    right_part = merge_sort(arr[mid_point_idx:])
    print ("right part -->", right_part)
    sorted_arr = merge_lists(left_part, right_part)
    print ("merge sorted arr -->", sorted_arr)
    return sorted_arr 

if __name__ == "__main__":
    unsorted_arr = [5, -1, 0, 3, 2]
    sorted_arr = merge_sort(unsorted_arr)
    print (sorted_arr)

