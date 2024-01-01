import itertools
import sys
def tsp(cities):
    return min(itertools.permutations(cities), key=lambda route: sum(calculate_distance(route)))
def calculate_distance(route):
    return [calculate_euclidean_distance(route[i], route[i+1]) for i in range(len(route)-1)]
def calculate_euclidean_distance(city1, city2):
    return ((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2) ** 0.5
cities = [(0, 0), (1, 2), (3, 1), (2, 4), (5, 2)]
optimal_route = tsp(cities)
min_distance = sum(calculate_distance(optimal_route))
print("Optimal Route:", optimal_route)
print("Minimum Distance:", min_distance)