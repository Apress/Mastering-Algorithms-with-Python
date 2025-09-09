def minimum_spanning_tree_kruskal(distance_lst, nodes):
    distance_lst.sort(key = lambda t: t[2], reverse=True)
    visited = set()
    paths = []
    while len(visited) < len(nodes):
        node_1, node_2, distance = distance_lst.pop()
        if not (node_1 in visited and node_2 in visited):
            paths.append((node_1, node_2, distance))
            visited.add(node_1)
            visited.add(node_2)    
    # print path
    total_distance = 0
    for node_1, node_2, distance in paths:
        total_distance += distance
        print (node_1, "-->", node_2, "--", distance) 
    print (f"Shortest total distance is {total_distance}")
    return paths 

if __name__ == "__main__":
    nodes = ["A", "B", "C", "D", "E", "F", "G"]
    distance_lst = [("A", "B", 1), ("A", "C", 20), ("A", "D", 2), ("A", "E", 6), ("A", "F", 10), 
                    ("B", "C", 5), ("B", "G", 8), 
                    ("C", "D", 4), 
                    ("E", "F", 5), 
                    ("F", "G", 15)]

    print (minimum_spanning_tree_kruskal(distance_lst, nodes))