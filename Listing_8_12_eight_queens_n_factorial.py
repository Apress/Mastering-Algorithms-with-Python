import time 
class NQueens:
    def __init__(self, num_queens, board_size):
        self.num_queens = num_queens 
        self.board_size = board_size
        self.n_queens_solutions = []

    def allowed_col_positions_for_new_queen(self, existing_queen_col_positions):
        # we put one queen in each row by default 
        allowed_positions = []
        cur_row_idx = len(existing_queen_col_positions)
        forbidden_diagnoal_cols = []
        for existing_queen_row_pos, existing_queen_col_pos in enumerate(existing_queen_col_positions):
            pos_1 = existing_queen_col_pos + (cur_row_idx - existing_queen_row_pos) # col position to rule out due to diagonal attack
            pos_2 = existing_queen_col_pos - (cur_row_idx - existing_queen_row_pos) # col position to rule out due to diagonal attack
            if 0<=pos_1<self.board_size:
                forbidden_diagnoal_cols.append(pos_1)
            if 0<=pos_2<self.board_size:
                forbidden_diagnoal_cols.append(pos_2)

        for col_idx in range(self.board_size):
            if col_idx in existing_queen_col_positions:
                continue

            if col_idx in forbidden_diagnoal_cols:
                continue 
            allowed_positions.append(col_idx)
        return allowed_positions
         
    def find_all_solutions(self):
        stack = [("root", [], 0)] # (node, exisiting queen positions, level)
        while stack:
            cur_col_position, existing_queen_positions, level = stack.pop()
            if level == self.num_queens:
                self.n_queens_solutions.append(existing_queen_positions)
            
            if cur_col_position == "root": # at root level
                for col_idx in range(self.board_size):
                    stack.append((col_idx, existing_queen_positions + [col_idx], 1))
            else:
                allowed_positions = self.allowed_col_positions_for_new_queen(existing_queen_positions)
                if not allowed_positions:
                    continue 
                for col_idx in allowed_positions:
                    stack.append((col_idx, existing_queen_positions + [col_idx], level + 1))
        return self.n_queens_solutions 

if __name__ == "__main__":
    t_start = time.time()
    eight_queens = NQueens(8,8)
    solutions = eight_queens.find_all_solutions()
    print (len(solutions))
    print (solutions)
    t_end = time.time()
    print ("time consumed", t_end - t_start)

        

    
        