# Divisor Functions τ(n) and σ(n) in FS-Geometry

---

## Overview

The divisor function tau(n) counts the number of divisors of n; the sum-of-divisors function sigma(n) sums them. Both are fundamental multiplicative functions whose average behavior, extreme values, and distributional properties are central to number theory.

In the Factor Skyline, these functions acquire geometric meaning through the recursive width decomposition of each column. The divisor count tau(n) measures the **branching complexity** of the column — how many distinct sub-column structures it contains. The sum sigma(n) measures the **total height budget** across all factor branches. Highly composite numbers appear as maximally branching columns, and the average orders of tau and sigma emerge from the coverage architecture.

---

## 1. τ(n) as Branching Complexity of the Width Decomposition

### 1.1. The recursive width decomposition

Each integer n > 1 has a recursive column structure in the skyline:

    n = p_1^{e_1} * p_2^{e_2} * ... * p_k^{e_k}

The FS column decomposes into a sequence of widths:

    [p_1, p_1, ..., p_1, p_2, p_2, ..., p_2, ..., p_k, ..., p_k]
     (e_1 copies)         (e_2 copies)           (e_k copies)

The total number of width steps is Omega(n) = e_1 + e_2 + ... + e_k.

### 1.2. Divisors as sub-column selections

A divisor d | n corresponds to a **sub-column** obtained by selecting a subset of the width steps. Specifically, d = p_1^{a_1} * p_2^{a_2} * ... * p_k^{a_k} where 0 <= a_i <= e_i. The number of such selections is:

    tau(n) = (e_1 + 1)(e_2 + 1) * ... * (e_k + 1)

In FS terms: **tau(n) counts the number of distinct sub-columns of n's width decomposition.** Each divisor corresponds to choosing, for each width-group (each prime p_i), how many layers of that width to include (from 0 to e_i).

### 1.3. The branching tree

The width decomposition can be viewed as a tree:

```
n = 12 = 2^2 * 3
Width groups: {2: multiplicity 2}, {3: multiplicity 1}

Branching choices:
  2^0 * 3^0 = 1
  2^1 * 3^0 = 2
  2^2 * 3^0 = 4
  2^0 * 3^1 = 3
  2^1 * 3^1 = 6
  2^2 * 3^1 = 12

tau(12) = (2+1)(1+1) = 6 divisors
```

Each path through the branching tree selects a specific power of each prime — a specific sub-column of n. The branching factor at each width-group is (e_i + 1).

### 1.4. FS column types by tau

| tau(n) | FS column type | Examples |
|--------|---------------|----------|
| 1 | Unit (n = 1) | 1 |
| 2 | Escape (prime) — single width, no branching | 2, 3, 5, 7, 11, ... |
| 3 | Prime square — one width group, 2 layers | 4, 9, 25, 49, ... |
| 4 | Semiprime or prime cube | 6, 10, 14, 15, 8, 27, ... |
| 6 | Two width groups, one repeated | 12, 18, 20, 28, ... |
| 8 | Three distinct widths or high multiplicity | 24, 30, 40, ... |
| 12 | Richly branching | 60, 72, 84, 96, ... |

Primes always have tau = 2 (divisors 1 and p). They are the **non-branching** columns — a single width, no choices.

---

## 2. σ(n) as Cumulative Height Across Factor Branches

### 2.1. The sigma formula from width groups

The sum of divisors is:

    sigma(n) = prod_{p^e || n} (1 + p + p^2 + ... + p^e) = prod_{p^e || n} (p^{e+1} - 1)/(p - 1)

Each factor (1 + p + ... + p^e) is the **geometric sum** over the width-group for prime p: it sums the heights of all sub-columns obtainable by selecting 0, 1, ..., e copies of width p.

### 2.2. The height-sum interpretation

For each width-group, the sub-column heights are 1, p, p^2, ..., p^e. The geometric sum adds all of these. When these sums are multiplied across width-groups (by the multiplicativity of sigma), the result is the total height-sum over all divisors:

    sigma(n) = sum_{d | n} d

In FS terms: **sigma(n) sums the heights of all sub-columns of n's width decomposition.** Each divisor d represents a sub-column of height d, and sigma accumulates these heights across all branches.

### 2.3. Numerical examples

| n    | Factorization | Width-group sums | sigma |
|------|--------------|-----------------|-------|
| 12   | 2^2 * 3      | (1+2+4) * (1+3) = 7 * 4 | 28 |
| 30   | 2 * 3 * 5    | (1+2) * (1+3) * (1+5) = 3 * 4 * 6 | 72 |
| 60   | 2^2 * 3 * 5  | (1+2+4) * (1+3) * (1+5) = 7 * 4 * 6 | 168 |
| 360  | 2^3 * 3^2 * 5 | (1+2+4+8) * (1+3+9) * (1+5) = 15 * 13 * 6 | 1170 |
| 2520 | 2^3 * 3^2 * 5 * 7 | 15 * 13 * 6 * 8 | 9360 |

Each width-group contributes a geometric sum. The product of these sums gives the total divisor sum. More width-groups (more distinct primes) and higher multiplicities both increase sigma.

---

## 3. Highly Composite Numbers as Maximally Branching Columns

### 3.1. Definition

A **highly composite number** (HCN) is an integer n where tau(n) > tau(m) for all m < n. These are the integers with the most divisors relative to their size — the most richly branching columns in the skyline.

### 3.2. The HCN sequence and its FS structure

| n    | tau | Factorization | Width sequence | Omega |
|------|-----|--------------|----------------|-------|
| 1    | 1   | 1            | []             | 0     |
| 2    | 2   | 2            | [2]            | 1     |
| 4    | 3   | 2^2          | [2,2]          | 2     |
| 6    | 4   | 2*3          | [2,3]          | 2     |
| 12   | 6   | 2^2*3        | [2,2,3]        | 3     |
| 24   | 8   | 2^3*3        | [2,2,2,3]      | 4     |
| 60   | 12  | 2^2*3*5      | [2,2,3,5]      | 4     |
| 120  | 16  | 2^3*3*5      | [2,2,2,3,5]    | 5     |
| 360  | 24  | 2^3*3^2*5    | [2,2,2,3,3,5]  | 6     |
| 720  | 30  | 2^4*3^2*5    | [2,2,2,2,3,3,5]| 7     |
| 840  | 32  | 2^3*3*5*7    | [2,2,2,3,5,7]  | 6     |
| 2520 | 48  | 2^3*3^2*5*7  | [2,2,2,3,3,5,7]| 7     |

### 3.3. The FS structure of HCNs

Every HCN has several distinctive FS properties:

**Always lpf = 2 and dx = 2.** Every HCN beyond 1 is even. In the skyline, HCNs are always width-2 columns (they begin with the earliest coverage layer). An HCN never wastes its "first width" on a large prime.

**Exponents are non-increasing.** In the factorization 2^{e_1} * 3^{e_2} * 5^{e_3} * ..., the exponents satisfy e_1 >= e_2 >= e_3 >= ... This is because increasing the exponent of a smaller prime always produces a better branching ratio than increasing the exponent of a larger prime (since (e+2)/(e+1) is the branching gain, and it is the same for all primes, but using a smaller prime gives a smaller number).

**The primes used are consecutive from 2.** An HCN always uses primes 2, 3, 5, 7, ..., p_k with no gaps. Skipping a small prime would waste branching potential.

**HCNs are smooth.** Every HCN is p_k-smooth where p_k is its largest prime factor. HCNs live in the **shallow** region of the skyline — they use only early activation layers and have the most complex branching structure possible within those layers.

### 3.4. The FS interpretation of maximal branching

An HCN maximizes tau(n) for its size by:

1. **Using the earliest widths.** Small primes (2, 3, 5, ...) provide the most branching per unit of column size. Width-2 doubles tau with each additional layer; width-3 triples tau for each added layer but costs 3 times as much column size.

2. **Distributing multiplicity optimally.** The non-increasing exponent condition ensures that the branching budget is allocated efficiently across width-groups.

3. **Including more width-groups rather than deeper stacks.** Adding a new width-group (a new distinct prime) multiplies tau by 2 (at the cost of one new width). Adding an extra layer to an existing group adds one to the branching factor but is less efficient.

This is the FS-geometric content of Ramanujan's characterization of HCNs: they are the integers that optimally distribute their factorization across the early activation layers to maximize branching.

---

## 4. Activation Depth and Width Multiplicity

### 4.1. tau(n) is controlled by width multiplicities

The divisor count tau(n) = prod(e_i + 1) depends only on the exponents in n's prime factorization — equivalently, on the **multiplicity of each width** in the FS column's recursive decomposition.

- A column with k distinct widths, each appearing once: tau = 2^k. This grows exponentially with the number of distinct width layers.
- A column with a single width appearing e times: tau = e + 1. This grows linearly with depth.

The exponential growth from distinct widths is much faster than the linear growth from repeated widths. This is why HCNs favor breadth (many distinct primes) over depth (high powers of few primes).

### 4.2. sigma(n) is controlled by geometric growth within width groups

While tau depends on multiplicities, sigma depends on both multiplicities and the sizes of the widths. The geometric sum (1 + p + ... + p^e) grows approximately as p^e / (1 - 1/p) for large p or e. Larger widths produce faster-growing geometric sums.

This creates a tension:
- For **tau**: use small widths (to get more groups cheaply).
- For **sigma**: large widths contribute more to the divisor sum per layer.

This is why the numbers that maximize sigma(n)/n (the sum-of-divisors ratio) are different from the HCNs: they may include slightly larger primes than the HCNs to boost the geometric sums.

### 4.3. The average order of tau from coverage architecture

The average value of tau(n) for n <= x is:

    (1/x) * sum_{n<=x} tau(n) ~ ln(x)

In FS terms: the average number of sub-columns per column grows logarithmically. This follows from the coverage architecture:

Each prime q contributes an average multiplicity of ~1/(q-1) to the factorization of a random integer. The average of tau = prod(e_i + 1) is:

    E[tau] = prod_q E[e_q + 1] = prod_q (1 + 1/q + 1/q^2 + ...) = prod_q q/(q-1) = prod_q 1/(1-1/q)

This divergent product, truncated at primes up to x, gives prod_q 1/(1-1/q) ~ e^gamma * ln(x) by Mertens' theorem. The average branching complexity of a column at scale x is approximately ln(x) — one additional branching factor for each doubling of the activation depth.

Numerically verified:

| x     | Average tau | ln(x) |
|-------|------------|-------|
| 100   | 4.82       | 4.61  |
| 1000  | 7.07       | 6.91  |
| 10000 | 9.37       | 9.21  |

The match is close, with the average tau slightly exceeding ln(x) (the ratio approaches e^gamma ~ 1.78 times the precise asymptotic).

### 4.4. The average order of sigma from coverage architecture

The average value of sigma(n)/n for n <= x converges to:

    (1/x) * sum_{n<=x} sigma(n)/n → pi^2/6 = zeta(2)

In FS terms: the average total sub-column height, normalized by the column's own height, approaches pi^2/6 ~ 1.6449. This constant is the **second Euler product**:

    zeta(2) = prod_q 1/(1 - 1/q^2) = prod_q q^2/(q^2 - 1)

Each width-group contributes a factor q^2/(q^2 - 1) to the normalized height-sum, and the product over all primes converges to pi^2/6. This is the FS-geometric origin of the Basel sum: the average divisor-sum ratio equals the product of activation-level contributions, each measuring how much height the width-q group adds on average.

---

## 5. Structural Insights

### 5.1. Primes are the minimally branching columns

Primes always have tau = 2 (divisors 1 and p only). They are escape events — single-width columns with no internal structure to branch. In the skyline, they are structurally minimal: the tallest columns with the simplest branching.

The average tau for primes up to 1000 is exactly 2.00. For composites, it is 8.10. Composites have four times the branching complexity of primes on average, because their multi-width structure creates exponentially many sub-column combinations.

### 5.2. The tau-sigma relationship in FS-geometry

For a given n, tau(n) and sigma(n) are related through the width-group structure:

- tau uses only the multiplicities (e_i + 1).
- sigma uses both the multiplicities and the prime sizes (via geometric sums).

This creates a characteristic pattern: highly composite numbers (which maximize tau) tend to also have large sigma, but the maximizers of sigma/n are slightly different (they include larger primes to boost geometric sums).

In FS terms: **branching complexity (tau) depends on how many layers the column has in each width-group; height budget (sigma) depends on how tall those layers are.**

### 5.3. The FS content of the Dirichlet series for tau and sigma

The Dirichlet series:

    sum tau(n)/n^s = zeta(s)^2
    sum sigma(n)/n^s = zeta(s) * zeta(s-1)

have FS interpretations:

**zeta(s)^2 for tau:** The divisor count is the convolution 1 * 1 (the Dirichlet convolution of two copies of the constant function). In FS terms: counting sub-columns of n is equivalent to counting ways to split n into two factors (d, n/d) — two independent walks through the width decomposition, one selecting d and one selecting the complement. The squared Euler product encodes this double-walk structure.

**zeta(s) * zeta(s-1) for sigma:** The divisor sum involves one factor at scale s (counting divisors) and one at scale s-1 (weighting by size). In FS terms: sigma sums the heights of sub-columns, with each sub-column weighted by its own height rather than counted uniformly. The shift from s to s-1 in the second zeta factor reflects this height-weighting.

### 5.4. Extreme values and the FS architecture

The maximum of tau(n) for n <= x grows as:

    max tau(n) ~ 2^{c * ln(x) / ln(ln(x))}

for a constant c ~ 1.066. This subexponential growth reflects the optimal HCN strategy: use the first ~ln(x)/ln(ln(x)) primes (those up to ~ln(x)), each with moderate exponents, to maximize the product of branching factors.

In FS terms: the maximally branching column at scale x uses **all width layers up to approximately ln(x)** — exactly the same primes that govern the escape density. The activation depth needed for maximal branching is ~ln(ln(x)), which matches the activation depth for the escape density to reach its asymptotic form. The skyline's branching complexity peaks at the same depth scale where its coverage architecture reaches maturity.

### 5.5. The FS connection between divisor functions and prime distribution

The Dirichlet series identities connect tau and sigma to zeta, which in turn connects to the escape density and zero spectrum. This chain of connections means:

1. The average branching complexity of skyline columns (avg tau ~ ln x) is governed by the escape density product (through Mertens' theorem).
2. The average height budget (avg sigma/n → pi^2/6) is governed by the squared escape density product (through the Euler product for zeta(2)).
3. The extreme branching (HCNs) is governed by the same primes that determine the escape corridor.

**Divisor statistics and prime statistics are dual manifestations of the same FS coverage architecture.** The primes determine which widths are available; the divisor functions measure how those widths combine.

---

## 6. Summary

| Concept | Classical | FS-Geometry |
|---------|-----------|-------------|
| tau(n) | Number of divisors | Branching complexity: count of sub-columns in width decomposition |
| sigma(n) | Sum of divisors | Height budget: total height across all sub-columns |
| tau(n) = prod(e_i+1) | Multiplicative formula | Product of branching factors per width-group |
| sigma(n) = prod(p^{e+1}-1)/(p-1) | Geometric sum product | Product of height-sums per width-group |
| tau(p) = 2 | Primes have 2 divisors | Escape columns are non-branching (single width) |
| avg tau ~ ln(x) | Dirichlet's theorem | Average branching grows with activation depth |
| avg sigma/n → pi^2/6 | Asymptotic mean | Product of width-group height contributions = zeta(2) |
| Highly composite numbers | Max tau for size | Maximally branching: all early widths, non-increasing exponents |
| HCNs are smooth | Always p_k-smooth | HCN columns use only early activation layers |
| HCNs have lpf = 2 | Always even | HCN columns start with the first coverage layer |
| zeta(s)^2 | Dirichlet series for tau | Double-walk through width decomposition |
| zeta(s)*zeta(s-1) | Dirichlet series for sigma | Height-weighted walk through width decomposition |
| Max tau ~ 2^{c*ln x/ln ln x} | Subexponential growth | Optimal branching uses widths up to ~ln(x) = escape-density scale |

Divisor functions in the Factor Skyline measure two aspects of a column's internal structure: branching complexity (how many sub-columns the recursive width decomposition contains) and height budget (the total height across all sub-columns). Both are governed by the coverage architecture that also governs prime distribution — the same width layers that determine escape events also determine divisor growth. The skyline unifies prime counting and divisor counting as dual views of a single geometric structure.
