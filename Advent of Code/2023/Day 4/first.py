input = open("input.txt").read().strip()
lines = input.split('\n')

part1 = 0
matching_nums = []
for i, line in enumerate(lines):
    line = line.split(':')[1].strip()
    winning_nums = set(line.split('|')[0].strip().split())
    nums_i_have = set(line.split('|')[1].strip().split())
    matching_nums.append(len(winning_nums.intersection(nums_i_have)))
    part1 += int(2**(matching_nums[i]-1))
print(part1)

scratchcard_nums = {i: 1 for i in range(1, len(lines) + 1)}
part2 = 0
for i in range(1, len(lines) + 1):
    for j in range(scratchcard_nums[i]):
        for k in range(i+1, i+matching_nums[i-1]+1):
            scratchcard_nums[k] += 1
    part2 += scratchcard_nums[i]
    
print(part2)