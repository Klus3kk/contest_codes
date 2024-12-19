def count_possible_designs(input_data):
    # Split input into patterns and designs
    sections = input_data.strip().split("\n\n")
    towel_patterns = sections[0].split(", ")
    designs = sections[1].split("\n")

    def can_form_design(design, patterns):
        n = len(design)
        dp = [False] * (n + 1)
        dp[0] = True 

        for i in range(1, n + 1):
            for pattern in patterns:
                if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                    dp[i] = dp[i] or dp[i - len(pattern)]

        return dp[n]

    # Count designs that can be formed
    possible_count = sum(can_form_design(design, towel_patterns) for design in designs)
    return possible_count

# Read input from file
with open('input', 'r') as f:
    input_data = f.read()

result = count_possible_designs(input_data)
print(f"Number of possible designs: {result}")
