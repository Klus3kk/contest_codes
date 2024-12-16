from heapq import heappop, heappush
from collections import defaultdict

# Directions: 0 = East, 1 = South, 2 = West, 3 = North
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def parse_maze(input_data):
    maze = input_data.strip().split("\n")
    start, end = None, None
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == 'S':
                start = (i, j)
            elif char == 'E':
                end = (i, j)
    return maze, start, end

def find_best_tiles(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    pq = [(0, *start, 0)]  # (cost, x, y, direction)
    visited = set()
    best_cost = float('inf')
    best_tiles = set()
    
    while pq:
        cost, x, y, direction = heappop(pq)

        # Skip if already visited
        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        # Add tile to best_tiles if within best cost
        if cost <= best_cost:
            best_tiles.add((x, y))

        # If cost exceeds best_cost, stop exploring this path
        if cost > best_cost:
            continue

        # If we reached the end, update best_cost
        if (x, y) == end:
            best_cost = min(best_cost, cost)
            continue

        # Move forward
        dx, dy = DIRS[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
            heappush(pq, (cost + 1, nx, ny, direction))

        # Rotate clockwise
        new_dir = (direction + 1) % 4
        heappush(pq, (cost + 1000, x, y, new_dir))

        # Rotate counterclockwise
        new_dir = (direction - 1) % 4
        heappush(pq, (cost + 1000, x, y, new_dir))

    return best_tiles

def mark_best_tiles(maze, best_tiles):
    marked_maze = [list(row) for row in maze]
    for x, y in best_tiles:
        if marked_maze[x][y] == '.':
            marked_maze[x][y] = 'O'
    return "\n".join("".join(row) for row in marked_maze)

# Example usage
with open("input") as f:
    input_data = f.read()

maze, start, end = parse_maze(input_data)
best_tiles = find_best_tiles(maze, start, end)
marked_maze = mark_best_tiles(maze, best_tiles)

print("Number of tiles on best paths:", len(best_tiles))
# Uncomment to see the marked maze
# print("Marked maze:")
# print(marked_maze)
