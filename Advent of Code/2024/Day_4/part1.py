# hate this problem, worst one yet
with open ("input.txt", 'r') as file:
    lines = file.readlines()

grid = [line.strip() for line in lines]

def count_xmas(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-Right
        (-1, -1), # Up-Left
        (1, -1),  # Down-Left
        (-1, 1)   # Up-Right
    ]

    def is_valid(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy 
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != word[i]:
                return False 
        return True 
    
    count = 0

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_valid(x ,y, dx, dy):
                    count += 1

    return count 

print(count_xmas(grid))