from collections import deque

def calculate_price(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    total_price = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(start_row, start_col):
        queue = deque([(start_row, start_col)])
        visited[start_row][start_col] = True
        plant_type = grid[start_row][start_col]
        area = 0
        perimeter = 0

        while queue:
            row, col = queue.popleft()
            area += 1
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == plant_type and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                    elif grid[nr][nc] != plant_type:
                        perimeter += 1
                else:
                    perimeter += 1  

        return area, perimeter

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                area, perimeter = bfs(r, c)
                total_price += area * perimeter

    return total_price

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

print(calculate_price(lines))
