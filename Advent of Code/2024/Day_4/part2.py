with open("input.txt", 'r') as file:
    grid = [line.strip() for line in file.readlines()]

def count_X_mas(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [
        [(-1, -1), (0, 0), (1, 1)],  # Top-left to bottom-right
        [(-1, 1), (0, 0), (1, -1)]   # Top-right to bottom-left
    ]
    patterns = ["MAS", "SAM"]

    def matches_pattern(x, y, diagonal):
        for pattern in patterns:
            if all(0 <= x + dx < rows and 0 <= y + dy < cols and grid[x + dx][y + dy] == char 
                   for (dx, dy), char in zip(diagonal, pattern)):
                return True
        return False

    return sum(
        grid[x][y] == 'A' and matches_pattern(x, y, directions[0]) and matches_pattern(x, y, directions[1])
        for x in range(1, rows - 1) for y in range(1, cols - 1)
    )

print(count_X_mas(grid))
