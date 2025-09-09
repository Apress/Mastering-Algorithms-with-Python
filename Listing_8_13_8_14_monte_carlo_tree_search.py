import numpy as np

class Node:
    def __init__(self, total_score = 0, num_visits = 0):
        self.left = None
        self.right = None
        self.parent = None 
        self.total_score = total_score
        self.num_visits = num_visits

    def calculate_ucb1_score(self, c=2):
        if not self.num_visits:
            return np.inf
        # if at root node
        if not self.parent:
            return 
        # at child node    
        ubc1_score = (self.total_score / self.num_visits) + c * np.sqrt(np.log(self.parent.num_visits) / self.num_visits)
        return ubc1_score

class MonteCarloTreeSearch:
    def __init__(self, num_iters = 4):
        self.num_iters = num_iters
        self.ROLL_OUT_RESULTS = [22, 6, 30, 100]

    def random_roll_out_result(self):
        return self.ROLL_OUT_RESULTS.pop()

    def selection(self, node):
        if not node.left and not node.right:
            return node

        if node.left and not node.right:
            return node.left
        
        if not node.left and node.right:
            return node.right
        
        if node.left and node.right:
            left_child_ucb1_score = node.left.calculate_ucb1_score()
            right_child_ucb1_score = node.right.calculate_ucb1_score()
            if left_child_ucb1_score > right_child_ucb1_score:
                return node.left
            elif left_child_ucb1_score < right_child_ucb1_score:
                return node.right
            else:
                return node.left

    def expansion(self, node):
        "add left and right children nodes"
        left_child_node = Node(0, 0)
        right_child_node = Node(0, 0)
        node.left = left_child_node
        node.right = right_child_node
        left_child_node.parent = node
        right_child_node.parent = node 

    def simulation(self):
        return self.random_roll_out_result()

    def backpropagation(self, node, score):
        while node.parent:
            node.num_visits += 1
            node.total_score += score
            node = node.parent 

        # root has no parent and update root separately
        node.num_visits += 1
        node.total_score += score
        return node 
    
    def perform_one_round_four_steps_simulation(self, node):
        # selection
        while node.left or node.right:
            node = self.selection(node)

        # expansion
        if node.num_visits > 0:
            self.expansion(node)
            node = node.left

        # simulation
        roll_out_val = self.simulation()

        # backpropagation
        node = self.backpropagation(node, roll_out_val)
        return node 

    def perform_many_rounds_four_steps_simulation(self, node):
        if self.num_iters < 1:
            return

        for _ in range(self.num_iters):
            node = self.perform_one_round_four_steps_simulation(node)
        return node 

    def return_best_path(self, root):
        path = [(root.total_score, root.num_visits)]
        while root:
            if root.left and not root.right:
                path.append(((root.left.total_score, root.left.num_visits)))
                root = root.left
            elif root.right and not root.left:
                path.append(((root.right.total_score, root.right.num_visits)))
                root = root.right
            elif root.left and root.right:
                if root.left.num_visits:
                    average_score_left = root.left.total_score / root.left.num_visits 
                else:
                    average_score_left = np.inf
                if root.right.num_visits:
                    average_score_right = root.right.total_score / root.right.num_visits  
                else:
                    average_score_right = np.inf
                if average_score_left >= average_score_right:
                    path.append(((root.left.total_score, root.left.num_visits)))
                    root = root.left
                else:
                    path.append(((root.right.total_score, root.right.num_visits)))
                    root = root.right  
            else:
                break  
        return path                

    def print_tree(self, root, space=0, LEVEL_SPACE = 7):
        "Reference: https://stackoverflow.com/a/70318281"
        if not root: 
            return
        space += LEVEL_SPACE
        self.print_tree(root.right, space)
        for i in range(LEVEL_SPACE, space): 
            print(end = " ")  
        print("|" + str(root.total_score) + ','+ str(root.num_visits) + "|<")
        self.print_tree(root.left, space)

if __name__ == "__main__":
    # construct a tree
    '''
            (0, 0)
            /    \
        (0,0)   (0,0)
    
    '''
    # construct a shallow tree
    root_node = Node(0, 0) 
    left_node = Node(0, 0)
    right_node = Node(0, 0)
    left_node.parent = root_node
    right_node.parent = root_node
    root_node.left = left_node
    root_node.right = right_node

    mcts = MonteCarloTreeSearch(num_iters=4)
    new_root_node = mcts.perform_many_rounds_four_steps_simulation(root_node)
    print ("Visualize tree")
    mcts.print_tree(new_root_node)
    path = mcts.return_best_path(new_root_node)
    print ("Best path")
    print (path)




