from copy import copy 
from math import exp 
import random
random.seed(1234)

def print_board(board):    
    row_sep = '-'*25
    for i in range(9):
        if i % 3 == 0:
            print(row_sep)
        row = "" 
        for c in range(9):
            row += board[(i, c)]
        print('| '+' '.join(row[0:3])+' | '+' '.join(row[3:6])+' | '+' '.join(row[6:])+' |')
    print(row_sep)

def calculate_total_cost():
    # total cost is the summation of duplicated numbers each row + each column
    total_counts = 0
    for i in range(9):
        row_count = 9 - len(set([board[(i,j)] for j in range(9)]))
        total_counts += row_count
    
    for j in range(9):
        col_count = 9 - len(set([board[(i,j)] for i in range(9)]))
        total_counts += col_count
    return total_counts

def fill_missing_numbers():
    for range_row in [range(0,3), range(3, 6), range(6,9)]:
        for range_col in [range(0,3), range(3, 6), range(6,9)]:
            block_numbers = ''
            unfilled_indexes = list()
            for i in range_row:
                for j in range_col:
                    if board[(i, j)] != 'x':
                       block_numbers += board[(i,j)] 
                    else:
                        unfilled_indexes.append((i,j))
            remained_numbers = [str(num) for num in range(1, 10) if str(num) not in block_numbers]
            missing_numbers_dict[tuple(unfilled_indexes)] = remained_numbers
            random.shuffle(remained_numbers)
            # assign number
            for index, value in zip(unfilled_indexes, remained_numbers):
                board[index] = value 

def random_swap_numbers_in_a_block():
    indexes, numbers = random.choice(list(missing_numbers_dict.items()))
    if len(indexes) < 2:
        return 
    i, j = random.sample(range(len(indexes)), 2)
    board[indexes[i]] = numbers[j]
    board[indexes[j]] = numbers[i]
    numbers[i], numbers[j] = numbers[j], numbers[i]

if __name__ == "__main__":
    board = dict(
        zip(((i, j) for i in range(9) for j in range(9)), 
            "73xxxx84x15xxx72xxxx8x1x3x5x96x5xx83xxx6x3xxx54xx2x76x3x2x4x6xxxx72xxx34x15xxxx28")) 
    missing_numbers_dict = dict() 
    # calculate the initial cost
    fill_missing_numbers()
    cur_cost = calculate_total_cost()
    # initial parameters for simulated annealing
    Tmax = 5000.0
    Tmin = 1e-3
    tau = 10000
    # start simulated annealing
    t = 0
    T = Tmax
    while T > Tmin:
        t += 1
        T = Tmax * exp(-t / tau)
        prev_cost = cur_cost
        prev_board = copy(board)
        random_swap_numbers_in_a_block()
        cur_cost = calculate_total_cost()
        diff_cost = cur_cost - prev_cost
        if diff_cost < 0:
            continue
        else:
            if exp(-diff_cost / T) > random.random():
                continue 
            else:
                board = prev_board
                cur_cost = prev_cost
        print (t, "--->", cur_cost)
        if cur_cost == 0:
            break

    print_board(board)



                