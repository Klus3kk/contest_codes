def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    robots = []
    for line in lines:
        line = line.strip()
        pos_part, vel_part = line.split(' ')
        px, py = map(int, pos_part[2:].split(','))
        vx, vy = map(int, vel_part[2:].split(','))
        robots.append(((px, py), (vx, vy)))
    return robots

def move_robot(position, velocity, width, height):
    px, py = position
    vx, vy = velocity
    new_px = (px + vx) % width
    new_py = (py + vy) % height
    return new_px, new_py

def simulate_robots(robots, seconds, width, height):
    for _ in range(seconds):
        robots = [(move_robot(pos, vel, width, height), vel) for pos, vel in robots]
    return robots

def count_quadrants(robots, width, height):
    mid_x, mid_y = width // 2, height // 2
    quadrants = [0, 0, 0, 0]  # top-left, top-right, bottom-left, bottom-right

    for (px, py), _ in robots:
        if px == mid_x or py == mid_y:
            continue  
        if px < mid_x and py < mid_y:
            quadrants[0] += 1
        elif px >= mid_x and py < mid_y:
            quadrants[1] += 1
        elif px < mid_x and py >= mid_y:
            quadrants[2] += 1
        elif px >= mid_x and py >= mid_y:
            quadrants[3] += 1

    return quadrants

def calculate_safety_factor(quadrants):
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count
    return safety_factor

if __name__ == "__main__":
    input_file = "input"  
    width, height = 101, 103
    seconds = 100

    robots = parse_input(input_file)
    robots = simulate_robots(robots, seconds, width, height)
    quadrants = count_quadrants(robots, width, height)
    safety_factor = calculate_safety_factor(quadrants)

    print(safety_factor)
