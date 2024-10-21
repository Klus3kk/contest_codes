import sys

def is_all_nines(s):
    return all(c == '9' for c in s)

def next_palindrome(num):
    n = len(num)
    if is_all_nines(num):
        return '1' + '0' * (n - 1) + '1'
    
    # Split the number into two halves
    if n % 2 == 0:
        left_half = num[:n//2]
        right_half = num[n//2:]
        middle = ''
    else:
        left_half = num[:n//2]
        middle = num[n//2]
        right_half = num[n//2+1:]
    
    # Generate the mirrored palindrome
    if middle:
        candidate = left_half + middle + left_half[::-1]
    else:
        candidate = left_half + left_half[::-1]
    
    # If the candidate is greater than num, return it
    if candidate > num:
        return candidate
    
    # Otherwise, increment the left half (and middle if odd)
    if middle:
        left_and_middle = left_half + middle
        incremented = str(int(left_and_middle) + 1)
        new_left_half = incremented[:-1]
        new_middle = incremented[-1]
        return new_left_half + new_middle + new_left_half[::-1]
    else:
        new_left_half = str(int(left_half) + 1)
        return new_left_half + new_left_half[::-1]

def main():
    t = int(input().strip())  # Read the number of test cases
    results = []
    
    for _ in range(t):
        num = input().strip()  # Read each number as a string
        results.append(next_palindrome(num))
    
    # Output all results at once
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
