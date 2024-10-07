from heapq import heapify, heappush, heappop

with open("input.txt", "r") as file:
    data = file.read().splitlines()
    ln, steps, cycle, seen, even, odd, n = len(data), 0, [], set(), set(), set(), 26501365
    grid = {(x, y) : data[y][x] for x in range(ln) for y in range(ln)}
    heapify(queue := [(steps, next((k for k, v in grid.items() if v == "S")))])
    while queue:
        new_steps, (x, y) = heappop(queue)
        if (x, y) in seen: 
            continue
        seen.add((x, y))
        if new_steps != steps:
            if steps == 64: 
                p1 = len(even)
            if steps % (ln * 2) == n % (ln * 2):
                if len(cycle := cycle + [len([even, odd][steps % 2])]) == 3:
                    p2, offset, increment = cycle[0], cycle[1] - cycle[0],  (cycle[2] - cycle[1]) - (cycle[1] - cycle[0])
                    for x in range(n // (ln * 2)):
                        p2 += offset
                        offset += increment
                    break
        steps, next_steps = new_steps, new_steps + 1
        for a, b in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if grid[a % ln, b % ln] != "#":
                if not next_steps % 2: 
                    even.add((a, b))
                else:                  
                    odd.add((a, b))
                heappush(queue, (next_steps, (a, b)))
    print(p1, p2)