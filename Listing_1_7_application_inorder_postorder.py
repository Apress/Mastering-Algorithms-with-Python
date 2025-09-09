class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 

def in_order_traversal(root):
    sequence = []
    def inorder_helper(node):
        if node: 
            inorder_helper(node.left)
            sequence.append(node.value)
            inorder_helper(node.right)
    inorder_helper(root)
    return sequence

def post_order_traversal(root):
    sequence = []
    def postorder_helper(node):
        if node: 
            postorder_helper(node.left)
            postorder_helper(node.right)
            sequence.append(node.value)
    postorder_helper(root)
    return sequence

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Inorder traversal of the tree:", in_order_traversal(root))
    print("Postorder traversal of the tree", post_order_traversal(root))