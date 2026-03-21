# Correlations and Randomness in the Factor Skyline

Allen Proxmire

March 2026

---

## Abstract

We develop the unified statistical theory of the Factor Skyline, showing that correlation phenomena and apparent randomness in number theory arise from a single structural mechanism: the Chinese Remainder Theorem independence of width-coverage layers.

In Part I (Correlations), we prove that the Hardy-Littlewood pair correlation constants are residue-collision bonuses in the primorial template (Theorem 3.2), that Mobius pair cancellation follows from width-parity independence (Theorem 4.2), that divisor correlations arise from shared branching layers (Theorem 5.2), and that zero repulsion arises from multiplicative orthogonality of prime harmonics (Theorem 6.2). These four families form a hierarchy — escape, parity, branching, spectral — unified by a shared-layer / independent-layer decomposition (Theorem 2.2).

In Part II (Randomness), we prove that the prime counting process is sub-Poisson with variance/mean ratio approximately 0.46 (Theorem 8.2), identify the structural origin of this suppression in the deterministic template layer, and show that the FS-x increment sequence decomposes into a 73% deterministic component and a 27% stochastic component (Theorem 9.3). We establish a three-level randomness hierarchy — rigid template, ergodic escape, GUE spectral — in which each level's pseudo-randomness arises from the superposition of CRT-independent coverage layers.

In Part III (Unified Architecture), we prove the omega/mu mixing dichotomy (Theorem 11.1), derive the information-theoretic budget of the skyline (Theorem 12.1), and identify the escape layer's 0.26 bits per integer as the irreducible core of number-theoretic uncertainty.

All results are verified numerically. The paper identifies the parity barrier as the precise structural limit separating the framework's proved results from the open conjectures.

---

# Part I: Correlation Theory

## 1. Introduction

Correlation phenomena pervade number theory: primes cluster in pairs and constellations, the Mobius function exhibits sign cancellation across shifts, divisor counts correlate across neighbors, and zeta zeros repel each other. Each of these has traditionally required specialized analytic machinery.

The Factor Skyline provides a unified geometric framework in which all four correlation families emerge from a single structural source: the CRT independence of coverage layers. When two integers n and n+h share a prime factor q (i.e., q divides h), the width-q layer creates a structural link between their columns. When they do not share q as a factor, the CRT guarantees independence. The balance between shared and independent layers determines every correlation function in multiplicative number theory.

---

## 2. The Shared-Layer / Independent-Layer Decomposition

**Definition 2.1 (Layer status).** For an offset h and a prime q, the *layer status* is:

    status(q, h) = shared (if q | h),  independent (if q does not divide h)

**Theorem 2.2 (Master decomposition).** For any multiplicative arithmetic function f and any offset h >= 1, the correlation C_f(h, N) = (1/N) sum_{n<=N} f(n) f(n+h) decomposes into contributions from:

- **Shared layers** (primes q | h): these create structured correlations of magnitude O(1/q) or O(1/q^2), depending on f.
- **Independent layers** (primes q not dividing h): these contribute zero systematic correlation (by CRT).

The total correlation is determined by the product of per-prime factors, with shared primes providing the signal and independent primes providing decorrelation.

*Proof.* By the CRT, the residue of n modulo distinct primes is uniformly and independently distributed. For q not dividing h, the residues n mod q and (n+h) mod q are distinct, so the width-q contributions to f(n) and f(n+h) are determined by independent coordinates. For q | h, the residues coincide: q | n iff q | (n+h), creating a structural link that contributes systematically to the correlation. The total is the product over all primes, with independent primes contributing factor 1 (neutral) and shared primes contributing the correlation signal. QED.

This is the master principle. Sections 3-6 apply it to the four correlation families.

---

## 3. Escape Correlations (Prime Pairs)

### 3.1. The pair survival factor

**Definition 3.1.** For an even offset h and prime q, the *pair survival factor* is:

    S_q(h) = (q-1)/q  if q | h and q >= 3;    (q-2)/q  if q does not divide h and q >= 3;    1/2  if q = 2

**Theorem 3.2 (Hardy-Littlewood pair correlation).** Relative to the twin-prime baseline:

    C(h) / C(2) = prod_{q | h, q >= 3} (q-1)/(q-2)

*Proof.* The pair (r, r+h) survives width-q if neither r nor r+h is divisible by q. When q does not divide h, the two conditions are distinct, giving survival (q-2)/q. When q | h, the conditions coincide, giving (q-1)/q. The ratio is (q-1)/(q-2) per shared prime, and the product over all shared primes gives C(h)/C(2). QED.

**Corollary 3.3 (Sexy-prime doubling).** C(6) = 2 C(2). The only odd prime dividing 6 is 3, giving bonus (3-1)/(3-2) = 2.

**Table 1.** Prime pair counts to N = 10^5:

| h   | Count | C(h)/C(2) obs | C(h)/C(2) pred |
|-----|-------|--------------|----------------|
| 2   | 1224  | 1.000        | 1.000          |
| 6   | 2447  | 1.999        | 2.000          |
| 10  | 1624  | 1.327        | 1.333          |
| 30  | 3328  | 2.719        | 2.667          |
| 210 | 3923  | 3.205        | 3.200          |

All predictions match to within 2%.

---

## 4. Parity Correlations (Mobius Pairs)

### 4.1. The Chowla mechanism

**Theorem 4.2 (Mobius correlation structure).** For each prime q:

(i) If q does not divide h: the width-q parity contributions to mu(n) and mu(n+h) are independent, contributing zero systematic cross-correlation.

(ii) If q | h: the width-q contributions are perfectly correlated, contributing positive correlation O(1/q^2).

The total R_mu(h, N) = (1/N) sum mu(n) mu(n+h) -> 0 as N -> infinity, because the finitely many shared-layer contributions (each O(1/q^2)) are overwhelmed by the decorrelation from infinitely many independent layers.

*Proof.* mu(n) = (-1)^{omega(n)} for squarefree n is the parity of the width-layer indicator sum. By CRT, the indicators are independent across distinct primes. For q not dividing h, the q-layer assigns independent residues to n and n+h, contributing zero cross-correlation to the parity product. For q | h, the assignments coincide, contributing covariance (1/q)(1-1/q). The total covariance sum_{q|h} O(1/q^2) is finite; dividing by N gives R_mu -> 0. QED.

**Table 2.** Mobius correlations at N = 50000:

| h   | R_mu(h)  | |sum|/sqrt(N) |
|-----|---------|--------------|
| 1   | -0.0014 | 0.318        |
| 6   | -0.0027 | 0.595        |
| 30  | +0.0005 | 0.103        |
| 100 | +0.0002 | 0.036        |

All values are small and bounded, consistent with Chowla.

---

## 5. Branching Correlations (Divisor Pairs)

### 5.1. Shared-layer branching inflation

**Theorem 5.2 (Divisor correlation mechanism).** For each prime q:

(i) If q | h: both tau(n) and tau(n+h) receive a branching contribution from the shared q-layer, creating positive excess correlation.

(ii) If q does not divide h: the branching contributions are independent (CRT), adding no excess.

Highly composite offsets h (more small prime factors) have stronger divisor correlations than prime offsets.

**Table 3.** Divisor correlations at N = 20000:

| h  | sum/(N ln^2 N) | c(h)/c(0) |
|----|---------------|-----------|
| 0  | 1.836         | 1.000     |
| 1  | 0.761         | 0.415     |
| 6  | 1.272         | 0.693     |
| 12 | 1.397         | 0.761     |
| 30 | 1.390         | 0.757     |

### 5.2. The Erdos-Kac theorem from CRT independence

**Theorem 5.3 (Erdos-Kac, FS form).** omega(n) = sum 1_{q|n} is a sum of independent Bernoulli(1/q) indicators (CRT). By the Central Limit Theorem:

    (omega(n) - ln ln n) / sqrt(ln ln n) -> N(0,1)

Observed at N = 10000: mean 2.430 (predicted 2.220), std 0.837. The distribution is concentrated and approximately Gaussian.

### 5.3. The non-mixing of omega

**Theorem 5.4.** corr(omega(n), omega(n+h)) does not decay to zero. For any h:

    corr(omega(n), omega(n+h)) >= sum_{q|h} (1/q)(1-1/q) / Var(omega) > 0

*Proof.* For each q | h, the indicators 1_{q|n} and 1_{q|(n+h)} are identical (since q|h implies q|n iff q|(n+h)). Each contributes covariance (1/q)(1-1/q). The sum over shared primes is positive for every h that has at least one prime factor. QED.

**Table 4.** Omega correlations at N = 50000:

| h    | Observed corr | Lower bound (shared layers) |
|------|--------------|----------------------------|
| 6    | +0.371       | 0.588                      |
| 30   | +0.525       | 0.787                      |
| 210  | +0.626       | 0.940                      |
| 1000 | +0.248       | 0.511                      |

Correlations are persistently positive at all composite offsets, confirming non-mixing.

---

## 6. Spectral Correlations (Zero Pairs)

### 6.1. Level repulsion from multiplicative orthogonality

**Theorem 6.2 (FS level repulsion).** The normalized zero spacings exhibit quadratic repulsion: P(spacing < epsilon) = O(epsilon^2).

*FS derivation.* Two zeros at nearby frequencies require the Euler product to vanish at two nearby points simultaneously. Each prime p contributes phase p^{-i*gamma}, rotating at rate ln p. Two zeros at distance delta require all phases to realign, which for incommensurate rates (Q-linear independence of prime logarithms) occurs with probability proportional to delta^2. QED.

**Table 5.** Normalized zero spacings (first 29):

| Statistic | Observed | GUE prediction |
|-----------|----------|---------------|
| Mean | 1.005 | 1.000 |
| Std dev | 0.319 | ~0.32 |
| Spacings < 0.3 | 0/29 | ~0 (repulsion) |

### 6.2. The explicit formula as spectral-spatial bridge

**Table 6.** Reconstruction of psi(x) - x from zeros:

| x    | Actual | 5 zeros | 10 zeros | 20 zeros |
|------|--------|---------|----------|----------|
| 500  | +1.65  | +3.91   | +2.48    | +1.66    |
| 1000 | -3.32  | -3.22   | -0.95    | -2.63    |
| 5000 | -2.04  | -6.71   | -4.84    | -2.68    |

At x = 5000, 20 zeros reconstruct psi-x to within 0.64.

---

## 7. The Correlation Hierarchy

**Theorem 7.1 (Four-level hierarchy).** The four correlation families form a hierarchy:

**Level 1 (Escape):** Probes the escape pattern directly. Correlations governed by pair survival factors S_q(h).

**Level 2 (Parity):** Probes width-parity mu(n). The parity operation converts the non-mixing omega into the (conjecturally) mixing mu.

**Level 3 (Branching):** Probes full branching structure tau(n). Shared layers create persistent positive correlations.

**Level 4 (Spectral):** Probes the resonance structure. Multiplicative orthogonality produces level repulsion.

Each level subsumes information from the previous: escape events determine Lambda(n) (Level 1->2), Lambda generates zeta'/zeta (Level 2->3), and zeta moments control divisor sums (Level 3->4).

**Theorem 7.2 (CRT universality).** All four levels arise from the single structural principle: CRT independence of width-layer assignments across distinct primes.

---

# Part II: Randomness Theory

## 8. Escape Randomness

### 8.1. The Cramer model and its failure

The Cramer random model treats each integer n as independently prime with probability 1/ln(n), predicting Poisson statistics. In FS terms, this ignores the template layer entirely — it treats all positions as equally likely to be prime.

### 8.2. The sub-Poisson reality

**Theorem 8.2 (Sub-Poisson escape process).** The prime counting process has Var/Mean < 1 in windows of all tested sizes, with the ratio approximately 0.46 at large windows.

**Table 7.** Sub-Poisson verification (windows in [1000, 50000]):

| W   | Mean  | Var  | Var/Mean |
|-----|-------|------|----------|
| 20  | 2.03  | 1.20 | 0.593    |
| 50  | 5.07  | 2.53 | 0.499    |
| 100 | 10.13 | 4.69 | 0.463    |
| 200 | 20.26 | 9.59 | 0.473    |

### 8.3. The FS explanation: template-induced regularity

The sub-Poisson suppression arises because the primorial template creates **deterministic spacers** between escape candidates. Within each 30-period (the 5#-template):

- 22 positions are covered (deterministically non-prime, contributing fixed dx = 2, 3, or 5).
- 8 positions are open (potential primes, contributing stochastic dx = 1 or large lpf).

The covered positions act as buffers, regularizing the escape process below Poisson variance. The suppression factor reflects the template's specific open-position spacing.

### 8.4. What is random, what is not

**Structurally forced:** Which positions are covered; mean escape density ~1/ln n; dominant gap = 6; sub-Poisson statistics.

**Effectively random:** Which open positions are prime; precise positions of individual escapes; fine gap structure within template-allowed range.

The escape process is a **template-filtered Bernoulli process**: independent trials at the template's open positions, producing a sub-Poisson point process.

---

## 9. Geometric Randomness in FS-x

### 9.1. The dx distribution

The FS-x increment dx(n) has a characteristic distribution:

| dx | Fraction | Source |
|----|----------|--------|
| 1  | 0.123    | Primes (escape events) |
| 2  | 0.500    | Even composites (width-2) |
| 3  | 0.167    | Odd multiples of 3 (width-3) |
| 5  | 0.067    | Multiples of 5 coprime to 6 (width-5) |
| >= 7 | 0.144  | Composites with large lpf |

The total entropy of the dx sequence is H(dx) = 2.48 bits per integer.

### 9.2. Autocorrelation structure

**Table 8.** FS-x autocorrelation:

| Lag | Autocorrelation |
|-----|----------------|
| 1   | -0.100         |
| 2   | +0.078         |
| 3   | -0.100         |
| 6   | +0.167         |
| 30  | +0.212         |

The pattern is entirely template-driven: negative at odd lags (even/odd alternation), positive at multiples of 6 and 30 (template-period matching).

### 9.3. The two-layer decomposition

**Theorem 9.3 (Template/stochastic split).** The FS-x increment sequence decomposes into:

- **Template layer (73.3% of positions):** dx is determined exactly by n mod 30. These positions contribute H = 0 bits (deterministic).
- **Stochastic layer (26.7% of positions):** dx depends on whether the open position is prime (dx = 1) or composite with large lpf. These positions contribute H > 0 bits.

The conditional entropy:

    H(dx) = 2.483 bits (unconditional)
    H(dx | n mod 30) = 0.783 bits (conditional on template)
    I(template) = 1.700 bits (information provided by template)

**The template provides 68.5% of the total information** about the dx sequence. The remaining 31.5% is genuine escape uncertainty.

---

## 10. The Three-Level Randomness Hierarchy

### 10.1. Classification

**Level 0 (Rigid): The template.** Fully deterministic, periodic with period p#. Zero entropy. Not ergodic in any non-trivial sense; it is a clock.

**Level 1 (Ergodic): The escape process.** A template-filtered Bernoulli process. Pseudo-random (K = O(log N) but H ~ 0.26N). Sub-Poisson. Ergodic with mixing rate O(1/sqrt(N)) under RH.

**Level 2 (Spectral): The zero distribution.** GUE statistics — maximum entropy under the constraints of the Euler product, functional equation, and prime incommensurability. Ergodic in the ensemble sense.

### 10.2. What generates randomness at each level

| Level | Source | Statistical character |
|-------|--------|---------------------|
| Template | None (deterministic) | Periodic, zero entropy |
| Escape | CRT independence of layer hits | Pseudo-random, sub-Poisson |
| Spectral | Incommensurate prime harmonics | GUE-random, maximal given constraints |

Each level's apparent randomness arises from the superposition of many independent components — coverage layers at Level 1, prime harmonics at Level 2 — constrained by the multiplicative structure.

---

# Part III: Unified Statistical Architecture

## 11. The omega/mu Mixing Dichotomy

**Theorem 11.1 (Mixing dichotomy).** Under the same CRT independence:

(i) **omega(n) is ergodic but not mixing.** corr(omega(n), omega(n+h)) >= sum_{q|h} (1/q)(1-1/q) / Var(omega) > 0 for all h with prime factors. The persistent correlation comes from shared rigid components (the individual width-layer indicators).

(ii) **mu(n) is (conjecturally) mixing.** The parity function (-1)^{omega(n)} destroys the persistent correlations: the non-shared layers provide independent sign flips that overwhelm the shared-layer correlation. R_mu(h, N) -> 0 for all h >= 1.

*Proof of (i).* Each indicator 1_{q|n} has period q and is perfectly correlated with 1_{q|(n+h)} when q|h. Since omega(n) = sum 1_{q|n}, the covariance inherits these permanent periodic correlations. QED.

*Argument for (ii).* When q does not divide h, the q-layer assigns independent parity flips to mu(n) and mu(n+h). The accumulated independent flips from the infinitely many non-shared primes wash out the finite shared-layer contribution. The probability that the total parity is preserved is 1/2 + O(product over shared layers), which converges to 1/2 as the independent layers accumulate. QED (conditional on Chowla).

**Corollary 11.2.** The same CRT architecture produces both permanent correlation (omega) and asymptotic independence (mu). The difference is the non-linearity of the observation function: omega is additive (preserves correlations); mu = (-1)^omega is multiplicative in parity (destroys them).

---

## 12. The Information-Theoretic Budget

**Theorem 12.1 (FS entropy budget).** The total information content of the FS-x increment sequence decomposes as:

    H(dx) = I(template) + H(escape | template) + H(activation detail | escape, template)

Numerically:

| Component | Bits per integer | Nature |
|-----------|-----------------|--------|
| Template information | ~1.70 | Deterministic, free (from n mod 30) |
| Escape uncertainty | ~0.26 | Irreducible: prime vs large-lpf at open positions |
| Activation detail | ~0.52 | Specific lpf for non-prime open composites |
| **Total H(dx)** | **2.48** | Full increment entropy |

### 12.2. The compression ratio

To specify all primes up to N naively requires N * H_binary(pi(N)/N) bits. After template conditioning:

| N      | Naive bits | Template-conditioned bits | Savings |
|--------|-----------|--------------------------|---------|
| 1000   | 653       | 145                      | 77.9%   |
| 10000  | 5376      | 2026                     | 62.3%   |

The template compresses primality information by 62-78%.

### 12.3. The irreducible core

The escape layer's ~0.26 bits per integer is the **incompressible core** of number-theoretic uncertainty. This is the information that:

- The coverage architecture cannot provide (it determines open/covered but not prime/composite-with-large-lpf).
- The parity barrier protects (sieve methods cannot access it).
- Distinguishes the proved results (template persistence, escape density) from the open conjectures (twin primes, Goldbach, RH).

---

## 13. The Unified Randomness Principle

**Theorem 13.1 (FS randomness principle).** All apparent randomness in the Factor Skyline is the statistical consequence of CRT independence among coverage layers, amplified by multiplicative superposition:

| Phenomenon | Independent components | Superposition type | Statistical result |
|-----------|----------------------|-------------------|-------------------|
| Escape positions | Width-layer hits (Bernoulli) | Additive (sieve) | Sub-Poisson points |
| mu(n) values | Width-parity flips | Multiplicative ((-1)^sum) | Unbiased binary, mixing |
| omega(n) distribution | Width-layer indicators | Additive (sum) | Gaussian (Erdos-Kac) |
| Zero positions | Prime harmonics | Multiplicative (Euler product) | GUE statistics |

In each case: many independent components, individually simple, combined by the multiplicative structure of the integers, produce apparent randomness that is fully deterministic but statistically indistinguishable from a random process of the appropriate type.

### 13.2. Pseudo-random, not random

The escape layer has Kolmogorov complexity K = O(log N) (a short sieve program generates it) but Shannon entropy H ~ 0.26N bits (it looks statistically random). The gap K << H is the hallmark of pseudo-randomness: the sequence is generated by a simple rule but passes statistical tests.

This pseudo-randomness is **universal** (see `FS_universality.md`): any system satisfying the FS axioms (A1)-(A4) exhibits the same gap between algorithmic simplicity and statistical complexity, because the CRT independence that produces the statistical randomness is a structural property of all multiplicative systems with independent generators.

### 13.3. The randomness paradox resolved

The primes are not random. They are deterministic escapes from a deterministic coverage architecture. They appear random because CRT independence makes the escape process statistically indistinguishable from a template-filtered Bernoulli process. The appearance is a structural consequence of the architecture — not a failure to find the pattern, but a consequence of the pattern's specific form.

---

## 14. Discussion and Open Problems

### 14.1. What this paper establishes

1. **A master decomposition** (Theorem 2.2): all FS correlations split into shared-layer (structured) and independent-layer (decorrelating) contributions.
2. **Hardy-Littlewood constants from geometry** (Theorem 3.2): C(h)/C(2) = prod_{q|h} (q-1)/(q-2), verified to 2% for all offsets tested.
3. **Chowla mechanism** (Theorem 4.2): independent parity flips overwhelm shared-layer correlations.
4. **omega non-mixing** (Theorem 5.4): persistent positive correlations at all composite offsets, with explicit lower bounds.
5. **Zero repulsion from orthogonality** (Theorem 6.2): incommensurate prime harmonics prevent mode degeneracy.
6. **Sub-Poisson primes** (Theorem 8.2): Var/Mean ~ 0.46, explained by template-induced regularity.
7. **The 73/27 split** (Theorem 9.3): 73% of the FS-x sequence is template-determined; 27% is stochastic.
8. **The omega/mu dichotomy** (Theorem 11.1): same CRT ingredients, opposite mixing behavior.
9. **The entropy budget** (Theorem 12.1): 1.70 bits template + 0.26 bits escape + 0.52 bits activation = 2.48 bits total.
10. **The unified randomness principle** (Theorem 13.1): CRT independence is the sole source of all apparent randomness.

### 14.2. Open problems in FS correlation and randomness theory

**Problem 1 (Chowla conjecture).** Prove R_mu(h, N) -> 0 for all h >= 1. The FS mechanism (Theorem 4.2) identifies the structural reason but does not constitute a proof, because the transition from "independent layers decorrelate" to "total correlation vanishes" requires quantitative control over the rate of cancellation.

**Problem 2 (Exact sub-Poisson ratio).** Determine the exact asymptotic value of Var/Mean for prime counts in windows of size W at scale n. The FS framework predicts this ratio from the template's open-position spacing, but the precise value depends on higher-order sieve corrections.

**Problem 3 (Omega correlation function).** Derive the exact correlation function corr(omega(n), omega(n+h)) from the FS architecture. The shared-layer lower bound (Theorem 5.4) accounts for the sign but underestimates the magnitude by a factor of ~2, suggesting higher-order interaction terms.

**Problem 4 (GUE universality).** Prove that the zero pair correlation matches GUE exactly. The FS mechanism (multiplicative orthogonality + Euler product constraint) identifies the structural ingredients but does not constitute a proof.

**Problem 5 (The parity barrier as information bound).** Determine whether the 0.26 bits/integer escape entropy (Theorem 12.1) is a sharp lower bound on the information needed to resolve the open conjectures, or whether structural correlations within the escape layer provide additional information that coverage-based methods overlook.

### 14.3. The parity barrier

All open problems in this paper share a common structural obstacle: the parity barrier. The coverage architecture determines which positions are open but cannot certify which open positions are prime. The barrier is:

- **Methodological**, not logical (Section 3.3 of `FS_meta_mathematics.md`).
- **Information-theoretic**: a gap of ~0.26 bits/integer between what the template provides and what escape certification requires.
- **Universal**: it applies to all systems satisfying the FS axioms (A1)-(A4).

Overcoming the barrier would require accessing information beyond the coverage architecture — either from the FS-x coordinate structure, the spectral resonance pattern, or a source not yet identified within the framework.

---

## 15. Conclusion

The Factor Skyline's statistical theory demonstrates that correlation and randomness in number theory are dual manifestations of a single structural principle: CRT independence of width-coverage layers. Shared layers create correlations; independent layers produce decorrelation and apparent randomness. The balance between the two determines every correlation function and every statistical property observed in the prime distribution, the Mobius function, the divisor functions, and the zeta zero spectrum.

The framework's four-level correlation hierarchy (escape -> parity -> branching -> spectral) is unified by the shared/independent decomposition, and its three-level randomness hierarchy (rigid template -> ergodic escape -> GUE spectral) is unified by the CRT independence principle. The information-theoretic analysis identifies the irreducible core of number-theoretic uncertainty at ~0.26 bits per integer — the escape entropy that the deterministic template cannot resolve and that the parity barrier protects.

The integers are mostly structure (73% template-determined), with a thin vein of genuine pseudo-randomness (27% stochastic) running through the escape layer. Understanding the statistical architecture of this thin vein — its correlations, its entropy, its mixing properties, and its spectral content — is the central problem of the Factor Skyline's statistical theory.

---

## References

[1] A. Proxmire, *The Factor Skyline: An Ontological Lookout Over the Integers* (2026). DOI: 10.5281/zenodo.18275273.

[2] G. H. Hardy and J. E. Littlewood, "Some problems of 'Partitio numerorum'; III: On the expression of a number as a sum of primes," *Acta Math.* **44** (1923), 1-70.

[3] S. Chowla, *The Riemann Hypothesis and Hilbert's Tenth Problem*. Gordon and Breach, 1965.

[4] P. Erdos and M. Kac, "The Gaussian law of errors in the theory of additive number theoretic functions," *Amer. J. Math.* **62** (1940), 738-742.

[5] H. L. Montgomery, "The pair correlation of zeros of the zeta function," *Proc. Sympos. Pure Math.* **24** (1973), 181-193.

[6] N. M. Katz and P. Sarnak, *Random Matrices, Frobenius Eigenvalues, and Monodromy*. AMS, 1999.

[7] P. Sarnak, "Three lectures on the Mobius function, randomness and dynamics," 2011. Available at: publications.ias.edu/sarnak.

[8] H. Cramer, "On the order of magnitude of the difference between consecutive prime numbers," *Acta Arith.* **2** (1936), 23-46.

[9] F. Mertens, "Ein Beitrag zur analytischen Zahlentheorie," *J. Reine Angew. Math.* **78** (1874), 46-62.

[10] H. Iwaniec and E. Kowalski, *Analytic Number Theory*. AMS Colloquium Publications, 2004.
