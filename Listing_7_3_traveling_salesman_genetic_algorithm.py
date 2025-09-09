from utils import city_coordinates, cities, haversine_distance, drawArrow, print_best_route_based_on_coords, print_best_route_based_on_indexes
import random
from copy import copy 
from itertools import permutations
import matplotlib.pyplot as plt
random.seed(1235) 

# These are global params
NUM_CITIES = 10
BEST_PATH = None
POPULATION = [] 
PARENTS = None 
NUM_CHROMOSOMES = 100
NUM_GENERATIONS = 500
        
# Step 2: Calculate fitness function
def calculate_fitness(coord_indexes):
    s = 0.0
    for i in range(NUM_CITIES):
        s += haversine_distance(city_coordinates[coord_indexes[i]][0], city_coordinates[coord_indexes[i]][1], 
                                city_coordinates[coord_indexes[(i + 1) % NUM_CITIES]][0], city_coordinates[coord_indexes[(i + 1) % NUM_CITIES]][1])
    return s

def genetic_algorithm_traveling_salesman():
    # Step 1: Generate initial population
    other_cities_indexes = [list(range(1, 10)) for _ in range(NUM_CHROMOSOMES)]
    for i in range(NUM_CHROMOSOMES):
        random.shuffle(other_cities_indexes[i])
        POPULATION.append([0] + other_cities_indexes[i])
    
    for _ in range(NUM_GENERATIONS):  
        # Step 3: Select Parent
        POPULATION.sort(key = lambda coordinates: calculate_fitness(coordinates))
        BEST = POPULATION[0]
        print (f"{print_best_route_based_on_indexes(BEST)}")
        print (f"Short distance is {calculate_fitness(BEST)}")
        PARENTS = POPULATION[:2] 
        # Step 4: Cross Over
        point_to_cross_over = random.randint(1, NUM_CITIES)
        parent_1_copy = copy(PARENTS[0])
        parent_2_copy = copy(PARENTS[1])
        parent_1_right_part = parent_1_copy[point_to_cross_over:]
        parent_2_right_part = parent_2_copy[point_to_cross_over:]
        random.shuffle(parent_1_right_part)
        random.shuffle(parent_2_right_part)
        parent_1 = [item for item in parent_1_copy if item not in parent_2_right_part] + parent_2_right_part
        parent_2 = [item for item in parent_2_copy if item not in parent_1_right_part] + parent_1_right_part
        PARENTS = [parent_1, parent_2]
        # Step 5: Mutation
        for parent in PARENTS:
            i, j = random.sample(range(1, NUM_CITIES), 2)
            parent[i], parent[j] = parent[j], parent[i]
        # substitute the last two in the POPULATION
        POPULATION[-1] = PARENTS[0]
        POPULATION[-2] = PARENTS[1]
    return BEST

def calculate_total_distance(coords):
    s = 0.0
    for i in range(NUM_CITIES):
        s += haversine_distance(coords[i][0], coords[i][1], coords[(i + 1) % NUM_CITIES][0], coords[(i + 1) % NUM_CITIES][1])
    return s 

def brute_force_search(coords):
    first_coord = coords[0]
    next_coords = coords[1:]
    optimal_next_coords = min(permutations(next_coords), key = lambda coords: calculate_total_distance([first_coord] + list(coords)))
    return [first_coord] + list(optimal_next_coords)

def compare_paths(coords, ga_coords):
    brute_force_coords = brute_force_search(coords)
    print (f"brute force total distance = {calculate_total_distance(brute_force_coords)}")
    print (f"visit sequence from brute force {print_best_route_based_on_coords(brute_force_coords)}")
    # plot cities
    for i in range(NUM_CITIES):
        plt.scatter(coords[i][0], coords[i][1], s=150, marker='*', color = "b")
        plt.text(coords[i][0], coords[i][1], cities[i], fontsize = 14)

    for i in range(1, NUM_CITIES + 1):
        drawArrow(ga_coords[i-1], ga_coords[i % NUM_CITIES], color = "g", label = "Path from Genetic Algorithm" if i == 1 else "")  
    
    for i in range(1, NUM_CITIES + 1):
        drawArrow(brute_force_coords[i-1], brute_force_coords[i % NUM_CITIES], color = "k", label = "Path from Brute Force Search" if i == 1 else "")

    plt.xlabel("Longitude", fontsize = 14)
    plt.ylabel("Latitude", fontsize = 14)
    plt.legend(loc=0)
    plt.tight_layout()
    plt.savefig("travelling_salesman_path_genetic_algorithm.jpg", dpi = 600)
    plt.show()

if __name__ == "__main__":
    ga_indexes = genetic_algorithm_traveling_salesman() 
    ga_coords = [city_coordinates[ga_index] for ga_index in ga_indexes]
    compare_paths(city_coordinates, ga_coords)
