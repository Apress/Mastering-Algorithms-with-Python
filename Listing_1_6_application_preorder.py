class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 

def pre_order_traversal(root):
    sequence = []
    def preorder_helper(node):
        if node: 
            sequence.append(node.value)
            preorder_helper(node.left)
            preorder_helper(node.right)
    preorder_helper(root)
    return sequence

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Preorder traversal of the tree:", pre_order_traversal(root))
