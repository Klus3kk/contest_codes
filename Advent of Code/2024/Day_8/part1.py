def parse_map(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    antennas = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char != '.':
                antennas.append((x, y, char))
    return antennas, len(lines), len(lines[0].strip())

def calculate_antinodes(antennas, width, height):
    antinodes = set()
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            x1, y1, f1 = antennas[i]
            x2, y2, f2 = antennas[j]
            if f1 == f2:
                # Calculate the midpoint and delta
                dx, dy = x2 - x1, y2 - y1
                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)
                # Check bounds
                if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                    antinodes.add(antinode2)
    return antinodes

def main():
    antennas, height, width = parse_map("input")
    antinodes = calculate_antinodes(antennas, width, height)
    print(f"Total unique antinodes: {len(antinodes)}")

if __name__ == "__main__":
    main()
