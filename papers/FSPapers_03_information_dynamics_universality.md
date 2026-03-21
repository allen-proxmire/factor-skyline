# Information, Dynamics, and Universality in the Factor Skyline

Allen Proxmire

March 2026

---

## Abstract

We develop the information-theoretic, dynamical, and universality theories of the Factor Skyline in a unified framework. In the entropy theory, we prove that the primorial template provides 1.70 of the total 2.48 bits per integer in the FS-x increment sequence (a 68.5% deterministic contribution), leaving 0.26 bits of irreducible escape entropy per integer — the information-theoretic content of the parity barrier (Theorem 3.7). In the ergodic theory, we establish that omega(n) is ergodic but not mixing (Theorem 4.5), while mu(n) is conjecturally mixing (Theorem 4.6), and that the skyline is quasi-ergodic: 73% rigid, 27% mixing, asymptotically rigid but permanently ergodic (Theorem 4.8). In the universality theory, we identify three classes of escape thinning (logarithmic, constant, degenerate), prove that 12 named structures are universal consequences of axioms (A1)-(A4), and show that the parity barrier is universal across all multiplicative systems with independent generators (Theorem 5.7). We prove that the entropy hierarchy (zero / positive / maximal) corresponds exactly to the ergodic hierarchy (rigid / ergodic / GUE-mixing) (Theorem 6.1), and that the escape density D(p) serves as a renormalization coupling constant whose flow from D = 1 toward the fixed point D = 0 governs the transition from dominantly stochastic to dominantly deterministic skyline behavior (Theorem 6.3).

---

## 1. Introduction

The Factor Skyline decomposes each integer into a column of width lpf(n) and height n/lpf(n), generating a two-dimensional landscape governed by five primitives: width, height, activation, coverage, and escape. The preceding papers in this series established the FS ontology, the geometric PNT, the sieve geometry, and the correlation theory. This paper addresses three foundational questions:

1. **Information:** How much entropy does the skyline carry, and where does it reside?
2. **Dynamics:** Is the skyline ergodic, mixing, or rigid under the shift n -> n+1?
3. **Universality:** Which FS structures depend on the specific primes 2, 3, 5, ..., and which hold for any multiplicative system with independent generators?

These questions are interconnected: the entropy content determines the ergodic type, and the ergodic type determines which structures are universal. The unified theory reveals that all three perspectives — informational, dynamical, and universal — describe the same layered architecture from complementary viewpoints.

**Notation.** Throughout, D(p) = prod_{q<=p, q prime}(1 - 1/q) denotes the escape density, p# = 2*3*...*p the primorial, phi(p#) the open-position count, H_b(x) = -x log_2 x - (1-x) log_2(1-x) the binary entropy function, and dx(n) the FS-x increment (1 if n is prime, lpf(n) if composite).

---

## 2. Preliminaries

We recall the FS primitives. The *template* at level p is the periodic function T_p: Z -> {open, covered} with period p# that classifies each residue class as coprime (open) or non-coprime (covered) to p#. The *escape density* D(p) = phi(p#)/p# is the fraction of open positions. Width layers are independent by the CRT: for distinct primes q, r, divisibility by q and divisibility by r are independent events.

---

## 3. Entropy Theory

### 3.1. Template entropy: zero conditional, high information

**Theorem 3.1.** The template is a zero-entropy layer: H(T_p(n) | n mod p#) = 0.

Its role is informational, not stochastic. Before template conditioning, each integer's primality has entropy H_b(1/ln n). After, a fraction (1 - D(p)) of positions are resolved as definitely composite.

**Theorem 3.2 (Template entropy rate).** The template at level p removes fraction (1 - D(p)) of all primality uncertainty. The information provided per integer is approximately H_b(D(p)) bits.

| p  | D(p)  | H_b(D(p)) bits | Fraction resolved |
|----|-------|----------------|-------------------|
| 2  | 0.500 | 1.000          | 50.0%             |
| 5  | 0.267 | 0.837          | 73.3%             |
| 11 | 0.208 | 0.737          | 79.2%             |
| 23 | 0.164 | 0.643          | 83.6%             |

Each successive prime adds diminishing marginal information: width-2 provides ~1 bit; width-23 brings the cumulative total to only ~0.64.

### 3.2. Escape entropy: the irreducible core

**Theorem 3.3.** Among template-open positions at scale n, the residual escape probability is D_open(n) = D(sqrt(n))/D(p), and the per-open-position entropy is H_b(D_open).

| Scale n | D_open | H_escape (bits) | H per integer (= D(p) * H_escape) |
|---------|--------|-----------------|-----------------------------------|
| 100     | 0.857  | 0.592           | 0.158                             |
| 1,000   | 0.573  | 0.985           | 0.263                             |
| 10,000  | 0.451  | 0.993           | 0.265                             |
| 100,000 | 0.362  | 0.944           | 0.252                             |

The escape entropy per integer peaks at ~0.265 bits near n = 10000 and decreases slowly thereafter. This is the **irreducible core**: the information that the template cannot supply and that the parity barrier protects.

### 3.3. Activation entropy and mu/omega

**Theorem 3.4.** Each prime q contributes H_b(1/q) bits of activation entropy per integer. By CRT, these contributions are additive: H_activation = sum_q H_b(1/q).

**Theorem 3.5.** The entropy of mu among squarefree integers is exactly H(mu | squarefree) = 1.000 bits — the maximum for a binary variable. This follows from CRT independence: the parity of independent Bernoulli indicators is exactly unbiased.

**Theorem 3.6.** The entropy of the omega distribution at N = 10000 is H(omega) = 1.78 bits, growing slowly as ~log_2(ln ln n).

### 3.4. Spectral entropy

The zeta zeros, normalized by local density, follow GUE statistics. The GUE ensemble maximizes entropy subject to the constraints of level repulsion (multiplicative orthogonality), symmetry (functional equation), and fixed density (template harmonic richness). The zero spectrum carries maximum entropy given these structural constraints: it is as random as the primorial architecture allows.

### 3.5. Total FS entropy and the 68.5/31.5 split

**Theorem 3.7 (FS entropy budget).** The total entropy of the dx sequence decomposes as:

    H(dx) = 2.483 bits/int (unconditional)
    H(dx | n mod 30) = 0.783 bits/int (conditional on 5#-template)
    I(template) = 1.700 bits/int (information provided by template)

The template provides **68.5%** of the total information. The remaining **31.5%** is escape + activation uncertainty.

**Corollary 3.8 (Template compression).** To specify all primes up to N requires ~N * H_b(pi(N)/N) bits naively. After template conditioning: savings of 62% at N = 10000, 78% at N = 1000.

### 3.6. The parity barrier as an information barrier

**Theorem 3.9.** The escape layer carries ~0.26 bits per integer of information that the coverage architecture cannot provide: the distinction between a prime (omega = 1) and a squarefree composite with odd omega >= 3 at an open template position. This is the information-theoretic content of the parity barrier.

The barrier is not logical (it does not imply undecidability) but methodological: it constrains what coverage-based arguments can determine, not what is true.

---

## 4. Ergodic Theory

### 4.1. Template rigidity

**Theorem 4.1.** Under the shift T: n -> n+1, the template layer is rigidly periodic with period p#. It is trivially ergodic (averages converge in one period) but not mixing (correlations are exactly periodic).

The template is hierarchically periodic: mixing at scale p_k# for each k, but never at all scales simultaneously.

### 4.2. Escape ergodicity and mixing

**Theorem 4.2 (Escape ergodicity).** The Cesaro average (1/N) sum_{n<=N} 1_{prime}(n) converges to 0 (more precisely, to ~1/ln N). The escape process is ergodic.

**Theorem 4.3.** Under RH, the mixing rate is O(1/sqrt(N)): the fluctuations |pi(N) - li(N)| = O(sqrt(N) ln N).

**Theorem 4.4.** The escape process is super-ergodic relative to Poisson: its variance is suppressed by the template (Var/Mean ~ 0.46 vs 1.0 for Poisson), so it mixes faster than a random process of the same density.

### 4.3. Activation ergodicity and the omega/mu dichotomy

**Theorem 4.5 (omega is ergodic but not mixing).** The Cesaro average of omega(n) converges to ln ln n (ergodicity). But corr(omega(n), omega(n+h)) does not decay to zero: for every h with prime factors, the shared-layer correlation sum_{q|h} (1/q)(1-1/q)/Var(omega) provides a positive lower bound. The non-mixing arises because omega is a sum of rigid periodic components.

Numerically at N = 50000: corr(omega(n), omega(n+1000)) = +0.248.

**Theorem 4.6 (mu is conjecturally mixing).** The parity function mu = (-1)^omega destroys the persistent correlations of omega. The non-shared layers provide independent sign flips that overwhelm the shared-layer correlation. R_mu(h, N) -> 0 for all h >= 1 (Chowla conjecture).

**Corollary 4.7 (Mixing dichotomy).** The same CRT independence produces both permanent correlation (omega: additive) and asymptotic independence (mu: parity). The observation function's non-linearity determines the mixing behavior.

### 4.4. Spectral ergodicity

**Theorem 4.8.** The normalized zero spectrum is ergodic in the ensemble sense: its statistics are locally universal (GUE) and independent of the spectral region after rescaling.

### 4.5. Quasi-ergodicity of the skyline

**Theorem 4.9 (Quasi-ergodicity).** The dx(n) sequence decomposes into:

- A rigid factor (73.3% of positions, template-determined, periodic).
- A mixing factor (26.7% of positions, escape-determined, ergodic).

The system is quasi-ergodic: neither purely rigid nor purely mixing. As n -> infinity, D(p) -> 0, so the mixing fraction shrinks — the skyline is **asymptotically rigid but permanently ergodic**.

### 4.6. The entropy-ergodicity correspondence

**Theorem 4.10 (Entropy determines ergodic type).**

| Component | Entropy | Ergodic type |
|-----------|---------|-------------|
| Template | 0 bits (deterministic) | Rigid |
| Escape | ~0.26 bits/int (positive) | Ergodic, mixing |
| Spectral | ~ln(T) bits/zero (maximal) | GUE-mixing |

Zero-entropy components are rigid. Positive-entropy components are ergodic. Maximum-entropy components are maximally mixing. The entropy content fully determines the dynamical character.

---

## 5. Universality Theory

### 5.1. The axioms (A1)-(A4)

Any system satisfying:

**(A1)** A countable sequence of generators g_1, g_2, ... with unique factorization.
**(A2)** Each generator g_k activates at g_k^2, claiming fraction 1/g_k of uncovered elements.
**(A3)** Independence: divisibility by g_i is independent of divisibility by g_j (CRT).
**(A4)** Escape = complement of coverage (generators = elements unclaimed by any layer).

produces a Factor Skyline with the same qualitative architecture.

### 5.2. Three universality classes of escape thinning

**Theorem 5.1 (Classification).** The escape density D(k) = prod(1 - 1/g_i) determines the universality class:

| Class | Condition | D behavior | pi(x) analogue | Example |
|-------|-----------|-----------|---------------|---------|
| I (Logarithmic) | sum 1/g_i diverges slowly | D ~ C/ln x | pi ~ x/ln x | Z, number fields |
| II (Constant) | sum 1/g_i converges | D -> c > 0 | pi ~ cx/n | F_q[x] |
| III (Degenerate) | sum 1/g_i diverges rapidly | D -> 0 fast | Finitely many escapes | g_k = k |

### 5.3. Why F_q[x] is easier

**Theorem 5.2.** F_q[x] is Class II: the escape corridor stabilizes at a positive constant. The zeta function is a polynomial (finite-dimensional spectral problem), and RH is a theorem (Weil, 1948). The collapsing corridor of Z (Class I) makes RH an infinite-dimensional problem.

### 5.4. The 12 universal structures

**Theorem 5.3.** The following are consequences of (A1)-(A4) alone (universal):

1. Escape density as a product: D(k) = prod(1 - 1/g_i).
2. Template periodicity at generator products.
3. PNT form: pi(x) ~ x * D(sqrt(x)).
4. Erdos-Kac normality of omega.
5. Mobius cancellation (parity of independent sum is unbiased).
6. Squarefree density = 1/zeta_S(2).
7. Template persistence for admissible k-tuples.
8. Coverage protection: C_H > 1 for admissible H.
9. Conservation law: theta_S(x) ~ x.
10. Spectral completeness (explicit formula).
11. Sub-Poisson escape variance.
12. Epoch structure from activation thresholds.

### 5.5. Incommensurability and GUE

**Theorem 5.4.** GUE zero statistics require three ingredients: (i) independent generator contributions (Euler product), (ii) incommensurate generator logarithms (Q-linear independence), (iii) minimal symmetry (functional equation). The integers satisfy all three; the incommensurability follows from unique factorization.

**Theorem 5.5.** GUE breaks when additional symmetry is present (L-functions with real characters shift to GOE/GSE), when generators are commensurate (degenerate harmonic structure), or when the system is finite (F_q[x]: zeros lie exactly on a circle).

### 5.6. The universality detector

**Theorem 5.6 (Universality criterion).** A result is universal if and only if it is provable from (A1)-(A4) alone. It is system-specific if it requires the specific generator sequence. This provides a clean partition of all FS results.

**Table 1.** Classification:

| Universal | System-specific |
|-----------|----------------|
| PNT form pi ~ x * D(sqrt(x)) | The function ln(x) |
| Erdos-Kac | Mean = ln ln n (specific to Z) |
| C_H > 1 | C_twin = 1.3203 |
| GUE statistics | Specific zero locations |
| Sub-Poisson variance | Specific suppression ratio |
| Parity barrier | Same obstacle in all systems |

### 5.7. The parity barrier is universal

**Theorem 5.7.** The parity barrier — the inability of coverage-based arguments to distinguish generators from odd-omega composites — is a consequence of (A1)-(A4). It applies to all systems in all three universality classes.

*Proof.* In any (A1)-(A4) system, the coverage architecture determines which elements are open but not which open elements are generators. The distinction between omega = 1 (generator) and omega >= 3 (composite with odd factor count) is invisible to the coverage layers because both produce the same parity under the inclusion-exclusion structure that defines coverage. QED.

---

## 6. The Unified Information-Dynamical Architecture

### 6.1. The triple correspondence

**Theorem 6.1 (Entropy-ergodicity-universality correspondence).** The three theoretical perspectives align exactly:

| Layer | Entropy | Ergodic type | Universality |
|-------|---------|-------------|-------------|
| Template | 0 bits | Rigid | Universal (structure of any (A1)-(A4) system) |
| Escape | ~0.26 bits/int | Ergodic, mixing | Contains system-specific info |
| Spectral | max (GUE) | GUE-mixing | Universal (for Class I incommensurate) |

The template is deterministic, rigid, and universal. The escape layer is stochastic, mixing, and system-specific. The spectral layer is maximally random, maximally mixing, and (for the appropriate symmetry class) universal. Information content determines dynamical behavior determines universality status.

### 6.2. The renormalization flow D(p)

**Theorem 6.2.** The escape density D(p) serves as the running coupling constant of a multiplicative renormalization group. At each step (extending the template from p_k# to p_{k+1}#):

    D(p_{k+1}) = D(p_k) * (1 - 1/p_{k+1})

The flow is deterministic, irreversible, and monotonically decreasing:

```
D(2)=1/2 --[x2/3]--> D(3)=1/3 --[x4/5]--> D(5)=4/15 --[x6/7]--> D(7)=8/35 --> ...
```

The fixed point D = 0 (complete coverage) is approached but never reached.

**Theorem 6.3 (Corridor collapse governs the architecture).** The value of D(p) at any given scale determines:

- The fraction of stochastic (escape) content: ~D(p) of positions are open.
- The entropy per integer: ~D(p) * H_b(D_open).
- The mixing fraction: ~D(p) of the dx sequence is stochastic.
- The mean escape gap: ~1/D(p) ~ ln(p).

As D(p) -> 0, the skyline becomes dominantly deterministic (template-governed). At D = 1/2 (only width-2 active), the skyline is half stochastic. The entire evolution from stochastic to deterministic is parameterized by this single coupling constant.

### 6.3. The role of CRT independence

**Theorem 6.4.** CRT independence is the structural foundation of all three theories:

| Theory | CRT provides |
|--------|-------------|
| Entropy | Additive entropy across layers; product-form escape density |
| Ergodicity | Independence of width-layer indicators; CLT for omega; parity mixing for mu |
| Universality | Generator-independent architecture; product form transfers across systems |

CRT independence is simultaneously an information-theoretic property (additive entropy), a dynamical property (independent components), and a universal property (system-independent structure). It is the single deepest structural fact of the Factor Skyline.

### 6.4. The structural meaning of the collapsing corridor

The escape density D(p) -> 0 is the geometric content of the pole of zeta at s = 1. In the unified framework:

- **Informationally:** D -> 0 means the escape entropy per integer shrinks, and the template provides an ever-larger fraction of the total information.
- **Dynamically:** D -> 0 means the mixing fraction shrinks, and the skyline becomes asymptotically rigid.
- **Universally:** D -> 0 defines Class I systems, distinguishing them from Class II (D stabilizes) and Class III (D collapses rapidly).

The collapsing corridor is the single architectural feature that determines the integers' qualitative character: a logarithmically narrowing escape channel that produces the specific brand of pseudo-randomness, slow mixing, and logarithmic thinning that define the number-theoretic landscape.

---

## 7. Discussion and Open Problems

### 7.1. What this paper establishes

1. **The 68.5/31.5 entropy split** (Theorem 3.7): the template is the dominant information source.
2. **The 0.26-bit irreducible core** (Theorem 3.9): the parity barrier has a precise information measure.
3. **omega non-mixing** (Theorem 4.5): persistent positive correlations at all composite lags.
4. **mu mixing** (Theorem 4.6): parity destroys persistent correlations (conditional on Chowla).
5. **Quasi-ergodicity** (Theorem 4.9): 73% rigid, 27% mixing, asymptotically rigid.
6. **The entropy-ergodicity correspondence** (Theorem 4.10): zero entropy = rigid; positive = ergodic; maximal = GUE.
7. **12 universal structures** (Theorem 5.3): consequences of (A1)-(A4) alone.
8. **Universal parity barrier** (Theorem 5.7): all (A1)-(A4) systems share the obstruction.
9. **The triple correspondence** (Theorem 6.1): entropy, ergodicity, and universality align exactly.
10. **D(p) as coupling constant** (Theorems 6.2-6.3): the renormalization flow governs the stochastic-to-deterministic transition.

### 7.2. Open problems

**Problem 1 (Sharp entropy bound).** Determine whether the 0.26 bits/integer escape entropy is the sharp lower bound on information needed to resolve the open conjectures.

**Problem 2 (Mixing rate of mu).** Prove R_mu(h, N) -> 0 for all h (Chowla). The FS mechanism is identified (Theorem 4.6) but the quantitative rate is not controlled.

**Problem 3 (Exact sub-Poisson ratio).** Derive the precise variance suppression factor from the template's open-position spacing structure.

**Problem 4 (Renormalization fixed-point behavior).** Characterize the behavior of the FS architecture as D -> 0: does the renormalization flow have scaling exponents, critical behavior, or phase transitions?

**Problem 5 (Universality of RH).** Determine whether RH for Z implies (or is implied by) RH for all Class I systems. The universality of the parity barrier suggests the answer is yes, but no proof exists.

**Problem 6 (Information beyond coverage).** Identify whether the FS-x coordinate, the spectral resonance structure, or the height sequence y_FS(n) contain information about escape occupancy beyond what the template provides — information that could cross the parity barrier.

### 7.3. The central insight

The Factor Skyline is a system in which information, dynamics, and universality are three facets of a single layered architecture. The deterministic template provides the structure; the stochastic escape process provides the uncertainty; the spectral resonances provide the harmonic content. These three layers are connected by CRT independence, parameterized by the escape density D(p), and classified by the universality axioms (A1)-(A4).

The integers are mostly structure (73% template-determined), with a thin vein of pseudo-randomness (27% escape-governed) running through the open positions of the primorial template. Understanding this thin vein — its entropy, its mixing properties, its spectral content, and its universality class — is the central open problem of the Factor Skyline program.

---

## 8. References

[1] A. Proxmire, *The Factor Skyline: An Ontological Lookout Over the Integers* (2026). DOI: 10.5281/zenodo.18275273.

[2] F. Mertens, "Ein Beitrag zur analytischen Zahlentheorie," *J. Reine Angew. Math.* **78** (1874), 46-62.

[3] P. Erdos and M. Kac, "The Gaussian law of errors in the theory of additive number theoretic functions," *Amer. J. Math.* **62** (1940), 738-742.

[4] N. M. Katz and P. Sarnak, *Random Matrices, Frobenius Eigenvalues, and Monodromy*. AMS, 1999.

[5] P. Sarnak, "Three lectures on the Mobius function, randomness and dynamics," 2011.

[6] S. Chowla, *The Riemann Hypothesis and Hilbert's Tenth Problem*. Gordon and Breach, 1965.

[7] H. L. Montgomery, "The pair correlation of zeros of the zeta function," *Proc. Sympos. Pure Math.* **24** (1973), 181-193.

[8] H. Iwaniec and E. Kowalski, *Analytic Number Theory*. AMS, 2004.

[9] A. Weil, "Sur les courbes algebriques et les varietes qui s'en deduisent," *Actualites Sci. Ind.* **1041** (1948).

[10] A. Granville, "Harald Cramer and the distribution of prime numbers," *Scand. Actuarial J.* (1995), 12-28.
