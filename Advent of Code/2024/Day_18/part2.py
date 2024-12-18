from collections import deque

# Read input from "input" file
with open("input", "r") as f:
    byte_positions = [
        tuple(map(int, line.strip().split(','))) for line in f.readlines()
    ]

# Define the grid size
grid_size = 71
grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

# BFS Function to check path existence
def bfs_exists(start, end):
    queue = deque([start])
    visited = set([start])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited:
                if grid[ny][nx] == ".":
                    queue.append((nx, ny))
                    visited.add((nx, ny))
    return False

# Simulate falling bytes and check for path blocking
start = (0, 0)
end = (70, 70)

for i, (x, y) in enumerate(byte_positions):
    # Corrupt the current position
    grid[y][x] = "#"
    
    # Check if the path is still valid
    if not bfs_exists(start, end):
        # If the path is blocked, output the coordinates
        print(f"{x},{y}")
        break
