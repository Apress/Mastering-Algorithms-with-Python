class TreeNode:
    def __init__(self, val):
        self.left = None 
        self.right = None 
        self.val = val 
    
    def __repr__(self):
        return f"Current Tree Node has a value of {self.val}"

    def __eq__(self, other):
        return self.val == other.val 

    def __lt__(self, other):
        return self.val < other.val
    
    def __gt__(self, other):
        return self.val > other.val

    def __add__(self, other):
        return self.val + other.val 

    def __sub__(self, other):
        return self.val - other.val 

    def __mul__(self, other):
        return self.val * other.val 

    def __call__(self):
        self.val += 1

if __name__ == "__main__":
    node_1 = TreeNode(100)
    node_2 = TreeNode(50)
    print (node_1)
    print (node_2)
    print (node_1 > node_2)
    print (node_1 == node_2)
    print (node_1 < node_2)
    print (node_1 + node_2)
    print (node_1 - node_2)
    print (node_1 * node_2)
    # call
    node_1()
    print (node_1)
