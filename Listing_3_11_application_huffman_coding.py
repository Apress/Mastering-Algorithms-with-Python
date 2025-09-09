from heapq import heapify, heappop, heappush
class TreeNode:
    def __init__(self, name, value):
        self.name = name 
        self.value = value 
        self.left = None 
        self.right = None 

# {"A": 50, "B": 30, "C": 15, "D": 10, "a": 40, "b": 20, "c": 5, "d": 8}
def construct_huffman_tree(frequency_dict):
    # construct the heap
    heap = [(frequency, name, TreeNode(name, frequency)) for name, frequency in frequency_dict.items()]
    heapify(heap)
    count = 1 
    while len(heap) > 1:
        freq_1, _, node_1 = heappop(heap)
        freq_2, _, node_2 = heappop(heap)
        parent_freq = freq_1 + freq_2
        parent_name = f"N_{count}"
        parent_node = TreeNode(parent_name, parent_freq)
        parent_node.left = node_1
        parent_node.right = node_2
        heappush(heap, (parent_freq, parent_name, parent_node))
        count += 1 
    root_node = heap[0][2] 
    return root_node

def retrieve_new_encoding(root_node):
    new_encoding_dict = {}
    stack = [(root_node, "")]
    while stack:
        node, encoding = stack.pop()
        if not node.left and not node.right:
            new_encoding_dict[node.name] = encoding
        if node.right:
            stack.append((node.right, encoding + '1'))
        if node.left:
            stack.append((node.left, encoding + '0'))
    return new_encoding_dict   

if __name__ == "__main__":
    freq_dict = {"A": 50, "B": 30, "C": 15, "D": 10, "a": 40, "b": 20, "c": 5, "d": 8}
    root_node = construct_huffman_tree(freq_dict)
    new_encoding_dict = retrieve_new_encoding(root_node)
    print (new_encoding_dict)