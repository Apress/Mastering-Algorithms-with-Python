import matplotlib.pyplot as plt
from collections import defaultdict
from utils import city_coordinates, cities
import random
import math 
EPISILON = 10**(-8)
N = len(city_coordinates)

def euclidean_distance(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def find_average_coordinate(list_of_coordinates):
    x_sum, y_sum = 0, 0
    num_points = len(list_of_coordinates)
    for x, y in list_of_coordinates:
        x_sum += x
        y_sum += y 
    return [x_sum / num_points, y_sum / num_points] 

def calculate_total_within_cluster_sum_of_squares(k_centroids, centroid_dict):
    total_sum_of_squares = 0
    for centroid_index in centroid_dict:
        for point_coord in centroid_dict[centroid_index]:
            total_sum_of_squares += euclidean_distance(k_centroids[centroid_index], point_coord)
    return total_sum_of_squares

def k_means_clustering(point_coords, num_clusters, num_iters):
    iter_count = 0
    # initial guess
    k_centroids = random.sample(point_coords, num_clusters)
    prev_total_within_cluster_sum_of_squares = math.inf
    while iter_count < num_iters: 
        point_dict = {}
        # find new k centroids
        for point_coord in point_coords:
            distance_to_centroids = [(euclidean_distance(point_coord, k_centroid), i) for i, k_centroid in enumerate(k_centroids)]
            closet_centroid_index = min(distance_to_centroids)[1]
            point_dict[tuple(point_coord)] = closet_centroid_index

        centroid_dict = defaultdict(list)
        for point, centroid_index in point_dict.items():
            centroid_dict[centroid_index].append(list(point))
        
        # udpate k centroids
        for i in range(num_clusters):
            if not centroid_dict[i]:
                continue 
            k_centroids[i] = find_average_coordinate(centroid_dict[i])

        total_within_cluster_sum_of_squares = calculate_total_within_cluster_sum_of_squares(k_centroids, centroid_dict)
        if abs(total_within_cluster_sum_of_squares - prev_total_within_cluster_sum_of_squares) <= EPISILON:
            break
        prev_total_within_cluster_sum_of_squares = total_within_cluster_sum_of_squares
        iter_count += 1
    
    return k_centroids, centroid_dict, total_within_cluster_sum_of_squares

def find_optimum_number_of_clusters(city_coordinates):
    num_clusters = range(1, N + 1)
    total_within_cluster_sum_of_squares_arr = []
    for num_cluster in num_clusters:
        cur_within_cluster_sum_of_squares_res = []
        for _ in range(10):
            _, _, total_within_cluster_sum_of_squares = k_means_clustering(city_coordinates, num_cluster, 1000)
            cur_within_cluster_sum_of_squares_res.append(total_within_cluster_sum_of_squares)
        total_within_cluster_sum_of_squares_arr.append(min(cur_within_cluster_sum_of_squares_res))
    plt.plot(num_clusters, total_within_cluster_sum_of_squares_arr, "ko-", lw=2)
    plt.xlabel("Number of Clusters", fontsize = 12)
    plt.ylabel("Total Within Cluster Sum of Squares", fontsize = 12)
    plt.title("Find Optimum Number of Clusters using Elbow Method", fontsize =12)
    plt.tight_layout()
    plt.show()    

def visualize_results(k_centroids, centroid_dict, colors = ["r", "b", "g", "m", "k", "c", "y", "tab:pink", "tab:brown", "tab:purple"]):
    for i, k_centroid in enumerate(k_centroids):
        for coord_x, coord_y in centroid_dict[i]:
            plt.scatter(coord_x, coord_y, c=colors[i], alpha = 0.6, s=50)
            plt.plot([coord_x, k_centroid[0]], [coord_y, k_centroid[1]], c = colors[i], alpha = 0.2)
        plt.scatter(k_centroid[0], k_centroid[1], marker='^', c=colors[i], s=70)
    # add city names
    for i in range(N):
        plt.text(city_coordinates[i][0], city_coordinates[i][1], cities[i], fontsize = 14)
    # title and labels
    plt.title(f'Clustering of Ten Major US Cities; n = {len(k_centroids)}', fontsize=14)
    plt.xlabel('Longitude', fontsize = 14)
    plt.ylabel('Latitude', fontsize = 14)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    k_centroids, centroid_dict, total_within_cluster_sum_of_squares = k_means_clustering(city_coordinates, 4, 1000)
    print (total_within_cluster_sum_of_squares)
    visualize_results(k_centroids, centroid_dict)
    find_optimum_number_of_clusters(city_coordinates)
