# Prime Gaps in FS-Geometry

---

## Overview

On the classical number line, a prime gap is the difference g_k = p_{k+1} - p_k between consecutive primes. In the Factor Skyline, prime gaps acquire a richer structure: they are not merely distances but **composite corridors** -- stretches of the skyline paved entirely by wide columns, whose total FS-x extent, internal width composition, and relationship to activation epochs are all visible.

This document develops the FS-geometric theory of prime gaps.

---

## 1. Prime Gaps as Composite Runs in FS-x

### 1.1. Definition

In FS-coordinates, a prime p_k has dx = 1 (escape event). A composite n has dx = lpf(n) >= 2. A **prime gap** is the interval of integers (p_k, p_{k+1}) between consecutive primes. In the skyline, this interval appears as a **composite run**: a contiguous stretch of columns with dx > 1.

The classical gap is:

    g_k = p_{k+1} - p_k

The **FS-x gap** is:

    G_k = x_FS(p_{k+1}) - x_FS(p_k) = 2 + sum_{n=p_k+1}^{p_{k+1}-1} lpf(n)

The 2 accounts for the two dx = 1 contributions from p_k and p_{k+1} themselves. The sum is over the g_k - 1 composites inside the gap.

### 1.2. The amplification effect

The FS-x gap G_k is always larger than the classical gap g_k, because every composite in the gap contributes dx = lpf(n) >= 2 rather than the unit step it would have on the number line. The **amplification ratio** is:

    A_k = G_k / g_k

Numerically, this ratio depends on the width composition of the composites inside the gap. The key structural observation is:

**The amplification ratio is determined by the mean least-prime-factor of the composites in the gap.**

If the mean lpf in the gap is w_bar, then:

    G_k ~ g_k * w_bar

Since at least half the composites in any gap are even (lpf = 2), and roughly a third of the odd composites have lpf = 3, the mean lpf is typically between 3 and 6. Empirically:

- For small gaps (g = 6): A ~ 2.5, driven by the fixed pattern of 3 evens and 2 odds
- For moderate gaps (g = 14-20): A ~ 4-6, as larger widths (5, 7, 11, ...) appear among the composites
- For large gaps near n ~ 10000: A ~ 7-10, reflecting the increasing contribution of wider composites

### 1.3. The anatomy of a gap

Every prime gap of size g contains exactly:

- floor(g/2) - 1 even composites (each contributing dx = 2)
- the remaining composites are odd, with lpf in {3, 5, 7, 11, ...}

The FS-x budget of a gap decomposes as:

    G_k = 2                                    (the two primes)
        + 2 * (number of even composites)       (width-2 columns)
        + 3 * (number of width-3 composites)    (width-3 columns)
        + 5 * (number of width-5 composites)    (width-5 columns)
        + ...

This decomposition is the **width spectrum** of the gap. It reveals internal structure that the classical gap size g_k completely hides.

**Example: g = 6 between primes 23 and 29.**
Composites: 24, 25, 26, 27, 28.
- 24: lpf = 2, dx = 2
- 25: lpf = 5, dx = 5
- 26: lpf = 2, dx = 2
- 27: lpf = 3, dx = 3
- 28: lpf = 2, dx = 2

Width spectrum: w2: 3x (+6), w3: 1x (+3), w5: 1x (+5). Total G = 2 + 6 + 3 + 5 = 16.

**Example: g = 20 between primes 887 and 907.**
Width spectrum: w2: 10x (+20), w3: 3x (+9), w5: 2x (+10), w7: 1x (+7), w17: 1x (+17), w19: 1x (+19), w29: 1x (+29). Total G = 2 + 20 + 9 + 10 + 7 + 17 + 19 + 29 = 113.

The second gap has the same classical size ratio (20/6 ~ 3.3x) but its FS-x ratio is 113/16 ~ 7x, because the larger gap contains composites with much wider columns (widths 17, 19, 29).

---

## 2. Activation Epochs and Gap Constraints

### 2.1. Epochs as frozen-coverage intervals

Recall that activation events at p_k^2 partition the integers into epochs:

    Epoch_k = [p_k^2, p_{k+1}^2)

Within each epoch, the set of active coverage layers is frozen. No new width enters the geometry. The escape density is constant at:

    D(p_k) = prod_{q <= p_k, q prime} (1 - 1/q)

### 2.2. Maximum gap within an epoch

Within Epoch_k, the escape density is D(p_k). The epoch contains |Epoch_k| = p_{k+1}^2 - p_k^2 integers. The expected number of escapes is:

    E_k ~ |Epoch_k| * D(p_k)

For the maximum gap within the epoch, we reason as follows: if primes occur with average density D(p_k), the expected gap between consecutive primes is:

    expected gap ~ 1 / D(p_k)

The maximum gap within the epoch is bounded by the epoch length (no gap can exceed the epoch), but more tightly, a gap of size g can occur only if g consecutive integers all fail to escape. The probability of this (under the independence heuristic from the CRT) is:

    P(gap >= g) ~ (1 - D(p_k))^g ~ exp(-g * D(p_k))

This becomes negligible when g >> 1/D(p_k). The expected maximum gap in an epoch of length L is therefore approximately:

    g_max ~ ln(L) / D(p_k)

This is the FS-geometric version of the Cramer heuristic, derived from the coverage architecture rather than from probabilistic assumptions.

### 2.3. Gaps cannot span activation boundaries easily

A prime gap that straddles an activation boundary at p_{k+1}^2 must survive in two different coverage regimes. Before p_{k+1}^2, the escape density is D(p_k). After p_{k+1}^2, it drops to D(p_{k+1}) = D(p_k) * (1 - 1/p_{k+1}).

The activation of width-p_{k+1} at p_{k+1}^2 removes an additional fraction 1/p_{k+1} of the corridor. This means that a gap extending past the activation boundary faces a *narrower* corridor on the far side -- making it harder for the gap to continue, not easier. Activation events therefore act as **gap terminators**: they introduce fresh coverage that tends to force an escape shortly after the new width enters the geometry.

This is the FS explanation for why very large gaps are rare: they must survive not just within a single frozen-coverage epoch but across activation boundaries that progressively tighten the corridor.

---

## 3. Escape Density and Expected Gap Size

### 3.1. The mean gap from escape density

At scale n, the active coverage layers are those with primes q <= sqrt(n). The escape density is:

    D(sqrt(n)) = prod_{q <= sqrt(n), q prime} (1 - 1/q)

The expected distance between consecutive escapes (primes) near n is the reciprocal:

    E[g] ~ 1 / D(sqrt(n))

By Mertens' theorem:

    1 / D(sqrt(n)) ~ ln(sqrt(n)) / e^{-gamma} = ln(n) / (2e^{-gamma}) ~ 0.89 * ln(n)

This recovers the classical result that the average prime gap near n is approximately ln(n), derived here from the escape density of the skyline rather than from the PNT.

### 3.2. Escape density table and predicted gaps

| Threshold p | D(p)     | 1/D(p) | Relevant scale n = p^2 | ln(n)  |
|-------------|----------|--------|------------------------|--------|
| 2           | 1/2      | 2.00   | 4                      | 1.39   |
| 3           | 1/3      | 3.00   | 9                      | 2.20   |
| 5           | 4/15     | 3.75   | 25                     | 3.22   |
| 7           | 8/35     | 4.38   | 49                     | 3.89   |
| 11          | 16/77    | 4.81   | 121                    | 4.80   |
| 13          | 192/1001 | 5.21   | 169                    | 5.13   |
| 17          | ~0.1805  | 5.54   | 289                    | 5.67   |
| 19          | ~0.1710  | 5.85   | 361                    | 5.89   |
| 23          | ~0.1636  | 6.11   | 529                    | 6.27   |
| 29          | ~0.1579  | 6.33   | 841                    | 6.73   |
| 37          | ~0.1487  | 6.72   | 1369                   | 7.22   |
| 47          | ~0.1387  | 7.21   | 2209                   | 7.70   |

Note that 1/D(p) tracks ln(p^2) = 2*ln(p) closely. This is the FS-geometric content of the ln(n) average gap: it is the reciprocal of the escape density at the relevant activation threshold.

### 3.3. The gap distribution from FS-geometry

The FS framework predicts not just the mean gap but the full distribution. Within an epoch of frozen coverage density D, the probability that a gap exceeds g is:

    P(gap > g) ~ (1 - D)^g ~ exp(-gD)

This is an exponential (geometric) distribution with rate D. The predicted gap distribution at scale n is therefore approximately exponential with mean 1/D(sqrt(n)) ~ ln(n).

Deviations from this distribution arise from two FS-geometric sources:

1. **Discrete width effects.** The escape density is not continuous -- it drops at each activation event. Gaps near activation boundaries see a changing density.
2. **Width correlations.** While the CRT guarantees independence of different width layers, the *positions* of width-p composites have local correlations (e.g., consecutive even numbers are both width-2). These correlations create the twin-prime and primorial patterns that modulate the gap distribution at small scales.

---

## 4. Classical Gaps vs. FS-x Gaps

### 4.1. The transformation formula

The FS-x gap G_k is related to the classical gap g_k by:

    G_k = 2 + sum_{n=p_k+1}^{p_{k+1}-1} lpf(n)

This can be decomposed by width:

    G_k = 2 + sum_{w in active widths} w * (number of composites with lpf = w in the gap)

### 4.2. Asymptotic amplification

For large gaps near scale n, the mean lpf of composites can be estimated from the coverage architecture. The fraction of composites with lpf = q is:

    f(q) = (1/q) * prod_{p < q, p prime} (1 - 1/p)

The mean lpf is therefore:

    w_bar = sum_q q * f(q) / sum_q f(q)

The denominator is 1 - D(sqrt(n)) (the total fraction of composites), and the numerator is:

    sum_{q <= sqrt(n)} prod_{p < q} (1 - 1/p)

Each term in this sum is a "weight-1" contribution (q * 1/q * prod(1-1/p) = prod(1-1/p) for p < q), so:

    w_bar ~ (1 / (1 - D(sqrt(n)))) * sum_{q <= sqrt(n)} prod_{p < q} (1 - 1/p)

For large n, D(sqrt(n)) -> 0 and the sum grows, so the mean width grows slowly with n. This is why the amplification ratio A_k = G_k / g_k increases with scale: larger composites (with larger least prime factors) become more common as the skyline extends.

### 4.3. What FS-x gaps reveal that classical gaps hide

Classical gap: g = 14 between 113 and 127.
FS-x gap: G = 49. Width spectrum: w2:7, w3:2, w5:2, w7:1, w11:1.

Classical gap: g = 14 between 293 and 307.
FS-x gap: G = 51. Width spectrum: w2:7, w3:2, w5:2, w7:1, w13:1.

These two gaps have the **same classical size** (g = 14) but different FS-x sizes (49 vs 51) and different width spectra. The difference comes from a single composite: in the first gap, 121 = 11^2 contributes dx = 11; in the second gap, 299 = 13 * 23 contributes dx = 13. The FS-x gap detects this structural difference; the classical gap does not.

---

## 5. Structural Bounds from FS-Geometry

### 5.1. Lower bound on gaps (trivial)

The minimum gap between primes > 2 is g = 2 (twin primes). In FS-x, a gap of g = 2 means the single composite between the two primes has some width w, giving G = 2 + w. The minimum FS-x gap for twin primes above 3 is G = 4 (the composite is even, w = 2).

### 5.2. Upper bound: the epoch bound

No prime gap within Epoch_k = [p_k^2, p_{k+1}^2) can exceed the epoch length:

    g_k < p_{k+1}^2 - p_k^2 = (p_{k+1} + p_k)(p_{k+1} - p_k)

By Bertrand's postulate, p_{k+1} < 2*p_k, so:

    g_k < (3*p_k)(p_k) = 3*p_k^2

This is a weak bound, but it comes directly from the FS architecture: within a single epoch, the frozen coverage density D(p_k) > 0 guarantees that escapes must occur, and the epoch length bounds how far apart they can be.

### 5.3. The Cramer-FS bound

The FS-geometric analogue of Cramer's conjecture arises from the observation that within an epoch of length L and escape density D, the longest expected composite run is:

    g_max ~ ln(L) / D ~ ln(L) * ln(p_k) / e^{-gamma}

At scale n, where p_k ~ sqrt(n), this gives:

    g_max ~ ln(n) * ln(sqrt(n)) ~ (1/2) * (ln(n))^2

This matches Cramer's conjecture that the largest prime gap below n is O((ln n)^2). In the FS framework, this bound arises from the interplay of epoch length and escape density: the corridor is narrow (density ~ 1/ln(n)), but the epoch is long enough that a run of ln(n) non-escapes is the longest plausible drought.

### 5.4. The primorial lower bound on gap occurrence

The FS ontology also predicts which gap sizes are structurally favored. The coverage layers create a repeating pattern with period equal to the primorial:

    P_k = p_1 * p_2 * ... * p_k = 2 * 3 * 5 * ... * p_k

Within each primorial period, the pattern of covered and uncovered positions is identical. The gaps within this pattern are determined by the combined coverage of all active widths.

The largest gap in the primorial pattern is the **maximal primorial gap** -- the longest run of consecutive integers divisible by at least one of 2, 3, 5, ..., p_k. This gap grows with each new prime added to the primorial and determines the structurally "dominant" gap size at that scale.

The sequence of dominant gap sizes follows the primorial sequence:

- After width-2 and width-3 activate: dominant gap = 6 = 2 * 3 (the most common gap for small primes)
- After width-5 activates: dominant gap = 30 = 2 * 3 * 5
- After width-7 activates: dominant gap = 210 = 2 * 3 * 5 * 7

This is the FS-geometric explanation of the empirical observation that the most common prime gap shifts through primorial values as the scale increases. The primorial is the period of the combined coverage pattern, and the dominant gap is the longest uncoverable stretch within that period.

---

## 6. Summary

| Concept | Classical | FS-Geometry |
|---------|-----------|-------------|
| Prime gap | g = p_{k+1} - p_k | Composite run: stretch of dx > 1 columns |
| Gap size | A single integer | Width spectrum: decomposition by lpf |
| Mean gap | ~ ln(n) | ~ 1/D(sqrt(n)), projected to ln(n) via Mertens |
| Max gap | Cramer: O((ln n)^2) | Epoch length / escape density |
| Gap distribution | Exponential with mean ln(n) | Geometric with rate D(sqrt(n)) |
| Dominant gaps | Primorial values (6, 30, 210, ...) | Period of combined coverage pattern |
| Two gaps of same size | Indistinguishable | Distinguished by width spectrum |
| Gap constraint | None visible | Activation epochs bound gap extent |

The FS-x gap is not merely a scaled version of the classical gap. It carries structural information -- the width spectrum -- that reveals the internal composition of the composite corridor. Two gaps of the same classical size can have different FS-x sizes because the composites they contain have different factorization structures.

Prime gaps in the Factor Skyline are architectural features of the corridor between escape events, shaped by the cumulative coverage of all active width layers.
