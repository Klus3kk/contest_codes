from itertools import product
# prode
def concatenate(a, b):
    return int(f"{a}{b}")

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = concatenate(result, numbers[i + 1])
    return result

def solve_calibration(file_path):
    total = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        target, nums = line.split(': ')
        target = int(target)
        numbers = list(map(int, nums.split()))
        n = len(numbers)
        
        possible_operators = product(['+', '*', '||'], repeat=n-1)
        
        for operators in possible_operators:
            if evaluate_expression(numbers, operators) == target:
                total += target
                break  
    return total

result = solve_calibration("input")
print(result)
