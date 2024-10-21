# Shunting-yard algorithm

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_rpn(expression):
    stack = []
    result = []
    
    for char in expression:
        if char.isalpha():  # Operand (letter)
            result.append(char)
        elif char == '(':  # Left parenthesis
            stack.append(char)
        elif char == ')':  # Right parenthesis
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  
        else:  # Operator
            while (stack and precedence(stack[-1]) > precedence(char)) or \
                  (char != '^' and stack and precedence(stack[-1]) == precedence(char)):
                result.append(stack.pop())
            stack.append(char)

    # Pop all the operators left in the stack
    while stack:
        result.append(stack.pop())
    
    return ''.join(result)

def main():
    t = int(input())  
    for _ in range(t):
        expression = input().strip()
        print(infix_to_rpn(expression))

if __name__ == "__main__":
    main()
