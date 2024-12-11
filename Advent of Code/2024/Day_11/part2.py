from collections import Counter, deque

def process_stones_optimized(stones, blinks):
    stone_counts = Counter(stones)  
    for _ in range(blinks):
        new_stone_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:  
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_stone_counts[left] += count
                new_stone_counts[right] += count
            else:
                new_stone_counts[stone * 2024] += count
        stone_counts = new_stone_counts
    return sum(stone_counts.values())

with open("input", 'r') as file:
    lines = file.readlines()

initial_stones = list(map(int, lines[0].split()))

result = process_stones_optimized(initial_stones, 75)

print(result)
