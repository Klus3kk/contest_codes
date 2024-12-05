from collections import defaultdict, deque
# topological sort, i hate this problem :/

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


def reorder(update, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages_in_update = set(update)

    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree[x] = in_degree.get(x, 0)  

    queue = deque([page for page in update if in_degree[page] == 0])
    ordered = []

    while queue:
        current = queue.popleft()
        ordered.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered if len(ordered) == len(update) else update


def sum_middle_pages(rules, updates):
    total = 0
    for update in updates:
        if not is_valid(update, rules):
            reordered = reorder(update, rules)
            total += reordered[len(reordered) // 2]
    return total


with open("input.txt", 'r') as file:
    lines = file.readlines()


rules, updates = parse_input(lines)
result = sum_middle_pages(rules, updates)
print(result)
