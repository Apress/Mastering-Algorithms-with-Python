import math
import matplotlib.pyplot as plt
from utils import city_coordinates, cities, haversine_distance, drawArrow

X_COORD_MEAN = sum([x for x, _ in city_coordinates]) / len(city_coordinates) 
Y_COORD_MEAN = sum([y for _, y in city_coordinates]) / len(city_coordinates) 
ETA = 10**(-3) # learning rate
MIN_STEP_SIZE = 10**(-8) # terminating condition for learning rate
NUM_STEPS = 200000

def euclidean_distance(x, y, coords):
    sum_distance = 0
    for coord_x, coord_y in coords:
        sum_distance += ((x  - coord_x)**2 + (y - coord_y)**2)**0.5
    return sum_distance

def partial_derivative_x_and_y(x, y, coords):
    partial_x = 0
    partial_y = 0
    for coord_x, coord_y in coords:
        partial_x += (x - coord_x) / ((x - coord_x)**2 + (y - coord_y)**2)**0.5
        partial_y += (y - coord_y) / ((x - coord_x)**2 + (y - coord_y)**2)**0.5
    return partial_x, partial_y

def gradient_descent(x_guess = X_COORD_MEAN, y_guess = Y_COORD_MEAN):
    x = x_guess
    y = y_guess
    learning_rate_x = ETA 
    learning_rate_y = ETA 
    step_x = math.inf
    step_y = math.inf 

    i = 0
    while i < NUM_STEPS and abs(step_x) > MIN_STEP_SIZE and abs(step_y) > MIN_STEP_SIZE:
        partial_x, partial_y = partial_derivative_x_and_y(x, y, city_coordinates)
        step_x = learning_rate_x * partial_x
        step_y = learning_rate_y * partial_y
        x -= step_x
        y -= step_y
        print (euclidean_distance(x, y, city_coordinates), "--->", step_x, step_y, i)
        i += 1 
    return x, y 

def plot_result(x, y):
    # plot cities
    N = len(city_coordinates)
    for i in range(N):
        plt.scatter(city_coordinates[i][0], city_coordinates[i][1], s=150, marker='*', color = "b")
        plt.text(city_coordinates[i][0], city_coordinates[i][1], cities[i], fontsize = 14)
    
    for i in range(N):
        drawArrow((x, y), city_coordinates[i], color = "gold", label = "")  

    plt.scatter(x, y, s=200, marker = "o", color = "gold")
    plt.xlabel("Longitude", fontsize = 14)
    plt.ylabel("Latitude", fontsize = 14)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    x, y = gradient_descent()
    print (x, y)
    plot_result(x, y)
    total_distance = 0
    for lon, lat in city_coordinates:
        total_distance += haversine_distance(x, y, lon, lat)
    print (f"The shortest distance to ten biggest cities in US is {round(total_distance, 2)} miles")