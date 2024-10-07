import re
import math
input = [line for line in open("input.txt")]
BOUNDS = {
        'red': 12,
        'green': 13,
        'blue': 14,
        }

def part1():
    sum = 0
    for line in input:
        is_valid = True

        for c in BOUNDS:
            largest_val = max([int(i) for i in re.findall(f'([0-9]+) {c}', line)])
            if BOUNDS[c] < largest_val:
                is_valid = False

        if is_valid:
            sum += int(re.findall('Game ([0-9]+)', line)[0])

    return sum

def part2():
    sum = 0
    for line in input:
        current = {}

        for c in BOUNDS:
            current[c] = max([int(i) for i in re.findall(f'([0-9]+) {c}', line)])
        sum += math.prod(current.values())
    return sum

print(part1())
print(part2())