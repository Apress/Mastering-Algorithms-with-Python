def random_number_mid_square_method(seed_num, N):
    random_numbers = []
    fractional_numbers = []
    cur_num = seed_num
    random_numbers.append((0, None, seed_num))
    fractional_numbers.append(seed_num / 10000.)
    for i in range(N):
        prev_num = cur_num
        squared_num = str(prev_num ** 2).zfill(8) 
        middle_part = int(squared_num[2:6])
        random_numbers.append((i + 1, int(squared_num), int(middle_part)))
        fractional_numbers.append(int(middle_part) / 10000.)
        cur_num = int(middle_part)
    return random_numbers, fractional_numbers

if __name__ == "__main__":
    print (random_number_mid_square_method(6632, 20)[1])
    print (random_number_mid_square_method(1009, 20)[1])