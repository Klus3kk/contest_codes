from heapq import heappop, heappush

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

def find_lowest_score(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    start_state = (*start, 0)  # Start at (x, y) facing East (0)
    pq = [(0, start_state)]  # Priority queue: (cost, state)
    visited = set()

    while pq:
        cost, (x, y, direction) = heappop(pq)

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        # Check if we reached the end
        if (x, y) == end:
            return cost

        # Move forward
        dx, dy = DIRS[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
            heappush(pq, (cost + 1, (nx, ny, direction)))

        # Rotate clockwise
        new_dir = (direction + 1) % 4
        heappush(pq, (cost + 1000, (x, y, new_dir)))

        # Rotate counterclockwise
        new_dir = (direction - 1) % 4
        heappush(pq, (cost + 1000, (x, y, new_dir)))

    return float('inf')  # Should not reach here

# Example usage
with open("input") as f:
    input_data = f.read()

maze, start, end = parse_maze(input_data)
lowest_score = find_lowest_score(maze, start, end)
print(lowest_score)
