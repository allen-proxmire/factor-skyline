# The Möbius Function and Möbius Randomness in FS-Geometry

---

## Overview

The Möbius function mu(n) is defined by:

    mu(n) = { 1          if n = 1
            { (-1)^k     if n is a product of k distinct primes
            { 0          if n is divisible by p^2 for some prime p

It encodes the "parity of the prime factorization" for squarefree integers and vanishes on square-divisible integers. The cumulative sum M(x) = sum_{n<=x} mu(n), the Mertens function, is one of the most studied objects in analytic number theory. Its behavior is intimately connected to the Riemann Hypothesis: RH is equivalent to M(x) = O(x^{1/2 + epsilon}) for every epsilon > 0.

In the Factor Skyline, the Möbius function partitions the integers into three geometric classes — escapes, multi-layer composites, and activation-contaminated integers — and the near-cancellation of M(x) becomes a statement about the geometric anti-alignment of these classes.

---

## 1. The Möbius Function as an FS Structural Classifier

### 1.1. The three classes

Every integer n >= 2 falls into exactly one of three FS-geometric classes:

**Class E: Escapes (primes).** mu(p) = -1 for all primes p.
- FS signature: dx = 1, y_FS = p.
- These are columns with width 1 — escape events in the skyline.
- Omega(p) = 1 (one prime factor), so mu = (-1)^1 = -1.
- Contribution to M(x): always negative.

**Class S+: Squarefree composites with even omega.** mu(n) = +1.
- Examples: 6 = 2*3, 10 = 2*5, 15 = 3*5, 35 = 5*7.
- FS signature: dx = lpf(n), y_FS = n/lpf(n). These are covered columns with two or more distinct width layers.
- Omega(n) is even (2, 4, 6, ...), so mu = (-1)^{even} = +1.
- Contribution to M(x): always positive.

**Class S-: Squarefree composites with odd omega >= 3.** mu(n) = -1.
- Examples: 30 = 2*3*5, 42 = 2*3*7, 66 = 2*3*11.
- FS signature: same as S+, but with an odd number of distinct prime factors.
- Omega(n) is odd >= 3, so mu = (-1)^{odd} = -1.
- Contribution to M(x): always negative.

**Class Z: Square-divisible integers.** mu(n) = 0.
- Examples: 4, 8, 9, 12, 16, 18, 20, 25, 27, ...
- FS signature: these are columns whose factorization includes a repeated prime — they have been "hit twice" by the same width layer.
- They are invisible to M(x): they contribute nothing to the Mertens function.

### 1.2. The FS classification table

For n = 1 to 50, the classification reveals the interleaving:

```
n:  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 ...
mu: 1 -1 -1  0 -1  1 -1  0  0  1 -1  0 -1  1  1 ...
    U  E  E  Z  E  S+ E  Z  Z  S+ E  Z  E  S+ S+ ...
```

The sequence alternates between escapes (mu = -1), squarefree composites (mu = +/- 1), and square-divisible integers (mu = 0). The mu = 0 class occupies fraction 1 - 6/pi^2 ~ 0.392 of all integers; the squarefree integers occupy 6/pi^2 ~ 0.608.

### 1.3. Densities of the three contributing classes

Among the squarefree integers, the split between mu = +1 and mu = -1 is nearly equal:

| x      | mu = -1 count | mu = +1 count | mu = 0 count | Squarefree fraction |
|--------|--------------|--------------|-------------|---------------------|
| 1000   | 303          | 305          | 392         | 0.608               |
| 10000  | 3053         | 3030         | 3917        | 0.608               |

The mu = -1 and mu = +1 counts are nearly identical (differing by O(sqrt(x))), which is why M(x) stays small.

---

## 2. Squarefree Structure in FS-Width Layers

### 2.1. Squarefree = no repeated width

An integer n is squarefree if and only if no prime appears more than once in its factorization. In FS-geometry, the factorization is the column's recursive width decomposition:

- n = lpf(n) * (n/lpf(n))
- n/lpf(n) = lpf(n/lpf(n)) * ...
- continuing until a prime is reached

The integer n is squarefree when each width in this decomposition appears at most once. A square-divisible integer has a **repeated width** — some prime p appears at two or more levels of the column's recursive structure.

### 2.2. Square-divisible integers and activation geometry

Square-divisible integers are those divisible by p^2 for some prime p. In the FS ontology, p^2 is the activation threshold for width-p. An integer divisible by p^2 has been "activated upon twice" — it carries a structural redundancy where the same width layer has claimed it at two levels.

The density of square-divisible integers is 1 - 6/pi^2 ~ 0.3917. This is the fraction of the skyline's columns that carry repeated width structure. These columns are "structurally redundant" in the sense that mu assigns them weight 0: they contribute nothing to the Möbius sum because their factorizations contain architectural repetitions.

### 2.3. The Euler product for squarefree density

The fraction of squarefree integers is:

    prod_{p prime} (1 - 1/p^2) = 1/zeta(2) = 6/pi^2

In FS-geometry, this is the probability that a random integer avoids all activation-squared events: for each prime p, the probability of not being divisible by p^2 is (1 - 1/p^2), and these events are independent (CRT). The product converges to 6/pi^2.

This is a **second-order escape density**: just as D(p) = prod(1 - 1/q) measures the fraction escaping all first-order coverage, the squarefree density prod(1 - 1/q^2) measures the fraction escaping all second-order (square) coverage.

---

## 3. Möbius Cancellation as Geometric Anti-Alignment

### 3.1. The three-way decomposition of M(x)

The Mertens function decomposes as:

    M(x) = mu(1) + sum_{p <= x} mu(p) + sum_{sqfree composites n <= x} mu(n)
         = 1 + (-pi(x)) + (N_even(x) - N_odd(x))

where:
- pi(x) = number of primes <= x (each contributing mu = -1)
- N_even(x) = count of squarefree composites with even omega (each contributing mu = +1)
- N_odd(x) = count of squarefree composites with odd omega >= 3 (each contributing mu = -1)

Numerically:

| x      | Escape sum | Even-omega sum | Odd-omega sum | M(x)  | M/sqrt(x) |
|--------|-----------|----------------|---------------|-------|-----------|
| 1000   | -168      | +304           | -135          | +2    | +0.063    |
| 10000  | -1229     | +3029          | -1824         | -23   | -0.230    |
| 100000 | -9592     | +30372         | -20829        | -48   | -0.152    |

The three terms are individually large (thousands to tens of thousands) but nearly cancel to leave a tiny residual M(x) of order sqrt(x).

### 3.2. The cancellation mechanism

The near-cancellation has a precise FS-geometric structure:

**The escape contribution** (-pi(x) ~ -x/ln(x)) is large and negative. Primes are structurally pure — single-width columns — and all contribute mu = -1.

**The even-omega contribution** (+N_even ~ +x * c_even) is large and positive. These are columns with exactly 2, 4, 6, ... distinct widths in their recursive structure. The products of two distinct primes (semiprimes) dominate this class.

**The odd-omega contribution** (-N_odd ~ -x * c_odd) is large and negative. These are columns with 3, 5, 7, ... distinct widths. The products of three distinct primes (triprimes) dominate.

The cancellation occurs because:

    pi(x) + N_odd(x) ~ N_even(x) + 1

to within O(sqrt(x)). The escapes and odd-omega composites together nearly balance the even-omega composites. This is not coincidence — it is a consequence of the inclusion-exclusion structure that defines mu.

### 3.3. The geometric meaning of cancellation

In the skyline, the Möbius cancellation says: **the signed count of single-width, triple-width, quintuple-width, ... columns nearly equals the signed count of double-width, quadruple-width, sextuple-width, ... columns.**

Each width layer added to a column's structure flips the sign of mu. The near-balance between odd-layered and even-layered squarefree columns is a structural consequence of the symmetry of the inclusion-exclusion principle applied to independent coverage layers.

The CRT guarantees that width layers are independent. For each configuration of k active widths, the probability that all k hit a given integer is prod(1/q_i), and the sign alternates with k. The total signed probability telescopes to a product:

    sum_{k} (-1)^k * sum_{|S|=k} prod_{q in S} 1/q = prod_q (1 - 1/q) = D(p)

This is the escape density. The identity sum mu(n)/n = 0 over all integers reflects the complete cancellation of the Möbius signs when averaged over the full number line — the escape density from inclusion-exclusion exactly exhausts the signed coverage.

---

## 4. The Mertens Function as Cumulative Signed Height

### 4.1. Definition in FS terms

Define the FS-Möbius height of integer n:

    h_mu(n) = mu(n) * log(y_FS(n))    (the signed logarithmic height)

Wait — this overcomplicates things. The Mertens function M(x) = sum mu(n) is simpler: it is a cumulative count with signs. Let us define it directly in FS terms.

### 4.2. M(x) as a signed walk on the skyline

Walking along the skyline from n = 1 to n = x:

- At each escape event (prime p): take a step of -1.
- At each squarefree even-omega composite: take a step of +1.
- At each squarefree odd-omega composite (omega >= 3): take a step of -1.
- At each square-divisible integer: take a step of 0 (stand still).
- At n = 1: start at +1.

M(x) is the position of this signed walk at step x.

### 4.3. The walk's behavior

The walk oscillates near zero, with excursions of size O(sqrt(x)):

| x      | M(x)  | M/sqrt(x) |
|--------|-------|-----------|
| 10     | -1    | -0.316    |
| 100    | +1    | +0.100    |
| 1000   | +2    | +0.063    |
| 5000   | +2    | +0.028    |
| 10000  | -23   | -0.230    |

The ratio M(x)/sqrt(x) stays bounded, consistent with the Mertens conjecture (that |M(x)| < sqrt(x), now known to be false for very large x, but true for all computationally accessible x).

### 4.4. Connection to RH

The Riemann Hypothesis is equivalent to:

    M(x) = O(x^{1/2 + epsilon}) for every epsilon > 0

In FS-geometry, this says the signed walk's excursions are bounded by the activation horizon sqrt(x), up to logarithmic corrections. The three-way cancellation between escapes, even-omega composites, and odd-omega composites is tight enough that the residual never exceeds the square-root scale.

This is the same square-root bound that appears in the FS-RH analysis (see `FS_RH_analogue.md`): the activation horizon sqrt(x) is the natural scale at which the skyline's structural events can deviate from their predicted balance.

---

## 5. Structural Insights on Möbius Randomness

### 5.1. Why mu(n) looks random

The Möbius function passes numerous statistical tests for randomness: it appears uncorrelated, equidistributed between +1 and -1 (among squarefree integers), and its partial sums behave like a random walk.

The FS framework explains this apparent randomness as the superposition of independent structural effects:

**Each width layer acts independently.** Whether n is divisible by prime q is independent of whether n is divisible by prime r (CRT). The sign mu(n) = (-1)^{omega(n)} depends on the parity of the number of width layers hitting n, and this parity is determined by a sum of independent Bernoulli variables (each width layer hits or misses independently). The parity of a sum of independent variables is asymptotically unbiased — hence the 50/50 split between mu = +1 and mu = -1 among squarefree integers.

**The mu = 0 class creates "dead zones."** The square-divisible integers (mu = 0) interrupt the signed walk with flat stretches. These dead zones are not uniformly distributed — they cluster near multiples of small squares (4, 8, 9, 12, ...) — but their effect on M(x) is to slow the walk without biasing it.

**The correlation structure is short-range.** Adjacent integers share divisibility structure (e.g., n and n+1 are always coprime, so mu(n) and mu(n+1) have weak correlations). But these correlations decay rapidly with separation, and the long-range behavior of M(x) is dominated by the independent-layer structure.

### 5.2. The Möbius dichotomy: escape parity vs composite parity

Among the mu = -1 integers, there are two structurally distinct subclasses:

- **Escapes (primes):** omega = 1. These have mu = -1 because a single width layer is odd.
- **Odd-omega composites:** omega = 3, 5, 7, ... These have mu = -1 because an odd number (>= 3) of width layers is still odd.

The escape subclass contributes -pi(x) ~ -x/ln(x) to M(x). The odd-omega composite subclass contributes -N_odd(x) ~ -c*x.

At x = 100000:
- Escape contribution: -9592
- Odd-omega(>=3) contribution: -20829
- Total mu = -1: -30421

The composites dominate the primes by a factor of ~2 at this scale. As x grows, the ratio N_odd/pi(x) increases further (N_odd grows linearly, pi(x) sublinearly). The Möbius cancellation is increasingly a balance between squarefree even-omega and odd-omega composites, with the escape contribution becoming a smaller perturbation.

**FS insight:** At large scales, Möbius randomness is not about primes at all. It is about the balance between even-layered and odd-layered composite columns in the skyline. The primes (escapes) contribute a slowly growing negative bias, but the dominant cancellation is between two classes of composites.

### 5.3. The FS content of sum mu(n)/n^s = 1/zeta(s)

The Dirichlet series identity:

    sum_{n=1}^{inf} mu(n)/n^s = 1/zeta(s)

has a direct FS interpretation. The right side is:

    1/zeta(s) = prod_p (1 - 1/p^s)

This is the escape density product generalized to arbitrary s. At s = 1, it equals D(P) -> 0 (the corridor collapse). At s = 2, it equals 6/pi^2 (the squarefree density).

The identity says: **the Möbius function is the arithmetic inverse of the coverage architecture.** Where zeta counts all integers (with multiplicative weights), mu inverts the count, peeling off the coverage layers one by one through inclusion-exclusion. The escape density product D(p) is the real-part shadow of this inversion.

### 5.4. The Mertens conjecture and FS corridor limits

The original Mertens conjecture (|M(x)| < sqrt(x) for all x) was disproved by Odlyzko and te Riele in 1985, though the first counterexample is astronomically large.

In FS-geometry, the Mertens conjecture would mean that the signed walk never exceeds the activation horizon by even a constant factor. The disproof means the walk occasionally slightly exceeds this scale — the three-way cancellation is not quite perfect enough to stay within sqrt(x) at all times.

The weaker bound M(x) = O(x^{1/2+epsilon}) (equivalent to RH) says the excursions never exceed x^{1/2+epsilon}. In FS terms: the signed walk can briefly exceed the activation horizon but cannot permanently escape to a higher scale. The activation architecture controls the walk's excursions to within the square-root scale, with occasional logarithmic overshoots.

### 5.5. Möbius orthogonality as FS structural independence

The Möbius randomness conjecture (Sarnak's conjecture) asserts that mu(n) is orthogonal to every bounded deterministic sequence of zero topological entropy. In FS-geometry, this says:

> The signed classification of skyline columns (escape, even-layered, odd-layered, redundant) is independent of every "simple" pattern imposed on the integers.

The coverage architecture of the skyline — determined by the primes through activation, coverage, and escape — produces a classification that no simple deterministic rule can predict. The factorization parity of squarefree integers is, from the perspective of simple dynamical systems, indistinguishable from randomness.

This is the deepest form of Möbius randomness: the skyline's width-layer structure, despite being entirely deterministic, produces signed counts that are asymptotically uncorrelated with every low-complexity signal.

---

## 6. Summary

| Concept | Classical | FS-Geometry |
|---------|-----------|-------------|
| mu(n) = (-1)^{omega} | Factorization parity | Width-layer parity of squarefree columns |
| mu(n) = 0 | Square-divisible | Repeated width in recursive column structure |
| Escapes (primes) | mu = -1 | Single-width columns, always odd parity |
| Squarefree composites | mu = +/-1 | Multi-width columns, sign = (-1)^{number of widths} |
| M(x) = sum mu(n) | Mertens function | Signed walk on skyline: -1 at escapes, +/-1 at squarefree composites, 0 at square-divisible |
| M(x) = O(sqrt(x)) | Equivalent to RH | Walk bounded by activation horizon |
| Squarefree density 6/pi^2 | 1/zeta(2) | Second-order escape density: prod(1 - 1/p^2) |
| sum mu(n)/n^s = 1/zeta(s) | Dirichlet series identity | Möbius function inverts coverage architecture |
| Three-way cancellation | mu = -1, +1, 0 nearly balance | Escapes + odd-omega ~ even-omega composites to O(sqrt(x)) |
| Möbius randomness | Sarnak conjecture | Width-layer parity independent of all simple patterns |
| Dominant cancellation at large x | Not visible | Between even-omega and odd-omega composites (primes become subdominant) |

The Möbius function in the Factor Skyline is the signed parity of the width-layer count for each column. Squarefree columns alternate signs with each additional width layer; square-divisible columns are structurally redundant and contribute nothing. The near-perfect cancellation in the Mertens function M(x) reflects the independence of width layers (CRT), which makes the parity of the layer count asymptotically unbiased. The activation horizon sqrt(x) bounds the walk's excursions, connecting Möbius randomness to the same square-root scale that governs the Riemann Hypothesis.
