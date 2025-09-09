class TreeNode:
    def __init__(self, val):
        self.left = None 
        self.right = None 
        self.val = val 
    
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    print (root.val)
    print (root.left.val)
    print (root.right.val)

