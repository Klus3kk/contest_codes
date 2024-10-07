from heapq import heappop, heappush
ll = [[int(y) for y in x] for x in open('input.txt').read().strip().split('\n')]
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def inr(pos, arr):
	return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))
def run(mindist, maxdist):
	# cost, x, y, disallowedDirection
	q = [(0, 0, 0, -1)]
	seen = set()
	costs = {}
	while q:
		cost, x, y, dd = heappop(q)
		if x == len(ll) - 1 and y == len(ll[0]) - 1: # goal x, goal y
			return cost
		if (x, y, dd) in seen:
			continue
		seen.add((x, y, dd))
		for direction in range(4):
			costincrease = 0
			if direction == dd or (direction + 2) % 4 == dd:
				# can't go this way
				continue
			for distance in range(1, maxdist + 1):
				xx = x + DIRS[direction][0] * distance
				yy = y + DIRS[direction][1] * distance
				if inr((xx, yy), ll):
					costincrease += ll[xx][yy]
					if distance < mindist:
						continue
					nc = cost + costincrease
					if costs.get((xx, yy, direction), 1e100) <= nc:
						continue
					costs[(xx, yy, direction)] = nc
					heappush(q, (nc, xx, yy, direction))

print(run(1, 3))
print(run(4, 10))