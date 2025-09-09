import heapq
from collections import defaultdict
from utils import city_coordinates, cities, haversine_distance, drawArrow
import matplotlib.pyplot as plt

N = 10
cities_coord_dict = {city : coord for city, coord in zip(cities, city_coordinates)}
edges = [["NYC", "Chicago"], ["NYC", "Philadelphia"], ["Chicago", "Philadelphia"],
         ["Chicago", "San Jose"], ["Chicago", "Phoenix"], ["Chicago", "Dallas"], 
         ["Philadelphia", "Dallas"], ["Dallas", "Phoenix"], ["Dallas", "San Antonio"], 
         ["Dallas", "Houston"], ["San Antonio", "Houston"], ["Phoenix", "San Antonio"],
         ["LA", "San Jose"], ["LA", "Phoenix"], ["LA", "San Diego"], 
         ["San Jose", "Phoenix"], ["San Diego", "Phoenix"]]

dists = [int(haversine_distance(*cities_coord_dict[city_1], *cities_coord_dict[city_2])) for city_1, city_2 in edges]

graph = defaultdict(list)
for i in range(len(edges)):
    graph[edges[i][0]].append((edges[i][1], dists[i]))
    graph[edges[i][1]].append((edges[i][0], dists[i]))

def shortest_path_between_cities(start_city, end_city):
    visited = {city: False for city in cities}
    distances = {city: float('inf') for city in cities}
    parent = {city: None for city in cities}
    parent[start_city] = start_city
    heap = [(0, start_city)]
    heapq.heapify(heap)

    while heap:
        dist, node = heapq.heappop(heap)
        if not visited[node]:
            distances[node] = dist
            visited[node] = True
            for k, d in graph[node]:
                if not visited[k]:
                    new_dist = dist + d
                    if new_dist < distances[k]:
                        distances[k] = new_dist
                        parent[k] = node
                        heapq.heappush(heap, (new_dist, k))
        
    # retrieve path
    if distances[end_city] == float('inf'):
        shortest_path = []

    path = []
    node = end_city
    while node != start_city:
        path.append(node)
        node = parent[node]
    path.append(start_city)
    shortest_path = path[::-1]

    print (distances)
    print (visited)
    print (parent)
    print (shortest_path)
    return shortest_path

def plot_shortest_path(shortest_path):
    plt.figure(figsize = (10,8))
    shortest_path_coordinates = [cities_coord_dict[city] for city in shortest_path]
    # plot cities
    for i in range(N):
        plt.scatter(city_coordinates[i][0], city_coordinates[i][1], s=150, marker='*', color = "b")
        if i == 6: # San Antonio
            plt.text(city_coordinates[i][0] - 5, city_coordinates[i][1] - 0.5, cities[i], fontsize = 14)
        else:
            plt.text(city_coordinates[i][0], city_coordinates[i][1], cities[i], fontsize = 14)

    for (start_city, end_city), distance in zip(edges, dists):
        plt.plot([cities_coord_dict[start_city][0], cities_coord_dict[end_city][0]],
                 [cities_coord_dict[start_city][1], cities_coord_dict[end_city][1]], "k-", lw=2, zorder = 1)
        if start_city == "San Antonio" and end_city == "Houston":
            plt.text(cities_coord_dict[start_city][0] * 0.5 + cities_coord_dict[end_city][0] * 0.5, 
                    cities_coord_dict[start_city][1] * 0.5 + cities_coord_dict[end_city][1] * 0.5 - 0.4,
                    str(distance), 
                    fontsize = 14)
        elif start_city == "NYC" and end_city == "Philadelphia":
            plt.text(cities_coord_dict[start_city][0] * 0.5 + cities_coord_dict[end_city][0] * 0.5 + 0.5, 
                    cities_coord_dict[start_city][1] * 0.5 + cities_coord_dict[end_city][1] * 0.5,
                    str(distance), 
                    fontsize = 14)
        else:
            plt.text(cities_coord_dict[start_city][0] * 0.5 + cities_coord_dict[end_city][0] * 0.5, 
                    cities_coord_dict[start_city][1] * 0.5 + cities_coord_dict[end_city][1] * 0.5,
                    str(distance), 
                    fontsize = 14)

    for i in range(len(shortest_path) - 1):
        drawArrow(shortest_path_coordinates[i], shortest_path_coordinates[(i + 1) % N], color = "r", label = "Shortest Path" if i == 1 else "", zorder = 2)  
    
    plt.xlabel("Longitude", fontsize = 14)
    plt.ylabel("Latitude", fontsize = 14)
    plt.legend(loc=0)
    plt.tight_layout()
    plt.savefig("Shortest_Path.jpg", dpi = 600)
    plt.show() 

if __name__ == "__main__":
    shortest_path = shortest_path_between_cities("NYC", "LA")
    plot_shortest_path(shortest_path)