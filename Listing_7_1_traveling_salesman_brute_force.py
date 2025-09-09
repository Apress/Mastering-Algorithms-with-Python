from itertools import permutations
from math import exp, sqrt,sin, cos, atan2, radians, inf 

def haversine_distance(lon1, lat1, lon2, lat2):
    R = 3958.8 # Approximate radius of earth in miles
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

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

def print_best_route_based_on_coords(coords):
    path = ""
    for coord in coords:
        path += coords_cities_dict[tuple(coord)]
        path += "-->"
    path += coords_cities_dict[tuple(coords[0])]
    return path 

if __name__ == "__main__":
    NUM_CITIES = 10
    cities = ["NYC", "LA", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
    city_coordinates = [[-73.940, 40.670], # NYC
        [-118.410, 34.110], # LA
        [-87.680, 41.840],  # Chicago 
        [-95.464, 29.741],  # Houston
        [-112.070, 33.540], # Phoenix
        [-75.130, 40.010],  # Philadelphia
        [-98.510, 29.460],  # San Antonio
        [-117.140, 32.810], # San Diego
        [-96.770, 32.790],  # Dallas
        [-121.850, 37.300]] # San Jose

    coords_cities_dict = {tuple(coord): city for city, coord in zip(cities, city_coordinates)}
    brute_force_coords = brute_force_search(city_coordinates)
    print (f"brute force total distance = {calculate_total_distance(brute_force_coords)}")
    print (f"visit sequence from brute force  {print_best_route_based_on_coords(brute_force_coords)}")
