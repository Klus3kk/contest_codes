import re
import math
import cmath


def solve_quadratic_equation(a, b, c):
    d = (b ** 2) - (4 * a * c)
    root_1 = (-b - cmath.sqrt(d)) / (2 * a)
    root_2 = (-b + cmath.sqrt(d)) / (2 * a)
    solutions = sorted([root_1.real, root_2.real])
    return math.ceil(solutions[0]), math.floor(solutions[1])


def part_one():
    with open("input.txt", "r") as input_file:
        data = list(zip(*[[int(n) for n in re.findall(r'\d+', line)]
                          for line in input_file.read().splitlines()]))    
    result = math.prod([len(range(a, b+1))
                        for a, b in [solve_quadratic_equation(-1, race_time, -distance)
                                     for race_time, distance in data]])
    print(f"part_one: {result}")


def part_two():
    with open("input.txt", "r") as input_file:
        data = tuple([int(''.join([n for n in re.findall(r'\d+', line)]))
                      for line in input_file.read().splitlines()])
    race_time, distance = data
    a, b = solve_quadratic_equation(-1, race_time, -distance)
    print(f"part_two: {len(range(a, b+1))}")
    
print(part_one())
print(part_two())