with open("input", 'r') as file:
    lines = file.readlines()

reports = []
safe = 0
for line in lines:
    values = list(map(int, line.split())) # better to use this, because already changed to int
    reports.append(values)

# print(reports)
def is_safe(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1)) # if everything is true, great function
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

for report in reports:
    if is_safe(report):
        safe += 1

print(safe)