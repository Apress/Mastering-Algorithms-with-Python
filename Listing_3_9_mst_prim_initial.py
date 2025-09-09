from collections import defaultdict
import random
random.seed(1234)

def minimum_spanning_tree_prim(graph, nodes):
    visited = set()
    start_node = random.choice(nodes)
    neighbors = graph[start_node].copy()
    paths = []
    while len(visited) < len(nodes):
        for i in range(len(neighbors) -1, -1, -1):
            start_node, next_node, next_distance = neighbors[i]
            if start_node in visited and next_node in visited:
                continue
            break 
        if (start_node, next_node, next_distance) not in paths and (next_node, start_node, next_distance) not in paths:
            paths.append((start_node, next_node, next_distance))
        neighbors.extend(graph[next_node])
        neighbors.sort(key = lambda t: t[2], reverse = True)
        visited.add(start_node)
        start_node = next_node
    return paths 

if __name__ == "__main__":
    nodes = ["A", "B", "C", "D", "E", "F", "G"]
    distance_lst = [("A", "B", 1), ("A", "C", 20), ("A", "D", 2), ("A", "E", 6), ("A", "F", 10), 
                    ("B", "C", 5), ("B", "G", 8), 
                    ("C", "D", 4), 
                    ("E", "F", 5), 
                    ("F", "G", 15)]

    graph = defaultdict(list)
    for node_1, node_2, distance in distance_lst:
        graph[node_1].append((node_1, node_2, distance))
        graph[node_2].append((node_2, node_1, distance))

    # sort the neighbors by distance
    for node in graph:
        graph[node].sort(key = lambda t: t[2], reverse = True)
    
    print (minimum_spanning_tree_prim(graph, nodes))