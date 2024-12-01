from collections import Counter

with open("input", 'r') as file:
    lines = file.readlines()

columns1 = []
columns2 = []

for line in lines:
    values = line.split()
    columns1.append(int(values[0]))
    columns2.append(int(values[1]))

count = Counter(columns2)
# print(count)

similarity_score = sum(num * count[num] for num in columns1)
print(similarity_score)    
