import regex as re
from collections import defaultdict


def process_operation(operation: str):
    captures = re.search(r'(\w+)([-=]{1})(\d*)', operation)
    return captures.groups()


def get_hash_value(string: str):
    current = 0
    for i in string:
        current += ord(i)
        current *= 17
        current = current % 256
    return current


def get_focusing_power(lenses: defaultdict[int, dict[str, int]]):
    total_focusing_power = 0

    for box_num, box_lenses in lenses.items():
        for slot_num, (_, focal_length) in enumerate(box_lenses.items()):
            total_focusing_power += (box_num + 1) * (slot_num + 1) * focal_length
    
    return total_focusing_power


def main():
    with open("input.txt", "r") as f:
        lines = f.read().strip()
        strings = lines.split(',')

    print(sum(map(get_hash_value, strings)))

    lenses = defaultdict(dict)
    operations = list(map(process_operation, strings))

    for label, command, focal_length in operations:
        box = get_hash_value(label)
        if command == '=':
            lenses[box][label] = int(focal_length)
        else:
            lenses[box].pop(label, None)
    
    print(get_focusing_power(lenses))
    return

main()
