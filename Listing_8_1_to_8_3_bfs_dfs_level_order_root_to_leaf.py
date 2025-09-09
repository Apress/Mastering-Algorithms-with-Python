from collections import deque 
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 

def breadth_first_search_traversal(root_node):
    BFS_values = []
    queue = deque([root_node])
    while queue:
        node = queue.popleft()
        BFS_values.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return BFS_values

def depth_first_search_traversal(root_node):
    DFS_values = []
    stack = [root_node]
    while stack:
        node = stack.pop()
        DFS_values.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return DFS_values

def level_order_traversal(root_node):
    all_level_values = []
    queue = deque([root_node])
    while queue:
        cur_level_values = []
        for _ in range(len(queue)):
            node = queue.popleft()
            cur_level_values.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        all_level_values.append(cur_level_values)
    return all_level_values

def root_to_leaf_paths(root_node):
    paths = []
    stack = [(root_node, [root_node.value])]
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)
        if node.right:
            stack.append((node.right, path + [node.right.value]))
        if node.left:
            stack.append((node.left, path + [node.left.value]))
    return paths

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print (breadth_first_search_traversal(root))
    print (depth_first_search_traversal(root))
    print (root_to_leaf_paths(root))
    print (level_order_traversal(root))