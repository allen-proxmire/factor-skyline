# The Sieve of Eratosthenes as FS-Geometry

---

## Overview

The Sieve of Eratosthenes is the oldest algorithm for finding primes. In its classical form, it is a procedure: mark, remove, survive. In the Factor Skyline, the sieve is not a procedure but a description of the geometry itself. Every operation the sieve performs corresponds to a structural feature of the skyline that exists whether or not we choose to compute it.

This document translates the sieve step by step into FS-geometry, shows where the classical sieve hides structure that the skyline reveals, and derives the sieve's quantitative content from the FS ontology.

---

## 1. The Classical Sieve as an Algorithm

The Sieve of Eratosthenes, applied to integers {2, 3, ..., N}:

1. Start with all integers unmarked.
2. Find the smallest unmarked integer p. It is prime.
3. Mark all multiples of p starting from p^2 (multiples kp with k < p are already marked by smaller primes).
4. Repeat step 2 until p > sqrt(N).
5. All remaining unmarked integers are prime.

The sieve terminates at sqrt(N) because every composite n <= N has a prime factor <= sqrt(n) <= sqrt(N).

---

## 2. Translation: Sieve Operations as FS-Geometry

Each operation of the classical sieve has a precise FS-geometric counterpart.

### 2.1. "Start with all integers unmarked" = The empty skyline

Before any coverage layer has activated, every integer is a potential escape event. The escape corridor has density D = 1 -- the full skyline is open. No column has been assigned a width by the sieve; every integer awaits its structural determination.

In FS-geometry, this is the state of the skyline below n = 4 (the first activation threshold). The integers 2 and 3 escape trivially -- no coverage layer exists to catch them.

### 2.2. "Find the smallest unmarked integer" = Escape detection

The sieve identifies the next prime by finding the smallest integer not yet marked. In FS-geometry, this is the detection of an **escape event**: the first column that has width 1 (not claimed by any active coverage layer).

The classical sieve discovers primes sequentially. The skyline contains them structurally -- each prime is a column whose width is 1 because no activated layer claims it. Discovery is reading the geometry; the geometry does not depend on being read.

### 2.3. "Mark all multiples starting from p^2" = Activation of width-p

This is the central translation.

In the classical sieve, marking multiples of p starting from p^2 is presented as an algorithmic optimization: multiples kp with k < p have already been handled by earlier rounds. This is correct but obscures the structural reason.

In FS-geometry, the reason is architectural:

**Every multiple of p below p^2 has a prime factor smaller than p.**

If n = kp with k < p, then k has some prime factor q <= k < p. Therefore lpf(n) <= q < p, and n is already assigned to the width-q layer. The width-p layer literally has no column to claim below p^2.

The integer p^2 is the first multiple of p whose cofactor (namely p) has no prime factor smaller than p. It is the **activation threshold** -- the point where the width-p layer first attaches to the skyline.

What the classical sieve calls an optimization, the skyline reveals as a geometric necessity. The width-p layer cannot exist below p^2 because there is no architectural space for it.

### 2.4. "Mark kp for k >= p" = Coverage sweep

Once width-p activates at p^2, it claims every integer n >= p^2 with lpf(n) = p. These are the integers of the form n = p * m where m >= p and lpf(m) >= p (i.e., m has no prime factor smaller than p).

In the classical sieve, this is a loop: mark p^2, p(p+1), p(p+2), ... But this overstates what happens -- many of these multiples are already marked. The sieve redundantly visits p(p+1) if (p+1) has a smaller factor.

In FS-geometry, there is no redundancy. Each integer has exactly one width -- its least prime factor. The width-p layer claims only those integers whose lpf is genuinely p. Coverage is a partition, not an overlap:

    {integers >= 2} = {width-2 columns} ∪ {width-3 columns} ∪ {width-5 columns} ∪ ... ∪ {primes}

Each integer belongs to exactly one class. The coverage layers do not compete; they partition.

### 2.5. "Stop at sqrt(N)" = The activation horizon

The sieve terminates when p > sqrt(N) because all composites <= N have been caught. In FS-geometry, this is the **activation horizon**: the largest prime whose coverage layer is architecturally present at scale N.

    p_max = max{p prime : p^2 <= N} = largest prime <= sqrt(N)

Beyond this threshold, no new coverage layer activates within the range [1, N]. The skyline's coverage configuration is complete. Every column that remains uncovered is an escape event -- a prime.

### 2.6. "Unmarked survivors are prime" = The escape set

The output of the sieve is the set of unmarked integers. In FS-geometry, this is the **escape set**: the columns with width 1.

    E(N) = {n <= N : lpf(n) = n} = {primes <= N}

The sieve computes this set by elimination. The skyline contains it by construction. The escape set is not the residue of an algorithm; it is a structural feature of the geometry.

---

## 3. What the Skyline Reveals That the Sieve Hides

The classical sieve is a correct algorithm, but its procedural form conceals several structural facts that are visible in the skyline.

### 3.1. The sieve hides the partition structure

The classical sieve marks integers as "composite" without recording which prime claimed them. An integer marked in round p and again in round q receives no distinction -- it is simply "not prime."

In the skyline, every composite has a definite width: its least prime factor. The marking is not a binary flag but a structural assignment. The integer 15 is not merely "composite" -- it is a width-3 column of height 5. The integer 12 is a width-2 column of height 6. The sieve discards this information; the skyline preserves it.

### 3.2. The sieve hides the height dimension

The classical sieve operates on a 1D list. It removes integers from a line. The vertical structure -- the quotient n/lpf(n) that determines each column's height -- is invisible.

In the skyline, the height of each column records the cofactor after the least prime factor is divided out. This is the recursive factorization structure. The sieve flattens it; the skyline displays it.

### 3.3. The sieve hides the reason for p^2

As discussed in Section 2.3, the classical sieve presents the p^2 starting point as an efficiency trick. The skyline reveals it as a geometric necessity: the width-p layer has no architectural presence below p^2.

### 3.4. The sieve hides the density product

The classical sieve counts survivors but does not directly express why the count takes the form it does. The skyline makes the density product visible:

    D(p) = prod_{q <= p, q prime} (1 - 1/q)

Each sieve round removes a fraction 1/q of the remaining integers. The cumulative effect is a product. This product is the escape density -- the fraction of the skyline that remains open. The sieve computes the survivors; the skyline explains the fraction.

---

## 4. The Sieve Count in FS Terms

### 4.1. The Legendre sieve formula

The classical Legendre sieve counts the number of integers in [1, N] that survive all sieve rounds up to prime p. By inclusion-exclusion:

    S(N, p) = N - sum_{q <= p} floor(N/q) + sum_{q1 < q2 <= p} floor(N/(q1*q2)) - ...

This alternating sum counts the integers coprime to all primes <= p.

### 4.2. The FS density form

In the skyline, the same count is expressed without inclusion-exclusion. The escape density gives:

    S(N, p) ~ N * D(p) = N * prod_{q <= p, q prime} (1 - 1/q)

The approximation is exact in the limit N -> infinity and carries bounded error terms for finite N. The product form replaces the alternating sum with a single multiplicative expression -- each factor (1 - 1/q) represents the fractional removal by one coverage layer.

### 4.3. The prime count

Setting p = sqrt(N) (the activation horizon), the escape count becomes the prime count:

    pi(N) ~ N * D(sqrt(N)) = N * prod_{q <= sqrt(N), q prime} (1 - 1/q)

This is the FS-geometric derivation of the sieve's output. The prime count is the product of the total space (N) and the fraction that escapes all active coverage layers (D(sqrt(N))).

Via Mertens' theorem (see `FS_PNT_derivation.md`), this projects to:

    pi(N) ~ N / ln(N)

---

## 5. Sieve Rounds as Activation Epochs

The sieve processes primes in order: first p = 2, then p = 3, then p = 5, and so on. Each round corresponds to an activation event in the skyline.

### 5.1. Epoch structure

The activation events at p_k^2 partition the integers into epochs:

    Epoch_k = [p_k^2, p_{k+1}^2)

Within each epoch, the coverage configuration is frozen. The sieve has completed rounds 1 through k (for primes p_1 through p_k) and has not yet begun round k+1.

| Epoch | Interval     | Length | Active widths        | Escape density D(p_k)          |
|-------|-------------|--------|----------------------|--------------------------------|
| 0     | [1, 4)       | 3      | (none)               | 1                              |
| 1     | [4, 9)       | 5      | {2}                  | 1/2                            |
| 2     | [9, 25)      | 16     | {2, 3}               | 1/2 * 2/3 = 1/3               |
| 3     | [25, 49)     | 24     | {2, 3, 5}            | 1/3 * 4/5 = 4/15              |
| 4     | [49, 121)    | 72     | {2, 3, 5, 7}         | 4/15 * 6/7 = 8/35             |
| 5     | [121, 169)   | 48     | {2, 3, 5, 7, 11}     | 8/35 * 10/11 = 16/77          |
| 6     | [169, 289)   | 120    | {2, 3, 5, 7, 11, 13} | 16/77 * 12/13 = 192/1001      |

### 5.2. Escapes per epoch

The expected number of escapes in Epoch_k is approximately:

    E_k ~ |Epoch_k| * D(p_k) = (p_{k+1}^2 - p_k^2) * prod_{q <= p_k} (1 - 1/q)

For the epochs listed above:

| Epoch | Length | D(p_k)   | Expected escapes | Actual primes in epoch               |
|-------|--------|----------|------------------|---------------------------------------|
| 0     | 3      | 1        | 3                | 2, 3 (2 primes, plus 1 is not prime) |
| 1     | 5      | 0.5000   | 2.5              | 5, 7 (2 primes)                      |
| 2     | 16     | 0.3333   | 5.3              | 11, 13, 17, 19, 23 (5 primes)        |
| 3     | 24     | 0.2667   | 6.4              | 29, 31, 37, 41, 43, 47 (6 primes)    |
| 4     | 72     | 0.2286   | 16.5             | 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113 (15 primes) |

The escape density predicts the prime count per epoch with reasonable accuracy. The prediction improves as epochs grow longer (boundary effects diminish relative to epoch length).

### 5.3. The sieve never empties the corridor

A fundamental structural fact: the escape density D(p_k) is always positive, and the epoch length grows faster than 1/D(p_k) decreases. Therefore:

    E_k = |Epoch_k| * D(p_k) -> infinity as k -> infinity

Every epoch contains primes. The sieve never finishes its work because the corridor never closes. This is the FS-geometric content of Euclid's theorem (infinitude of primes): the escape density is always positive, and each epoch is long enough to produce escapes.

---

## 6. The FS Sieve vs. the Classical Sieve: A Comparison

| Feature                    | Classical Sieve                          | FS-Geometric Sieve                       |
|----------------------------|------------------------------------------|------------------------------------------|
| Representation of n        | A point on a 1D list                     | A column with width and height           |
| "Marking" a composite      | Binary flag: marked or unmarked          | Structural assignment: width = lpf(n)    |
| Starting at p^2            | Algorithmic optimization                 | Geometric necessity (activation)         |
| Removal fraction           | Implicit in the marking pattern          | Explicit: 1/p of remaining columns       |
| Redundant markings         | Common (multiples hit by multiple primes)| None (partition by least prime factor)   |
| Survivor count             | Requires inclusion-exclusion (Legendre)  | Direct product: D(p) = prod(1 - 1/q)    |
| Prime density              | Observed empirically, proved analytically| Structural: escape density via Mertens   |
| Termination at sqrt(N)     | Efficiency bound                         | Activation horizon                       |
| Output                     | A list of unmarked integers              | The escape set: columns with width 1     |
| What it explains           | Which integers are prime                 | Why they are prime (and where, and how many) |

---

## 7. Summary

The Sieve of Eratosthenes, when translated into FS-geometry, is not an algorithm but a description:

- **Sieve rounds** are **activation events** at p^2.
- **Marking multiples** is **coverage** by width-p layers.
- **Survivors** are **escape events** -- columns with width 1.
- **The p^2 starting point** is not an optimization but a **geometric necessity**.
- **The survivor count** is not an inclusion-exclusion sum but a **density product**.
- **Termination at sqrt(N)** is not an efficiency bound but the **activation horizon**.

The classical sieve asks: which integers survive? The skyline answers: how is the space partitioned, and what escapes?

The sieve is the shadow of the skyline's architecture, projected onto a sequential procedure. The skyline is the geometry that makes the sieve's behavior structurally inevitable.
