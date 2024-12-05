def parse_input(lines):
    sections = ''.join(lines).strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(','))) for line in sections[1].splitlines()]
    return rules, updates


def is_valid(update, rules):
    for x, y in rules:
        if x in update and y in update and update.index(x) > update.index(y):
            return False
    return True


def sum_middle_pages(rules, updates):
    valid_updates = []
    for update in updates:
        if is_valid(update, rules):
            valid_updates.append(update)
    
    middle_sum = 0
    for update in valid_updates:
        middle_page = update[len(update) // 2]
        middle_sum += middle_page
    return middle_sum


with open("input.txt", 'r') as file:
    lines = file.readlines()


rules, updates = parse_input(lines)
result = sum_middle_pages(rules, updates)
print(result)
