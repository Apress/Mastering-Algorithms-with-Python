from collections import defaultdict
import string 
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.size = [1 for i in range(size + 1)]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
		
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return px
			
        if self.size[px] > self.size[py]:
            px, py = py, px
		
		# component y is bigger than component x
        self.parent[px] = py
        self.size[py] += self.size[px]
        return py

def minimum_spanning_tree_kruskal(graph, distance_lst):
    num_nodes = len(graph)
    union_find = UnionFind(num_nodes)
    distance_lst.sort(key = lambda t: t[2], reverse=True)
    visited = set()
    paths = []
    while len(visited) < num_nodes:
        node_1, node_2, distance = distance_lst.pop()
        # make sure joining node_1, node_2 not forming a cycle
        node_1_parent = union_find.find(node_1)
        node_2_parent = union_find.find(node_2)
        if node_1_parent != node_2_parent:
            union_find.union(node_1, node_2) 
            paths.append((node_1, node_2, distance))
            visited |= {node_1, node_2}

    # print path
    total_distance = 0
    uppercase_letters = string.ascii_uppercase
    for node_1, node_2, distance in paths:
        total_distance += distance
        print (uppercase_letters[node_1], "-->", uppercase_letters[node_2], "--", distance) 
    print (f"Shortest total distance is {total_distance}")
    return paths    

if __name__ == "__main__":
    distance_lst = [(0, 1, 1), (0, 2, 20), (0, 3, 2), (0, 4, 6), (0, 5, 10), 
                    (1, 2, 5), (1, 6, 8), 
                    (2, 3, 4), 
                    (4, 5, 5), 
                    (5, 6, 15)]

    graph = defaultdict(list)
    for node_1, node_2, distance in distance_lst:
        graph[node_1].append((node_1, node_2, distance))
        graph[node_2].append((node_2, node_1, distance))

    print (minimum_spanning_tree_kruskal(graph, distance_lst))