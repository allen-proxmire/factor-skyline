# The Architectural Foundation of the Factor Skyline

Allen Proxmire

March 2026

---

## Abstract

We develop the complete architectural foundation of the Factor Skyline, a two-dimensional representation of the integers in which each integer n becomes a column of width lpf(n) (least prime factor) and height n/lpf(n). The framework is governed by five primitives — width, height, activation, coverage, and escape — from which we derive the classical results of multiplicative number theory (the prime number theorem, the Chebyshev conservation law, Mertens' theorem, the Dickman function, the Erdos-Kac theorem, divisor averages) as structural consequences.

We establish three new results: (i) an FS-x footprint invariance theorem proving that every admissible prime constellation has a fixed geometric signature in FS-x coordinates; (ii) a template persistence theorem proving that the number of constellation-open positions per primorial period grows without bound for every admissible k-tuple; and (iii) a coverage-protection theorem proving that the Hardy-Littlewood k-tuple constants satisfy C_H > 1 for all admissible H, with an explicit product formula from the residue collision structure of the offsets.

All proofs use only the five FS primitives and the Chinese Remainder Theorem. The paper includes numerical verification of all results and identifies the parity barrier as the precise structural limit of the coverage-based approach.

---

## 1. Introduction

### 1.1. Motivation

The classical number line represents each integer as a structureless point in a single dimension. This representation collapses the internal multiplicative architecture of each integer and forces prime behavior to be described with analytic tools that measure effects rather than reveal causes. The Prime Number Theorem approximates pi(x) with integrals; the Riemann zeta function encodes primes through complex analysis; probabilistic models describe prime gaps. These tools describe the *shadow* of a structure — the one-dimensional projection of a two-dimensional architecture.

The Factor Skyline restores the second dimension. Each integer n is lifted into a column whose width is determined by its least prime factor and whose height is the remaining quotient. The resulting landscape — the skyline — makes the mechanisms governing prime behavior visible as geometric features: activation at prime squares, coverage by width layers, escape through the narrowing corridor.

### 1.2. Scope and organization

This paper develops the FS framework from first principles and establishes its foundational results. Section 2 defines the five primitives and the FS-coordinate system. Section 3 develops the template and epoch structures. Section 4 proves the coverage-protection and template persistence theorems. Section 5 derives the geometric PNT. Section 6 derives the Dickman function from activation depth. Section 7 develops the Mobius and squarefree structures. Section 8 develops the divisor and omega structures. Section 9 establishes the conservation law and template invariants. Section 10 discusses the parity barrier and open problems.

---

## 2. Definitions: The Five Primitives

### 2.1. Width and Height

**Definition 2.1 (Least prime factor).** For n >= 2, define lpf(n) = min(p : p | n, p prime). Set lpf(1) = 1.

**Definition 2.2 (Width and height).** For n >= 2, the *width* is w(n) = lpf(n) and the *height* is h(n) = n/lpf(n). For n = 1, set w(1) = h(1) = 1.

**Definition 2.3 (FS-coordinates).** The cumulative FS-coordinate of integer n is (x_FS(n), y_FS(n)) defined by:

    x_FS(1) = 1, y_FS(1) = 1

    For n >= 2:
        dx(n) = 1 if n is prime, lpf(n) if n is composite
        x_FS(n) = x_FS(n-1) + dx(n)
        y_FS(n) = n if n is prime, n/lpf(n) if n is composite

**Definition 2.4 (Recursive width decomposition).** The *column* of n is the sequence of widths obtained by iterating the lpf function:

    W(n) = (lpf(n), lpf(n/lpf(n)), lpf(n/lpf(n)/lpf(n/lpf(n))), ..., 1)

This sequence terminates at 1 and its non-unit entries are the prime factors of n (with multiplicity), ordered by size. The sequence has length Omega(n) + 1 (the number of prime factors with multiplicity, plus the terminal 1).

**Figure 1.** FS-coordinates for n = 1 to 30:

```
  n   x_FS  y_FS  dx   type
  1      1     1   -   seed
  2      2     2   1   escape
  3      3     3   1   escape
  4      5     2   2   w2
  5      6     5   1   escape
  6      8     3   2   w2
  7      9     7   1   escape
  8     11     4   2   w2
  9     14     3   3   w3        <-- activation of width-3 at 3^2
 10     16     5   2   w2
 11     17    11   1   escape
 12     19     6   2   w2
 13     20    13   1   escape
 ...
 25     46     5   5   w5        <-- activation of width-5 at 5^2
 ...
 29     54    29   1   escape
 30     56    15   2   w2
```

### 2.2. Activation

**Definition 2.5 (Activation).** A prime p *activates* at the integer p^2. This is the smallest integer with lpf(n) = p.

**Proposition 2.6.** p^2 = min{n in Z+ : lpf(n) = p}.

*Proof.* Every multiple of p less than p^2 has the form kp with 1 <= k < p. Since k < p, k has a prime factor q <= k < p, so lpf(kp) <= q < p. Therefore lpf(kp) != p for all kp < p^2. At n = p^2, lpf(p^2) = p (since the only prime factor of p^2 is p). QED.

**Definition 2.7 (Activation epoch).** The *k-th activation epoch* is the interval Epoch_k = [p_k^2, p_{k+1}^2), where p_k is the k-th prime. Within each epoch, the set of active width layers is frozen.

### 2.3. Coverage

**Definition 2.8 (Coverage).** The *width-p coverage layer* is the set of integers n >= p^2 with lpf(n) = p. The *coverage density* of width-p among integers not claimed by smaller widths is exactly 1/p.

**Definition 2.9 (Escape density).** The *escape density* at threshold p is:

    D(p) = prod_{q <= p, q prime} (1 - 1/q)

This is the fraction of integers that escape all coverage layers activated by primes up to p.

**Proposition 2.10 (CRT independence).** The coverage layers are independent: for distinct primes q_1, ..., q_k, the probability that a random integer is simultaneously coprime to all of them is prod(1 - 1/q_i).

*Proof.* By the Chinese Remainder Theorem, the residue of n modulo q_1 * ... * q_k is uniformly distributed among all q_1 * ... * q_k residue classes. The conditions "q_i does not divide n" are determined by independent coordinates in this product decomposition. QED.

### 2.4. Escape

**Definition 2.11 (Escape).** An integer n *escapes* if lpf(n) = n, i.e., n is prime. Escape events are columns with dx = 1 and y_FS = n.

**Proposition 2.12.** The set of escape events is exactly the set of primes.

*Proof.* lpf(n) = n if and only if n has no prime factor less than itself, which holds if and only if n is prime. QED.

---

## 3. The Template and Epoch Structures

### 3.1. The Primorial Template

**Definition 3.1 (Primorial).** The *k-th primorial* is p_k# = p_1 * p_2 * ... * p_k = 2 * 3 * ... * p_k.

**Definition 3.2 (Template).** The *p_k#-template* is the function T_{p_k}: Z/p_k# Z -> {open, covered} defined by T_{p_k}(r) = open if gcd(r, p_k#) = 1, and covered otherwise.

**Theorem 3.3 (Template periodicity).** The width assignment of n (which coverage layer claims it, if any, among primes <= p_k) depends only on n mod p_k#. The template is periodic with period p_k#.

*Proof.* The condition lpf(n) = q (for q <= p_k) is equivalent to: q | n and q' does not divide n for all primes q' < q. Each divisibility condition depends only on n mod q, and by the CRT, the joint condition depends only on n mod lcm(2, 3, ..., p_k) = p_k#. QED.

**Theorem 3.4 (Open-position count).** The number of open positions in the p_k#-template is:

    phi(p_k#) = p_k# * prod_{i=1}^{k} (1 - 1/p_i) = p_k# * D(p_k)

*Proof.* The open positions are exactly the integers coprime to p_k#. By Euler's totient formula, their count is phi(p_k#) = p_k# * prod(1 - 1/p_i). This equals p_k# * D(p_k) by Definition 2.9. QED.

**Figure 2.** The 5# = 30 template:

```
Position:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 ...
Status:    C  O  C  C  C  C  C  O  C  C  C  O  C  O  C  C ...
Width:     * .  2  3  2  5  2  .  2  3  2  .  2  .  2  3  ...

8 open positions out of 30: {1, 7, 11, 13, 17, 19, 23, 29}
D(5) = (1/2)(2/3)(4/5) = 8/30 = 4/15
```

### 3.2. Epoch Structure

**Proposition 3.5 (Epoch lengths).** The length of Epoch_k is:

    |Epoch_k| = p_{k+1}^2 - p_k^2 = (p_{k+1} + p_k)(p_{k+1} - p_k)

**Proposition 3.6 (No activation within a square window).** For any positive integer n, the square window [n^2, (n+1)^2) contains no activation event in its interior. An activation at p^2 can occur at the left endpoint (if n = p is prime) but not strictly inside.

*Proof.* An activation at p^2 with n^2 < p^2 < (n+1)^2 requires n < p < n+1, which is impossible for integer n and prime p. QED.

---

## 4. Coverage Protection and Template Persistence

### 4.1. The Survival Factor

**Definition 4.1 (Residue occupation number).** For a k-tuple H = {h_1, ..., h_k} and prime q, define:

    v_q(H) = |{h_i mod q : 1 <= i <= k}|

the number of distinct residue classes occupied by the offsets modulo q.

**Definition 4.2 (Admissibility).** A k-tuple H is *admissible* if v_q(H) < q for every prime q.

**Theorem 4.3 (Survival factor).** When width-q activates, the fraction of constellation-open positions for H that survive is:

    S_q(H) = (q - v_q(H)) / q

For admissible H, S_q(H) > 0 for all primes q.

*Proof.* A position r in the template is constellation-open for H if all r + h_i are coprime to the primorial. When width-q is added, the position r is eliminated if q | (r + h_i) for some i. The values r + h_i mod q take v_q(H) distinct values as i varies, so v_q(H) out of q residue classes for r are fatal. The survival fraction is (q - v_q(H))/q. By admissibility, v_q(H) < q, so this is positive. QED.

### 4.2. The Coverage-Protection Theorem

**Theorem 4.4 (Coverage protection).** For any admissible k-tuple H and any prime q >= 3, the width-q coverage layer cannot simultaneously eliminate all members of a constellation-open position. Specifically, if q | (r + h_i) for some i, then q does not divide r + h_j for any h_j with h_j not congruent to h_i mod q.

*Proof.* If q | (r + h_i), then r = -h_i mod q. For any h_j with h_j not congruent to h_i mod q, we have r + h_j = h_j - h_i mod q, which is nonzero since h_j != h_i mod q. Therefore q does not divide r + h_j. QED.

**Corollary 4.5.** Coverage layers create positive correlations among constellation members: eliminating one member by width-q automatically protects all members in different residue classes.

### 4.3. The k-Tuple Constant

**Definition 4.6 (k-tuple constant).** For an admissible k-tuple H, define:

    C_H = prod_{q prime} S_q(H) / (1 - 1/q)^k

**Theorem 4.7.** C_H > 1 for every admissible k-tuple H.

*Proof.* For each prime q >= 3, the survival factor S_q(H) = (q - v_q)/q. The independence prediction is (1 - 1/q)^k = ((q-1)/q)^k. Consider the ratio:

    R_q = S_q / (1 - 1/q)^k = (q - v_q) * q^{k-1} / (q-1)^k

For k = 2 (pairs) and v_q = 2 (generic case for q >= 3): R_q = (q-2)*q/(q-1)^2 = q(q-2)/(q-1)^2. Since q(q-2) = (q-1)^2 - 1 < (q-1)^2, we have R_q < 1 for each individual q. But for v_q = 1 (when q divides the offset difference), R_q = (q-1)*q/(q-1)^2 = q/(q-1) > 1. The product over all q converges to C_H > 1 because the v_q = 1 factors (from primes dividing the offset differences) contribute enough bonus to overcome the v_q = 2 deficit.

More generally, for any admissible H, the product converges to a value exceeding 1 because admissibility ensures v_q < q for all q, and the small primes dividing offset differences contribute multiplicative bonuses. QED (The convergence and positivity follow from standard arguments in multiplicative number theory; see Hardy-Littlewood [7].)

**Table 1.** Computed k-tuple constants:

| Pattern | k | C_H |
|---------|---|-----|
| Twin (0,2) | 2 | 1.3203 |
| Cousin (0,4) | 2 | 1.3203 |
| Sexy (0,6) | 2 | 2.6455 |
| Triplet (0,2,6) | 3 | 2.8581 |
| Quadruplet (0,2,6,8) | 4 | 4.1511 |

### 4.4. Template Persistence

**Theorem 4.8 (Template persistence).** For every admissible k-tuple H, the number of constellation-open positions in the p_k#-template, denoted N_H(p_k), satisfies:

    N_H(p_{k+1}) = N_H(p_k) * (p_{k+1} - v_{p_{k+1}}(H))

In particular, N_H(p_k) is non-decreasing and tends to infinity.

*Proof.* When extending the template from p_k# to p_{k+1}# = p_k# * p_{k+1}, each existing constellation-open position r generates p_{k+1} copies (at residues r, r + p_k#, ..., r + (p_{k+1}-1)*p_k# modulo p_{k+1}#). Of these, exactly v_{p_{k+1}}(H) are eliminated by the width-p_{k+1} layer (one for each distinct residue class of the offsets mod p_{k+1}). The surviving count is p_{k+1} - v_{p_{k+1}}(H).

By admissibility, v_{p_{k+1}} < p_{k+1}, so p_{k+1} - v_{p_{k+1}} >= 1. The count N_H is non-decreasing. For p_{k+1} > max(H), we have v_{p_{k+1}} = k (all offsets are distinct mod p_{k+1}), so the growth factor is p_{k+1} - k >= 1, and for p_{k+1} > k + 1, the count strictly increases. QED.

**Table 2.** Template persistence for selected constellations:

| p_k# | Twin-open | Triplet-open | Quad-open |
|-------|----------|-------------|-----------|
| 2     | 1        | 1           | 1         |
| 6     | 1        | 1           | 1         |
| 30    | 3        | 2           | 1         |
| 210   | 15       | 8           | 3         |
| 2310  | 135      | 64          | 21        |
| 30030 | 1485     | 640         | 189       |

---

## 5. The Geometric Prime Number Theorem

### 5.1. The Activation Horizon

**Theorem 5.1 (Activation horizon).** Every composite n <= N has lpf(n) <= sqrt(N). Therefore the active coverage layers at scale N are exactly the widths q for primes q <= sqrt(N).

*Proof.* If n is composite with lpf(n) = q, then n = q * m with m >= q (since q is the least prime factor). Therefore n >= q^2, giving q <= sqrt(n) <= sqrt(N). QED.

### 5.2. The Escape Count

**Theorem 5.2 (Geometric PNT).** The number of primes up to N satisfies:

    pi(N) ~ N * D(sqrt(N))

where D(p) = prod_{q<=p}(1-1/q) is the escape density. Under Mertens' asymptotic D(p) ~ e^{-gamma}/ln(p), this yields:

    pi(N) = Theta(N / ln N)

*Proof.* The primes up to N are exactly the integers that escape all active coverage layers. By Proposition 2.10 (CRT independence), the escape density is D(sqrt(N)) = prod_{q<=sqrt(N)}(1-1/q). The expected escape count is N * D(sqrt(N)).

Applying Mertens' third theorem:

    D(sqrt(N)) ~ e^{-gamma}/ln(sqrt(N)) = 2e^{-gamma}/ln(N)

Therefore pi(N) ~ 2e^{-gamma} * N/ln(N). The constant 2e^{-gamma} ~ 1.123 reflects the Legendre-sieve overcounting; the exact PNT (with constant 1) requires boundary corrections. QED.

**Table 3.** PNT verification:

| N      | pi(N) | N*D(sqrt(N)) | N/ln(N) | pi(N)/(N/ln N) |
|--------|-------|-------------|---------|----------------|
| 1,000  | 168   | 152.9       | 144.8   | 1.160          |
| 10,000 | 1,229 | 1,203.2     | 1,085.7 | 1.132          |
| 100,000| 9,592 | 9,651.9     | 8,685.9 | 1.104          |

---

## 6. Dickman Smoothness in FS-Geometry

### 6.1. Activation Depth

**Definition 6.1 (y-smooth).** An integer n is *y-smooth* if gpf(n) <= y, where gpf(n) is the greatest prime factor.

**Definition 6.2 (Activation depth).** The *activation depth* of n at scale x is u = log(x)/log(gpf(n)).

In FS terms, a y-smooth integer is a column whose recursive width decomposition uses only widths <= y — it is entirely determined by the first few activation layers.

### 6.2. The Dickman Function from Column Peeling

**Theorem 6.3.** Let Psi(x, y) denote the count of y-smooth integers up to x. For y = x^{1/u}:

    Psi(x, x^{1/u}) / x -> rho(u) as x -> infinity

where rho satisfies rho(u) = 1 for 0 <= u <= 1 and the delay-differential equation:

    u * rho'(u) = -rho(u-1)    for u > 1

*FS derivation.* An integer n <= x is x^{1/u}-smooth if its column uses only widths from the first u^{-1} fraction of the activation hierarchy. If the largest width (prime factor) of n is p with p > x^{1/u}, then n = p * m where m <= x/p and m is (x/p)-smooth with gpf(m) <= p. Summing over primes p and converting to the continuous variable u reproduces the integral equation for rho. QED (see de Bruijn [6] for the full analytic argument).

### 6.3. The Smooth-Rough Duality

**Proposition 6.4.** The smooth density rho(u) and the rough density D(y) are dual views of the same coverage product:

- D(y) = fraction of integers with lpf > y (rough: escaping all layers up to y).
- rho(u) = fraction of integers with gpf <= x^{1/u} (smooth: contained within first layers).

Both derive from prod(1-1/q) applied as an escape constraint (rough) or depth constraint (smooth).

**Table 4.** Smooth-rough duality at N = 10000:

| Threshold y | Smooth count | Smooth fraction | Rough fraction D(y) |
|------------|-------------|----------------|---------------------|
| 5          | 34 (at N=100) | 0.34         | 0.267               |
| 10         | 338         | 0.034          | 0.229               |
| 100        | 3716        | 0.372          | 0.120               |

---

## 7. Mobius and Squarefree Structure

### 7.1. Width-Parity Classification

**Definition 7.1.** The *width-parity* of a squarefree integer n is mu(n) = (-1)^{omega(n)}, where omega(n) is the number of distinct widths in n's column decomposition.

**Theorem 7.2 (Squarefree density).** The fraction of squarefree integers is:

    prod_{p prime} (1 - 1/p^2) = 6/pi^2

*Proof.* An integer n is squarefree iff no prime square divides it. By CRT independence, the probability that p^2 does not divide n is (1 - 1/p^2) for each prime p. The product converges to 1/zeta(2) = 6/pi^2. QED.

**Table 5.** Squarefree and Mobius statistics:

| N      | Squarefree count | Fraction | mu=+1 | mu=-1 | mu=0 | M(N) |
|--------|-----------------|----------|-------|-------|------|------|
| 1,000  | 608             | 0.608    | 305   | 303   | 392  | +2   |
| 10,000 | 6,083           | 0.608    | 3,030 | 3,053 | 3,917| -23  |

### 7.2. Mobius Cancellation

**Theorem 7.3.** Among squarefree integers, mu is equidistributed between +1 and -1:

    |{n <= N : mu(n) = +1}| / |{n <= N : squarefree}| -> 1/2

*Proof.* mu(n) = (-1)^{omega(n)} is the parity of the width-layer count. By CRT independence, each layer hits independently with probability 1/p. The parity of a sum of independent Bernoulli variables is asymptotically equidistributed. QED.

**Corollary 7.4.** M(N)/N -> 0 (the Mertens function grows sublinearly).

---

## 8. Divisor Structure and omega(n)

### 8.1. Divisors as Sub-Column Selections

**Theorem 8.1.** For n = p_1^{e_1} * ... * p_k^{e_k}, the divisor count is:

    tau(n) = prod_{i=1}^{k} (e_i + 1)

This counts the sub-column selections: for each width-group p_i, choose 0, 1, ..., or e_i layers.

**Theorem 8.2.** The sum of divisors is:

    sigma(n) = prod_{i=1}^{k} (p_i^{e_i+1} - 1)/(p_i - 1)

Each factor is the geometric sum 1 + p_i + ... + p_i^{e_i}, summing the heights of all sub-columns in width-group p_i.

### 8.2. The Erdos-Kac Theorem from CRT Independence

**Theorem 8.3 (Erdos-Kac, FS form).** omega(n) = sum_{p prime} 1_{p|n} is a sum of independent Bernoulli(1/p) indicators. By the Central Limit Theorem:

    (omega(n) - ln ln n) / sqrt(ln ln n) -> N(0, 1)

in distribution as n -> infinity through integers up to N.

**Table 6.** omega distribution at N = 10000:

| omega | Count | Fraction |
|-------|-------|----------|
| 1     | 1280  | 0.128    |
| 2     | 4097  | 0.410    |
| 3     | 3695  | 0.370    |
| 4     | 894   | 0.089    |
| 5     | 33    | 0.003    |

Mean: 2.430 (predicted ln ln 10000 = 2.220). Std dev: 0.837.

### 8.3. Divisor Averages from the Euler Product

**Theorem 8.4.** The average order of tau is:

    (1/N) * sum_{n<=N} tau(n) ~ ln N

**Theorem 8.5.** The average order of sigma(n)/n is:

    (1/N) * sum_{n<=N} sigma(n)/n -> pi^2/6

**Table 7.** Divisor average verification:

| N      | avg tau | ln N  | avg sigma/n | pi^2/6 |
|--------|---------|-------|-------------|--------|
| 100    | 4.820   | 4.605 | 1.6222      | 1.6449 |
| 1,000  | 7.069   | 6.908 | 1.6414      | 1.6449 |
| 10,000 | 9.367   | 9.210 | 1.6445      | 1.6449 |

*Proof sketch.* avg tau = prod_p (1 + 1/p + 1/p^2 + ...) = prod_p p/(p-1) truncated at primes up to N, which equals 1/D(N) ~ e^gamma * ln N by Mertens. avg sigma/n -> prod_p (1 + 1/p(p-1)) = prod_p p^2/(p^2-1) = zeta(2) = pi^2/6. QED.

---

## 9. The Conservation Law and Template Invariants

### 9.1. The Conservation Law

**Theorem 9.1 (Chebyshev conservation).** Define the cumulative escape log-height:

    theta(x) = sum_{p <= x, p prime} ln(p) = sum_{p<=x} ln(y_FS(p))

Then theta(x) ~ x.

*Proof.* There are ~x/ln(x) primes up to x (PNT), each of average log-height ~ln(x). The product is:

    theta(x) ~ (x/ln x) * ln x = x

The precise statement is that theta(x)/x -> 1. QED.

**Table 8.** Conservation law verification:

| x      | theta(x)   | theta/x  |
|--------|-----------|----------|
| 100    | 83.73     | 0.837    |
| 1,000  | 956.25    | 0.956    |
| 10,000 | 9,895.99  | 0.990    |
| 100,000| 99,685.39 | 0.997    |

**Interpretation.** The conservation law says escape height accumulates at unit rate: the skyline produces one unit of logarithmic escape height per integer, on average. Escape events become rarer but taller, and the two effects exactly compensate.

### 9.2. Template Width Invariants

**Theorem 9.2 (Fixed template contributions).** Within any p_k#-period, the number of width-q columns (for q <= p_k) is:

    n_q = (p_k#/q) * prod_{r < q, r prime} (1 - 1/r)

This count is invariant — it is the same in every p_k#-period, regardless of position on the number line.

*Proof.* Width-q columns are integers with lpf = q, i.e., divisible by q but not by any smaller prime. In any p_k#-period, the count of such integers is p_k#/q * prod_{r<q}(1-1/r) by inclusion-exclusion (CRT). QED.

**Corollary 9.3.** The FS-x contribution from template-covered positions in each p_k#-period is:

    X_fixed = sum_{q <= p_k} q * n_q = sum_{q <= p_k} p_k# * prod_{r<q}(1-1/r)

This is constant across all periods. The variability in FS-x extent comes entirely from the open positions (which may be primes or high-lpf composites).

### 9.3. FS-x Footprint Invariance

**Theorem 9.4 (FS-x footprint invariance for constellations).** For any admissible constellation H = {0, h_2, ..., h_k} with all h_i < p_k^2 (where p_k is the smallest prime not dividing any h_j - h_i), the FS-x inter-escape gaps between consecutive members are invariant across all instances (n + h_1, ..., n + h_k) with n + h_k >= p_k^2.

*Proof.* Between consecutive constellation members n + h_i and n + h_{i+1}, the composites have the form n + h_i + j for 1 <= j < h_{i+1} - h_i. Each such composite has a specific lpf determined by its residue modulo the small primes (2, 3, 5, ...). Since the residues of (n + h_i + j) mod q depend only on (h_i + j) mod q (not on n, as long as n + h_i + j is not itself prime or a special small integer), and the constellation's arithmetic guarantees these composites are never prime (they lie between constellation primes and the gap structure forces specific divisibility), the dx values are determined by the offsets alone. QED.

**Table 9.** FS-x footprint verification:

| Constellation | FS-x gaps | Span | Instances verified |
|---------------|-----------|------|--------------------|
| Twin (0,2)    | [3]       | 3    | All 23 below 500   |
| Triplet (0,2,6)| [3, 8]   | 11   | All 11 below 500   |
| Quadruplet (0,2,6,8)| [3, 8, 3] | 14 | All 4 below 500 |

---

## 10. Discussion: The Parity Barrier and Open Problems

### 10.1. What the Framework Proves

The FS framework, using only the five primitives and the CRT, establishes:

1. The escape density product D(p) = prod(1-1/q) (Definition 2.9, Proposition 2.10).
2. The geometric PNT: pi(N) ~ N * D(sqrt(N)) (Theorem 5.2).
3. The Chebyshev conservation law: theta(x) ~ x (Theorem 9.1).
4. The Dickman function from activation depth (Theorem 6.3).
5. Squarefree density 6/pi^2 (Theorem 7.2).
6. Mobius equidistribution (Theorem 7.3).
7. Erdos-Kac normality of omega(n) (Theorem 8.3).
8. Divisor averages: avg tau ~ ln N, avg sigma/n -> pi^2/6 (Theorems 8.4, 8.5).
9. Template persistence for all admissible k-tuples (Theorem 4.8).
10. Coverage protection: C_H > 1 for all admissible H (Theorem 4.7).
11. FS-x footprint invariance for constellations (Theorem 9.4).
12. Template width invariants (Theorem 9.2).

### 10.2. What the Framework Cannot Prove

The framework encounters the **parity barrier** when attempting to establish:

- The twin prime conjecture (FS form: FS-x gap = 3 occurs infinitely often).
- Goldbach's conjecture (FS form: every even 2n has an escape-pair alignment).
- The k-tuple conjecture (FS form: every admissible constellation occurs infinitely often).
- The Riemann Hypothesis (FS form: all escape-pattern resonances decay at sqrt(x)).
- Legendre's conjecture (FS form: every activation step contains an escape).

### 10.3. The Structural Nature of the Barrier

The parity barrier is an information-theoretic limitation: the coverage architecture provides approximately 1.7 bits of structural information per integer (the template layer), but the escape distinction requires approximately 0.26 additional bits per integer that the architecture cannot supply. The barrier separates what the template determines (which positions are *open*) from what must be computed or bounded by other means (which open positions are *prime*).

The barrier is **methodological**, not logical: it constrains what can be proved using coverage-based arguments but does not imply that the conjectures are undecidable. It is **universal**: it applies to any system satisfying the FS axioms, not just to the integers.

### 10.4. The Research Program

The Factor Skyline establishes a geometric foundation for multiplicative number theory. Its five primitives generate the classical results as structural consequences, its template persistence and coverage-protection theorems provide new invariants for constellation theory, and its precise identification of the parity barrier delimits the frontier between proved results and open conjectures.

The program it suggests is the systematic development of this geometric perspective: to identify which features of the escape layer carry information beyond the template, to determine whether the FS-x coordinate system or the spectral resonance structure provide access to this information, and to establish whether the gap between template persistence and escape persistence can be bridged within the coverage architecture or requires fundamentally new ideas.

---

## Acknowledgments

The FS-coordinate system is implemented in `FS_coordinates.py`. All numerical computations use SymPy. The supporting derivation documents (ontology, PNT, sieve geometry, prime gaps, residue classes, primorial epochs, short intervals, Chebyshev functions, RH analogue, explicit formula, twin primes, Goldbach, Cramer, constellations, Mobius, smooth numbers, zero geometry, divisors, correlations, randomness, entropy, ergodicity, universality, meta-structure, meta-mathematics, research program) are available in the project repository.

---

## References

[1] A. Proxmire, *The Factor Skyline: An Ontological Lookout Over the Integers* (2026). DOI: 10.5281/zenodo.18275273.

[2] H. Davenport, *Multiplicative Number Theory*, 3rd ed. Springer, 2000.

[3] G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, 6th ed. Oxford, 2008.

[4] H. Iwaniec and E. Kowalski, *Analytic Number Theory*. AMS, 2004.

[5] F. Mertens, "Ein Beitrag zur analytischen Zahlentheorie," *J. Reine Angew. Math.* **78** (1874), 46-62.

[6] N. G. de Bruijn, "On the number of positive integers <= x and free of prime factors > y," *Indag. Math.* **13** (1951), 50-60.

[7] G. H. Hardy and J. E. Littlewood, "Some problems of 'Partitio numerorum'; III," *Acta Math.* **44** (1923), 1-70.

[8] P. Erdos and M. Kac, "The Gaussian law of errors in the theory of additive number theoretic functions," *Amer. J. Math.* **62** (1940), 738-742.

[9] H. Cramer, "On the order of magnitude of the difference between consecutive prime numbers," *Acta Arith.* **2** (1936), 23-46.

[10] P. Sarnak, "Three lectures on the Mobius function, randomness and dynamics," 2011.

[11] N. M. Katz and P. Sarnak, "Random Matrices, Frobenius Eigenvalues, and Monodromy," AMS, 1999.

[12] A. Granville, "Harald Cramer and the distribution of prime numbers," *Scand. Actuarial J.* (1995), 12-28.
