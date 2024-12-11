def parse_map(lines):
    return [list(map(int, line.strip())) for line in lines]

def find_trailheads(topomap):
    trailheads = []
    for r, row in enumerate(topomap):
        for c, val in enumerate(row):
            if val == 0:
                trailheads.append((r, c))
    return trailheads

def count_trails(topomap, start):
    def dfs(r, c, current_height):
        if not (0 <= r < len(topomap) and 0 <= c < len(topomap[0])):
            return 0
        if topomap[r][c] != current_height:
            return 0
        if current_height == 9:
            return 1  

        visited.add((r, c))

        trails = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited:
                trails += dfs(nr, nc, current_height + 1)

        visited.remove((r, c))
        return trails

    visited = set()
    return dfs(start[0], start[1], 0)

def calculate_total_rating(lines):
    topomap = parse_map(lines)
    trailheads = find_trailheads(topomap)
    total_rating = 0

    for trailhead in trailheads:
        total_rating += count_trails(topomap, trailhead)

    return total_rating

with open("input", 'r') as file:
    lines = file.readlines()

total_rating = calculate_total_rating(lines)
print(total_rating)
