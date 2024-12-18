from collections import deque

# Read input from "input" file
with open("input", "r") as f:
    byte_positions = [
        tuple(map(int, line.strip().split(','))) for line in f.readlines()
    ]

# Define the grid size
grid_size = 71
grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

# Simulate falling bytes
for x, y in byte_positions[:1024]:
    grid[y][x] = "#"

# Pathfinding with BFS
def bfs(start, end):
    queue = deque([start])
    visited = set([start])
    steps = 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if (x, y) == end:
                return steps
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited:
                    if grid[ny][nx] == ".":
                        queue.append((nx, ny))
                        visited.add((nx, ny))
        steps += 1
    return -1  # No path found

# Solve for minimum steps
start = (0, 0)
end = (70, 70)
min_steps = bfs(start, end)

print("Minimum number of steps:", min_steps)
