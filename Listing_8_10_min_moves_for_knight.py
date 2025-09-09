from collections import deque 
DIRECTIONS = [(1,2), (2,1), (-1, 2), (-2,1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
# DIRECTIONS = [(1,-2), (2, -1), (-1, -2), (-2, -1),(1,2), (2,1), (-1, 2), (-2,1)]

def min_moves_for_knight_bfs(start_pos, end_pos, size_of_board=8):
    start_pos_x, start_pos_y = start_pos
    end_pos_x, end_pos_y = end_pos
    num_moves = 0
    visited = set()
    queue = deque([(start_pos_x, start_pos_y, num_moves)])
    path_dict = dict()

    while queue:
        cur_pos_x, cur_pos_y, num_moves_so_far = queue.popleft()
        if cur_pos_x == end_pos_x and cur_pos_y == end_pos_y:
            # retrieve the path
            paths = []
            while (end_pos_x, end_pos_y) != (start_pos_x, start_pos_y):
                paths.append((end_pos_x, end_pos_y))
                end_pos_x, end_pos_y = path_dict[(end_pos_x, end_pos_y)]
            paths.append((start_pos_x, start_pos_y))
            return num_moves_so_far, paths[::-1]

        # 8 possible next moves for knight
        for direction_x, direction_y in DIRECTIONS:
            next_pos_x = cur_pos_x + direction_x
            next_pos_y = cur_pos_y + direction_y
            # make sure positions are valid
            if 0<=next_pos_x<=size_of_board-1 and 0<=next_pos_y <=size_of_board-1 and (next_pos_x, next_pos_y) not in visited:
                queue.append((next_pos_x, next_pos_y, num_moves_so_far + 1))
                visited.add((next_pos_x, next_pos_y))
                path_dict[(next_pos_x, next_pos_y)] = (cur_pos_x, cur_pos_y)

def min_moves_for_knight_dfs(start_pos, end_pos):
    def dfs_helper(start_loc, end_loc, num_moves, visited, paths = []):
        start_pos_x, start_pos_y = start_loc

        if start_loc == end_loc:
            paths.append((num_moves, visited))
            return

        # 8 possible next moves for knight
        for direction_x, direction_y in DIRECTIONS:
            next_pos_x = start_pos_x + direction_x
            next_pos_y = start_pos_y + direction_y
            # make sure positions are valid
            if 0<=next_pos_x<=7 and 0<=next_pos_y <=7 and (next_pos_x, next_pos_y) not in visited:
                visited.append((next_pos_x, next_pos_y))
                dfs_helper((next_pos_x, next_pos_y), end_loc, num_moves + 1, visited)

        return paths 
    return dfs_helper(start_pos, end_pos, 0, [start_pos])

if __name__ == "__main__":
    print (min_moves_for_knight_bfs((0, 0), (7,7))) 
