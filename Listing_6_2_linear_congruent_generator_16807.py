def linear_congruent_generator_16807(seed, N):
    random_nums = [seed]
    cycle = 2**31 - 1
    prev_num = seed 
    for _ in range(N - 1):
        cur_num = 16807 * prev_num % cycle 
        random_nums.append(cur_num)
        prev_num = cur_num    
    return [round(rand_num / cycle, 4) for rand_num in random_nums]

if __name__ == "__main__":
    print (linear_congruent_generator_16807(12345678, 20))
