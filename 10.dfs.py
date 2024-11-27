def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
graph = {
    'A': ['D', 'E', 'C'],
    'B': [],
    'C': ['B'],
    'D': ['E'],
    'E': []
}
start_node = 'A'
print("Depth-First Search traversal:")
dfs(graph, start_node)
