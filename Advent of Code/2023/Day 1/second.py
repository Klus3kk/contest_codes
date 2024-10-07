import re

number_map = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

f = open("input.txt").read().strip()
for k, v in number_map.items():
    f = f.replace(k, v)

total = 0
for line in f.split("\n"):
    found = re.findall(r'\d', line)
    number_as_string = found[0] + found[-1]
    total += int(number_as_string)

print(total)