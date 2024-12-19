def count_possible_designs_and_arrangements_from_file(file_path):
    # Read input from file
    with open(file_path, 'r') as f:
        input_data = f.read()

    # Split input into patterns and designs
    sections = input_data.strip().split("\n\n")
    towel_patterns = sections[0].split(", ")
    designs = sections[1].split("\n")

    def count_arrangements(design, patterns):
        n = len(design)
        dp = [0] * (n + 1)
        dp[0] = 1  

        for i in range(1, n + 1):
            for pattern in patterns:
                if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                    dp[i] += dp[i - len(pattern)]

        return dp[n]

    # Count the total number of arrangements for all designs
    total_arrangements = sum(count_arrangements(design, towel_patterns) for design in designs)
    return total_arrangements

file_path = "input"
result = count_possible_designs_and_arrangements_from_file(file_path)
print(f"Total number of arrangements: {result}")
