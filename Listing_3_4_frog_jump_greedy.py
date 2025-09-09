def frog_jump(jump_lengths):
    n = len(jump_lengths)
    max_reachable_indexes = [-1]*n
    for i in range(n - 1): # we do not care the last index
        max_reachable_index = i + jump_lengths[i]
        max_reachable_indexes[i] = max(max_reachable_indexes[i], max_reachable_index)
        if max_reachable_index >= n - 1:
            return True
        if max_reachable_index < i + 1:
            return False 

if __name__ == "__main__":
    assert frog_jump([2,3,1,1,4])==True
    assert frog_jump([1,1,1,1,4])==True
    assert frog_jump([3,2,1,0,4])==False
