import sympy as sp
import csv

def lowest_prime_factor(n):
    """Return the lowest prime factor of n."""
    if n < 2:
        return 1
    return min(sp.factorint(n).keys())

def generate_factor_stairs(N, filename="factor_stairs.csv"):
    """
    Generate coordinates for numbers 1..N using:
      - x accumulates by 1 for primes, or by lpf(n) for composites
      - y = n for primes
      - y = n / lpf(n) for composites
    """
    x = 1
    y = 1
    coords = [(1, x, y)]  # number 1 is given (1,1)

    for n in range(2, N + 1):
        if sp.isprime(n):
            x += 1
            y = n
        else:
            lpf = lowest_prime_factor(n)
            x += lpf
            y = n // lpf

        coords.append((n, x, y))

    # write CSV
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["number", "x", "y"])
        writer.writerows(coords)

    return coords


# Example usage:
coords = generate_factor_stairs(1000)
for row in coords[:10]:
    print(row)
