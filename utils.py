from math import exp, sqrt,sin, cos, atan2, radians, inf 
import matplotlib.pyplot as plt

def drawArrow(A, B, label, color = 'k', zorder = 2):
    plt.arrow(A[0], A[1], B[0] - A[0], B[1] - A[1], 
            width=0.005, length_includes_head=True, color = color, head_width = 0.2, head_length = 0.5, label = label, zorder=zorder)

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

cities = ["NYC", "LA", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
# from https://www.fittotravel.net/latitude-and-longitude-of-u-s-largest-cities

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

def print_best_route_based_on_coords(coords):
    path = ""
    for coord in coords:
        path += coords_cities_dict[tuple(coord)]
        path += "-->"
    path += coords_cities_dict[tuple(coords[0])]
    return path 

def print_best_route_based_on_indexes(coord_indexes):
    path = ""
    for coord_index in coord_indexes:
        path += cities[coord_index]
        path += "-->"
    path += cities[coord_indexes[0]]
    return path 