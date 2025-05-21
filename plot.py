import numpy as np
import itertools
import time
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

# Sample TSP instance (distance matrix)
CITY_COORDINATES = np.array([
    [0, 0], [2, 4], [5, 2], [7, 6], [8, 3]
])

DIST_MATRIX = cdist(CITY_COORDINATES, CITY_COORDINATES, metric='euclidean')

### Classical Approach: Dynamic Programming (Held-Karp Algorithm) ###
def tsp_dp(distance_matrix):
    n = len(distance_matrix)
    memo = {}
    
    def visit(city, visited):
        if visited == (1 << n) - 1:
            return distance_matrix[city][0]
        if (city, visited) in memo:
            return memo[(city, visited)]
        
        min_cost = float('inf')
        for next_city in range(n):
            if visited & (1 << next_city) == 0:
                cost = distance_matrix[city][next_city] + visit(next_city, visited | (1 << next_city))
                min_cost = min(min_cost, cost)
        
        memo[(city, visited)] = min_cost
        return min_cost
    
    return visit(0, 1)

### Self-Organizing Map (SOM) Approach ###
def tsp_som(city_coords, num_iterations=1000, learning_rate=0.8, neighborhood_size=2):
    num_cities = len(city_coords)
    num_nodes = num_cities * 2  # More nodes than cities
    nodes = np.random.rand(num_nodes, 2) * np.max(city_coords)
    
    for iteration in range(num_iterations):
        city = city_coords[np.random.randint(num_cities)]
        winner_idx = np.argmin(np.linalg.norm(nodes - city, axis=1))
        
        for j in range(-neighborhood_size, neighborhood_size + 1):
            neighbor_idx = (winner_idx + j) % num_nodes
            nodes[neighbor_idx] += learning_rate * (city - nodes[neighbor_idx])
    
    # Compute distances from each node to all cities and order nodes
    node_distances = np.array([np.sum(np.linalg.norm(city_coords - node, axis=1)) for node in nodes])
    tour = np.argsort(node_distances)
    
    return nodes[tour]

### Visualization Function ###
def plot_som_solution(city_coords, nodes):
    plt.figure(figsize=(6, 6))
    plt.scatter(city_coords[:, 0], city_coords[:, 1], c='red', label='Cities')
    plt.plot(nodes[:, 0], nodes[:, 1], 'bo-', label='SOM Path')
    plt.legend()
    plt.title("TSP Solution using SOM")
    plt.show()

### Comparison ###
start_time = time.time()
dp_solution = tsp_dp(DIST_MATRIX)
dp_time = time.time() - start_time

start_time = time.time()
som_solution = tsp_som(CITY_COORDINATES)
som_time = time.time() - start_time

print(f"DP Solution Distance: {dp_solution}, Time: {dp_time:.4f} sec")
print(f"SOM Approximate Solution, Time: {som_time:.4f} sec")

# Plot SOM solution
plot_som_solution(CITY_COORDINATES, som_solution)
