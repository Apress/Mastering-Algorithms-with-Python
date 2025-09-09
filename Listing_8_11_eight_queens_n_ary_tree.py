from copy import deepcopy
import time 
class TreeNode:
    def __init__(self, value = None):
        self.value = value 
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class NQueens:
    def __init__(self, num_queens, board_size):
        self.num_queens = num_queens 
        self.board_size = board_size
        self.coordinates = set((i,j) for i in range(self.board_size) for j in range(self.board_size))
        self.n_queens_solutions = set()

    def root_to_leaf_paths_n_ary_tree(self, root):
        paths = []
        stack = [(root, [root.value])]
        while stack:
            node, path = stack.pop()
            if not node.children and len(path) == self.num_queens + 1: # check if the length of path equals num of queens
                paths.append(path[1:]) # ignore the dummy root value
            else:
                for child in node.children[::-1]:
                    stack.append((child, path + [child.value]))
        return paths

    def allowed_positions_for_new_queens(self, existing_queen_positions):
        not_allowed_positions = set()
        for i in range(self.board_size):
            for j in range(self.board_size):
                if any(r == i or j == c or abs(r - i) == abs(c - j) for r, c in existing_queen_positions):
                    not_allowed_positions.add((i, j))
        remaining_allowed_positions = deepcopy(self.coordinates) - not_allowed_positions 
        return remaining_allowed_positions

    def construct_n_ary_tree(self):
        root = TreeNode("root") # dummy root node
        stack = [(root, [])] # (node, exisiting queen positions)
        while stack:
            node, existing_queen_positions = stack.pop()
            if node.value == "root": # at root level
                for i in range(self.board_size):
                    for j in range(self.board_size):
                        child = TreeNode((i, j))
                        node.add_child(child)
                        stack.append((child, existing_queen_positions + [(i, j)]))
            else:
                allowed_positions = self.allowed_positions_for_new_queens(existing_queen_positions)
                if not allowed_positions:
                    continue 
                for i, j in allowed_positions:
                    child = TreeNode((i,j))
                    node.add_child(child)
                    stack.append((child, existing_queen_positions + [(i, j)]))
        return root 

    def find_all_solutions(self):
        root = self.construct_n_ary_tree()
        paths = self.root_to_leaf_paths_n_ary_tree(root)
        for path in paths:
            path.sort()
            self.n_queens_solutions.add(tuple(path))
        return self.n_queens_solutions

if __name__ == "__main__":
    t_start = time.time()
    eight_queens = NQueens(6, 6)
    print (eight_queens.find_all_solutions())
    t_end = time.time()
    print ("time consumed", t_end - t_start)

        

    
        