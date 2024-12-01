with open("input", 'r') as file:
    lines = file.readlines()

sum = 0
columns1 = []
columns2 = []

for line in lines:
    values = line.split()
    columns1.append(int(values[0]))
    columns2.append(int(values[1]))

columns1.sort()
columns2.sort()

for i in range(len(columns1)):
    sum += abs(columns1[i] - columns2[i])

# print(columns1)
# print(columns2)
print(sum)    
