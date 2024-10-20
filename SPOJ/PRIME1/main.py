# Segmented Sieve Algorithm method (sieve of erathostenes won't work here, because of the large ranges)

import math

def simple_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [num for num, prime in enumerate(is_prime) if prime]

# Function to implement the segmented sieve for finding primes in range [m, n]
def segmented_sieve(m, n, primes):
    is_prime_range = [True] * (n - m + 1)

    for prime in primes:
        start = max(prime * prime, (m + prime - 1) // prime * prime)

        for j in range(start, n + 1, prime):
            is_prime_range[j - m] = False

    if m == 1:
        is_prime_range[0] = False

    return [m + i for i in range(n - m + 1) if is_prime_range[i]]

def main():
    t = int(input())  

    test_cases = []
    for _ in range(t):
        m, n = map(int, input().split())
        test_cases.append((m, n))

    max_n = max(n for _, n in test_cases)
    limit = int(math.sqrt(max_n)) + 1

    primes = simple_sieve(limit)

    for m, n in test_cases:
        primes_in_range = segmented_sieve(m, n, primes)
        print("\n".join(map(str, primes_in_range)))
        if test_cases.index((m, n)) != len(test_cases) - 1:
            print()  

if __name__ == "__main__":
    main()
