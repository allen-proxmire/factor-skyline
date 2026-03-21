# Ergodicity in the Factor Skyline

---

## Overview

Ergodic theory studies systems where time averages equal space averages — where exploring a single long trajectory is equivalent to sampling the entire space. The Factor Skyline is not a dynamical system in the standard sense (there is no continuous flow), but the sequence n = 1, 2, 3, ... can be viewed as a discrete-time trajectory through the skyline, and the question of ergodicity becomes: do Cesaro averages of arithmetic functions along this trajectory converge to their predicted values? If so, at what rate, and with what residual structure?

The FS framework reveals a layered ergodic structure: the template is rigidly periodic (not ergodic but mixing at the template period), the escape process is ergodic with sub-Poisson fluctuations, the width-layer process is ergodic layer by layer but non-mixing in aggregate, and the spectral layer is ergodic in the GUE sense. This decomposition separates the deterministic, pseudo-random, and spectrally random components of the skyline.

---

## 1. Template Ergodicity

### 1.1. Template periodicity as rigid structure

The primorial template is periodic with period p#. Under the shift map T: n -> n+1, the template classification of n repeats exactly every p# integers. This is the hallmark of a **rigid** (non-ergodic) system: the trajectory is periodic, and time averages converge to space averages trivially (by averaging over one complete period).

For the 5#-template (period 30):
- Exactly 15/30 positions are even composites (dx = 2).
- Exactly 5/30 are odd multiples of 3 (dx = 3).
- Exactly 2/30 are multiples of 5 coprime to 6 (dx = 5).
- Exactly 8/30 are open positions (coprime to 30).

These fractions are exact and period-independent. The template is a deterministic clock.

### 1.2. Equidistribution in FS-x residues

Despite the template's rigid periodicity on the number line, the FS-x coordinate does not inherit this periodicity. Because the FS-x increment dx(n) varies (1 for primes, lpf(n) for composites), the FS-x residues mod p# do not follow a simple periodic pattern.

Numerically, x_FS(n) mod 30 for n in [31, 10000]:

    Min count: 291, Max count: 370, Ratio max/min: 1.271

The distribution is approximately uniform (each residue gets ~3.3%) but not exactly so. The deviations arise because the stochastic escape events (dx = 1) break the template's period. The FS-x coordinate is a sum of periodic (template) and quasi-random (escape) increments, producing a quasi-uniform distribution of residues.

### 1.3. Template mixing at scale p#

The template is ergodic in a weaker sense: it is **mixing at scale p#**. Any arithmetic function that depends only on n mod p# has its Cesaro average converge to its period average after sampling O(p#) integers. The mixing time is exactly one template period.

For functions that depend on deeper template structure (n mod q# for larger q), the mixing time increases to q#. The template is therefore mixing at every finite scale but never at all scales simultaneously — it is **hierarchically periodic**, with progressively longer mixing times at each template level.

---

## 2. Escape Ergodicity

### 2.1. Cesaro convergence of the prime indicator

The most fundamental ergodic question: does (1/N) * sum_{n<=N} 1_{prime}(n) converge?

The PNT says yes: pi(N)/N -> 0 (primes have density zero), and more precisely pi(N)/(N/ln N) -> 1.

| N      | pi(N)/N  | 1/ln(N) | Ratio |
|--------|---------|---------|-------|
| 100    | 0.2500  | 0.2171  | 1.151 |
| 1000   | 0.1680  | 0.1448  | 1.161 |
| 10000  | 0.1229  | 0.1086  | 1.132 |
| 100000 | 0.0959  | 0.0869  | 1.104 |

The ratio converges to 1 (PNT). The escape process is **ergodic**: the Cesaro average of the prime indicator converges to its predicted density.

### 2.2. The rate of convergence

The rate at which pi(N)/N approaches 1/ln(N) is O(1/(ln N)^2) — a logarithmic rate, not a power-law rate. This is slower than typical ergodic convergence for mixing systems, reflecting the fact that the escape process has long-range correlations induced by the template structure.

Under RH, the fluctuations |pi(x) - li(x)| are O(sqrt(x)*ln(x)), which gives:

    |pi(N)/N - 1/ln(N)| = O(ln(N) / sqrt(N))

This is a power-law convergence rate in N (the fluctuations decay as 1/sqrt(N)), consistent with the escape process being ergodic with mixing rate O(1/sqrt(N)).

### 2.3. Escape ergodicity vs Poisson ergodicity

A Poisson process with rate lambda has Cesaro averages converging at rate O(1/sqrt(N)) (standard CLT). The prime escape process also converges at this rate (under RH), but with sub-Poisson variance: the fluctuations are smaller than Poisson by a factor of ~0.4-0.5 (see `FS_randomness.md`).

This means the escape process is **super-ergodic** relative to a Poisson process: it mixes faster because the template constrains where escapes can occur, reducing the effective randomness.

---

## 3. Activation Ergodicity

### 3.1. Individual width layers are perfectly ergodic

For each prime q, the indicator 1_{q|n} is periodic with period q. Its Cesaro average converges exactly to 1/q after any multiple of q integers:

| q  | Observed average (N=10000) | 1/q |
|----|--------------------------|-----|
| 2  | 0.500000                 | 0.500000 |
| 3  | 0.333300                 | 0.333333 |
| 5  | 0.200000                 | 0.200000 |
| 7  | 0.142800                 | 0.142857 |
| 11 | 0.090900                 | 0.090909 |

Each width layer is a **periodic ergodic component** with period q. Its Cesaro average converges at rate O(1/N) (deterministic convergence, since the function is periodic).

### 3.2. The product structure and CRT independence

The width-layer process is the product of independent periodic components. By the CRT, the joint distribution of (1_{2|n}, 1_{3|n}, 1_{5|n}, ...) is the product of its marginals. Each component is independently ergodic with its own period.

The product system is **ergodic** if and only if the periods are pairwise coprime — which they are (being prime). The joint system is therefore ergodic: the Cesaro average of any function of finitely many width-layer indicators converges to its expected value.

### 3.3. Cesaro convergence of omega(n) and mu(n)

The Cesaro average of omega(n) converges to its expected value:

| N      | avg omega | ln(ln(N)) + M |
|--------|----------|---------------|
| 100    | 1.727    | ~1.789        |
| 1000   | 2.128    | ~2.194        |
| 10000  | 2.430    | ~2.482        |
| 100000 | 2.664    | ~2.705        |

The convergence is logarithmically slow because omega(n) is a sum of indicators with periods that span all primes. The slowest-mixing component has period equal to the largest prime considered.

The Cesaro average of mu(n) converges to 0:

| N      | M(N)/N     | M/sqrt(N) |
|--------|-----------|-----------|
| 100    | +0.0100   | +0.100    |
| 1000   | +0.0020   | +0.063    |
| 10000  | -0.0023   | -0.230    |
| 100000 | -0.0005   | -0.152    |

M(N)/N -> 0 (ergodic convergence). The rate is O(1/sqrt(N)) under RH — consistent with the escape process mixing rate.

### 3.4. The non-mixing aggregate: persistent omega correlations

A crucial subtlety: while each width layer is independently ergodic, the aggregate function omega(n) is **not mixing** in the standard sense. The correlation corr(omega(n), omega(n+h)) does not decay to zero for all h:

| h    | Observed corr | Predicted (shared-prime) |
|------|--------------|------------------------|
| 1    | -0.379       | 0.000                  |
| 6    | +0.381       | 0.194                  |
| 30   | +0.537       | 0.259                  |
| 100  | +0.254       | 0.168                  |
| 1000 | +0.255       | 0.168                  |

The correlation at h = 1000 is still +0.255, far from zero. This persistent correlation arises because every even h shares the width-2 indicator (contributing ~0.10 to the correlation), and highly composite h shares additional layers.

**The FS diagnosis:** omega(n) is ergodic (Cesaro averages converge) but **not mixing** (correlations do not decay to zero). The persistent correlations come from the shared width layers — the primes dividing h that create permanent structural links between n and n+h.

This is a fundamental property of the activation layer: it is a **product of rigid components**, each perfectly correlated with its translates at multiples of its period. The product is ergodic (by CRT coprimality of periods) but retains positive correlation at every lag h that is divisible by any small prime.

---

## 4. Spectral Ergodicity

### 4.1. The zero spectrum as an ergodic ensemble

The nontrivial zeros of zeta, when normalized by their local density, form a point process on the real line. The Montgomery-Odlyzko conjecture asserts that this process has the same statistics as the GUE eigenvalue process.

The GUE eigenvalue process is **ergodic**: its statistical properties are completely determined by the local density and pair correlation, and these properties are the same in every region of the spectrum (after normalization). The zeros of zeta appear to share this ergodicity.

### 4.2. Numerical evidence for spectral ergodicity

The mean zero spacing near height T is 2*pi/ln(T/(2*pi)). After normalizing by this local density, the zero spacings should have a universal distribution independent of T. The observed statistics (pair correlation, nearest-neighbor spacing, number variance) are consistent across all computed ranges (up to T ~ 10^{23}), supporting spectral ergodicity.

### 4.3. The FS interpretation of spectral ergodicity

In the FS framework, spectral ergodicity means that the resonance structure of the primorial template hierarchy is statistically self-similar under rescaling. The template at any scale produces the same pattern of resonances (after normalization) because the prime contributions are incommensurate and the Euler product structure is uniform across frequency ranges.

The ergodicity is not of a dynamical system but of a **statistical ensemble**: the zeros in any frequency band are drawn from the same GUE distribution, just as eigenvalues from different parts of a large random matrix are drawn from the same local statistics.

---

## 5. The Ergodic Decomposition of the Skyline

### 5.1. Three ergodic regimes

The Factor Skyline decomposes into three distinct ergodic regimes:

**Regime R (Rigid): The template layer.**
- Behavior: perfectly periodic with period p#.
- Ergodicity: trivially ergodic (periodic averages converge in one period).
- Mixing: not mixing (correlations are perfectly periodic, never decay).
- FS content: the deterministic coverage architecture.

**Regime E (Ergodic): The escape layer.**
- Behavior: sub-Poisson point process on the template-open positions.
- Ergodicity: ergodic (Cesaro averages converge to predicted densities).
- Mixing: mixing at rate O(1/sqrt(N)) under RH, but with template-induced sub-Poisson suppression.
- FS content: which open positions are primes vs large-lpf composites.

**Regime S (Spectral): The resonance layer.**
- Behavior: GUE-distributed point process of zeta zeros.
- Ergodicity: ergodic in the ensemble sense (statistics uniform after local normalization).
- Mixing: maximal mixing (GUE is the maximum-entropy ensemble under constraints).
- FS content: the oscillatory corrections to the escape pattern.

### 5.2. The hierarchical structure

The three regimes are nested:

```
Rigid template (deterministic, periodic)
  └─ constrains ─→ Escape process (ergodic, sub-Poisson)
                       └─ determines ─→ Spectral resonances (GUE-ergodic)
```

The template constrains the escape process (by determining which positions are open). The escape process determines the spectral resonances (through the explicit formula). Information flows downward: template → escape → spectrum.

Ergodic properties also flow downward: the template's rigidity constrains the escape process to be sub-Poisson (more regular than random), and the escape process's specific structure constrains the zero spectrum to be GUE (maximally random given the constraints).

### 5.3. What is ergodic, what is mixing, what is rigid

| Component | Ergodic? | Mixing? | Rate |
|-----------|----------|---------|------|
| Template (n mod p#) | Yes (trivially) | No (periodic) | Exact after p# |
| Individual width layer (1_{q\|n}) | Yes | No (periodic) | Exact after q |
| Escape indicator (1_{prime}) | Yes | Yes (under RH) | O(1/sqrt(N)) |
| mu(n) Cesaro | Yes | Yes (Chowla) | O(1/sqrt(N)) under RH |
| omega(n) Cesaro | Yes | **No** | Persistent correlation from shared primes |
| omega(n) correlations | N/A | Not decaying | ~sum_{q\|h} 1/q(1-1/q) > 0 |
| Zero spectrum | Yes (ensemble) | Yes (GUE) | Universal after normalization |

The key surprise: **omega(n) is ergodic but not mixing.** Its Cesaro average converges, but its correlations do not decay. This is because omega is a sum of rigid (periodic) components whose individual periodicities create permanent correlations at every composite lag.

---

## 6. Structural Insights

### 6.1. The ergodic hierarchy reflects the information hierarchy

The ergodic decomposition (rigid / ergodic / spectral) mirrors the entropy decomposition from `FS_entropy.md` (template / escape / spectral):

| Layer | Entropy | Ergodic type |
|-------|---------|-------------|
| Template | 0 (deterministic) | Rigid (periodic) |
| Escape | ~0.26 bits/int | Ergodic, mixing |
| Spectral | ~ln(T) bits/zero | GUE-ergodic |

Zero-entropy components are rigid. Positive-entropy components are ergodic. Maximum-entropy components are maximally mixing. The entropy content determines the ergodic type.

### 6.2. Why omega(n) is ergodic but not mixing

The non-mixing of omega(n) is a fundamental property of the activation layer, not an artifact. It arises because omega(n) couples all width layers into a single function, and the width layers have permanent periodic correlations with their own translates.

In dynamical systems terminology, the system (Z, T: n->n+1) acting on omega(n) has a **non-trivial rigid factor**: the projection onto the width-2 indicator. This rigid factor contributes a permanent positive correlation at every even lag, preventing mixing.

More generally, the system has a rigid factor for every prime q (the projection onto 1_{q|n}), and the aggregate rigid factor is the full template layer. The system decomposes as:

    omega(n) = [rigid template part] + [mixing escape part]

The rigid part produces the persistent correlations; the mixing part produces the decay at non-template lags. The two coexist because the CRT makes the components independent — but independence does not imply mixing when the individual components are rigid.

### 6.3. The Mobius function is mixing despite having a rigid factor

Interestingly, mu(n) is (conjecturally) mixing even though it depends on the same rigid width layers as omega(n). This is because mu takes the **parity** of the width count, which is a highly non-linear function of the individual layers.

The parity function destroys the persistent correlations: while 1_{2|n} and 1_{2|n+h} are perfectly correlated when h is even, the parities (-1)^{omega(n)} and (-1)^{omega(n+h)} are not, because the parity depends on all layers simultaneously, and the non-shared layers provide independent sign flips that wash out the correlation from the shared layers.

This is the FS content of the Chowla conjecture: the parity operation on the width-layer count converts a non-mixing process (omega) into a mixing process (mu).

### 6.4. Escape ergodicity and the Prime Number Theorem

The PNT is, in ergodic-theoretic terms, the statement that the prime indicator 1_{prime}(n) is ergodic under the shift T: n -> n+1, with spatial average equal to zero (primes have density zero).

The rate of ergodic convergence — how fast pi(N)/N approaches 0, or equivalently how fast pi(N)/(N/ln N) approaches 1 — is governed by the mixing rate of the escape process. Under RH, this rate is O(1/sqrt(N)), the fastest mixing consistent with the spectral constraints (the zeros on the critical line).

If some zero had Re(rho) > 1/2, the mixing rate would be slower — the escape process would have a slowly decaying correlation mode, and Cesaro averages would converge more slowly. RH asserts that no such slow mode exists: the escape process mixes as fast as its spectral structure allows.

### 6.5. The skyline as a quasi-ergodic system

The Factor Skyline, viewed as the dynamical system (Z, T: n->n+1) with observable dx(n), is **quasi-ergodic**: it has a non-trivial rigid factor (the template) and a mixing factor (the escape process). The rigid factor produces periodic correlations; the mixing factor produces ergodic convergence.

The decomposition:

    dx(n) = [template-determined part] + [escape-determined part]

where the template part is periodic (and accounts for 73.3% of the dx sequence) and the escape part is mixing (and accounts for 26.7%). The system is neither purely ergodic (the template prevents this) nor purely rigid (the escape process prevents this). It is a precise mixture of the two, with the mixing fraction determined by the escape density D(p) ~ 1/ln(n).

As n -> infinity, D(p) -> 0, so the escape fraction shrinks and the system becomes "more rigid" — the template dominates an ever-larger fraction of the dx sequence. But the escape process never vanishes entirely (D(p) > 0 for all finite p), so the system retains its mixing component forever. The skyline is **asymptotically rigid but permanently ergodic**.

---

## 7. Summary

| Component | Ergodic type | Mixing? | Convergence rate | FS content |
|-----------|-------------|---------|-----------------|------------|
| **Template** | Rigid (periodic) | No | Exact at p# | Deterministic coverage architecture |
| **Width layer 1_{q\|n}** | Rigid (period q) | No | Exact at q | Individual coverage layer |
| **Escape indicator** | Ergodic | Yes (RH) | O(1/sqrt(N)) | Prime positions among open slots |
| **omega(n) average** | Ergodic | **No** | O(1/sqrt(N)) for mean; correlations persist | Width-layer count: sum of rigid components |
| **mu(n) average** | Ergodic | Yes (Chowla) | O(1/sqrt(N)) | Width-layer parity: non-linear mixing of rigid |
| **Zero spectrum** | GUE-ergodic | Yes (maximal) | Universal after normalization | Spectral resonances of primorial hierarchy |
| **dx(n) sequence** | Quasi-ergodic | Partially | Template part: exact at 30; escape part: O(1/sqrt(N)) | 73% rigid + 27% mixing |

The Factor Skyline exhibits a layered ergodic structure: a rigid deterministic template constraining an ergodic escape process that generates a maximally mixing spectral resonance pattern. The template provides periodic order; the escape process provides ergodic mixing; the zeros provide spectral universality. The skyline is not ergodic or rigid — it is both, in precise proportions determined by the escape density.

The deepest structural insight: **the non-mixing of omega(n) and the mixing of mu(n) share the same rigid components but differ in the non-linearity of the observation function.** The width layers are rigid; the sum omega is non-mixing; the parity mu is mixing. The same coverage architecture produces both permanent correlation and asymptotic independence, depending on how you look at it.
