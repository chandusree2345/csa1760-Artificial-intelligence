from collections import deque

grid = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

start = (0, 0)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def vacuum_cleaner_bfs(start, grid):
    visited = set()
    dirty_cells = sum(row.count(1) for row in grid)
    queue = deque([(start, 0, 0)})
    visited.add(start)

    while queue:
        (x, y), cleaned, steps = queue.popleft()
        if grid[x][y] == 1:
            cleaned += 1
            grid[x][y] = 0  
            print(f"Cleaned cell at ({x}, {y}) in {steps} steps.")

          
            if cleaned == dirty_cells:
                return steps  
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny, grid) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), cleaned, steps + 1))

    return -1  
steps_to_clean = vacuum_cleaner_bfs(start, grid)
if steps_to_clean != -1:
    print(f"All cells cleaned in {steps_to_clean} steps.")
else:
    print("Unable to clean all cells.")
