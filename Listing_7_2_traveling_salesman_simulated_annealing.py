import random
import numpy as np
from math import exp 
import matplotlib.pyplot as plt
from itertools import permutations
import time
from utils import haversine_distance, drawArrow, cities, city_coordinates, print_best_route_based_on_coords
from copy import deepcopy 
random.seed(1234)

t_start = time.time()
N = 10
Tmax = 10.0
Tmin = 1e-3
tau = 1e4

def calculate_total_distance(coords):
    s = 0.0
    for i in range(N):
        s += haversine_distance(coords[i][0], coords[i][1], coords[(i + 1) % N][0], coords[(i + 1) % N][1])
    return s 

def brute_force_search(coords):
    first_coord = coords[0]
    next_coords = coords[1:]
    optimal_next_coords = min(permutations(next_coords), key = lambda coords: calculate_total_distance([first_coord] + list(coords)))
    return [first_coord] + list(optimal_next_coords)

def compare_paths(coords, sa_coords):
    brute_force_coords = brute_force_search(coords)
    print (f"brute force total distance = {calculate_total_distance(brute_force_coords)}")
    print (f"visit sequence from brute force {print_best_route_based_on_coords(brute_force_coords)}")
    # plot cities
    for i in range(N):
        plt.scatter(coords[i][0], coords[i][1], s=150, marker='*', color = "b")
        plt.text(coords[i][0], coords[i][1], cities[i], fontsize = 14)

    for i in range(1, N + 1):
        drawArrow(sa_coords[i-1], sa_coords[i % N], color = "b", label = "Path from Simulated Annealing" if i == 1 else "")  
    
    for i in range(1, N + 1):
        drawArrow(brute_force_coords[i-1], brute_force_coords[i % N], color = "k", label = "Path from Brute Force Search" if i == 1 else "")

    plt.xlabel("Longitude", fontsize = 14)
    plt.ylabel("Latitude", fontsize = 14)
    plt.legend(loc=0)
    plt.tight_layout()
    plt.savefig("travelling_salesman_path_simulated_annealing.jpg", dpi = 600)
    plt.show()

def swap_array_element(i, j, coords):
    coords[i][0], coords[j][0] = coords[j][0], coords[i][0]
    coords[i][1], coords[j][1] = coords[j][1], coords[i][1]

def run_simulated_annealing(coords):
    cur_total_distance = calculate_total_distance(coords)
    # Main loop 
    t = 0
    T = Tmax 
    while T > Tmin:
        t += 1
        T = Tmax * exp(-t / tau) # cooling
        # choose two cities to swap and make sure they are distinct
        i, j = random.sample(range(1, N), 2)
        # swap them and calculate the change in distance
        prev_total_distance = cur_total_distance
        swap_array_element(i, j, coords)
        cur_total_distance = calculate_total_distance(coords)
        diff_distance = cur_total_distance - prev_total_distance 
        if diff_distance < 0:
            continue
        else:
            if exp(-diff_distance/T) > random.random():
                continue 
            else:
                swap_array_element(i, j, coords)
                cur_total_distance = prev_total_distance

    t_end = time.time()
    print (t_end - t_start)
    print(f"total distance from simulated annealing = {calculate_total_distance(coords)}")
    print (f"sequence from simulated annealing {print_best_route_based_on_coords(coords)}")
    return coords 

if __name__ == "__main__":
    city_coordinates_copy_1, city_coordinates_copy_2 = deepcopy(city_coordinates), deepcopy(city_coordinates)
    sa_coords = run_simulated_annealing(city_coordinates_copy_1)
    compare_paths(city_coordinates_copy_2, sa_coords)
