from collections import defaultdict
import random
import heapq

random.seed(1234)
def minimum_spanning_tree_prim(graph, nodes):
    cur_node = random.choice(nodes)
    visited = set()
    min_edge_length_dict = {node: float("inf") for node in nodes}
    min_heap = []
    heapq.heappush(min_heap, min(graph[cur_node]))
    paths_dict = {node: None for node in nodes} # {child: parent}

    while len(visited) < len(nodes):
        # pop from min heap
        distance, cur_node, neighbor_node = heapq.heappop(min_heap)
        visited.add(cur_node)

        # push to min heap
        for distance, cur_node, neighbor_node in graph[cur_node]:
            if neighbor_node not in visited and distance < min_edge_length_dict[neighbor_node]:
                min_edge_length_dict[neighbor_node] = distance
                heapq.heappush(min_heap, (distance, neighbor_node, cur_node))
                paths_dict[neighbor_node] = (cur_node, distance)

    # print path
    total_distance = 0
    for child_node in nodes:
        if paths_dict[child_node]:
            parent_node, distance = paths_dict[child_node]
            total_distance += distance
            print (child_node, "-->", parent_node, "--", distance)
    print (f"Shortest total distance is {total_distance}")
    return paths_dict 

if __name__ == "__main__":
    nodes = ["A", "B", "C", "D", "E", "F", "G"]
    distance_lst = [("A", "B", 1), ("A", "C", 20), ("A", "D", 2), ("A", "E", 6), ("A", "F", 10), 
                    ("B", "C", 5), ("B", "G", 8), 
                    ("C", "D", 4), 
                    ("E", "F", 5), 
                    ("F", "G", 15)]
    
    graph = defaultdict(list)
    for node_1, node_2, distance in distance_lst:
        graph[node_1].append((distance, node_1, node_2))
        graph[node_2].append((distance, node_2, node_1))

    print (minimum_spanning_tree_prim(graph, nodes))

"""
Complexity Analysis:

Time Complexity:
Building the adjacency list takes O(E), where E is the number of edges.
Each edge is processed at most once, and operations on the priority queue (heap) take O(logV) time, where V is the number of vertices.
The overall time complexity is O((V+E)logV).
Space Complexity:
The space complexity is O(V+E) due to the adjacency list and the priority queue.
"""