# Difference array (+1 -1 trick)
def maximum_sum(n, q, a, queries):
    # Initialize frequency array to zero
    freq = [0] * (n + 1)

    # Process each query with the +1 -1 trick
    for l, r in queries:
        freq[l - 1] += 1  # increment at the start of the range
        if r < n:
            freq[r] -= 1  # decrement just after the end of the range

    # Calculate the prefix sums for the frequency array
    for i in range(1, n):
        freq[i] += freq[i - 1]

    # Remove the extra element from the frequency array
    freq = freq[:n]

    # Sort the array and the frequency array
    a.sort()
    freq.sort()

    # Calculate the maximum sum by multiplying corresponding elements
    max_sum = sum(a[i] * freq[i] for i in range(n))

    return max_sum

# Input
n, q = map(int, input().split())
a = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Calculate and print the maximum sum
print(maximum_sum(n, q, a, queries))
