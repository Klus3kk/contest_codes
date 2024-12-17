# Read input values
with open("input") as f:
    lines = f.read().splitlines()

# Extract register and program information
registers = {}
program = []
for line in lines:
    if line.startswith("Register A"):
        registers['A'] = int(line.split(": ")[1])
    elif line.startswith("Register B"):
        registers['B'] = int(line.split(": ")[1])
    elif line.startswith("Register C"):
        registers['C'] = int(line.split(": ")[1])
    elif line.startswith("Program"):
        program = list(map(int, line.split(": ")[1].split(",")))

# Initialize instruction pointer and output
ip = 0
output = []

# Define combo operand values
def combo_value(operand, registers):
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']
    elif operand == 7:
        raise ValueError("Invalid combo operand 7")

# Execute the program
while ip < len(program):
    opcode = program[ip]
    operand = program[ip + 1]

    if opcode == 0:  # adv
        registers['A'] //= 2 ** combo_value(operand, registers)
    elif opcode == 1:  # bxl
        registers['B'] ^= operand
    elif opcode == 2:  # bst
        registers['B'] = combo_value(operand, registers) % 8
    elif opcode == 3:  # jnz
        if registers['A'] != 0:
            ip = operand
            continue
    elif opcode == 4:  # bxc
        registers['B'] ^= registers['C']
    elif opcode == 5:  # out
        output.append(combo_value(operand, registers) % 8)
    elif opcode == 6:  # bdv
        registers['B'] = registers['A'] // (2 ** combo_value(operand, registers))
    elif opcode == 7:  # cdv
        registers['C'] = registers['A'] // (2 ** combo_value(operand, registers))
    else:
        raise ValueError(f"Unknown opcode {opcode}")

    ip += 2

# Output the result
print(",".join(map(str, output)))
