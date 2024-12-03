import re

with open("input", 'r') as file:
    lines = file.readlines()

result = 0
mul_enabled = True

# regex my beloved
pattern = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"

for line in lines:
    instructions = re.finditer(pattern, line)
    
    for instruction in instructions:
        match = instruction.group(1)  
        if match == "do()":
            mul_enabled = True
        elif match == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                x, y = map(int, instruction.groups()[1:])
                result += x * y

print(result)
