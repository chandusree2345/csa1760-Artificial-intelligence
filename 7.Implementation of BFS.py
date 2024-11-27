from collections import deque

# BFS function to traverse the graph from a starting node
def bfs(graph, start_node):
    visited = set()  # Set to track visited nodes
    queue = deque([start_node])  # Initialize the queue with the start node
    visited.add(start_node)

    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        print(f"Visited: {node}")  # Process the node (print it here)

        # Visit all the adjacent nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)  # Add unvisited neighbors to the queue
                visited.add(neighbor)  # Mark neighbor as visited

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run BFS starting from node 'A'
bfs(graph, 'A')
