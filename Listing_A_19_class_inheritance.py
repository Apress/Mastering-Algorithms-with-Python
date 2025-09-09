import numpy as np 
class TreeNode:
    def __init__(self, val):
        self.left = None 
        self.right = None 
        self.parent = None 
        self.val = val 

    def __repr__(self):
        return f"Current Tree Node has a value of {self.val}"

class MonteCarloTreeNode(TreeNode):
    def __init__(self, total_score, num_visits):
        self.num_visits = num_visits
        super().__init__(val=total_score)

    def __repr__(self):
        return f"Current Tree Node has a value of {self.val} and a total visit of {self.num_visits}"

    def calculate_ucb1_score(self, c=2):
        if not self.num_visits:
            return np.inf
        # if at root node
        if not self.parent:
            return 
        # at child node    
        ubc1_score = (self.val / self.num_visits) + c * np.sqrt(np.log(self.parent.num_visits) / self.num_visits)
        return ubc1_score

    def print_tree(self, root, space=0, LEVEL_SPACE = 7):
        "Reference: https://stackoverflow.com/a/70318281"
        if not root: 
            return
        space += LEVEL_SPACE
        self.print_tree(root.right, space)
        for i in range(LEVEL_SPACE, space): 
            print(end = " ")  
        print("|" + str(root.val) + ','+ str(root.num_visits) + "|<")
        self.print_tree(root.left, space)

if __name__ == "__main__":
    root_node = MonteCarloTreeNode(100, 10) 
    left_node = MonteCarloTreeNode(20, 50)
    right_node = MonteCarloTreeNode(40, 60)
    left_node.parent = root_node
    right_node.parent = root_node
    root_node.left = left_node
    root_node.right = right_node

    print (root_node)
    print (left_node.calculate_ucb1_score())
    print (right_node.calculate_ucb1_score())
    root_node.print_tree(root_node)

