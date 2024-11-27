import heapq
graph = {'A': [('B', 1), ('C', 4)], 'B': [('D', 2), ('E', 5)], 'C': [('E', 1)], 'D': [], 'E': []}
heuristics = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0}
def a_star(start, goal):
    queue, visited = [(0, start, [start])], set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == goal: return path, cost
        if node in visited: continue
        visited.add(node)
        for neighbor, travel_cost in graph[node]:
            heapq.heappush(queue, (cost + travel_cost + heuristics[neighbor], neighbor, path + [neighbor]))
path, cost = a_star('A', 'E')
print("Path:", " -> ".join(path) if path else "No path found.", "\nCost:", cost)
