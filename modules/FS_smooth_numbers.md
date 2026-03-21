# Smooth Numbers in FS-Geometry

---

## Overview

An integer n is **y-smooth** if its greatest prime factor (gpf) satisfies gpf(n) <= y. Smooth numbers are fundamental in computational number theory (factoring algorithms, cryptanalysis) and in the anatomy of integers. Their distribution is governed by the Dickman-de Bruijn function rho(u), which describes the fraction of integers up to x that are x^{1/u}-smooth.

In the Factor Skyline, smooth numbers have a distinctive geometric signature: they are columns built entirely from small widths, with shallow recursive height structure. Their FS-y height reflects only early-activation layers, and their FS-x contribution comes only from the smallest primes. The FS framework reveals smoothness as a constraint on **activation depth** — how far up the activation hierarchy a number's factorization reaches.

---

## 1. Smoothness as Early Activation and Shallow Height

### 1.1. The FS-geometric definition of smoothness

An integer n is y-smooth if gpf(n) <= y. In FS-geometry, this means:

- **Every width in n's recursive column structure is at most y.** The column is built entirely from coverage layers that activated at or before y^2.
- **The column does not reach into any activation epoch beyond y^2.** Its factorization is "contained" within the first few layers of the skyline.

A y-smooth number interacts only with the coverage architecture up to activation threshold y^2. Beyond that, it is invisible — no width layer above y touches it.

### 1.2. The recursive column structure of smooth numbers

The FS column of n is built by repeatedly extracting lpf:

    n → lpf(n), n/lpf(n) → lpf(n/lpf(n)), ... → 1

For y-smooth n, every width in this sequence is at most y. The column is a **shallow stack** of small widths.

Examples (5-smooth numbers):

| n   | Factorization | Width sequence | Height sequence |
|-----|--------------|----------------|-----------------|
| 8   | 2^3          | [2, 2, 2]      | [8, 4, 2, 1]   |
| 12  | 2^2 * 3      | [2, 2, 3]      | [12, 6, 3, 1]  |
| 30  | 2 * 3 * 5    | [2, 3, 5]      | [30, 15, 5, 1] |
| 60  | 2^2 * 3 * 5  | [2, 2, 3, 5]   | [60, 30, 15, 5, 1] |
| 360 | 2^3 * 3^2 * 5| [2, 2, 2, 3, 3, 5] | [360, 180, 90, 45, 15, 5, 1] |
| 720 | 2^4 * 3^2 * 5| [2, 2, 2, 2, 3, 3, 5] | [720, 360, 180, 90, 45, 15, 5, 1] |

The height sequence for a smooth number descends through intermediate values that are themselves smooth. The column structure is entirely contained within the small-prime coverage layers.

### 1.3. Rough numbers: the FS complement

An integer n is **y-rough** if lpf(n) > y. In FS-geometry, a y-rough number is one that escapes all coverage layers up to y — its first width assignment comes from a layer that activates at q^2 > y^2.

The density of y-rough integers is exactly the escape density:

    fraction of y-rough integers = D(y) = prod_{q <= y} (1 - 1/q)

Numerically verified:

| y  | D(y) (predicted) | Fraction of y-rough among [2, 10000] |
|----|-----------------|--------------------------------------|
| 2  | 0.5000          | 0.4999                               |
| 5  | 0.2667          | 0.2665                               |
| 10 | 0.2286          | 0.2284                               |
| 20 | 0.1710          | 0.1710                               |

The match is exact to within O(1/x) boundary effects. The escape density D(y) is simultaneously the density of y-rough integers (the FS-geometric connection established in `FS_ontology.md`).

### 1.4. The smooth-rough-middle trichotomy

Every integer falls into one of three smoothness classes relative to a threshold y:

| Class | Condition | FS signature | Density |
|-------|-----------|-------------|---------|
| y-smooth | gpf(n) <= y | All widths <= y | Psi(x,y)/x ~ rho(u) |
| Middle | lpf(n) <= y < gpf(n) | First width <= y, some width > y | 1 - rho(u) - D(y) |
| y-rough | lpf(n) > y | First width > y | D(y) |

At y = 5, among integers 2 to 1000:
- 5-smooth: contribute 5.9% of total FS-x budget (all small widths)
- Middle: contribute 50.8% of total FS-x budget (mixed widths)
- 5-rough: contribute 43.4% of total FS-x budget (all large widths)

The rough numbers, despite being only ~27% of integers, contribute 43% of the FS-x budget because their widths are large (lpf > 5, so each composite contributes dx >= 7).

---

## 2. The Dickman-de Bruijn Function from Activation Depth

### 2.1. Activation depth

Define the **activation depth** of an integer n as:

    u(n) = log(n) / log(gpf(n))

This measures how many "doublings" of the largest prime factor are needed to reach n. For a y-smooth number n <= x with y = x^{1/u}:

    u = log(x) / log(y)

The activation depth u counts how many levels of the activation hierarchy n's factorization spans, measured in logarithmic units relative to the largest prime factor.

### 2.2. The Dickman function as an activation-depth distribution

The Dickman-de Bruijn function rho(u) gives the density of integers with activation depth at most u:

    Psi(x, x^{1/u}) / x → rho(u) as x → infinity

Key values:

| u   | rho(u)  | Meaning |
|-----|---------|---------|
| 1.0 | 1.0000  | All integers are x-smooth (trivially) |
| 1.5 | 0.5828  | 58% are x^{2/3}-smooth |
| 2.0 | 0.3069  | 31% are sqrt(x)-smooth |
| 3.0 | 0.0486  | 5% are x^{1/3}-smooth |
| 4.0 | 0.0049  | 0.5% are x^{1/4}-smooth |
| 5.0 | 0.00035 | 0.035% are x^{1/5}-smooth |

### 2.3. The FS derivation of rho(u)

In FS-geometry, the Dickman function arises from the **recursive peeling** of the column structure.

An integer n <= x is x^{1/u}-smooth if its largest prime factor is at most x^{1/u}. Equivalently, the FS column of n uses only widths from coverage layers that activated at or before x^{2/u}.

The recursive definition of rho: For u > 1,

    rho(u) = 1 - integral from 1 to u of rho(t-1)/t dt

has the following FS interpretation:

**(i)** Start with all integers <= x (density 1).

**(ii)** Remove those with gpf(n) > x^{1/u}. These are integers whose FS column includes at least one width from a late-activation layer (beyond x^{2/u}).

**(iii)** The fraction removed depends on how the largest prime factor distributes among integers — which is controlled by the density of integers whose largest width falls in each range of the activation hierarchy.

The key observation: if the largest prime factor of n is p (with x^{1/u} < p <= x), then n = p * m where m <= x/p is (x/p)-smooth with gpf(m) <= p. The density of such n is:

    sum over primes p in (x^{1/u}, x]: (1/p) * rho(log(x/p)/log(p))

This recursive structure — peeling off the largest width and considering what remains — is the FS-geometric content of the integral equation for rho.

### 2.4. The u = 2 threshold: the activation horizon

The case u = 2 has special FS significance: rho(2) = 1 - ln(2) ~ 0.3069.

At u = 2, the smoothness threshold is y = sqrt(x). This is the **activation horizon** — the scale at which all relevant coverage layers are active. An integer n <= x is sqrt(x)-smooth if and only if all its prime factors are below the activation horizon.

The fraction rho(2) ~ 0.307 says that roughly 30% of integers up to x have all their prime factors below the activation horizon. These are the integers entirely "contained" within the active coverage architecture — they require no factorization knowledge beyond what the activation layers provide.

The remaining 69% have at least one prime factor above the activation horizon — they reach into uncatalogued territory, where coverage layers have not yet activated.

---

## 3. The Skyline Geometry of Smooth, Rough, and Semi-Smooth Integers

### 3.1. Smooth columns: compact and internally structured

A y-smooth column has:
- Width dx = lpf(n) <= y (small first width)
- All subsequent widths in the recursive decomposition <= y
- Total FS-x contribution: bounded by the product of widths, all <= y

Smooth columns are **compact**: they occupy modest FS-x space because their widths are small. A 5-smooth number never contributes dx > 5. These columns cluster in the "low-width" region of the skyline.

### 3.2. Rough columns: wide and escape-like

A y-rough column has:
- Width dx = lpf(n) > y (large first width)
- The first width comes from a high activation layer

If n is y-rough and composite, its smallest prime factor exceeds y, making its FS-x contribution large (dx > y). These columns are **wide** — they consume significant FS-x space relative to their number-line extent.

Primes are the extreme rough numbers: lpf(p) = p, so a prime near x is x-rough and contributes dx = 1 (because escape events bypass the width assignment). The prime's "roughness" is maximal, but its FS-x contribution is minimal. This is the fundamental FS paradox of primes: they are the roughest possible integers, yet they are the narrowest possible columns.

### 3.3. Semi-smooth: the mixed interior

Integers that are neither y-smooth nor y-rough have lpf(n) <= y but gpf(n) > y. Their FS columns start with a small width (from an early activation layer) but contain at least one large width deeper in the recursive structure.

These "semi-smooth" integers are the majority of all integers for typical y. They are structurally heterogeneous: their columns begin with familiar small widths but eventually include a "surprise" large width from a late-activated layer.

### 3.4. The FS-x budget by smoothness class

The FS-x axis grows as a sum of widths. The contribution of each smoothness class to the total FS-x budget is:

At scale 1000 with threshold y = 5:
- 5-smooth integers: 5.9% of total FS-x (small widths, compact columns)
- Middle integers: 50.8% of total FS-x (mixed widths, heterogeneous)
- 5-rough integers: 43.4% of total FS-x (large widths, wide columns)

The rough integers are disproportionately expensive in FS-x. They are a minority (~27%) by count but consume ~43% of the horizontal space. The skyline is horizontally dominated by wide, rough columns interspersed with narrow escape spires.

---

## 4. Primorial Templates and Smooth-Number Density

### 4.1. The primorial as the smooth-number factory

The p#-primorial is itself the product of all primes up to p — the prototypical p-smooth number. Its divisors form a complete system of p-smooth numbers within a bounded range: every divisor of p# is p-smooth, and there are prod(e_i + 1) = 2^{pi(p)} divisors (when p# = product of distinct primes).

The p#-template determines which positions in each period are occupied by p-smooth numbers (those whose factorizations use only primes <= p) versus non-p-smooth numbers (those with at least one prime factor > p).

### 4.2. Smooth numbers within a template period

Within one p#-period, the p-smooth integers are exactly the divisors of p# (times the period offset). There are 2^{pi(p)} of them in each period, but many are concentrated near the period boundaries. The density of p-smooth integers in [1, x] is:

    Psi(x, p) / x ~ rho(log(x)/log(p))

For fixed p as x grows, this density decreases (because x becomes much larger than p, increasing the activation depth u).

### 4.3. Smooth numbers and coverage completeness

A y-smooth number n is one where every prime in n's factorization has its coverage layer active at scale y^2. In FS terms: the column's complete structure is determined by the first pi(y) coverage layers. No information from later activation events is needed to understand the column.

This is why smooth numbers are computationally tractable: their factorizations are "visible" within the early activation layers. The sieve of Eratosthenes, run up to y, completely factors all y-smooth integers. In FS-geometry, the coverage architecture up to y^2 is sufficient to describe every smooth column.

---

## 5. Structural Insights

### 5.1. The smooth-rough duality

The FS framework reveals a fundamental duality between smooth and rough numbers:

| Property | Smooth (gpf <= y) | Rough (lpf > y) |
|----------|--------------------|------------------|
| Width constraint | All widths <= y | First width > y |
| Activation depth | Shallow (within first layers) | Deep (reaches late layers) |
| FS-x contribution per integer | Small (compact columns) | Large (wide columns) |
| Density | Psi(x,y)/x ~ rho(u) | D(y) ~ e^{-gamma}/ln(y) |
| Template role | Divisors of p# | Open positions in p#-template |
| Governing function | Dickman rho | Mertens escape density |

The smooth numbers are governed by the Dickman function rho; the rough numbers are governed by the escape density D. Both describe the same coverage architecture from opposite directions:

- **Smooth:** which integers are completely captured by the first k layers?
- **Rough:** which integers escape the first k layers entirely?

The duality is exact: the smooth density rho(u) and the rough density D(y) are both derivable from the same coverage product prod(1 - 1/q), applied differently.

### 5.2. The Dickman function as a depth profile of the skyline

The Dickman function rho(u) describes the **depth profile** of the skyline's column structure. It answers: what fraction of columns have their deepest width assignment at activation depth u or less?

- rho(1) = 1: all columns have at least one width (trivially).
- rho(2) ~ 0.31: 31% of columns have all widths from the first half of the activation hierarchy (in log scale).
- rho(3) ~ 0.05: 5% of columns are "shallow" — all widths in the first third of the hierarchy.
- rho(u) → 0 as u → infinity: vanishingly few columns are confined to an arbitrarily shallow portion of the activation hierarchy.

This depth profile is a global property of the skyline, determined entirely by the activation-coverage architecture.

### 5.3. The FS height of smooth vs non-smooth numbers

Smooth numbers tend to have smaller FS-y heights because their cofactors (n/lpf(n)) are also smooth, keeping the height within the smooth range. Non-smooth numbers can have arbitrarily large FS-y heights because their cofactors may include large primes.

For integers up to 100:
- 5-smooth numbers: mean y_FS = 17.7, max y_FS = 50
- Non-5-smooth numbers: mean y_FS = 32.4, max y_FS = 97

The non-smooth numbers reach higher in the skyline because their columns contain components from late-activation layers.

### 5.4. Why smooth numbers matter for factoring

The FS framework illuminates why smooth numbers are central to factoring algorithms (quadratic sieve, number field sieve):

Factoring n requires finding its width decomposition — its sequence of coverage layers. If n is y-smooth, this decomposition uses only layers up to y, and the template up to y# suffices. The number of such layers is pi(y), which is small for y << n.

The factoring strategy is: find relations involving y-smooth integers (whose factorizations are computable from the first pi(y) coverage layers) and combine them to reveal the target's factorization. The probability of finding a y-smooth integer near x is rho(log(x)/log(y)), and the optimal y balances this probability against the computational cost of processing the relations.

In FS terms: factoring algorithms exploit the **shallow region** of the skyline — the columns whose structure is entirely determined by early activation layers — to build up information about the deep structure of the target number.

### 5.5. The FS content of the subexponential complexity

The number field sieve factors n in time exp(c * (ln n)^{1/3} * (ln ln n)^{2/3}). This subexponential complexity arises from the Dickman function:

The optimal smoothness bound y = exp((ln n)^{1/3} * (ln ln n)^{2/3}) balances the smooth probability rho(u) ~ u^{-u} against the number of factor-base elements pi(y). The Dickman function's rapid decay (rho(u) decreases super-exponentially for u > 1) means the optimal y is much larger than polynomial in ln(n) but much smaller than n — it sits in the subexponential regime.

In FS-geometry, this optimal point is where the **activation depth** u = ln(n)/ln(y) is large enough that smooth numbers are rare, but not so large that the factor base (the active coverage layers up to y) is unmanageably large. The subexponential complexity is the geometric cost of probing the skyline at the optimal depth.

---

## 6. Summary

| Concept | Classical | FS-Geometry |
|---------|-----------|-------------|
| y-smooth number | gpf(n) <= y | Column uses only widths <= y (early activation layers) |
| y-rough number | lpf(n) > y | Column's first width > y (escapes all layers up to y) |
| Psi(x,y) | Count of y-smooth n <= x | Count of shallow columns up to x |
| Dickman rho(u) | Asymptotic smooth density | Activation-depth profile of the skyline |
| rho(2) ~ 0.31 | 31% are sqrt(x)-smooth | 31% of columns contained within activation horizon |
| D(y) | Rough density | Escape density (fraction avoiding all layers up to y) |
| Smooth-rough duality | Not explicit | Same coverage product, viewed from opposite ends |
| Recursive column peeling | Not visible | FS height sequence descends through smooth intermediates |
| FS-x budget share | Not visible | Rough columns disproportionately wide; smooth columns compact |
| Factoring algorithms | Exploit smooth numbers | Probe the shallow region of the skyline |
| Subexponential complexity | NFS optimal y | Optimal activation depth: deep enough for rarity, shallow enough for tractability |

Smooth numbers in the Factor Skyline are the columns whose structure is entirely determined by the earliest activation layers. Their distribution is governed by the Dickman function, which describes the depth profile of the skyline — how deeply each column's factorization reaches into the activation hierarchy. The FS framework reveals smoothness as a geometric constraint on activation depth and connects it to the coverage architecture that governs all prime behavior.
