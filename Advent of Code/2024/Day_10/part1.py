def parse_map(lines):
    return [list(map(int, line.strip())) for line in lines]

def find_trailheads(topomap):
    trailheads = []
    for r, row in enumerate(topomap):
        for c, val in enumerate(row):
            if val == 0:
                trailheads.append((r, c))
    return trailheads

def is_valid_move(topomap, current_height, r, c):
    return (
        0 <= r < len(topomap) and
        0 <= c < len(topomap[0]) and
        topomap[r][c] == current_height + 1
    )

def calculate_trailhead_score(topomap, trailhead):
    queue = [trailhead]
    visited = set()
    scores = set()
    
    while queue:
        r, c = queue.pop(0)
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        current_height = topomap[r][c]
        if current_height == 9:
            scores.add((r, c))
            continue
        
        # dfs my beloved
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if is_valid_move(topomap, current_height, nr, nc):
                queue.append((nr, nc))
    
    return len(scores)

def calculate_total_score(lines):
    topomap = parse_map(lines)
    trailheads = find_trailheads(topomap)
    total_score = 0
    
    for trailhead in trailheads:
        total_score += calculate_trailhead_score(topomap, trailhead)
    
    return total_score

with open("input", 'r') as file:
    lines = file.readlines()

total_score = calculate_total_score(lines)
print(total_score)
