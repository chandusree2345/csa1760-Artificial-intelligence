from itertools import permutations
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance
def find_shortest_route():
    num_cities = len(distance_matrix)
    all_routes = permutations(range(num_cities))
    shortest_distance = float('inf')
    best_route = None
    for route in all_routes:
        current_distance = calculate_distance(route)
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            best_route = route
    return best_route, shortest_distance
route, distance = find_shortest_route()
print("Shortest route:", route)
print("Minimum distance:", distance)
