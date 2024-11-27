from collections import deque

# Define the initial and goal states
initial_state = (3, 3, 1)  
goal_state = (0, 0, 0)  

# Possible moves
moves = [
    (1, 0), 
    (2, 0),  
    (0, 1),  
    (0, 2),  
    (1, 1)   
]

# Check if the state is valid
def is_valid_state(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:  # Missionaries can't be outnumbered by cannibals
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):  # Same for the right side
        return False
    return True

# Perform Breadth-First Search (BFS) to find the solution
def missionaries_cannibals_bfs():
    queue = deque([(initial_state, [])])  # State and path to reach it
    visited = set()  # To track visited states
    visited.add(initial_state)

    while queue:
        (m, c, boat), path = queue.popleft()

        # Check if the goal is reached
        if (m, c, boat) == goal_state:
            return path + [(m, c, boat)]

        # Generate next states
        for move_m, move_c in moves:
            if boat == 1:  # Moving from left to right
                new_state = (m - move_m, c - move_c, 0)
            else:  # Moving from right to left
                new_state = (m + move_m, c + move_c, 1)

 
            if is_valid_state(new_state[0], new_state[1]) and new_state not in visited:
                queue.append((new_state, path + [(m, c, boat)]))
                visited.add(new_state)

    return None  # No solution found


solution = missionaries_cannibals_bfs()
if solution:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print("No solution found.")
