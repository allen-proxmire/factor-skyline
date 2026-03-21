# Short-Interval Prime Theorems in FS-Geometry: Square Windows and the Chebyshev-Bertrand Corridor

---

## Overview

Classical short-interval prime theorems ask: how many primes lie in a window [x, x+h] for various choices of h? The two most natural windows are:

- **The square window:** [n^2, (n+1)^2), length 2n+1. Legendre's conjecture (still unproved) asserts this always contains a prime.
- **The Bertrand window:** [n, 2n], length n. Bertrand's postulate (proved by Chebyshev, 1852) guarantees at least one prime.

In the Factor Skyline, both windows acquire geometric meaning. The square window is special because it spans the interval between two potential activation thresholds. The Bertrand window is special because its width exactly matches the scale at which escape density is evaluated. Both are governed by the same mechanism: activation, coverage, and escape.

This document derives the FS-geometric theory of short-interval prime distribution.

---

## 1. The Square Window in FS-Geometry

### 1.1. Definition and structure

The **square window** at n is the interval [n^2, (n+1)^2), containing exactly 2n+1 integers (including the left endpoint, excluding the right). In FS-x coordinates, this window maps to a stretch of the x-axis:

    X_sq(n) = x_FS((n+1)^2 - 1) - x_FS(n^2)
            = sum_{m=n^2+1}^{(n+1)^2-1} dx(m)

The width spectrum of this stretch decomposes by coverage layer, just as for prime gaps (see `FS_prime_gaps.md`). Numerically, for the window [100, 121):

| Width | Columns | dx contribution |
|-------|---------|-----------------|
| w2    | 11      | 22              |
| w3    | 3       | 9               |
| w5    | 1       | 5               |
| w7    | 1       | 7               |
| escape| 5       | 5               |
| **Total** | **21** | **48**      |

The 21 integers occupy 48 units of FS-x space. The escape events (primes 101, 103, 107, 109, 113) contribute dx = 1 each; the composites contribute their widths. The FS-x extent is roughly 2.3 times the classical window length.

### 1.2. The width spectrum is template-governed

The width-2, width-3, and width-5 column counts within a square window are approximately determined by the primorial template. In a window of length 2n+1:

- Width-2 columns: approximately (2n+1)/2 = n (the even integers)
- Width-3 columns: approximately (2n+1)/6 (the odd multiples of 3)
- Width-5 columns: approximately (2n+1)/30 * 2 (the integers coprime to 6 but divisible by 5)

These template-level counts are stable across windows at the same scale. What varies between windows is the distribution of the **open positions** (integers coprime to all small primes) between escapes and higher-width composites.

### 1.3. The FS-x extent grows with scale

As n increases, the FS-x extent of the square window grows faster than 2n+1 because:

1. The template contributions are fixed proportionally (they scale with 2n+1).
2. The open positions increasingly contain composites with large lpf rather than primes, and these composites have larger dx.

Numerically:

| n   | Window length | FS-x extent | Ratio |
|-----|--------------|-------------|-------|
| 10  | 21           | 46          | 2.2   |
| 20  | 41           | 132         | 3.2   |
| 30  | 61           | 216         | 3.5   |
| 50  | 101          | 502         | 5.0   |
| 70  | 141          | 518         | 3.7   |

The ratio fluctuates but trends upward, reflecting the increasing mean width of composites at higher scales.

---

## 2. Why Activation at p^2 Makes Square Windows Natural

### 2.1. Activation thresholds are squares

In the FS ontology, the prime p activates at p^2. The activation sequence is:

    4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, ...

These are the squares of primes. Between consecutive activation thresholds p_k^2 and p_{k+1}^2, the coverage configuration is frozen -- no new width enters the geometry.

### 2.2. Square windows straddle at most one activation

The square window [n^2, (n+1)^2) has length 2n+1. An activation event at p^2 falls inside this window if and only if n < p < n+1, which is impossible for integer n (since p would be a non-integer). Therefore:

**No activation event falls strictly inside a square window [n^2, (n+1)^2) when n is a positive integer.**

But an activation event can occur at the boundary: if n = p for some prime p, then p^2 = n^2 is the left endpoint of the window, and the activation of width-p occurs at the window's start.

This means every square window lives within a single activation epoch (or starts at an epoch boundary). The coverage density is constant (or changes only at the first integer). This is the structural reason why square windows are the natural FS scale: **they are the largest windows guaranteed to experience at most one activation event.**

### 2.3. The general square gap 2n+1 vs. the prime-square gap

For general n, the window [n^2, (n+1)^2) always has length 2n+1. For consecutive prime squares, the epoch [p_k^2, p_{k+1}^2) has length:

    p_{k+1}^2 - p_k^2 = (p_{k+1} + p_k)(p_{k+1} - p_k)

This is much larger than a single square window (which has length ~2p_k). The epoch contains approximately p_{k+1} - p_k consecutive square windows. Since the prime gap g_k = p_{k+1} - p_k is typically small (O(ln p_k)), each epoch contains O(ln p_k) square windows -- all sharing the same frozen coverage configuration.

---

## 3. Escape Density Predicts the Prime Count

### 3.1. The prediction formula

At scale n, the active coverage layers are the widths q for all primes q <= n (since the relevant threshold is sqrt(n^2) = n). The escape density is:

    D(n) = prod_{q <= n, q prime} (1 - 1/q)

The expected number of primes in the square window [n^2, (n+1)^2) is:

    E[primes] = (2n+1) * D(n)

### 3.2. Numerical verification

| n   | Window length | D(n)   | Predicted | Actual | Ratio |
|-----|--------------|--------|-----------|--------|-------|
| 2   | 5            | 0.5000 | 2.5       | 2      | 0.80  |
| 5   | 11           | 0.2667 | 2.9       | 2      | 0.68  |
| 10  | 21           | 0.2286 | 4.8       | 5      | 1.04  |
| 15  | 31           | 0.1918 | 5.9       | 6      | 1.01  |
| 20  | 41           | 0.1710 | 7.0       | 7      | 1.00  |
| 25  | 51           | 0.1636 | 8.3       | 8      | 0.96  |
| 30  | 61           | 0.1579 | 9.6       | 8      | 0.83  |
| 35  | 71           | 0.1529 | 10.9      | 10     | 0.92  |
| 39  | 79           | 0.1487 | 11.7      | 11     | 0.94  |

The prediction (2n+1) * D(n) tracks the actual prime count with typical accuracy of 10-20%. The ratio fluctuates around 0.85-1.05, consistent with the known overcounting of the Legendre sieve (factor ~2e^{-gamma} ~ 1.12) tempered by finite-size effects.

### 3.3. Asymptotic form

By Mertens' theorem, D(n) ~ e^{-gamma}/ln(n). Therefore:

    E[primes in [n^2, (n+1)^2)] ~ (2n+1) * e^{-gamma}/ln(n) ~ 2e^{-gamma} * n/ln(n)

For large n, this grows without bound. The expected prime count in a square window grows like n/ln(n), which goes to infinity. This is the FS-geometric content of the (heuristic) expectation behind Legendre's conjecture: the escape density, applied to a window of width 2n+1, predicts a prime count that increases without bound.

### 3.4. The minimum prime count

Up to n = 999, the minimum number of primes in any square window is 2 (at n = 2, the window [4, 9) contains primes 5 and 7). No empty square window has been found. The FS prediction for this minimum is D(2) * 5 = 2.5, consistent with the observed value.

Legendre's conjecture (that no square window is empty) corresponds to the FS statement that the escape corridor is never simultaneously empty across all 2n+1 positions of a square window. As established in the ontology, the escape density is always positive and the window width grows, so the expected count grows -- but converting this heuristic into a proof requires bounding the variance, which the FS framework identifies but does not resolve.

---

## 4. The FS-Geometric Reformulation of Bertrand's Postulate

### 4.1. Bertrand in classical terms

Bertrand's postulate states: for every integer n > 1, there exists a prime p with n < p < 2n.

The Bertrand window [n+1, 2n) has length n-1, which is much larger than the square window of length 2sqrt(n)+1 at the same scale. Bertrand is therefore a weaker statement than Legendre -- the window is wider, making it easier to guarantee a prime.

### 4.2. Three FS reformulations

**Form A — Escape corridor non-emptiness:**

> For every n > 1, the interval [n+1, 2n) on the number line, which maps to the FS-x corridor [x_FS(n+1), x_FS(2n)], contains at least one escape event (a column with dx = 1 and y_FS = p for some prime p).

**Form B — Epoch-relative guarantee:**

> Within any activation epoch [p_k^2, p_{k+1}^2), the Bertrand window [n, 2n] for any n in the epoch is contained within the interval [p_k^2, 2*p_{k+1}^2). The frozen escape density D(p_k) applied to a window of length n guarantees:
>
>     E[primes] = n * D(p_k)
>
> which exceeds 1 for all n > 1/D(p_k) ~ ln(p_k). Since n >= p_k^2 >> ln(p_k) within the epoch, the expected count is much larger than 1.

**Form C — Coverage cannot pave a doubling window:**

> The combined coverage layers of all primes up to sqrt(2n) cannot pave the entire interval [n+1, 2n). Equivalently, the composite columns in this interval, despite having total FS-x width much larger than n, cannot fill the interval without leaving at least one gap of width 1 (an escape).

### 4.3. Why Bertrand is structurally inevitable in FS-geometry

The FS proof sketch proceeds as follows:

**(i) The escape density at scale n is D(sqrt(n)) > 0.**

This is always positive because D(p) is a finite product of terms strictly less than 1 but strictly greater than 0.

**(ii) The Bertrand window has length n-1.**

The expected number of escapes is:

    E = (n-1) * D(sqrt(2n)) ~ (n-1) * e^{-gamma}/ln(sqrt(2n)) = (n-1) * 2e^{-gamma}/ln(2n)

For n >= 3, this exceeds 1. For large n, it grows like n/ln(n), ensuring many primes.

**(iii) The key structural point: coverage layers are too thin to pave a doubling window.**

Each active width-q layer covers fraction 1/q of the integers. The total fraction covered by all layers up to sqrt(2n) is:

    1 - D(sqrt(2n)) = 1 - prod(1 - 1/q)

This is less than 1 for any finite set of layers. The uncovered fraction D(sqrt(2n)) > 0 guarantees that a positive density of the window escapes. In a window of length n, this means at least ~n * D(sqrt(2n)) ~ n/ln(n) escape events.

The doubling structure of [n, 2n] is significant: it ensures the window length is always proportional to n itself, which is much larger than the typical gap between primes (~ln n). No matter how narrow the escape corridor becomes, a window of length n always contains ~n/ln(n) >> 1 primes.

### 4.4. Comparison: square window vs. Bertrand window

| Feature | Square window [n^2, (n+1)^2) | Bertrand window [n, 2n] |
|---------|------------------------------|------------------------|
| Length | 2n+1 | n |
| Scale parameter | n^2 | n |
| At the same number-line position m: | length ~ 2sqrt(m) | length ~ m |
| Expected primes | (2n+1)*D(n) ~ 2n/ln(n) | n*D(sqrt(n)) ~ n/ln(n) |
| Activation events inside | At most 1 (boundary only) | Potentially several |
| Coverage regime | Frozen (single epoch) | May span multiple epochs |
| Conjecture status | Legendre (open) | Bertrand (proved) |

The square window is the **structurally pure** interval: it lives within one coverage regime. The Bertrand window is the **robustly large** interval: it is wide enough to guarantee primes regardless of local fluctuations.

At the same number-line position m = n^2, the Bertrand window [n^2, 2n^2] has length n^2, while the square window has length 2n+1. The Bertrand window is ~n/2 times wider. This is why Bertrand is provable and Legendre is not: the extra width provides overwhelming statistical margin.

---

## 5. Structural Insights from the FS Short-Interval Theory

### 5.1. The activation-epoch hierarchy of short intervals

The FS framework reveals a natural hierarchy of short intervals, ordered by their relationship to activation events:

**Level 0: Sub-activation intervals (length < 2n+1).**
These fit inside a single square window and therefore inside a single activation epoch. The coverage density is frozen throughout. Primality within these intervals is governed entirely by the primorial template at the current activation level.

**Level 1: Square windows (length = 2n+1).**
These span exactly one square step and encounter at most one activation boundary. They are the largest intervals guaranteed to have a uniform coverage regime. Legendre's conjecture is the assertion that Level-1 intervals always contain escapes.

**Level 2: Activation epochs (length = p_{k+1}^2 - p_k^2 ~ 2p_k * g_k).**
These span the interval between consecutive prime-square activations. Within each epoch, coverage is frozen. The epoch contains O(g_k) square windows, all sharing the same escape density. The assertion that every epoch contains at least one escape is weaker than Legendre but still unproved in general (it follows from known results for small prime gaps but not unconditionally).

**Level 3: Bertrand windows (length = n).**
These are wide enough to span multiple activation epochs. New coverage layers may activate during the window, but each new layer removes only a fraction 1/p of the remaining corridor, which is never enough to close it entirely. The width of the window (proportional to n) overwhelms the narrowing of the corridor (proportional to 1/ln(n)).

**Level 4: PNT-scale intervals (length = n/ln(n) or larger).**
These are the shortest intervals for which the PNT guarantees a prime (by the result of Hoheisel, Ingham, and subsequent refinements). The FS interpretation is that the corridor narrowing and the interval width are in exact balance.

### 5.2. The square window as the FS natural unit

The square window [n^2, (n+1)^2) is the natural "pixel" of the Factor Skyline, for three reasons:

1. **Activation alignment.** It encounters at most one activation event and therefore has a nearly uniform coverage density. It is the largest interval with this property.

2. **Scale matching.** Its length 2n+1 matches the scale at which n itself measures the activation threshold. The escape density D(n), evaluated at the same parameter that defines the window, directly predicts the prime count.

3. **Geometric meaning.** In the skyline, the square window corresponds to the vertical strip above the "step" from height n to height n+1 in the activation staircase. It is the region of the skyline where the geometry transitions from one activation level to the next.

The square window is to the Factor Skyline what the unit cell is to a crystal lattice: the minimal region that captures the local structure of the geometry.

### 5.3. The corridor-narrowing race

The FS framework reveals a fundamental race between two competing effects in short intervals:

**Widening force:** As n increases, the square window grows (length 2n+1) and the Bertrand window grows (length n). Both provide more space for escapes.

**Narrowing force:** As n increases, more coverage layers activate, and D(n) decreases. The escape corridor becomes thinner.

The race is governed by the product:

    E[primes] = (window length) * D(activation threshold)

For the square window: (2n+1) * D(n) ~ 2n * e^{-gamma}/ln(n) -> infinity.
For the Bertrand window: n * D(sqrt(n)) ~ n * 2e^{-gamma}/ln(n) -> infinity.

In both cases, the widening force wins decisively. The window length grows linearly while the escape density decays only logarithmically. The corridor narrows, but not fast enough to overcome the growing window.

This is the structural reason why Bertrand's postulate holds (and why Legendre's conjecture is almost certainly true): **linear growth always beats logarithmic decay.** The FS framework makes this race visible as a competition between window width (a geometric quantity) and escape density (a coverage quantity).

### 5.4. Why the constant 2 in Bertrand is not special

Bertrand's postulate guarantees a prime in [n, 2n] -- a window obtained by *doubling*. But the FS analysis shows nothing special about the factor 2. The expected prime count in [n, cn] for any constant c > 1 is:

    E = (c-1)*n * D(sqrt(cn)) ~ (c-1)*n * 2e^{-gamma}/ln(cn)

This grows without bound for any fixed c > 1. The doubling factor 2 gives a particularly clean statement, but the FS mechanism guarantees primes in [n, cn] for any c > 1 and sufficiently large n.

The true structural threshold is not a multiplicative constant but an additive one: the shortest interval [n, n+h] guaranteed to contain a prime. The FS framework predicts this threshold is h ~ C*(ln n)^2 (the Cramer-scale interval), because the escape corridor of density ~1/ln(n) needs a window of width ~ln(n)/D ~ (ln n)^2 to be guaranteed non-empty. This is the FS-geometric content of Cramer's conjecture.

### 5.5. The FS bridge between Legendre and Bertrand

The FS framework reveals a continuum between the Legendre and Bertrand scales:

- Legendre asks about windows of width 2n+1 at position n^2. In FS terms: one square step, frozen coverage.
- Bertrand asks about windows of width n at position n. In FS terms: a doubling window, multiple epochs.

At position m on the number line:
- The Legendre window has width 2sqrt(m) + 1.
- The Bertrand window has width m.

The ratio is m / (2sqrt(m)) = sqrt(m)/2, which grows without bound. Bertrand provides sqrt(m)/2 times more room than Legendre.

The FS framework suggests a natural interpolation: for any exponent alpha in (1/2, 1), consider windows of width m^alpha at position m. The expected prime count is:

    E ~ m^alpha * D(sqrt(m)) ~ m^alpha / ln(m)

This grows for any alpha > 0, but proving it requires progressively stronger control over the escape corridor's local behavior:

| Window width | alpha | Status | FS interpretation |
|-------------|-------|--------|-------------------|
| m           | 1     | Proved (Bertrand) | Overwhelming margin |
| m^{0.525}   | 0.525 | Proved (Baker-Harman-Pintz) | Strong corridor control |
| m^{1/2+eps} | 1/2+eps | Proved (Ingham-type) | Epoch-crossing with margin |
| 2sqrt(m)+1  | 1/2   | Open (Legendre) | Single epoch, no margin |
| (ln m)^2    | 0+    | Open (Cramer) | Corridor-width scale |

Each step down in alpha requires finer control over the corridor's behavior within shorter intervals. The FS framework identifies the structural obstacle: at the Legendre scale, the window length matches the epoch length, so there is no room for the coverage fluctuations to average out.

---

## 6. Summary

| Concept | Classical | FS-Geometry |
|---------|-----------|-------------|
| Square window [n^2, (n+1)^2) | Interval of length 2n+1 | Single activation step; frozen coverage |
| Bertrand window [n, 2n] | Interval of length n | Doubling window; multi-epoch |
| Activation at p^2 | Trial division bound | Width-p layer enters the skyline |
| Expected primes in square window | ~2n/ln(n) | (2n+1)*D(n) via escape density |
| Expected primes in Bertrand window | ~n/ln(n) | n*D(sqrt(n)) via escape density |
| Legendre's conjecture | Every square window has a prime | Escape corridor non-empty in every activation step |
| Bertrand's postulate | Every doubling window has a prime | Coverage too thin to pave a doubling interval |
| Why Bertrand holds | Analytic (Chebyshev's proof) | Linear growth beats logarithmic decay |
| Natural FS unit | Not apparent classically | The square window is the skyline's unit cell |
| Cramer's conjecture | Largest gap ~ (ln n)^2 | Corridor width 1/ln(n) times gap ~ ln(n) |
| Interpolation Legendre-Bertrand | Baker-Harman-Pintz scale | Exponent alpha between 1/2 and 1 |

The Factor Skyline reveals that short-interval prime theorems are statements about the escape corridor's behavior over specific window sizes. The square window is the natural unit (aligned with activation), the Bertrand window is the robust unit (wide enough to overwhelm corridor narrowing), and the hierarchy between them is governed by the race between linear window growth and logarithmic density decay.
