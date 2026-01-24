import sympy as sp
import csv

def lowest_prime_factor(n):
    """Return the lowest prime factor of n."""
    if n < 2:
        return 1
    return min(sp.factorint(n).keys())

def generate_prime_skyline(N, filename="prime_skyline.csv"):
    """
    Generate coordinates for primes only, using the full Factor Stair walk.
    x accumulates; y resets each step.
    """
    x = 1
    y = 1

    prime_rows = []

    # number 1 is not prime, but we start at (1,1)
    for n in range(2, N + 1):
        if sp.isprime(n):
            x += 1
            y = n
            prime_rows.append((n, x, y))
        else:
            lpf = lowest_prime_factor(n)
            x += lpf
            y = n // lpf

    # write CSV
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["prime", "x", "y"])
        writer.writerows(prime_rows)

    return prime_rows


# Example usage:
prime_coords = generate_prime_skyline(1000)
for row in prime_coords[:10]:
    print(row)
