def frog_jump(jump_lengths):
    n = len(jump_lengths)
    is_reachable = [False]*n
    for i in range(n - 1): # we do not care about the last index
        for j in range(i, i + jump_lengths[i] + 1):
            is_reachable[j] = True
    return is_reachable[-1]

if __name__ == "__main__":
    assert frog_jump([2,3,1,1,4])==True
    assert frog_jump([3,2,1,0,4])==False
