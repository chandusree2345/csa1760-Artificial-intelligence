from queue import PriorityQueue

# Define the goal state for reference
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 represents the blank tile
]

# Find the Manhattan distance heuristic
def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(goal.index(state[i][j]), 3)
                distance += abs(x - i) + abs(y - j)
    return distance

# Convert the 2D list to a tuple for immutability and hashing
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

# Check if the current state is the goal state
def is_goal(state):
    return state == goal_state

# Get possible moves (up, down, left, right) of the blank tile
def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)  # Blank tile position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Swap the blank tile with the adjacent tile
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Perform A* Search to solve the 8-puzzle
def a_star(start):
    # Priority queue for states, with priority as the cost function f(n)
    pq = PriorityQueue()
    pq.put((0, start, 0, []))  # (priority, state, g(n), path)
    visited = set()
    visited.add(state_to_tuple(start))

    while not pq.empty():
        _, current, g, path = pq.get()

        # Check if the goal is reached
        if is_goal(current):
            return path + [current]

        # Explore neighbors
        for neighbor in get_neighbors(current):
            neighbor_tuple = state_to_tuple(neighbor)
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                h = manhattan_distance(neighbor, sum(goal_state, []))
                f = g + 1 + h
                pq.put((f, neighbor, g + 1, path + [current]))

    return None  # No solution found

# Test the algorithm with an initial state
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Run the A* search algorithm
solution_path = a_star(initial_state)

# Output the solution path if one was found
if solution_path:
    print("Solution path:")
    for step in solution_path:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
