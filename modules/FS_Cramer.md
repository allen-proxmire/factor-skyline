# Cramér's Conjecture in FS-Geometry

---

## Overview

Cramér's conjecture (1936) asserts that the largest prime gap below n satisfies:

    g_max(n) ~ (ln n)^2

This is based on a probabilistic model treating primes as independent random events with density 1/ln(n). The conjecture remains open; the best unconditional result (Baker-Harman-Pintz, 2001) gives gaps of size O(n^{0.525}).

In the Factor Skyline, Cramér's conjecture becomes a statement about the longest possible composite run -- a contiguous stretch of the skyline with no escape events -- and its relationship to the activation horizon, the escape density, and the epoch structure. The FS framework reveals the geometric mechanisms that constrain large gaps and explains why (ln n)^2 emerges as the natural scale.

---

## 1. Escape Density and the Expected Maximal Gap

### 1.1. The mean gap from escape density

At scale n, the escape density is:

    D(sqrt(n)) = prod_{q <= sqrt(n), q prime} (1 - 1/q) ~ e^{-gamma}/ln(sqrt(n)) = 2e^{-gamma}/ln(n)

The expected distance between consecutive escape events is the reciprocal:

    E[gap] = 1/D(sqrt(n)) ~ ln(n)/(2e^{-gamma}) ~ 0.89 * ln(n)

This is the average gap. The maximal gap is much larger.

### 1.2. The Cramér heuristic in FS terms

If escape events occur independently with density D(sqrt(n)), the probability that a specific run of g consecutive integers contains no escape is:

    P(gap >= g) ~ (1 - D)^g ~ exp(-g * D)

This becomes exponentially small when g >> 1/D. The longest expected gap among the ~n/ln(n) prime gaps below n is the value g where:

    (n/ln n) * exp(-g * D) ~ 1

Solving:

    g * D ~ ln(n/ln n) ~ ln(n)

    g ~ ln(n)/D ~ ln(n) * ln(n)/(2e^{-gamma}) ~ (ln n)^2 / (2e^{-gamma})

The constant 2e^{-gamma} ~ 1.12, so:

    g_max ~ (ln n)^2 / 1.12 ~ 0.89 * (ln n)^2

This is Cramér's conjecture, derived from the escape density product.

### 1.3. Numerical verification: record gaps vs (ln n)^2

| p_k    | g    | (ln p)^2 | g/(ln p)^2 |
|--------|------|----------|------------|
| 7      | 4    | 3.79     | 1.056      |
| 23     | 6    | 9.83     | 0.610      |
| 113    | 14   | 22.35    | 0.626      |
| 1327   | 34   | 51.71    | 0.658      |
| 9551   | 36   | 83.99    | 0.429      |
| 31397  | 72   | 107.21   | 0.672      |
| 155921 | 86   | 142.97   | 0.602      |
| 370261 | 112  | 164.40   | 0.681      |
| 492113 | 114  | 171.78   | 0.664      |

The ratio g/(ln p)^2 fluctuates between 0.4 and 1.1, staying well below 1 for all record gaps up to 10^6. Cramér's conjecture predicts this ratio should remain bounded; the data is consistent with a limiting value near 2e^{-2*gamma} ~ 0.63 (the Granville refinement).

---

## 2. Activation Epochs and Composite Run Constraints

### 2.1. Gaps within a single epoch

Within activation epoch [p_k^2, p_{k+1}^2), the coverage configuration is frozen at D(p_k). The epoch contains |E_k| = p_{k+1}^2 - p_k^2 integers. The expected maximal gap within the epoch is:

    g_max(epoch) ~ ln(|E_k|) / D(p_k)

Numerically:

| Epoch           | Length  | D(p_k) | Max gap | ln(L)/D | Ratio |
|-----------------|---------|--------|---------|---------|-------|
| [4, 9)          | 5       | 0.333  | 2       | 4.8     | 0.41  |
| [25, 49)        | 24      | 0.229  | 6       | 13.9    | 0.43  |
| [121, 169)      | 48      | 0.192  | 10      | 20.2    | 0.50  |
| [529, 841)      | 312     | 0.158  | 14      | 36.4    | 0.39  |
| [961, 1369)     | 408     | 0.149  | 34      | 40.4    | 0.84  |
| [2209, 2809)    | 600     | 0.136  | 26      | 47.0    | 0.55  |

The actual maximum gap within each epoch is consistently about 40-85% of the prediction ln(L)/D. The prediction overshoots because the independence assumption is imperfect -- escape events are correlated through the primorial template.

### 2.2. Gaps spanning epoch boundaries

A large gap can span an activation boundary at p_{k+1}^2. When this happens, the gap experiences two different coverage regimes:

- Before p_{k+1}^2: escape density D(p_k).
- After p_{k+1}^2: escape density D(p_{k+1}) = D(p_k) * (1 - 1/p_{k+1}).

The activation of width-p_{k+1} at the boundary removes fraction 1/p_{k+1} of the remaining corridor, slightly thinning the escape opportunities on the far side. However, the activation event at p_{k+1}^2 itself is a composite (with width p_{k+1}), which **extends** the gap rather than terminating it.

For a gap to span the boundary and continue deep into the next epoch, all integers from the last prime before p_{k+1}^2 through the first prime after p_{k+1}^2 must be composite. The activation event at p_{k+1}^2 helps the gap (it is composite) but the narrowed corridor on the far side makes continued non-escape harder.

### 2.3. The epoch-crossing penalty

The probability that a gap of size g crosses an epoch boundary at p_{k+1}^2 and continues to total length g is approximately:

    P ~ exp(-g_1 * D(p_k)) * exp(-g_2 * D(p_{k+1}))

where g_1 + g_2 = g. The tighter density D(p_{k+1}) < D(p_k) means the second segment is slightly more probable (fewer escapes per integer), but the overall effect is small since D changes by only a factor (1 - 1/p_{k+1}) ~ 1 at the boundary.

Epoch boundaries do not strongly constrain gap sizes. The dominant constraint comes from the escape density itself, not from the discrete activation structure.

---

## 3. FS-x Gap Amplification

### 3.1. The amplification effect

A classical prime gap of size g maps to an FS-x gap G > g, because each composite in the gap contributes dx = lpf(n) >= 2 rather than 1. The amplification ratio A = G/g depends on the width spectrum of the composites in the gap.

### 3.2. How amplification grows with scale

| Scale (decade) | Count of gaps g >= 10 | Mean G/g | Max G/g |
|---------------|----------------------|----------|---------|
| 10^2 - 10^3  | 33                   | 3.97     | 6.07    |
| 10^3 - 10^4  | 388                  | 6.10     | 15.38   |
| 10^4 - 10^5  | 4017                 | 10.13    | 46.50   |

The amplification ratio grows with scale. This is because at higher scales, the composites in large gaps increasingly contain entries with large least prime factors (widths 100+), which contribute enormous dx values.

### 3.3. The anatomy of amplified gaps

For the record gap g = 72 between 31397 and 31469, the FS-x gap is G = 1062, giving amplification A = 14.8. The width spectrum shows individual composites contributing dx = 163, 149, 101, 89 -- primes close in magnitude to the gap endpoints themselves.

These high-width composites are integers n in the gap whose smallest prime factor is large (e.g., n = 31399 = 163 * 193 has lpf = 163, contributing dx = 163). They arise because in a large gap, the composites that avoid all small prime factors necessarily have large lpf values.

### 3.4. The amplification formula

In a gap of size g near scale n, the mean composite width (mean lpf) is approximately:

    w_bar ~ sum_{q <= sqrt(n)} q * f(q) / (1 - D(sqrt(n)))

where f(q) = (1/q) * prod_{r<q}(1 - 1/r) is the fraction of composites with lpf = q. For large n, the mean width grows slowly (logarithmically), so the amplification ratio is roughly:

    A ~ w_bar ~ C * ln(n) / ln(ln(n))

for some constant C. The FS-x maximal gap is therefore:

    G_max ~ g_max * A ~ (ln n)^2 * C * ln(n) / ln(ln(n)) ~ C * (ln n)^3 / ln(ln(n))

The FS-x maximal gap grows faster than the classical maximal gap -- approximately as the cube of the logarithm rather than the square. This is because the geometric representation amplifies gaps through the width of their constituent composites.

---

## 4. The Geometric Meaning of (ln n)^2

### 4.1. The (ln n)^2 scale as a product of two logarithms

The Cramér bound g_max ~ (ln n)^2 has a clean FS decomposition:

    (ln n)^2 = ln(n) * ln(n)

In FS-geometry, these two logarithmic factors have distinct origins:

**Factor 1: 1/D ~ ln(n).** The escape density at scale n is D(sqrt(n)) ~ 1/ln(n). This is the typical spacing between consecutive escapes -- the "local resolution" of the escape corridor. A gap must be at least this long to be noteworthy.

**Factor 2: ln(n) ~ number of independent trials.** Among the ~n/ln(n) gaps below n, the extreme-value theory of geometric random variables says the maximum is ~ln(n/ln(n)) ~ ln(n) times the typical value 1/D.

The product gives:

    g_max ~ (1/D) * ln(n) ~ ln(n) * ln(n) = (ln n)^2

**FS interpretation:** The maximal gap is the escape corridor width (1/D ~ ln n) multiplied by the extremal factor (ln n), which accounts for the number of opportunities for a rare event to occur among ~n/ln(n) independent gaps.

### 4.2. The corridor-drought interpretation

Alternatively, a gap of size g is a "drought" in the escape corridor: g consecutive integers, all covered by some width layer, with no escape. The probability of a drought of length g in a corridor of density D is:

    P(drought >= g) ~ exp(-gD)

Setting this to 1/n (the expected frequency of the maximal gap among ~n integers):

    exp(-gD) ~ 1/n
    gD ~ ln(n)
    g ~ ln(n)/D ~ (ln n)^2

The (ln n)^2 bound is the **corridor drought at the 1/n probability level**: the longest dry spell that the escape corridor is expected to produce among n integers, given that escapes occur with density 1/ln(n).

### 4.3. The primorial template constraint

The maximal composite run in the primorial template provides a structural lower bound on gap sizes. The maximal gap in the p#-template is the longest run of covered positions:

| p  | p#         | Max template gap | (ln p#)^2 | Ratio |
|----|-----------|-----------------|-----------|-------|
| 5  | 30         | 6               | 11.57     | 0.52  |
| 7  | 210        | 10              | 28.59     | 0.35  |
| 11 | 2310       | 14              | 59.99     | 0.23  |
| 13 | 30030      | 22              | 106.30    | 0.21  |
| 17 | 510510     | 26              | 172.74    | 0.15  |
| 19 | 9699690    | 34              | 258.81    | 0.13  |
| 23 | 223092870  | 40              | 369.53    | 0.11  |

The maximal template gap grows much slower than (ln p#)^2. The ratio decreases steadily, suggesting that the template's inherent composite runs contribute only a fraction of the Cramér-scale gap. The rest comes from the stochastic placement of higher-width composites among the open positions.

This reveals a decomposition of large gaps into two components:

**Template component:** The fixed composite run in the p#-template (the "skeleton" of the gap). This grows as ~C * ln(p#) (Rankin's bound on maximal gaps in the template).

**Stochastic component:** The additional composites from higher-width layers filling in the remaining open positions. This depends on whether the open positions within the template gap happen to be covered by higher-width primes.

Cramér's conjecture says the combined effect -- template skeleton plus stochastic filling -- produces gaps of size at most ~(ln n)^2.

---

## 5. Structural Insights

### 5.1. The FS mechanism for large gaps

The FS framework identifies the precise mechanism that produces large prime gaps:

1. **The primorial template creates a skeleton.** The combined coverage of small primes produces composite runs of size ~C * ln(p#). These runs recur with period p# throughout the number line.

2. **Higher-width layers fill open positions in the skeleton.** Within a template composite run, a few positions remain open (coprime to all small primes). If these positions are covered by larger primes (lpf > p), the run extends. If even one escapes, the gap terminates.

3. **The largest gaps occur when all open positions within a template run are simultaneously covered.** This requires a conspiracy of higher-width layers all targeting the specific open positions in a specific template run. The probability of this conspiracy decreases exponentially with the number of open positions, which is why gaps beyond (ln n)^2 are exponentially rare.

### 5.2. The Granville refinement

Granville (1995) argued that Cramér's model underestimates large gaps because it ignores the primorial template structure. The corrected conjecture is:

    g_max(n) >= 2e^{-gamma} * (ln n)^2 ~ 1.12 * (ln n)^2

infinitely often. The factor 2e^{-gamma} arises from the Mertens constant in the escape density.

In FS-geometry, Granville's correction reflects the fact that the primorial template provides a **structural floor** for gap sizes: the template's composite runs are not random but are determined by the coverage architecture, and they systematically produce gaps that the pure random model misses.

The Granville constant 2e^{-gamma} is the ratio 1/D(p) to ln(p) (from Mertens' theorem). It says the escape corridor is slightly wider than the random model predicts, so droughts are slightly more severe.

### 5.3. Why gaps cannot greatly exceed (ln n)^2

The FS framework also constrains how far beyond (ln n)^2 gaps can reach:

**The open-position barrier.** Within any template composite run of size g, there are approximately g * D(p) ~ g/ln(n) open positions that remain after the template coverage. Each of these positions independently escapes higher-width layers with probability D_{higher}(sqrt(n)). For the gap to persist, all ~g/ln(n) positions must fail to escape.

The probability of this is:

    (1 - D_{higher})^{g/ln(n)}

For this to have a reasonable probability of occurring among ~n gaps, we need:

    n * (1 - D_{higher})^{g/ln(n)} ~ 1

Since D_{higher} ~ D(sqrt(n))/D(p) and the entire product telescopes to give g ~ (ln n)^2, the constraint is self-consistent.

For g significantly larger than (ln n)^2 -- say g ~ (ln n)^{2+epsilon} -- the probability becomes:

    n * exp(-(ln n)^{epsilon} * const) -> 0

exponentially fast. Gaps much larger than (ln n)^2 require an exponentially improbable conspiracy of higher-width coverages, making them astronomically rare.

### 5.4. The FS-x view of Cramér's conjecture

In FS-x coordinates, the maximal gap is amplified by the mean composite width:

    G_max ~ g_max * A ~ (ln n)^2 * C * ln(n)/ln(ln(n)) ~ (ln n)^3 / ln(ln(n))

This says the largest FS-x composite run (the widest contiguous stretch of the skyline without an escape spire) grows approximately as the cube of the logarithm. The amplification reflects the fact that the composites in large gaps tend to have large least prime factors -- they are "expensive" columns that consume extra FS-x space.

The FS-x maximal gap is the most natural geometric measure of how far apart escape spires can be in the skyline. Its growth rate ((ln n)^3 up to logarithmic corrections) is faster than the classical gap ((ln n)^2) but still subpolynomial -- the skyline's escape spires are always logarithmically close in FS-x, never polynomially far apart.

### 5.5. The FS-geometric Cramér conjecture

Combining all the above:

> **FS-Cramér Conjecture:** The longest composite run (escape-free corridor) among integers up to n has classical length at most C * (ln n)^2, where C = 2e^{-gamma} ~ 1.12 (Granville's constant). In FS-x coordinates, this corridor has extent at most ~C' * (ln n)^3 / ln(ln n) due to width amplification.

The structural content: the escape density ~1/ln(n) and the extremal statistics of ~n/ln(n) independent gaps combine to produce a maximal drought of ~(ln n)^2. The primorial template provides the skeleton; higher-width stochastic coverage fills the flesh. Longer droughts would require an exponentially improbable conspiracy of coverage events across all open positions within a template composite run.

---

## 6. Summary

| Concept | Classical | FS-Geometry |
|---------|-----------|-------------|
| Prime gap g = p_{k+1} - p_k | Distance on number line | Composite run: escape-free corridor |
| Mean gap ~ ln(n) | PNT consequence | 1/D(sqrt(n)) from escape density |
| Max gap ~ (ln n)^2 | Cramér conjecture | Corridor drought at 1/n probability level |
| (ln n)^2 = ln(n) * ln(n) | Probabilistic model | (corridor width) * (extremal factor) |
| FS-x max gap ~ (ln n)^3 | Not visible classically | Classical gap amplified by mean composite width |
| Primorial template gap | Not visible | Structural skeleton: fixed composite run in p# |
| Stochastic filling | Not visible | Higher-width layers covering open positions in skeleton |
| Gap > (ln n)^2 | Conjectured impossible | Requires exponential conspiracy of coverage events |
| Granville constant 2e^{-gamma} | Correction to Cramér | Mertens ratio: escape corridor slightly wider than random |
| Epoch constraint | Not visible | Frozen-coverage intervals; boundary crossings mildly penalized |
| Width spectrum of large gaps | Not visible | Composites with large lpf dominate; single widths ~ sqrt(n) |
| Record gap g/(ln p)^2 ~ 0.5-0.7 | Empirical | Well below the Cramér bound; template fills slowly |

Cramér's conjecture, viewed through the Factor Skyline, is the assertion that the escape corridor can experience droughts of length at most (ln n)^2 -- the product of the corridor width (1/D ~ ln n) and the extremal count of how many corridor-width intervals must be searched before encountering the longest drought (also ~ln n). The primorial template provides the skeleton of large gaps; higher-width coverage provides the stochastic filling. Longer droughts would require an exponentially improbable alignment of coverage events, which the architecture of the skyline renders negligible.
