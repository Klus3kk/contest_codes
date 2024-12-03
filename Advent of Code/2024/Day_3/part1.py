import re

with open("input", 'r') as file:
    lines = file.readlines()

# print(lines)

pattern = r"mul\((\d+),(\d+)\)"
result = 0

for line in lines:
    matches = re.findall(pattern, line)
    for match in matches:
        x, y = map(int, match)
        result += x * y 

print(result) 