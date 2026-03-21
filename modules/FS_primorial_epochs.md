# Primorial Epochs and the Tiling Structure of the Factor Skyline

---

## Overview

The primorial p# = 2 * 3 * 5 * ... * p is the product of all primes up to p. In the Factor Skyline, primorials are not merely arithmetic curiosities -- they are the **periods of the combined coverage pattern**. The coverage layers of all primes up to p create a repeating template of width assignments with period exactly p#. This template determines which positions are structurally open for escape, which gap sizes dominate at a given scale, and how the skyline's architecture evolves as new primes activate.

This document develops the primorial tiling structure and its consequences.

---

## 1. The Primorial Template: Combined Coverage with Period p#

### 1.1. Construction

Fix a set of primes {2, 3, 5, ..., p}. Each prime q in this set creates a coverage layer that claims every q-th integer (among those not already claimed by smaller primes). The combined pattern of assignments repeats with period:

    p# = 2 * 3 * 5 * ... * p

This follows from the Chinese Remainder Theorem: the residue of an integer modulo each prime in {2, ..., p} determines its width assignment (which layer claims it), and these residues repeat with period p# = lcm(2, 3, ..., p) (which equals the product, since all factors are prime).

### 1.2. The template for 5# = 30

The combined coverage pattern for primes {2, 3, 5} repeats every 30 integers. Within one period [0, 29]:

```
r :  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
lpf: *  .  2  3  2  5  2  .  2  3  2  .  2  .  2  3  2  .  2  .  2  3  2  .  2  5  2  3  2  .

    * = multiple of several primes (covered)
    . = OPEN (coprime to 30, potential escape)
    2,3,5 = covered by that width layer
```

The 8 open positions are: {1, 7, 11, 13, 17, 19, 23, 29}.

These are the integers coprime to 30 -- the only positions where escape can occur, once all primes up to 5 have activated.

### 1.3. The template structure is fixed

A remarkable structural invariant: within each p#-period, the counts of width-q columns (for q in {2, ..., p}) are **exactly the same**, regardless of where the period starts on the number line. Numerically verified for the 30-period:

| Start | w2 columns | w3 columns | w5 columns | Escapes | Other |
|-------|-----------|-----------|-----------|---------|-------|
| 30    | 15        | 5         | 2         | 7       | 1     |
| 60    | 15        | 5         | 2         | 7       | 1     |
| 90    | 15        | 5         | 2         | 6       | 2     |
| 1000  | 15        | 5         | 2         | 4       | 4     |
| 5000  | 15        | 5         | 2         | 5       | 3     |

The width-2, width-3, and width-5 column counts are always 15, 5, and 2 respectively. These are fixed by the template: within any 30-period, exactly 15 integers are even (and not odd multiples of 3 or 5), exactly 5 are odd multiples of 3 (and not multiples of 5), and exactly 2 are multiples of 5 coprime to 2 and 3.

What changes across periods is the distribution of the 8 open positions between **escapes** (primes) and **other** (composites with lpf > 5, i.e., width-7 or higher). At small scales, most open positions are primes. At large scales, more open positions are claimed by higher width layers (7, 11, 13, ...) that activated after 5.

### 1.4. The open positions and phi

The number of open positions in a p#-period is Euler's totient:

    phi(p#) = p# * prod_{q <= p} (1 - 1/q) = p# * D(p)

For the first few primorials:

| p# | Value | phi(p#) | D(p) = phi/p# |
|----|-------|---------|----------------|
| 2# | 2     | 1       | 1/2            |
| 3# | 6     | 2       | 1/3            |
| 5# | 30    | 8       | 4/15           |
| 7# | 210   | 48      | 8/35           |
| 11#| 2310  | 480     | 16/77          |

The escape density D(p) counts the fraction of positions that survive the combined coverage of all primes up to p. This is the same escape density product that governs the PNT -- here it appears as a combinatorial count within the primorial template.

---

## 2. Primorial Tilings in FS-x and Their Interaction with Activation Epochs

### 2.1. The FS-x extent of a primorial period

The template determines the column counts by width. The FS-x extent of one p#-period is:

    X(p#) = sum over all n in the period of dx(n)
          = (# of escapes) * 1 + sum_{q <= p} (# of width-q columns) * q + (# of other composites) * (their widths)

The first two terms are fixed by the template:

    X_fixed(p#) = sum_{q <= p} (p#/q * prod_{r<q}(1-1/r)) * q = sum_{q <= p} p# * prod_{r<q}(1-1/r)

For the 30-period:
- Width-2 contributes: 15 columns * 2 = 30
- Width-3 contributes: 5 columns * 3 = 15
- Width-5 contributes: 2 columns * 5 = 10
- Fixed total: 55

The remaining 8 open positions contribute variable amounts depending on whether they are escapes (dx = 1) or higher-width composites (dx = 7, 11, 13, ...). Verified numerically:

| Start | Fixed dx | Open-position dx | Total dx |
|-------|----------|------------------|----------|
| 30    | 55       | 14               | 69       |
| 1000  | 55       | 60               | 115      |
| 5000  | 55       | 92               | 147      |

The fixed contribution (55) is constant. The open-position contribution grows with scale because the open positions increasingly contain composites with large least prime factors rather than primes.

### 2.2. Interaction with activation epochs

Activation epochs and primorial periods are two different partitions of the integers:

- **Activation epochs** partition by coverage configuration: [p_k^2, p_{k+1}^2).
- **Primorial periods** partition by template repetition: [m*p#, (m+1)*p#).

These interact in a crucial way. At activation threshold p_k, the relevant primorial template has period p_k#. But the epoch length is only p_{k+1}^2 - p_k^2, which is much smaller than p_k# for large k:

| p   | p#        | Epoch length  | Periods per epoch |
|-----|-----------|---------------|-------------------|
| 2   | 2         | 5             | 2.50              |
| 3   | 6         | 16            | 2.67              |
| 5   | 30        | 24            | 0.80              |
| 7   | 210       | 72            | 0.34              |
| 11  | 2310      | 48            | 0.02              |
| 13  | 30030     | 120           | 0.004             |

**Key structural observation:** For p >= 5, the epoch is shorter than one full primorial period. This means:

- The primorial template at scale p# describes the *global* coverage pattern, but individual epochs only sample a small fragment of that template.
- The full primorial structure is never "seen" within a single epoch. It is a trans-epochal pattern that spans many activation boundaries.
- Each epoch adds one new width to the template, extending the period by a factor of p_{k+1}. The template is always growing faster than the epoch can contain it.

This is a fundamental asymmetry in the FS architecture: **the coverage pattern's period outgrows the epoch length**, so the local behavior within any epoch is a partial view of a global tiling that extends far beyond it.

### 2.3. The primorial staircase in FS-x

As the skyline extends, the FS-x extent per primorial period grows:

    X(p#, at scale n) = X_fixed(p#) + X_open(p#, n)

The fixed part is constant (it depends only on which primes are in the template). The open part grows because:

1. Fewer open positions are occupied by primes (escape density decreases).
2. More open positions are occupied by composites with large lpf (their widths are larger).

This creates a **primorial staircase** in FS-x: the skyline's horizontal growth rate increases at each activation event, because the open positions in the template become increasingly expensive (wider composites replace narrow primes).

---

## 3. Why Dominant Prime Gaps Follow the Primorial Sequence

### 3.1. The gap structure within a primorial template

The gaps between consecutive open positions in the p#-template determine the possible gap sizes between primes at the corresponding scale. If two consecutive open positions in the template are separated by g, then a prime gap of size g can occur whenever those two positions are both occupied by primes.

The gap distribution within primorial templates:

| Template | Period | Open positions | Gaps between open positions         | Max gap |
|----------|--------|----------------|-------------------------------------|---------|
| 2#       | 2      | {1}            | {2: 1x}                             | 2       |
| 3#       | 6      | {1, 5}         | {2: 1x, 4: 1x}                     | 4       |
| 5#       | 30     | 8 positions    | {2: 3x, 4: 3x, 6: 2x}             | 6       |
| 7#       | 210    | 48 positions   | {2: 15x, 4: 15x, 6: 14x, 8: 2x, 10: 2x} | 10 |
| 11#      | 2310   | 480 positions  | max gap = 14                         | 14      |

### 3.2. Why gap = 6 dominates

The most common prime gap up to 100000 is g = 6 (1940 occurrences), followed by g = 2 (1224) and g = 4 (1215).

In the 5#-template (period 30), the open positions are {1, 7, 11, 13, 17, 19, 23, 29}. The gaps between them are:

    7-1=6, 11-7=4, 13-11=2, 17-13=4, 19-17=2, 23-19=4, 29-23=6, (1+30)-29=2

Gap counts: {2: 3, 4: 3, 6: 2}.

But gap-6 dominates among *actual primes* because of a structural effect: the two gap-6 intervals ({1,7} and {23,29}) are the widest open stretches in the template, and they bracket positions that are especially likely to both be prime (they are far from multiples of small primes). The gap-2 intervals, while as numerous in the template, require twin primes, which become rarer as additional coverage layers (7, 11, ...) thin the corridor further.

More precisely: a gap of size g between primes requires that the g - 1 composites between them are all covered. For gap-6, the 5 intervening composites are always fully covered by widths 2, 3, and 5 -- the template guarantees it. For gap-2, only 1 composite needs to be covered, but twin primes require two consecutive open positions to both escape, which becomes harder at larger scales.

**The FS insight:** Gap-6 is dominant because it is the **maximal gap in the 5#-template** -- the largest guaranteed composite run within the coverage pattern of {2, 3, 5}. As the scale increases, gap-30 (the maximal gap in the 7#-template) will eventually dominate, then gap-210, and so on. The dominant gap tracks the primorial sequence because the coverage pattern's maximal composite run grows with each new prime.

### 3.3. The primorial gap progression

The dominant prime gap at scale n is approximately the **maximal gap in the p#-template** where p is the largest prime whose coverage fully governs behavior at that scale. The progression is:

    Scale ~ p^2  -->  Dominant gap ~ maximal gap in p#-template

| Dominant gap | Governing primorial | Scale where it dominates |
|-------------|--------------------|--------------------------|
| 2           | 2# = 2             | n ~ 4-9                  |
| 4           | 3# = 6             | n ~ 9-25                 |
| 6           | 5# = 30            | n ~ 25 - 10^8 (long reign) |
| 30          | 7# = 210           | n ~ 10^8 - ?             |
| 210         | 11# = 2310         | much larger n             |

Gap-6 dominates for an enormous range because the 5#-template is the last one where the epoch length is comparable to the period length (24 vs 30). After that, the primorial period far exceeds the epoch length, and the transition to the next dominant gap size is extremely slow.

### 3.4. The architectural inevitability of primorial gaps

In the FS framework, the sequence of dominant gaps (2, 4, 6, 30, 210, ...) is not empirical -- it is architectural. Each primorial p# defines a coverage template. The maximal composite run in that template is the longest stretch of consecutive integers all divisible by at least one prime <= p. This run is:

- determined entirely by the template (it is a combinatorial property of the open-position set)
- inherited by all scales governed by that template
- replaced only when the next primorial template becomes dominant

The primorial gaps are the **structural skeleton** of the prime gap distribution, directly visible in the FS-geometry as the maximal composite corridors within each tiling level.

---

## 4. Escape Density Across a Primorial Period

### 4.1. The two-level density structure

Within a single p#-period, there are two levels of structure:

**Level 1: Template coverage (fixed).** Of the p# positions, exactly phi(p#) are open (coprime to p#). The rest are covered by width layers 2, 3, ..., p. This level is completely determined by the primorial and does not change with scale.

**Level 2: Higher-width coverage (scale-dependent).** Among the phi(p#) open positions, some are primes (escapes) and some are composites with lpf > p. The fraction that are primes depends on the coverage layers with primes > p, which activate at scales beyond p^2.

The escape density within the open positions of the p#-template, at scale n, is:

    D_{open}(n) = D(sqrt(n)) / D(p) = prod_{p < q <= sqrt(n)} (1 - 1/q)

This is the residual escape density after the template's coverage has been accounted for. It represents the additional thinning caused by primes that activate after p.

### 4.2. The open-position budget

Within a p#-period starting at offset m * p# (for m >> p), the phi(p#) open positions are divided:

    phi(p#) = (# of primes) + (# of composites with lpf > p)

The expected number of primes is:

    phi(p#) * D_{open}(n) = phi(p#) * prod_{p < q <= sqrt(n)} (1 - 1/q)

and the expected number of higher-width composites is:

    phi(p#) * (1 - D_{open}(n))

As n grows, D_{open}(n) decreases (more higher-width layers activate), so fewer open positions are primes and more are composites with large widths. This is the mechanism behind the growing FS-x extent of each primorial period (Section 2.3).

### 4.3. Density variation within a period

The escape density is *not* uniform across the phi(p#) open positions within a single period. Some open positions are more likely to be prime than others, because they have different relationships to primes > p.

For example, in the 30-period, the open positions {1, 7, 11, 13, 17, 19, 23, 29} are all coprime to 30, but their residues mod 7 differ:

    1≡1, 7≡0, 11≡4, 13≡6, 17≡3, 19≡5, 23≡2, 29≡1 (mod 7)

Position 7 is divisible by 7 (it is 7 itself, or 37, 67, ... at higher offsets). So at offsets where position 7 falls on a multiple of 7, it will be covered by the width-7 layer and cannot be a prime. The other 7 positions are never affected by width-7.

This creates **intra-period density variation**: some open positions in the template are more susceptible to higher-width coverage than others. This variation is the origin of the fine structure in prime gap distributions -- why some gap-6 intervals produce primes more often than others.

---

## 5. Structural Insights from Primorial Tiling

### 5.1. The skyline has a fractal-like layered structure

Each primorial template is nested inside the next:

    2#-template (period 2) ⊂ 3#-template (period 6) ⊂ 5#-template (period 30) ⊂ ...

The 6-template refines the 2-template by adding width-3 coverage. The 30-template refines the 6-template by adding width-5 coverage. Each refinement:

- preserves all existing covered positions
- covers some previously open positions
- increases the period by a factor of p_{k+1}
- reduces the escape density by factor (1 - 1/p_{k+1})

This nested refinement creates a **self-similar structure** in the skyline. The coverage pattern at scale p_k# contains the coverage pattern at scale p_{k-1}# as a sublattice. Zooming out by a factor of p_{k+1} reveals the previous template as a repeating motif within the current one.

### 5.2. The primorial template encodes the "DNA" of the primes

The open positions within the p#-template are the only candidates for primes beyond p. No prime > p can occupy a template-covered position (it would be divisible by some q <= p and therefore not prime). Every prime > p must land on one of the phi(p#) open positions.

The p#-template is therefore a **constraint structure**: it narrows the search space for primes from all integers to a fraction D(p) = phi(p#)/p# of the integers. The remaining primes are those open positions that additionally escape all higher-width layers.

As p increases, the template becomes more restrictive (D(p) decreases), but also more informative: it eliminates more composite positions and leaves only the most "structurally protected" candidates.

### 5.3. The FS-x signature of primorial structure

In FS-x coordinates, the primorial template creates a **repeating rhythm** in the x-axis growth. Within each p#-period:

- The width-2, width-3, ..., width-p contributions are fixed and identical across all periods.
- Only the open-position contributions vary.

This means the FS-x growth rate has a **periodic component** with period p# (from the fixed template contributions) plus a **variable component** (from the open positions). The periodic component creates a regular pulse in the skyline's horizontal growth, while the variable component introduces the irregularity associated with prime distribution.

The interplay between these two components -- the deterministic template and the stochastic-looking escape pattern -- is the FS-geometric version of the interplay between the smooth approximation pi(x) ~ x/ln(x) and the fluctuating error term.

### 5.4. Why the Euler product is a primorial limit

The Euler product for the Riemann zeta function is:

    zeta(s) = prod_{p prime} 1/(1 - p^{-s})

At s = 1 (where zeta has a pole), the product diverges, and the rate of divergence encodes the density of primes.

In the FS framework, the escape density is:

    D(p) = prod_{q <= p} (1 - 1/q) = 1 / prod_{q <= p} 1/(1-1/q)

The reciprocal 1/D(p) is the "Euler product at s = 1, truncated at p." Its divergence rate (~ ln p by Mertens) is the FS-geometric content of the pole of zeta(s) at s = 1. The primorial template makes this connection concrete: phi(p#) = p# * D(p), so the number of open positions in the template is controlled by the partial Euler product.

The Euler product is the primorial template's escape density, written multiplicatively. The pole of zeta at s = 1 is the statement that the escape corridor narrows to zero density -- the same statement as D(p) -> 0 in the FS ontology.

### 5.5. Primorial structure and the twin prime conjecture

The twin prime conjecture (infinitely many pairs (p, p+2) with both prime) has a natural FS-primorial formulation.

Within the p#-template, the **twin-open positions** are pairs of open positions separated by 2. In the 30-template, these are: (11,13), (17,19), (29,31≡1). There are 3 such pairs out of 8 open positions.

For both positions in a twin pair to be prime, both must escape all higher-width layers (q > p). The probability of this is approximately:

    D_{open}(n)^2 * C_twin

where C_twin is a correction factor (the Hardy-Littlewood twin prime constant) that accounts for the fact that twin positions are not independent -- they share the constraint of being simultaneously coprime to all q > p.

In the FS framework, the twin prime conjecture reduces to: **the twin-open positions in the primorial template are never simultaneously closed by all higher-width layers.** Since the higher-width layers each close only a fraction 1/q of the open positions, and distinct layers are independent (CRT), the probability that a specific twin pair survives through all layers decreases but never reaches zero at any finite stage.

This does not constitute a proof (the transition from "density > 0" to "infinitely many" requires care), but it shows the structural mechanism: twin primes exist because the primorial template preserves twin-open positions, and no finite set of higher-width layers can close all of them simultaneously.

---

## 6. Summary

| Concept | Classical | FS-Geometry |
|---------|-----------|-------------|
| Primorial p# | Product of primes <= p | Period of the combined coverage template |
| phi(p#) | Euler totient | Number of open (escape-candidate) positions per period |
| D(p) = phi(p#)/p# | Escape density | Fraction of template that is structurally open |
| Dominant gap | Empirical observation | Maximal composite run in the p#-template |
| Gap = 6 dominance | "Happens to be common" | Maximal gap in 5#-template; persists because 5# ≈ epoch length |
| Primorial gap sequence 2,4,6,30,210,... | Empirical | Structural skeleton: max gaps of successive templates |
| Euler product | Analytic identity for zeta(s) | Reciprocal of escape density; encodes template structure |
| Twin prime candidates | Pairs p, p+2 | Twin-open positions in the primorial template |
| Fixed FS-x contribution | Not visible classically | Template widths contribute constant dx per period |
| Variable FS-x contribution | Not visible classically | Open positions contribute scale-dependent dx |

The primorial template is the architectural blueprint of the Factor Skyline. It determines which positions are structurally available for primes, which gap sizes dominate at each scale, and how the skyline's horizontal growth decomposes into a fixed periodic component and a variable escape component. The sequence of primorial templates, nested inside each other, creates the layered, self-similar geometry that governs prime distribution.
