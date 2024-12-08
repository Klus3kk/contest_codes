def parse_map(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    antennas = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char != '.':
                antennas.append((x, y, char))
    return antennas, len(lines), len(lines[0].strip())

def calculate_antinodes_with_resonant_harmonics(antennas, width, height):
    from collections import defaultdict

    antinodes = set()
    frequency_map = defaultdict(list)

    # Group antennas by frequency
    for x, y, freq in antennas:
        frequency_map[freq].append((x, y))

    for freq, positions in frequency_map.items():
        # Add antinodes for each pair of antennas with the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Add the two antennas' positions as antinodes
                antinodes.add((x1, y1))
                antinodes.add((x2, y2))

                # Add all positions in line with the antennas
                dx, dy = x2 - x1, y2 - y1
                gcd = abs(__import__("math").gcd(dx, dy))
                dx, dy = dx // gcd, dy // gcd  # Normalize the direction vector

                # Move in both directions along the line
                k = 1
                while True:
                    nx, ny = x1 - k * dx, y1 - k * dy
                    if 0 <= nx < width and 0 <= ny < height:
                        antinodes.add((nx, ny))
                    else:
                        break
                    k += 1

                k = 1
                while True:
                    nx, ny = x2 + k * dx, y2 + k * dy
                    if 0 <= nx < width and 0 <= ny < height:
                        antinodes.add((nx, ny))
                    else:
                        break
                    k += 1

    return antinodes

def main():
    antennas, height, width = parse_map("input")
    antinodes = calculate_antinodes_with_resonant_harmonics(antennas, width, height)
    print(f"Total unique antinodes: {len(antinodes)}")

if __name__ == "__main__":
    main()
