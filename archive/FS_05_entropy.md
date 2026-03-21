# Entropy in the Factor Skyline

---

## Overview

Information theory provides a precise language for quantifying the "randomness" or "unpredictability" of a sequence. The Factor Skyline, by decomposing the integers into a deterministic template layer and a stochastic escape layer, allows a clean information-theoretic analysis: how much entropy does the skyline carry, where does it reside, and how does it distribute across the architectural levels?

This document derives the entropy budget of the Factor Skyline at each of its structural levels — template, escape, activation, and spectral — and identifies the information-theoretic content of the major number-theoretic functions.

---

## 1. Template Entropy

### 1.1. The template is a zero-entropy layer

The primorial template is fully deterministic: given n mod p#, the template classification (open or covered, and if covered, which width layer claims it) is uniquely determined. The template carries **zero conditional entropy**:

    H(template status | n mod p#) = 0

The template is not random; it is a fixed, periodic structure. Its role in the entropy budget is not to contribute uncertainty but to **remove** it.

### 1.2. How much uncertainty the template removes

Before knowing the template classification, each integer has primality probability ~1/ln(n), giving per-integer entropy:

    H(is prime?) = H_binary(1/ln(n)) bits

After applying the p#-template, a fraction (1 - D(p)) of positions are classified as definitely composite (covered by some width <= p). Their primality uncertainty drops to zero. The remaining fraction D(p) of positions (the open positions) retain uncertainty about whether they are prime or composite with large lpf.

The entropy removed by the template is:

    I_template = H(is prime?) - D(p) * H(is prime | open)

The template provides the largest information gain per bit because it resolves the status of the most common integers (the covered positions) completely.

### 1.3. Entropy rate as p grows

As the template incorporates more primes, D(p) decreases and more positions are resolved:

| p  | D(p)  | H(open/covered) | Fraction resolved |
|----|-------|-----------------|-------------------|
| 2  | 0.500 | 1.000 bits      | 50.0%             |
| 3  | 0.333 | 0.918 bits      | 66.7%             |
| 5  | 0.267 | 0.837 bits      | 73.3%             |
| 7  | 0.229 | 0.776 bits      | 77.1%             |
| 11 | 0.208 | 0.737 bits      | 79.2%             |
| 23 | 0.164 | 0.643 bits      | 83.6%             |

Each new prime adds to the resolved fraction but with diminishing returns: the marginal resolution from width-p is 1/p of the remaining open positions, which is a fraction D(p)/p ~ e^{-gamma}/(p*ln p) of all integers.

### 1.4. The template information rate

The total information provided by the p#-template is approximately:

    I_template(p) ~ H_binary(D(p)) bits per integer

This decreases with p because H_binary is a concave function and D(p) is moving away from 1/2. The template provides the most information per bit from the first few primes (width-2 alone provides nearly 1 bit by resolving half the integers).

---

## 2. Escape Entropy

### 2.1. The entropy of the escape process

Among the template-open positions, each is independently (approximately) prime with probability:

    D_open(n) = D(sqrt(n)) / D(p)

where D(p) is the template density and D(sqrt(n)) is the total escape density at scale n. This ratio measures the fraction of open positions that are actually prime.

The per-open-position entropy is:

    H_escape = H_binary(D_open(n)) bits

| Scale n | D(sqrt(n)) | D_open | H_escape (bits) | H * D(p) (per integer) |
|---------|-----------|--------|-----------------|----------------------|
| 100     | 0.229     | 0.857  | 0.592           | 0.158                |
| 1000    | 0.153     | 0.573  | 0.985           | 0.263                |
| 10000   | 0.120     | 0.451  | 0.993           | 0.265                |
| 100000  | 0.097     | 0.362  | 0.944           | 0.252                |

### 2.2. The peak-entropy scale

The escape entropy per open position peaks near D_open = 0.5 (maximum binary entropy), which occurs when approximately half the open positions are prime. This happens at moderate scales (n ~ 1000-10000).

At small scales (n ~ 100), D_open ~ 0.86 — most open positions are prime, giving low entropy (high predictability: "probably prime").

At large scales (n -> infinity), D_open -> 0 — very few open positions are prime, again giving low entropy (high predictability: "probably composite with large lpf").

The entropy per integer (H * D(p)) peaks at approximately 0.265 bits near n ~ 10000 and then slowly decreases. The skyline carries the most primality uncertainty per integer at moderate scales.

### 2.3. Comparison to a Poisson process

A true Poisson process with rate 1/ln(n) would have per-integer entropy:

    H_Poisson = H_binary(1/ln(n)) bits

The FS escape process has lower entropy because the template resolves most positions deterministically. The entropy savings from the template is:

| N      | H_total (bits) | H_after_template (bits) | Savings |
|--------|---------------|------------------------|---------|
| 100    | 81            | ~0                     | ~100%   |
| 1000   | 653           | 145                    | 77.9%   |
| 10000  | 5376          | 2026                   | 62.3%   |

At N = 100, the template resolves nearly everything (all primes below 10 are known from the 7#-template). At N = 10000, the template still captures 62% of the total primality information. The remaining 38% is the genuine escape uncertainty — the information that the coverage architecture cannot provide.

### 2.4. The sub-Poisson variance as an entropy signature

The observed var/mean ratio ~0.4-0.5 for prime counts (see `FS_randomness.md`) corresponds to the entropy reduction from the template. A Poisson process has maximum entropy for its mean; the sub-Poisson prime process has lower entropy because the template constrains where primes can appear. The variance reduction factor (~0.4) is the information-theoretic footprint of the template's contribution.

---

## 3. Activation Entropy

### 3.1. Width-layer entropy

For a random integer n, each prime q contributes an independent Bernoulli trial: q | n with probability 1/q. The total entropy from all width-layer assignments is:

    H_activation = sum_{q prime} H_binary(1/q) bits per integer

The first few terms:

| q  | H_binary(1/q) |
|----|---------------|
| 2  | 1.000         |
| 3  | 0.918         |
| 5  | 0.722         |
| 7  | 0.592         |
| 11 | 0.440         |
| 13 | 0.391         |

The sum diverges (slowly) as more primes contribute, reflecting the fact that a random integer's complete factorization carries unbounded information. But for practical purposes, the first few primes dominate: width-2 and width-3 alone account for 1.918 bits.

### 3.2. CRT independence produces additive entropy

Because the CRT guarantees independence of width-layer hits, the total activation entropy is the sum of individual layer entropies:

    H_activation = sum_q H_binary(1/q)

This additive decomposition is the information-theoretic content of the Euler product. Each prime contributes an independent, additive entropy term.

### 3.3. Entropy of omega(n) and mu(n)

The number of distinct prime factors omega(n) is a sum of independent Bernoulli indicators, so its entropy is the entropy of a sum of independent variables:

    H(omega) at N = 1000: 1.59 bits
    H(omega) at N = 10000: 1.78 bits

This grows slowly (approximately as log2(ln(ln(N))) + constant), reflecting the Erdos-Kac Gaussian distribution becoming broader.

The Mobius function among squarefree integers has:

    H(mu | squarefree) = 1.000 bits (at both N = 1000 and N = 10000)

This is the maximum possible entropy for a binary variable — mu is a perfect coin flip among squarefree integers. The CRT independence of width layers ensures exact equipartition between mu = +1 and mu = -1, giving maximal parity entropy.

---

## 4. Spectral Entropy

### 4.1. The entropy of the zero distribution

The zeta zeros, normalized by their local density, exhibit GUE statistics. The GUE ensemble is the maximum-entropy distribution for Hermitian matrices with fixed second moments — it maximizes the randomness of eigenvalue positions subject to the constraint that the matrix is Hermitian with a given spectral density.

In FS terms: the zero positions are the **most random** distribution consistent with the primorial template's harmonic constraints and the functional equation's symmetry. The spectral entropy is maximized.

### 4.2. GUE as constrained maximum entropy

The GUE pair correlation 1 - (sin(pi*u)/(pi*u))^2 can be derived as the maximum-entropy pair distribution subject to:

1. **Level repulsion:** Zeros cannot coincide (the determinant of the matrix vanishes when eigenvalues collide).
2. **Hermiticity:** The eigenvalues are real (the zeros lie on the critical line, under RH).
3. **Fixed density:** The local density of zeros is prescribed (N(T) ~ T*ln(T)/(2*pi)).

In FS-geometry, these constraints correspond to:
1. **Multiplicative orthogonality:** Incommensurate prime harmonics prevent degenerate resonances.
2. **Functional equation symmetry:** Constrains zeros to the critical line.
3. **Template harmonic density:** Determines the local resonance density.

The zero spectrum is maximally random *given these structural constraints*. No additional structure is imposed — the zeros are as disordered as the primorial architecture allows.

### 4.3. Spectral entropy rate

The entropy of the zero distribution in an interval [0, T] is approximately:

    H_spectral(T) ~ N(T) * ln(N(T)) ~ (T*ln T/(2*pi)) * ln(T*ln T/(2*pi))

This grows super-linearly: the spectral entropy accumulates faster than the zero count because higher zeros are embedded in a denser spectrum with more possible configurations.

The spectral entropy per zero is approximately:

    H_per_zero ~ ln(N(T)) ~ ln(T) + ln(ln(T))

This grows logarithmically: each new zero carries slightly more entropy than the last because it must be placed among a denser field of existing zeros.

---

## 5. The Total Entropy Budget

### 5.1. Decomposition

The total entropy of the FS-x increment sequence (the primary observable of the skyline) decomposes as:

    H(dx) = H(dx | template known) + I(template)

Numerically:

    H(dx) = 2.483 bits per integer (unconditional)
    H(dx | n mod 30) = 0.783 bits per integer (conditional on 5#-template)
    I(5#-template) = 1.700 bits per integer (information from template)

The template provides **68.5% of the total information** about the dx sequence. The remaining 31.5% is the genuine escape uncertainty — the unpredictable part.

### 5.2. Where the entropy resides

The entropy budget of the skyline distributes across structural levels:

**Template layer (0 bits of uncertainty, 1.700 bits of information):**
The template is deterministic. It contributes no entropy to the dx sequence but provides 1.700 bits of information per integer by resolving the status of covered positions. This is "free" information — the coverage architecture provides it without any stochastic input.

**Escape layer (~0.26 bits per integer):**
The uncertainty about whether each open position is prime or composite with large lpf. This is the genuine stochastic component — the information that the template cannot provide.

**Activation layer (~0.52 bits per integer among open positions):**
For open positions that turn out to be composite, the uncertainty about which specific large prime is the lpf. A composite open position with lpf = 7 carries different information than one with lpf = 97. This component distributes across the tail of the dx distribution.

### 5.3. The entropy compression ratio

The skyline achieves a remarkable compression of the primality information:

- **Naive encoding:** To specify which of N integers are prime requires ~N * H_binary(pi(N)/N) bits.
- **Template-assisted encoding:** After conditioning on the template, only the open-position statuses need to be specified, requiring ~N * D(p) * H_binary(D_open) bits.

The compression ratio is:

    compression = D(p) * H_binary(D_open) / H_binary(1/ln N)

At N = 10000: compression = 2026 / 5376 = 0.377. The template compresses the primality information to 37.7% of its naive size. The remaining 37.7% is incompressible — it is the genuine entropy of the escape process.

### 5.4. The information hierarchy

| Structural level | Entropy content | Information role |
|-----------------|----------------|-----------------|
| Template (Level 0) | 0 bits (deterministic) | Removes 62-78% of primality uncertainty |
| Escape (Level 1) | ~0.26 bits/int | Prime vs large-lpf composite at open positions |
| Activation (Level 2) | ~0.52 bits/int (at open composites) | Specific lpf for non-prime open positions |
| Spectral (Level 3) | ~ln(T) bits/zero | Zero positions within GUE-constrained spectrum |

Each level carries progressively more subtle information:
- The template tells you *where* primes can appear.
- The escape process tells you *which* of those positions are actually prime.
- The activation detail tells you *what kind* of composite occupies non-prime positions.
- The spectral structure tells you *how the whole pattern oscillates* around its mean.

### 5.5. The information-theoretic content of the integers

The FS entropy analysis reveals that the multiplicative structure of the integers has a definite information content, decomposable into layers:

**The deterministic layer is dominant.** The primorial template — a fully predictable structure — accounts for the majority of what can be said about any integer's factorization. Most of the "information" in the number line is actually structure, not randomness.

**The random layer is thin but irreducible.** The escape process carries only ~0.26 bits per integer of genuine uncertainty. This is the hard core of number theory — the part that cannot be resolved by structural arguments alone. It is precisely this thin layer of irreducible uncertainty that the parity barrier protects.

**The spectral layer is maximal given constraints.** The zeta zeros are as random as the primorial architecture allows. Their GUE statistics represent maximum entropy under the structural constraints of the coverage architecture. This means the zero spectrum carries no unnecessary order — it is as disordered as it can be without violating the multiplicative structure of the integers.

---

## 6. Structural Insights

### 6.1. The entropy of the parity barrier

The parity barrier (see `FS_twin_primes.md`, Section 6.4) has a precise information-theoretic formulation:

The template resolves whether a position is open or covered. But distinguishing a prime (omega = 1) from a squarefree composite with odd omega (omega = 3, 5, ...) among open positions requires information that the template does not provide. The entropy of this distinction is:

    H(prime vs odd-omega composite | open position) > 0

This entropy is irreducible by coverage-based arguments. Overcoming the parity barrier would require an information source beyond the template — one that resolves the specific omega value, not just the open/covered classification.

### 6.2. The bits-per-prime efficiency

The information needed to specify a single prime near N is approximately:

    log2(ln N) bits (to specify which open position it occupies)

This is remarkably small: at N = 10000, specifying one prime requires only ~3.3 bits (distinguishing it from ~10 nearby open positions). The template does most of the work; the escape process needs only a few bits to pin down each prime.

### 6.3. Why the PNT is a low-entropy statement

The PNT (pi(x) ~ x/ln x) specifies only the *total count* of escapes, which is a single number requiring O(log x) bits. The complete prime sequence below x requires O(x/ln x * log ln x) bits. The ratio:

    bits for PNT / bits for full prime list ~ (log x) / (x/ln x * log ln x) -> 0

The PNT captures a vanishing fraction of the total information. It is a statement about the *average* of the escape process, not its individual realizations. The vast majority of the information about primes resides in the positions of individual escape events — the entropy layer that the PNT does not touch.

### 6.4. Why RH is an entropy constraint

RH bounds the error term |psi(x) - x| at O(sqrt(x) * log^2 x). In information-theoretic terms, RH asserts that the **predictability** of the cumulative escape height is bounded: you can predict psi(x) from the smooth term x to within O(sqrt(x)) accuracy, which means the unpredictable (entropic) component of psi is at most O(sqrt(x) * log^2 x) bits.

This is a constraint on how much entropy the escape process can carry in its cumulative form: the partial sums of the escape impulse train are more predictable than the individual terms. The smoothing effect of summation compresses the escape entropy.

---

## 7. Summary

| Entropy component | Bits per integer | Source | Nature |
|-------------------|-----------------|--------|--------|
| **Template information** | ~1.70 (provided, not uncertain) | Primorial coverage architecture | Deterministic, free |
| **Escape uncertainty** | ~0.26 | Prime vs large-lpf at open positions | Irreducible, CRT-based |
| **Activation detail** | ~0.52 (at open composites) | Specific lpf of non-prime composites | Additional factorization info |
| **Total dx entropy** | 2.48 | Full increment sequence | Template + escape + activation |
| **Mu entropy** (among squarefree) | 1.00 | Width-parity coin flip | Maximum (perfect binary) |
| **Omega entropy** | ~1.78 (at N=10^4) | Gaussian width-layer count | Grows as log2(ln ln n) |
| **Template savings** | 62-78% of naive primality bits | Coverage resolves covered positions | Structural compression |
| **Spectral entropy** | ~ln(T) per zero | GUE-constrained zero placement | Maximum under constraints |

The Factor Skyline's entropy budget reveals that the multiplicative structure of the integers is predominantly deterministic: the primorial template accounts for 62-78% of the information needed to describe prime distribution. The remaining irreducible uncertainty — the escape entropy — is thin (~0.26 bits per integer) but constitutes the hard core of number theory: the information that no structural argument can resolve, protected by the parity barrier. The spectral layer (zeta zeros) carries maximum entropy given the structural constraints, confirming that the zero distribution is as random as the architecture allows. The integers are mostly structure, with a thin vein of genuine randomness running through the escape layer.
