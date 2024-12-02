with open("input", 'r') as file:
    lines = file.readlines()

reports = []
safe = 0
for line in lines:
    values = list(map(int, line.split())) # better to use this, because already changed to int
    reports.append(values)

# print(reports)
def is_safe(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

# We're adding this function to check, if removing one level makes the report safe
def is_safe_dampener(report):
    for i in range(len(report)):
        report_mod = report[:i] + report[i+1:]
        if is_safe(report_mod):
            return True
    return False

for report in reports:
    if is_safe(report) or is_safe_dampener(report):
        safe += 1

print(safe)