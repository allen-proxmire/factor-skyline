# Goldbach's Conjecture in FS-Geometry

---

## Overview

Goldbach's conjecture (1742) asserts that every even integer 2n >= 4 can be written as the sum of two primes. Despite extensive numerical verification (up to 4 * 10^18) and strong heuristic support, no proof exists.

In the Factor Skyline, Goldbach's conjecture becomes a statement about **escape-pair alignments**: for every even number 2n, there must exist at least one pair of open positions (r, 2n-r) in the primorial template such that both positions are occupied by escape events (primes). The FS framework reveals the structural mechanisms that make Goldbach representations abundant and explains why even numbers with more odd prime factors tend to have more representations.

---

## 1. Goldbach Pairs as Escape-Pair Alignments

### 1.1. The alignment condition

A Goldbach representation of an even number 2n is a pair of primes (p, q) with p + q = 2n. In FS-geometry:

- p is an escape event: a column with dx = 1 and y_FS = p.
- q = 2n - p is also an escape event: a column with dx = 1 and y_FS = q.

The pair (p, q) represents a **symmetric alignment** of two escape events around the midpoint n: one escape at position p below n, another at position 2n - p above n, and their sum hits exactly 2n.

### 1.2. The primorial template view

Fix a primorial p# and consider the even number 2n. The template determines which residue classes can contribute escape events. A **Goldbach-open pair** for target 2n is a pair (r, s) of open positions in the p#-template such that r + s = 2n (mod p#).

For 2n to have a Goldbach representation, at least one Goldbach-open pair must have both members occupied by actual primes (not just template-open positions).

### 1.3. The 5#-template example

In the 5# = 30 template, the open positions are {1, 7, 11, 13, 17, 19, 23, 29}.

For target 2n = 0 mod 30 (e.g., 30, 60, 90, ...), the Goldbach-open pairs are:

    (1, 29):  1 + 29 = 30 ≡ 0 mod 30   ✓
    (7, 23):  7 + 23 = 30 ≡ 0 mod 30   ✓
    (11, 19): 11 + 19 = 30 ≡ 0 mod 30  ✓
    (13, 17): 13 + 17 = 30 ≡ 0 mod 30  ✓

There are 4 Goldbach-open pairs for this target class. Each provides a structural slot where a Goldbach representation can occur. The conjecture asserts that for every even 2n >= 4, at least one such slot is occupied by a pair of primes.

---

## 2. How Coverage Layers Constrain Goldbach-Open Pairs

### 2.1. The survival factor for each prime

When a new prime q joins the template, its coverage layer affects Goldbach-open pairs for target 2n. The pair (r, 2n - r) survives if neither r nor 2n - r is divisible by q.

**Case 1: q does not divide 2n.**
Then the conditions q | r and q | (2n - r) are independent: q | r means r ≡ 0 mod q, while q | (2n - r) means r ≡ 2n mod q. Since q does not divide 2n, these are two distinct residue classes. The probability that a random r avoids both is:

    survival = (q - 2)/q    [two out of q classes are fatal]

This is the same factor as for twin primes. When q does not divide the target, Goldbach pairs and twin pairs have identical survival rates.

**Case 2: q divides 2n.**
Then q | r and q | (2n - r) are the same condition (if q | r then q | (2n - r) since q | 2n). Only one residue class is fatal, not two. The survival factor is:

    survival = (q - 1)/q    [only one class is fatal]

This is more favorable: when q divides the target, the coverage layer is less destructive to Goldbach pairs.

### 2.2. The singular series

The ratio between the q-divides and q-doesn't-divide survival factors is:

    (q-1)/q  /  (q-2)/q  =  (q-1)/(q-2)

For each odd prime q dividing 2n, the Goldbach-open count receives a multiplicative bonus of (q-1)/(q-2) relative to the baseline. The **singular series** for the target 2n is:

    S(2n) = prod_{q | 2n, q >= 3} (q-1)/(q-2)

This product is always >= 1 (since each factor exceeds 1). Even numbers with many distinct odd prime factors have larger singular series values and therefore more Goldbach representations.

### 2.3. Numerical verification

In the 7# = 210 template, the Goldbach-open count depends on which primes divide the target:

| Target 2n | Odd prime factors | Goldbach-open (ordered) | Relative to baseline |
|-----------|-------------------|------------------------|---------------------|
| 210       | {3, 5, 7}         | 48                     | 1.00 (baseline)     |
| 30        | {3, 5}            | 40                     | 0.83                |
| 42        | {3, 7}            | 36                     | 0.75                |
| 70        | {5, 7}            | 24                     | 0.50                |
| 66        | {3, 11}           | 30                     | 0.63                |

Targets whose odd prime factors align with the template primes {3, 5, 7} receive the full bonus. Targets divisible by primes outside the template (like 11 in 66) get a partial bonus from those template primes they do share, but no bonus from the non-template prime.

### 2.4. Why even numbers with more factors have more representations

From the Goldbach representation counts up to 1000, grouped by number of distinct odd prime factors:

| Odd prime factors | Count of even numbers | Average r(2n) |
|-------------------|----------------------|---------------|
| 0                 | 8 (powers of 2)      | 8.1           |
| 1                 | 247                  | 22.8          |
| 2                 | 221                  | 40.6          |
| 3                 | 23                   | 73.1          |

Each additional odd prime factor approximately doubles the average representation count. The FS explanation: each odd prime factor q of 2n converts the survival factor for width-q from (q-2)/q (harsh: two fatal classes) to (q-1)/q (mild: one fatal class). The bonus factor (q-1)/(q-2) compounds multiplicatively across all odd prime factors.

Powers of 2 (2n = 4, 8, 16, ...) have no odd prime factors and receive no bonuses. They have the fewest Goldbach representations -- they are the "hardest" cases for the conjecture.

---

## 3. The Goldbach Density Heuristic in FS-Geometry

### 3.1. The Hardy-Littlewood prediction

The Hardy-Littlewood conjecture for Goldbach representations predicts:

    r(2n) ~ C * S(2n) * 2n / (ln 2n)^2

where C is a constant and S(2n) is the singular series. The factor 2n/(ln 2n)^2 arises because two independent escape events must occur, each with density ~1/ln(2n).

### 3.2. The FS derivation

In FS-geometry, the expected Goldbach representation count for 2n is:

**(i)** The number of Goldbach-open positions in the template is approximately:

    G(p) * 2n / p#

where G(p) is the Goldbach-open count per template period (dependent on which primes divide 2n).

**(ii)** Among these Goldbach-open positions, both members of each pair must escape all higher-width layers. The probability that a single open position is prime near scale n is D(sqrt(n)) ~ e^{-gamma}/ln(sqrt(n)) = 2e^{-gamma}/ln(n). For both members of a pair to be prime (approximately independently):

    P(both prime) ~ D(sqrt(n))^2 ~ 4e^{-2*gamma} / (ln n)^2

**(iii)** The expected count is:

    r(2n) ~ (Goldbach-open pairs near scale n) * P(both prime)
           ~ [2n * T_G(p)] * [4e^{-2*gamma} / (ln n)^2]

where T_G(p) is the Goldbach-open pair density for target 2n in the p-template.

**(iv)** The Goldbach-open density decomposes as:

    T_G(p, 2n) = D(p)^2 * S(2n, p)

where S(2n, p) is the partial singular series. The product T_G * D_higher^2 gives the full prediction.

The functional form 2n / (ln 2n)^2 arises identically to the twin prime case: two escape events must occur, each contributing a factor of 1/ln(n) from the escape density.

### 3.3. Why Goldbach representations grow

The predicted count r(2n) grows with 2n because the window [2, 2n] contains more Goldbach-open pairs as 2n increases (the template contributes more slots), while the escape density decreases only logarithmically. The product:

    r(2n) ~ C * S(2n) * 2n / (ln 2n)^2

grows without bound (since 2n dominates (ln 2n)^2). For sufficiently large 2n, the expected count vastly exceeds 1.

The smallest expected counts occur for powers of 2 (S(2n) = 1, no bonus factors). Even for these worst-case targets, the prediction r(2n) ~ C * 2n / (ln 2n)^2 grows unboundedly.

---

## 4. Activation Epochs and Goldbach Representations

### 4.1. Goldbach pairs within an epoch

Within activation epoch [p_k^2, p_{k+1}^2), the coverage configuration is frozen. For an even number 2n in this range, the Goldbach-open pairs are determined by the p_k#-template, and the probability that both members are prime depends on the escape density D(p_k) and the higher-width coverage.

### 4.2. The epoch-level Goldbach count

The expected number of Goldbach representations for 2n ~ p_k^2 is:

    r(2n) ~ 2n * T_G(p_k, 2n) * D_{higher}^2

As 2n increases through the epoch, 2n grows linearly while T_G and D_{higher} change negligibly (they depend on primes up to p_k and on higher-width densities). The representation count therefore increases roughly linearly within each epoch.

### 4.3. Epoch transitions and representation count

At the activation boundary p_{k+1}^2, a new width enters the geometry. This has two effects on Goldbach representations:

**Template refinement.** The p_{k+1}#-template refines the p_k#-template, reducing the Goldbach-open density by a factor of:
- (p_{k+1} - 2)/p_{k+1} if p_{k+1} does not divide 2n
- (p_{k+1} - 1)/p_{k+1} if p_{k+1} divides 2n

**Epoch expansion.** The next epoch is longer, providing more room for Goldbach pairs.

The net effect: the representation count continues to grow across epoch boundaries, despite the slight density reduction from each new coverage layer.

### 4.4. The worst-case targets

The targets most vulnerable to having few Goldbach representations are those with no odd prime factors (powers of 2) near the beginning of an activation epoch (where the coverage has just been tightened by a new width layer).

Even in this worst case, the representation count is approximately:

    r(2^k) ~ C * 2^k / (k * ln 2)^2

which grows exponentially. No power of 2 can have zero Goldbach representations for large k.

---

## 5. The FS-x Signature of Goldbach Pairs

### 5.1. Goldbach pairs in FS-x coordinates

For a Goldbach representation p + q = 2n, the three FS-x coordinates are x_FS(p), x_FS(q), and x_FS(2n). A striking numerical pattern emerges:

**For 2n = 30:** All three Goldbach pairs (7+23, 11+19, 13+17) have x_FS(p) + x_FS(q) = 48, while x_FS(30) = 56. The ratio 48/56 = 0.857.

**For 2n = 48:** The pairs cluster into two groups: three with x-sum 89 and two with x-sum 85, against x_FS(48) = 93.

The FS-x sum x_FS(p) + x_FS(q) is always less than x_FS(2n) = x_FS(p + q). This is because x_FS is superadditive for primes: the composites between 1 and p contribute their widths to x_FS(p), and similarly for q, but the composites between 1 and p+q include additional wide columns (particularly those between p and q) that inflate x_FS(p+q) beyond the sum.

### 5.2. The FS-x Goldbach alignment

In FS-x coordinates, a Goldbach pair (p, q) with p + q = 2n corresponds to two escape events at FS-x positions x_FS(p) and x_FS(q). The target 2n sits at FS-x position x_FS(2n).

The Goldbach condition is that two escape spires exist whose underlying integers sum to 2n. In the FS-x view, these spires are not necessarily symmetric around x_FS(n) -- the FS-x positions are distorted by the composite corridor between them. But the arithmetic alignment (p + q = 2n) is preserved regardless of the FS-x distortion.

---

## 6. Structural Insights on the Persistence of Goldbach Pairs

### 6.1. The coverage-protection mechanism (Goldbach version)

The same coverage-protection mechanism that operates for twin primes (see `FS_twin_primes.md`) applies to Goldbach pairs, with an important enhancement:

For twin pairs, coverage by width-q (q >= 3) eliminates one member and protects the other. The survival factor is (q-2)/q.

For Goldbach pairs where q | 2n, coverage by width-q has a reduced impact: the two fatal conditions q | r and q | (2n-r) collapse to a single condition. The survival factor improves to (q-1)/q.

**Every odd prime factor of 2n provides additional protection to its Goldbach pairs.** This is the structural reason why highly composite even numbers have the most Goldbach representations: their factors act as shields against coverage elimination.

### 6.2. The structural abundance of Goldbach-open pairs

The Goldbach-open pair count per primorial period grows without bound:

| p  | p#       | Goldbach-open (ordered, for 0 mod p#) |
|----|----------|--------------------------------------|
| 2  | 2        | 1                                    |
| 3  | 6        | 2                                    |
| 5  | 30       | 8                                    |
| 7  | 210      | 48                                   |
| 11 | 2310     | 480                                  |
| 13 | 30030    | 5760                                 |

The count grows by a factor of approximately (q-1) at each step (since the template expands by factor q and the survival rate is ~(q-2)/q for most pairs, giving net growth ~(q-2)). This growth is superlinear, ensuring that the structural availability of Goldbach pairs increases without limit.

### 6.3. Why Goldbach is "easier" than twin primes

The FS framework reveals a structural asymmetry between the twin prime conjecture and Goldbach's conjecture:

**Twin primes** require two consecutive escapes separated by exactly 2. The constraint is positional: the two primes must be adjacent. The number of twin-open positions per primorial period grows, but the positional constraint (gap = 2) is rigid.

**Goldbach pairs** require two escapes that sum to a given target. The constraint is additive: many different (p, q) pairs can satisfy p + q = 2n. The number of Goldbach-open pairs per primorial period grows much faster than the number of twin-open pairs, because the additive constraint allows many more configurations.

Moreover, Goldbach has the **singular series bonus**: when the target 2n is divisible by an odd prime q, the survival factor improves from (q-2)/q to (q-1)/q. Twin primes have no such bonus -- the gap 2 is fixed and does not interact with the prime factors of nearby integers.

This structural asymmetry suggests that Goldbach's conjecture is, in a precise FS-geometric sense, "easier" than the twin prime conjecture: the additive constraint is more permissive than the positional constraint, and the singular series provides additional protection for Goldbach pairs.

### 6.4. The parity barrier in FS terms

Despite the structural abundance, proving Goldbach's conjecture faces the same obstacle as proving the twin prime conjecture: the **parity barrier** of sieve theory.

In FS terms, the parity barrier is the inability to distinguish between:
- An open position occupied by a prime (escape event)
- An open position occupied by a composite with large lpf (covered by a high-width layer)

The primorial template tells us which positions are structurally available. The escape density tells us what fraction should be prime. But converting "positive density of Goldbach-open pairs" into "at least one pair has both members prime" requires ruling out the possibility that every Goldbach-open pair has at least one composite member -- a possibility that the sieve cannot exclude because it cannot detect whether a given open position is prime or composite with large factors.

### 6.5. The FS-geometric Goldbach conjecture

Combining the structural analysis:

> **FS-Goldbach Conjecture:** For every even integer 2n >= 4, the primorial template contains Goldbach-open pairs (structural availability), and at least one such pair has both members escaping all higher-width coverage layers (escape realization). Equivalently: for every even 2n >= 4, there exist escape events p and q with p + q = 2n.

The structural availability is proved (Section 6.2). The escape realization remains open, but the FS framework identifies why it should hold:

1. The Goldbach-open pair count per template period grows without bound.
2. The singular series provides extra protection for highly composite targets.
3. The expected representation count r(2n) grows as 2n/(ln 2n)^2.
4. Powers of 2 are the worst case, but even for them r(2^k) grows exponentially.

The structural obstacles to proof are:
1. The parity barrier prevents sieves from certifying that specific open positions are prime.
2. The escape events at r and 2n-r are not fully independent (they share dependence on the factorization of 2n).

---

## 7. Summary

| Concept | Classical | FS-Geometry |
|---------|-----------|-------------|
| Goldbach pair (p, q) | p + q = 2n, both prime | Two escape events with sum 2n |
| Goldbach-open pair | Not visible | (r, 2n-r) both coprime to p# in the template |
| Singular series S(2n) | Analytic correction factor | Survival bonus from q \| 2n: (q-1)/(q-2) per factor |
| r(2n) ~ C*S*2n/(ln 2n)^2 | Hardy-Littlewood prediction | Template open pairs * escape density squared |
| More factors → more reps | Empirical observation | Each odd factor improves survival from (q-2)/q to (q-1)/q |
| Powers of 2 = hardest case | No odd factors, S = 1 | No singular series bonus; baseline survival only |
| Template persistence | Not visible | Goldbach-open count per period grows without bound |
| Coverage protection | Not visible | q \| 2n merges two fatal classes into one |
| Goldbach vs twin primes | Both open conjectures | Goldbach structurally easier: additive flexibility + singular series |
| Obstacle to proof | Parity barrier | Cannot certify open positions as prime vs large-lpf composite |

Goldbach's conjecture, viewed through the Factor Skyline, is the assertion that the additive structure of the integers -- when lifted into two-dimensional escape geometry -- always provides at least one escape-pair alignment for every even target. The coverage-protection mechanism, the singular series bonus, and the growing abundance of Goldbach-open pairs all make this structurally plausible. The geometry favors Goldbach; only the parity barrier prevents us from crossing from plausibility to proof.
