from collections import deque
class TreeNode:
    def __init__(self, value = None):
        self.value = value 
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def breadth_first_search_traversal_n_ary_tree(root_node):
    BFS_values = []
    queue = deque([root_node])
    while queue:
        node = queue.popleft()
        BFS_values.append(node.value)
        if node.children:
            queue.extend(node.children)
    return BFS_values   

def depth_first_search_traversal_n_ary_tree(root_node):
    DFS_values = []
    stack = [root_node]
    while stack:
        node = stack.pop()
        DFS_values.append(node.value)
        if node.children:
            stack.extend(node.children[::-1])
    return DFS_values   

def level_order_traversal_n_ary_tree(root_node):
    all_level_values = []
    queue = deque([root_node])
    while queue:
        cur_level_values = []
        for _ in range(len(queue)):
            node = queue.popleft()
            cur_level_values.append(node.value)
            if node.children:
                queue.extend(node.children)
        all_level_values.append(cur_level_values)
    return all_level_values  

def root_to_leaf_paths_n_ary_tree(root):
    paths = []
    stack = [(root, [root.value])]
    while stack:
        node, path = stack.pop()
        if not node.children:
            paths.append(path)
        else:
            for child in node.children[::-1]:
                stack.append((child, path + [child.value]))
    return paths 

if __name__ == "__main__":
    #                      0       
    #      1               2                 3    
    # 4    5    6     7    8     9    10     11     12
    #
    #
    root = TreeNode(0)
    child_1 = TreeNode(1)
    child_2 = TreeNode(2)
    child_3 = TreeNode(3)
    child_4 = TreeNode(4)
    child_5 = TreeNode(5)
    child_6 = TreeNode(6)
    child_7 = TreeNode(7)
    child_8 = TreeNode(8)
    child_9 = TreeNode(9)
    child_10 = TreeNode(10)
    child_11 = TreeNode(11)
    child_12 = TreeNode(12)
    root.add_child(child_1)
    root.add_child(child_2)
    root.add_child(child_3)
    child_1.add_child(child_4)
    child_1.add_child(child_5)
    child_1.add_child(child_6)
    child_2.add_child(child_7)
    child_2.add_child(child_8)
    child_2.add_child(child_9)
    child_3.add_child(child_10)
    child_3.add_child(child_11)
    child_3.add_child(child_12)
    print (breadth_first_search_traversal_n_ary_tree(root))
    print (depth_first_search_traversal_n_ary_tree(root))
    print (level_order_traversal_n_ary_tree(root))
    print (root_to_leaf_paths_n_ary_tree(root))






