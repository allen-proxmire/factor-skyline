# The Factor Skyline: A Unified Architecture for Multiplicative Number Theory

Allen Proxmire

March 2026

---

# Front Matter

## Preface

This monograph develops the Factor Skyline — a two-dimensional representation of the integers in which each integer n becomes a column of width lpf(n) and height n/lpf(n) — as a unified geometric framework for multiplicative number theory. The work synthesizes four streams of investigation: the architectural foundation (Part I), the correlation and randomness theories (Part II), the information-theoretic, dynamical, and universality theories (Part III), and the meta-structural analysis of the framework itself (Part IV).

The central claim is that a single function — the least prime factor — generates, through five emergent concepts (width, height, activation, coverage, escape), the full suite of classical results in prime distribution theory, together with new structural invariants that are invisible on the one-dimensional number line.

The Factor Skyline does not change the integers or contradict existing mathematics. It provides a new ontology — a new way of seeing — in which the mechanisms behind prime behavior become geometrically visible.

## Overview of the Factor Skyline

Each integer n >= 2 has **width** w(n) = lpf(n) and **height** h(n) = n/lpf(n). Columns are placed consecutively; the cumulative position is x_FS(n). Primes contribute dx = 1 (narrow escape spires); composites contribute dx = lpf(n) (wide covered columns).

Prime squares p^2 are **activation** thresholds where new width layers enter the geometry. Each layer **covers** fraction 1/p of the remaining space. What escapes all layers is prime. The **escape density** D(p) = prod(1-1/q) governs everything.

## Notation Guide

| Symbol | Meaning |
|--------|---------|
| lpf(n) | Least prime factor of n |
| w(n), h(n) | Width and height: w = lpf, h = n/lpf |
| (x_FS(n), y_FS(n)) | FS-coordinates |
| dx(n) | FS-x increment: 1 if prime, lpf(n) if composite |
| D(p) | Escape density: prod_{q<=p}(1-1/q) |
| p# | Primorial: 2*3*...*p |
| phi(p#) | Euler totient of p# = p# * D(p) |
| v_q(H) | Distinct residues of k-tuple H modulo q |
| S_q(H) | Survival factor: (q - v_q)/q |
| C_H | Hardy-Littlewood k-tuple constant |
| H_b(x) | Binary entropy: -x log_2 x - (1-x) log_2(1-x) |
| K(x) | Kolmogorov complexity |
| omega(n) | Number of distinct prime factors |
| Omega(n) | Number of prime factors with multiplicity |
| tau(n), sigma(n) | Divisor count and divisor sum |
| mu(n) | Mobius function |
| theta(x), psi(x) | Chebyshev functions |
| T_FS | First-order theory of FS axioms |
| (A1)-(A4) | Universality axioms |
| (M1)-(M3) | Meta-axioms: order, multiplication, UF |

## Architectural Map

```
Part I: ARCHITECTURE                      Part II: STATISTICS
  Ch 1. Primitives & coordinates             Ch 6. Correlation theory
  Ch 2. Templates & epochs                   Ch 7. Randomness theory
  Ch 3. Coverage protection                  Ch 8. Unified statistics
  Ch 4. Geometric PNT & Dickman
  Ch 5. Mobius, divisors, conservation

Part III: FOUNDATIONS                     Part IV: META-THEORY
  Ch 9. Entropy theory                      Ch 12. Meta-structure
  Ch 10. Ergodic theory                     Ch 13. Meta-mathematics
  Ch 11. Universality theory                Ch 14. Unified meta-architecture
```

---

# Part I: The Factor Skyline Architecture

## Chapter 1. The Five Primitives

**Definition I.1 (Least prime factor).** For n >= 2, lpf(n) = min{p : p | n, p prime}. Set lpf(1) = 1.

**Definition I.2 (Width and height).** w(n) = lpf(n), h(n) = n/lpf(n).

**Definition I.3 (FS-coordinates).**

    x_FS(1) = 1, y_FS(1) = 1
    dx(n) = 1 if n prime, lpf(n) if composite
    x_FS(n) = x_FS(n-1) + dx(n)
    y_FS(n) = n if prime, n/lpf(n) if composite

**Definition I.4 (Recursive width decomposition).** The column W(n) is the sequence of widths from iterated lpf extraction, terminating at 1. Length = Omega(n) + 1.

**Definition I.5 (Activation).** Prime p activates at p^2.

**Theorem I.1.** p^2 = min{n : lpf(n) = p}. *(Proof: all multiples of p below p^2 have a smaller factor.)*

**Definition I.6 (Epoch).** Epoch_k = [p_k^2, p_{k+1}^2). Coverage is frozen within each epoch.

**Definition I.7 (Coverage and escape density).**

    D(p) = prod_{q <= p, q prime} (1 - 1/q)

**Theorem I.2 (CRT independence).** Coverage layers are independent: for distinct primes q_1,...,q_k, the probability that a random integer is coprime to all of them is prod(1-1/q_i). *(Proof: CRT.)*

**Definition I.8 (Escape).** n escapes iff lpf(n) = n (n is prime).

**Theorem I.3.** The escape set is exactly the set of primes.

**Table I.1.** FS-coordinates for n = 1 to 30 (see Appendix A).

---

## Chapter 2. Templates and Epochs

**Definition I.9 (Primorial and template).** p# = 2*3*...*p. The template T_p classifies each residue mod p# as open (coprime) or covered.

**Theorem I.4 (Template periodicity).** Width assignments mod p# depend only on n mod p#.

**Theorem I.5 (Open-position count).** phi(p#) = p# * D(p).

**Table I.2.** Template statistics:

| p# | Period | phi | D(p) | Twin-open | Triplet-open |
|----|--------|-----|------|-----------|-------------|
| 30 | 30 | 8 | 0.267 | 3 | 2 |
| 210 | 210 | 48 | 0.229 | 15 | 8 |
| 2310 | 2310 | 480 | 0.208 | 135 | 64 |
| 30030 | 30030 | 5760 | 0.192 | 1485 | 640 |

**Theorem I.6 (No activation within a square window).** [n^2, (n+1)^2) contains no activation event in its interior.

---

## Chapter 3. Coverage Protection and Template Persistence

**Definition I.10 (Residue occupation number).** v_q(H) = |{h_i mod q}| for k-tuple H.

**Definition I.11 (Admissibility).** H is admissible iff v_q(H) < q for all primes q.

**Theorem I.7 (Survival factor).** S_q(H) = (q - v_q(H))/q > 0 for admissible H.

**Theorem I.8 (Coverage protection).** Width-q cannot eliminate all members of an admissible constellation. If q|(r+h_i), then q does not divide r+h_j for h_j not congruent to h_i mod q.

**Theorem I.9 (k-tuple constant).** C_H = prod_q S_q(H)/(1-1/q)^k > 1 for all admissible H.

**Table I.3.** k-tuple constants: C_twin = 1.320, C_sexy = 2.646, C_triplet = 2.858, C_quad = 4.151.

**Theorem I.10 (Template persistence).** N_H(p_{k+1}) = N_H(p_k) * (p_{k+1} - v_{p_{k+1}}). The constellation-open count per template period grows without bound.

**Theorem I.11 (FS-x footprint invariance).** Every admissible constellation has a fixed FS-x inter-escape gap pattern, invariant across all sufficiently large instances:

| Constellation | FS-x gaps | Span | Verified instances |
|---------------|-----------|------|--------------------|
| Twin (0,2) | [3] | 3 | All 23 below 500 |
| Triplet (0,2,6) | [3,8] | 11 | All 11 below 500 |
| Quadruplet (0,2,6,8) | [3,8,3] | 14 | All 4 below 500 |

---

## Chapter 4. The Geometric PNT and Dickman Smoothness

**Theorem I.12 (Activation horizon).** Every composite n <= N has lpf(n) <= sqrt(N).

**Theorem I.13 (Geometric PNT).** pi(N) ~ N * D(sqrt(N)). Via Mertens: pi(N) = Theta(N/ln N).

**Table I.4.** PNT verification:

| N | pi(N) | N*D(sqrt N) | N/ln N | pi/(N/ln N) |
|---|-------|-------------|--------|-------------|
| 1000 | 168 | 152.9 | 144.8 | 1.160 |
| 10000 | 1229 | 1203.2 | 1085.7 | 1.132 |
| 100000 | 9592 | 9651.9 | 8685.9 | 1.104 |

**Theorem I.14 (Dickman function from column peeling).** Psi(x, x^{1/u})/x -> rho(u), where rho satisfies u*rho'(u) = -rho(u-1).

**Theorem I.15 (Smooth-rough duality).** Smooth density rho(u) and rough density D(y) are dual views of the same coverage product.

---

## Chapter 5. Mobius, Divisors, and the Conservation Law

**Theorem I.16 (Squarefree density).** prod_p(1-1/p^2) = 6/pi^2.

**Theorem I.17 (Mobius equidistribution).** Among squarefree integers, mu is equidistributed between +1 and -1.

**Theorem I.18.** tau(n) = prod(e_i + 1) counts sub-column selections. sigma(n) = prod(p^{e+1}-1)/(p-1) sums sub-column heights.

**Theorem I.19 (Erdos-Kac).** (omega(n) - ln ln n)/sqrt(ln ln n) -> N(0,1). *(CRT independence + CLT.)*

**Theorem I.20.** avg tau ~ ln N; avg sigma/n -> pi^2/6.

**Theorem I.21 (Conservation law).** theta(x) = sum_{p<=x} ln p ~ x. Escape height accumulates at unit rate.

**Table I.5.** Conservation verification: theta/x = 0.837, 0.956, 0.990, 0.997 at x = 10^2, 10^3, 10^4, 10^5.

**Theorem I.22 (Template width invariants).** The width-q column count per p#-period is invariant: n_q = (p#/q) * prod_{r<q}(1-1/r).

*This completes Part I. The architectural foundation comprises 22 theorems, 11 definitions, and 5 verification tables.*

---

# Part II: Correlations and Randomness in the Skyline

*Part II builds on the architectural foundation of Part I to develop the statistical theory. The key insight: all correlations and all apparent randomness arise from a single mechanism — CRT independence of width layers (Theorem I.2).*

## Chapter 6. Correlation Theory

### 6.1. The master decomposition

**Definition II.1 (Layer status).** status(q, h) = shared if q | h, independent otherwise.

**Theorem II.1 (Shared/independent decomposition).** For any multiplicative f and offset h, the correlation C_f(h) decomposes: shared layers (q | h) produce the correlation signal; independent layers (q does not divide h) produce decorrelation.

### 6.2. Escape correlations

**Theorem II.2 (Hardy-Littlewood pair correlation).** C(h)/C(2) = prod_{q|h, q>=3} (q-1)/(q-2).

**Corollary II.1 (Sexy-prime doubling).** C(6) = 2*C(2). *(The factor 2 comes from q=3: (3-1)/(3-2) = 2.)*

**Table II.1.** Pair counts to 10^5: h=2 (1224), h=6 (2447, ratio 1.999), h=30 (3328, ratio 2.719), h=210 (3923, ratio 3.205). All match predictions to within 2%.

### 6.3. Parity correlations

**Theorem II.3 (Mobius correlation).** For q not dividing h: independent parity flips, zero cross-correlation. For q | h: correlated contribution O(1/q^2). Total: R_mu(h, N) -> 0. *(This is the Chowla mechanism.)*

**Table II.2.** Mobius correlations at N=50000: all |R_mu(h)| < 0.006.

### 6.4. Branching correlations

**Theorem II.4 (Divisor correlation).** Shared width layers inflate both tau(n) and tau(n+h), creating positive excess. Composite offsets have stronger correlations.

**Theorem II.5 (omega non-mixing).** corr(omega(n), omega(n+h)) >= sum_{q|h}(1/q)(1-1/q)/Var(omega) > 0 for all h with prime factors. The correlation does not decay.

**Table II.3.** Omega correlations at N=50000: h=6 (+0.371), h=30 (+0.525), h=1000 (+0.248). Persistently positive.

### 6.5. Spectral correlations

**Theorem II.6 (Level repulsion).** Normalized zero spacings exhibit quadratic repulsion: P(spacing < epsilon) = O(epsilon^2). *(Incommensurate prime harmonics prevent mode degeneracy.)*

**Table II.4.** Normalized spacings (first 29): 0 below 0.3, 27 in [0.3, 1.5], 2 above 1.5. GUE-consistent.

### 6.6. The correlation hierarchy

**Theorem II.7 (Four-level hierarchy).** Escape -> parity -> branching -> spectral. Each level subsumes the previous through Dirichlet series.

**Theorem II.8 (CRT universality).** All four levels arise from CRT independence.

---

## Chapter 7. Randomness Theory

### 7.1. The sub-Poisson escape process

**Theorem II.9 (Sub-Poisson).** Var/Mean of prime counts in windows ~ 0.46, vs 1.0 for Poisson. The template creates deterministic spacers that suppress variance.

**Table II.5.** Sub-Poisson verification: W=50 (0.499), W=100 (0.463), W=200 (0.473).

### 7.2. The template/stochastic split

**Theorem II.10 (73/27 split).** The dx sequence is 73.3% template-determined (dx forced by n mod 30) and 26.7% stochastic (open positions where dx = 1 or large lpf).

**Table II.6.** dx autocorrelation: lag-1 = -0.100, lag-6 = +0.167, lag-30 = +0.212. Entirely template-driven.

### 7.3. The randomness hierarchy

**Theorem II.11 (Three levels).** Level 0 (template): rigid, zero entropy. Level 1 (escape): pseudo-random, sub-Poisson. Level 2 (spectral): GUE-random, maximal given constraints.

### 7.4. The mixing dichotomy

**Theorem II.12 (omega/mu dichotomy).** omega is ergodic but not mixing (persistent shared-layer correlations). mu is conjecturally mixing (parity destroys persistent correlations through independent sign flips).

**Corollary II.2.** Same CRT, opposite mixing behavior. The non-linearity of the observation function determines mixing.

---

## Chapter 8. Unified Statistical Architecture

### 8.1. The entropy budget

**Theorem II.13 (FS entropy budget).**

    H(dx) = 2.483 bits/int (total)
    I(template) = 1.700 bits/int (deterministic, 68.5%)
    H(escape + activation | template) = 0.783 bits/int (stochastic, 31.5%)

The escape layer alone carries ~0.26 bits/int of irreducible uncertainty — the information-theoretic content of the parity barrier.

### 8.2. The unified randomness principle

**Theorem II.14 (FS randomness principle).** All apparent randomness in the skyline arises from CRT independence among coverage layers, amplified by multiplicative superposition. The primes are not random; they are deterministic escapes that appear random because CRT independence makes the escape process statistically indistinguishable from filtered-Bernoulli.

*Part II comprises 14 theorems, 1 definition, 2 corollaries, and 6 verification tables. All results derive from CRT independence (Theorem I.2).*

---

# Part III: Information, Dynamics, and Universality

*Part III examines the foundations of the statistical theory developed in Part II: what information does the skyline carry (entropy), how does it evolve (dynamics), and which features are universal (universality).*

## Chapter 9. Entropy Theory

**Theorem III.1 (Template: zero entropy, high information).** H(template | n mod p#) = 0. The template removes 50-84% of primality uncertainty (Table III.1).

**Theorem III.2 (Escape entropy).** Per-open-position entropy H_b(D_open) peaks near n = 10000 where D_open ~ 0.45. Per-integer escape entropy ~ 0.265 bits. This is the irreducible core.

**Theorem III.3 (Activation entropy).** H_activation = sum_q H_b(1/q), additive by CRT. H(mu | squarefree) = 1.000 bits (maximum binary entropy).

**Theorem III.4 (Spectral entropy).** GUE = maximum entropy under prime-harmonic constraints.

**Theorem III.5 (Parity barrier as information barrier).** ~0.26 bits/int that the architecture cannot provide: the distinction between omega = 1 and omega >= 3 at open positions. This equals the conditional entropy H(escape | template).

---

## Chapter 10. Ergodic Theory

**Theorem III.6 (Template rigidity).** The template is periodic with period p#; trivially ergodic, not mixing.

**Theorem III.7 (Escape ergodicity).** pi(N)/N -> 0 (ergodic). Mixing rate O(1/sqrt(N)) under RH. Super-ergodic relative to Poisson (variance suppressed by template).

**Theorem III.8 (omega non-mixing, mu mixing).** = Theorems II.5 and II.12, restated in ergodic language. omega: ergodic, not mixing (persistent correlations from shared rigid components). mu: conjecturally mixing (parity destroys persistence).

**Theorem III.9 (Quasi-ergodicity).** dx(n) is 73% rigid + 27% mixing. Asymptotically rigid but permanently ergodic (D(p) -> 0 but D(p) > 0 always).

**Theorem III.10 (Entropy-ergodicity correspondence).** Zero entropy = rigid. Positive entropy = ergodic. Maximum entropy = GUE-mixing. The entropy content determines the dynamical type.

---

## Chapter 11. Universality Theory

**Axioms (A1)-(A4).** (A1) Countable generators with UF. (A2) Activation at g_k^2. (A3) CRT independence. (A4) Escape = complement of coverage.

**Theorem III.11 (Three universality classes).**

| Class | D behavior | pi analogue | Example |
|-------|-----------|------------|---------|
| I (Logarithmic) | D ~ C/ln x | pi ~ x/ln x | Z |
| II (Constant) | D -> c > 0 | pi ~ cx/n | F_q[x] |
| III (Degenerate) | D -> 0 fast | Finite escapes | g_k = k |

**Theorem III.12 (12 universal structures).** The following are consequences of (A1)-(A4):

1. Product-form escape density. 2. Template periodicity. 3. PNT form pi ~ x*D(sqrt x). 4. Erdos-Kac normality. 5. Mobius cancellation. 6. Squarefree density = 1/zeta_S(2). 7. Template persistence. 8. Coverage protection C_H > 1. 9. Conservation law theta ~ x. 10. Explicit formula structure. 11. Sub-Poisson variance. 12. Epoch structure.

**Theorem III.13 (GUE from incommensurability).** GUE requires: independent generators (Euler product), incommensurate logarithms (Q-linear independence), minimal symmetry (functional equation).

**Theorem III.14 (Universality criterion).** Universal iff provable from (A1)-(A4). System-specific iff requires generator values.

**Theorem III.15 (Universal parity barrier).** The parity barrier is a consequence of (A1)-(A4), applying to all systems in all universality classes.

### 11.6. The renormalization flow

**Theorem III.16 (D(p) as coupling constant).** D(p_{k+1}) = D(p_k)*(1-1/p_{k+1}). Flow: deterministic, irreversible, D -> 0. The entire stochastic-to-deterministic transition is parameterized by D.

**Theorem III.17 (Triple correspondence).** Entropy, ergodicity, and universality align:

| Layer | Entropy | Ergodic type | Universality |
|-------|---------|-------------|-------------|
| Template | 0 | Rigid | Universal |
| Escape | ~0.26 bits/int | Mixing | System-specific |
| Spectral | Max (GUE) | GUE-mixing | Universal (Class I) |

*Part III comprises 17 theorems. The key result is the triple correspondence (Theorem III.17): information content determines dynamical behavior determines universality status.*

---

# Part IV: The Meta-Structure of the Factor Skyline

*Part IV steps outside the framework to examine its own architecture: what are its minimal assumptions, its structural symmetries, its computational and logical properties?*

## Chapter 12. Meta-Structure

**Theorem IV.1 (Primitive reduction).** The five FS concepts derive from lpf alone: lpf -> width -> height, coverage -> activation -> escape.

**Theorem IV.2 (Three meta-axioms).** lpf requires (M1) total order, (M2) multiplication, (M3) unique factorization. These are minimal.

**Theorem IV.3 (Emergence hierarchy).**

| Level | Structures |
|-------|-----------|
| Primitive | lpf |
| First-order | Width, height, D(p), templates |
| Second-order | PNT, Chebyshev, persistence, protection |
| Third-order | Explicit formula, zeros, GUE |

**Theorem IV.4 (Three dualities).**

| Duality | Domain A | Domain B | Bridge |
|---------|----------|----------|--------|
| Coverage-Escape | Composites | Primes | Partition |
| Width-Spectral | Width layers | Zeta zeros | Explicit formula |
| Rigidity-Randomness | Template | GUE spectrum | Fourier analysis |

**Theorem IV.5 (Self-referential structure).** The framework's meta-structure mirrors its object-level structure: layers partition results as width layers partition integers; the parity barrier limits provability as coverage limits escape.

---

## Chapter 13. Meta-Mathematics

**Theorem IV.6 (Computability).** The skyline up to N is computable in O(N log log N). Template statistics: O(k). Escape layer: as hard as primality.

**Theorem IV.7 (Pseudo-randomness).** K(S_N) = O(log N) but H(escape | template) >= 0.26N. The escape layer is pseudo-random: K << H.

**Theorem IV.8 (Barrier is methodological).** The parity barrier is not Godel incompleteness. It constrains coverage-based proofs, not logic itself. It is analogous to the impossibility of ruler-and-compass angle trisection.

**Theorem IV.9 (T_FS as first-order theory).** (A1)-(A4) define a first-order theory with models including Z, Z[i], F_q[x]. T_FS is incomplete (non-isomorphic models exist).

**Theorem IV.10 (Universality = logical consequence).** Universal iff provable from T_FS. This is the model-theoretic content of the universality criterion (Theorem III.14).

**Theorem IV.11 (Computational-mathematical mirror).**

| Level | Math | Computation | Proof |
|-------|------|------------|-------|
| Template | Coverage | O(1)/int | Trivial |
| Density | Averages | O(log N) | Elementary |
| Escapes | Primes | O(N log log N) | Hard |
| Spectrum | Zeros | Unknown | Frontier |

---

## Chapter 14. Unified Meta-Architecture

**Theorem IV.12 (Meta-correspondence).** Every meta-structural concept has a meta-mathematical counterpart: lpf <-> sieve program, meta-axioms <-> T_FS, emergence <-> computational hierarchy, dualities <-> compression/entropy, renormalization <-> increasing compression, parity barrier <-> incompressible core.

**Theorem IV.13 (Boundary between architecture and logic).** The parity barrier admits four equivalent characterizations:

1. **Information-theoretic:** ~0.26 bits/int that the template cannot provide.
2. **Computational:** escape layer as hard to compute as primality.
3. **Logical:** gap between Sigma_1^0 (template persistence) and Pi_2^0 (escape persistence).
4. **Universal:** same boundary in all (A1)-(A4) systems.

These four descriptions characterize the same structural limit.

*Part IV comprises 13 theorems. The key insight: the framework's limits are as revealing as its successes — the parity barrier tells us exactly what a proof of the open conjectures must provide.*

---

# Back Matter

## Glossary

| Term | Definition | First appearance |
|------|-----------|-----------------|
| **Activation** | Entry of width-p coverage at p^2 | Def I.5 |
| **Admissible** | v_q(H) < q for all primes q | Def I.11 |
| **Column** | Recursive width decomposition of n | Def I.4 |
| **Coverage** | Cumulative width-layer claiming | Def I.7 |
| **Coverage protection** | Width-q cannot hit all members of admissible tuple | Thm I.8 |
| **Epoch** | [p_k^2, p_{k+1}^2): frozen coverage interval | Def I.6 |
| **Escape** | n with lpf(n) = n (prime) | Def I.8 |
| **Escape density** | D(p) = prod(1-1/q) | Def I.7 |
| **FS-x gap invariant** | Fixed FS-x inter-escape pattern for each constellation | Thm I.11 |
| **k-tuple constant** | C_H = prod S_q/(1-1/q)^k | Def I.10, Thm I.9 |
| **Parity barrier** | ~0.26 bits/int that coverage cannot supply | Thm III.5, IV.13 |
| **Primorial** | p# = 2*3*...*p | Def I.9 |
| **Quasi-ergodic** | 73% rigid + 27% mixing | Thm III.9 |
| **Renormalization** | Template extension p_k# -> p_{k+1}#; D as coupling | Thm III.16 |
| **Sub-Poisson** | Var/Mean < 1 for escape counts | Thm II.9 |
| **Survival factor** | S_q(H) = (q-v_q)/q | Thm I.7 |
| **Template** | Periodic open/covered classification mod p# | Def I.9 |
| **Template persistence** | Constellation-open count grows without bound | Thm I.10 |

## Theorem Index

**Part I (Architecture):** Theorems I.1-I.22 (Definitions I.1-I.11)
**Part II (Statistics):** Theorems II.1-II.14 (Definition II.1, Corollaries II.1-II.2)
**Part III (Foundations):** Theorems III.1-III.17
**Part IV (Meta-theory):** Theorems IV.1-IV.13

Total: **66 theorems**, 12 definitions, 2 corollaries across four parts.

## Comprehensive Reference List

[1] A. Proxmire, *The Factor Skyline: An Ontological Lookout Over the Integers* (2026). DOI: 10.5281/zenodo.18275273.

[2] H. Davenport, *Multiplicative Number Theory*, 3rd ed. Springer, 2000.

[3] G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, 6th ed. Oxford, 2008.

[4] H. Iwaniec and E. Kowalski, *Analytic Number Theory*. AMS Colloquium Publications, 2004.

[5] F. Mertens, "Ein Beitrag zur analytischen Zahlentheorie," *J. Reine Angew. Math.* **78** (1874), 46-62.

[6] N. G. de Bruijn, "On the number of positive integers <= x and free of prime factors > y," *Indag. Math.* **13** (1951), 50-60.

[7] G. H. Hardy and J. E. Littlewood, "Some problems of 'Partitio numerorum'; III," *Acta Math.* **44** (1923), 1-70.

[8] P. Erdos and M. Kac, "The Gaussian law of errors in the theory of additive number theoretic functions," *Amer. J. Math.* **62** (1940), 738-742.

[9] H. Cramer, "On the order of magnitude of the difference between consecutive prime numbers," *Acta Arith.* **2** (1936), 23-46.

[10] A. Granville, "Harald Cramer and the distribution of prime numbers," *Scand. Actuarial J.* (1995), 12-28.

[11] H. L. Montgomery, "The pair correlation of zeros of the zeta function," *Proc. Sympos. Pure Math.* **24** (1973), 181-193.

[12] N. M. Katz and P. Sarnak, *Random Matrices, Frobenius Eigenvalues, and Monodromy*. AMS, 1999.

[13] P. Sarnak, "Three lectures on the Mobius function, randomness and dynamics," 2011.

[14] S. Chowla, *The Riemann Hypothesis and Hilbert's Tenth Problem*. Gordon and Breach, 1965.

[15] K. Godel, "Uber formal unentscheidbare Satze der Principia Mathematica," *Monatsh. Math. Phys.* **38** (1931), 173-198.

[16] A. N. Kolmogorov, "Three approaches to the quantitative definition of information," *Problems Inform. Transmission* **1** (1965), 1-7.

[17] A. Weil, "Sur les courbes algebriques et les varietes qui s'en deduisent," *Actualites Sci. Ind.* **1041** (1948).

## Appendix A: Numerical Tables and Reproducibility

All numerical computations were performed using SymPy (Python) with the coordinate system implemented in `FS_coordinates.py`. The tables in the text are reproducible from the scripts in the project repository at https://github.com/allen-proxmire/factor-skyline.

**Table A.1.** FS-coordinates for n = 1 to 30.
**Table A.2.** Escape density convergence (D(p) vs e^{-gamma}/ln(p) for p = 2 to 47).
**Table A.3.** Primorial template statistics (2# through 13#).
**Table A.4.** PNT verification (N = 100 through 100000).
**Table A.5.** Conservation law verification (theta(x)/x for x = 10^2 through 10^5).
**Table A.6.** Dickman function verification (rho(u) for u = 1 to 5 at N = 10000).
**Table A.7.** Squarefree and Mobius statistics (N = 1000 and 10000).
**Table A.8.** Divisor average verification (avg tau and avg sigma/n for N = 100, 1000, 10000).
**Table A.9.** Omega distribution (N = 10000).
**Table A.10.** FS-x constellation footprints (twin, triplet, quadruplet verified below 500).
**Table A.11.** Prime pair counts to 10^5 for offsets h = 2 through 210.
**Table A.12.** Mobius pair correlations at N = 50000.
**Table A.13.** Divisor pair correlations at N = 20000.
**Table A.14.** Omega correlations at N = 50000.
**Table A.15.** Normalized zero spacings (first 29).
**Table A.16.** Sub-Poisson prime count variance (W = 20 through 200).
**Table A.17.** Explicit formula reconstruction from 5, 10, 20 zeros.
**Table A.18.** FS-x autocorrelation at lags 1, 2, 3, 6, 30.
**Table A.19.** Template entropy rates (p = 2 through 23).
**Table A.20.** Escape entropy per integer (n = 100 through 100000).
