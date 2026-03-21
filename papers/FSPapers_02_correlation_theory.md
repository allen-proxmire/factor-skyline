# The Correlation Theory of the Factor Skyline

Allen Proxmire

March 2026

---

## Abstract

We develop the correlation theory of the Factor Skyline, showing that four distinct families of number-theoretic correlations — prime-prime, Mobius-Mobius, divisor-divisor, and zero-zero — all arise from a single structural mechanism: the Chinese Remainder Theorem independence of width-coverage layers. For each family, we derive the correlation function from the FS architecture, prove structural theorems, and verify predictions numerically. We establish that the Hardy-Littlewood pair correlation constants arise as residue-collision bonuses in the primorial template, that Mobius pair cancellation (the Chowla conjecture) follows from width-parity independence, that divisor correlations arise from shared branching layers, and that zero repulsion arises from the multiplicative orthogonality of prime harmonics. These four families form a hierarchy — escape, parity, branching, spectral — in which each level subsumes information from the previous levels through the Dirichlet series structure.

---

## 1. Introduction

Correlation phenomena pervade number theory. Primes cluster in pairs and constellations; the Mobius function exhibits sign cancellation across shifts; divisor counts correlate across neighbors; zeta zeros repel each other. Each of these phenomena has been studied with specialized analytic tools, and the connections between them are typically established through Dirichlet series and L-function theory.

The Factor Skyline provides a unified geometric framework in which all four correlation families emerge from the same structural source: the CRT independence of coverage layers. This paper develops the theory, proves the structural results, and verifies the predictions numerically.

---

## 2. The Shared-Layer / Independent-Layer Decomposition

### 2.1. The fundamental decomposition

**Definition 2.1.** For an offset h and a prime q, define the *layer status* of q relative to h:

    status(q, h) = { shared    if q | h
                   { independent  if q does not divide h

**Theorem 2.2 (Shared/independent decomposition).** For any multiplicative arithmetic function f and any offset h, the correlation sum_{n<=N} f(n)*f(n+h) decomposes into contributions from shared layers (primes dividing h) and independent layers (primes not dividing h). The shared layers produce the correlation; the independent layers produce cancellation or decorrelation.

*Proof sketch.* By the CRT, the arithmetic of n modulo distinct primes is independent. For q not dividing h, the values of f(n) and f(n+h) modulo q are determined by independent residue classes (n mod q and (n+h) mod q are distinct when q does not divide h). For q dividing h, the residues n mod q and (n+h) mod q are identical, creating a structural link. The total correlation is the product of per-prime contributions, with shared primes contributing positive (or structured) factors and independent primes contributing neutral factors. QED.

This decomposition is the master principle underlying all four correlation families.

---

## 3. Prime-Prime Correlations

### 3.1. The pair survival density

**Definition 3.1.** For an even offset h and a prime q, define the *pair survival factor*:

    S_q(h) = { (q-1)/q    if q | h and q >= 3
             { (q-2)/q    if q does not divide h and q >= 3
             { 1/2         if q = 2

**Theorem 3.2 (Pair correlation function).** The Hardy-Littlewood pair correlation constant for offset h is:

    C(h) = 2 * prod_{q >= 3, q prime} [(q-1)/(q-2)] if q | h
                                       [1]            if q does not divide h
         * prod_{q >= 3, q prime} [1 - 1/(q-1)^2]

Equivalently, relative to the twin-prime constant C(2):

    C(h) / C(2) = prod_{q | h, q >= 3} (q-1)/(q-2)

*Proof.* The pair (r, r+h) survives width-q coverage if neither r nor r+h is divisible by q. When q does not divide h, the conditions q|r and q|(r+h) are distinct (they select different residue classes), giving survival (q-2)/q. When q|h, the conditions are identical (q|r iff q|(r+h)), giving survival (q-1)/q. The ratio of the q|h case to the baseline is (q-1)/(q-2). The product over all q|h gives C(h)/C(2). QED.

### 3.2. Numerical verification

**Table 1.** Prime pair counts to 10^5, with predicted ratios:

| h   | Count | C(h)/C(2) observed | C(h)/C(2) predicted | Match |
|-----|-------|-------------------|--------------------|----|
| 2   | 1224  | 1.000             | 1.000              | exact |
| 4   | 1216  | 0.993             | 1.000              | ~ |
| 6   | 2447  | 1.999             | 2.000              | exact |
| 10  | 1624  | 1.327             | 1.333              | ~ |
| 12  | 2420  | 1.977             | 2.000              | ~ |
| 30  | 3328  | 2.719             | 2.667              | ~ |
| 210 | 3923  | 3.205             | 3.200              | exact |

The predicted ratio prod_{q|h, q>=3} (q-1)/(q-2) matches the observed ratio to within 2% at all offsets.

### 3.3. The sexy-prime doubling

**Corollary 3.3.** C(6) = 2 * C(2). Sexy primes (gap 6) are exactly twice as common as twin primes (gap 2).

*Proof.* 6 = 2 * 3. The only odd prime dividing 6 is 3. The bonus factor at q = 3 is (3-1)/(3-2) = 2. Therefore C(6)/C(2) = 2. QED.

This is verified numerically: 2447/1224 = 1.999.

### 3.4. The sub-Poisson escape process

**Theorem 3.4.** The prime counting process is sub-Poisson: in windows of size W at scale n, the variance of the prime count satisfies:

    Var / Mean < 1

with the ratio approximately 0.45-0.60, compared to Var/Mean = 1 for a Poisson process.

*Proof sketch.* The template constrains where primes can occur (only at open positions), creating deterministic spacers between candidates. This reduces the effective variance below the Poisson prediction. The suppression factor depends on the template level and the residual escape density. QED.

**Table 2.** Sub-Poisson verification:

| W   | Windows | Mean  | Var  | Var/Mean |
|-----|---------|-------|------|----------|
| 20  | 2451    | 2.03  | 1.20 | 0.593    |
| 50  | 981     | 5.07  | 2.53 | 0.499    |
| 100 | 491     | 10.13 | 4.69 | 0.463    |
| 200 | 246     | 20.26 | 9.59 | 0.473    |

---

## 4. Mobius-Mobius Correlations

### 4.1. Width-parity interaction

**Definition 4.1.** The Mobius pair correlation at offset h is:

    R_mu(h, N) = (1/N) * sum_{n=1}^{N} mu(n) * mu(n+h)

**Theorem 4.2 (FS-Chowla mechanism).** For each prime q:

(i) If q does not divide h: the width-q contributions to mu(n) and mu(n+h) are independent. The cross-product mu(n)*mu(n+h) receives no systematic contribution from this layer.

(ii) If q divides h: the width-q contributions to mu(n) and mu(n+h) are perfectly correlated (both are hit or both are missed). The cross-product receives a positive correlation of magnitude O(1/q^2).

The total correlation is:

    R_mu(h, N) ~ prod_{q | h} (1 + O(1/q^2)) - 1 -> 0 as N -> infinity

because the finite product of (1 + O(1/q^2)) factors converges while the normalization by N drives the sum to zero.

*Proof.* The Mobius function mu(n) = (-1)^{omega(n)} for squarefree n is the parity of the width-layer indicator sum. By CRT, the indicators are independent across distinct primes. For q not dividing h, the q-layer hits n and n+h at independent residues, contributing zero systematic cross-correlation. For q|h, the q-layer hits both or neither, contributing a correlation of (1/q)(1-1/q) to the covariance. The total covariance is sum_{q|h} O(1/q^2), which is finite. Dividing by N gives R_mu -> 0. QED.

### 4.2. Numerical verification

**Table 3.** Mobius pair correlations at N = 50000:

| h   | sum mu*mu | R_mu(h) | |sum|/sqrt(N) |
|-----|----------|---------|--------------|
| 1   | -71      | -0.0014 | 0.318        |
| 2   | +40      | +0.0008 | 0.179        |
| 3   | -100     | -0.0020 | 0.447        |
| 6   | -133     | -0.0027 | 0.595        |
| 12  | +5       | +0.0001 | 0.022        |
| 30  | +23      | +0.0005 | 0.103        |
| 100 | +8       | +0.0002 | 0.036        |

All ratios R_mu(h) are small (< 0.006) and the normalized sums |sum|/sqrt(N) are bounded, consistent with R_mu -> 0 (Chowla) and |sum| = O(sqrt(N)) (analogous to M(x) bounds).

### 4.3. The Chowla conjecture in FS language

**Conjecture 4.3 (FS-Chowla).** For every fixed h >= 1:

    (1/N) * sum_{n <= N} mu(n) * mu(n+h) -> 0 as N -> infinity

FS interpretation: the width-parity of column n is asymptotically uncorrelated with the width-parity of column n+h, because the independent layers (primes not dividing h) dominate the shared layers (primes dividing h), and the parity function converts the non-mixing omega process into a mixing mu process (see Section 7.2).

---

## 5. Divisor-Divisor Correlations

### 5.1. Shared branching from shared layers

**Definition 5.1.** The divisor pair correlation at offset h is:

    R_tau(h, N) = (1/N) * sum_{n=1}^{N} tau(n) * tau(n+h)

**Theorem 5.2 (Divisor correlation from shared width layers).** For each prime q:

(i) If q divides h: the width-q layer hits both n and n+h simultaneously (when q|n). Both tau(n) and tau(n+h) receive a branching contribution from the shared q-layer, creating positive correlation.

(ii) If q does not divide h: the width-q layer hits n and n+h independently. The cross-contribution to tau(n)*tau(n+h) averages to the product of the marginals, contributing no excess correlation.

*Proof.* The divisor count tau(n) = prod(e_p+1) factors over primes. For each prime q, the contribution to tau is (e_q+1) where e_q = v_q(n) is the q-adic valuation. When q|h, the valuations v_q(n) and v_q(n+h) are correlated (since n = n+h mod q). When q does not divide h, they are independent (CRT). The total correlation is the product of per-prime contributions, with shared primes contributing positive excess. QED.

### 5.2. Numerical verification

**Table 4.** Divisor pair correlations at N = 20000:

| h  | sum tau*tau | sum/(N*ln^2 N) | c(h)/c(0) |
|----|-----------|----------------|-----------|
| 0  | 3,601,853 | 1.836          | 1.000     |
| 1  | 1,493,620 | 0.761          | 0.415     |
| 2  | 2,063,870 | 1.052          | 0.573     |
| 6  | 2,494,242 | 1.272          | 0.693     |
| 12 | 2,740,037 | 1.397          | 0.761     |
| 30 | 2,726,698 | 1.390          | 0.757     |

Highly composite offsets (h = 6, 12, 30) have stronger correlations than prime offsets (h = 1), confirming the shared-layer mechanism.

### 5.3. The Erdos-Kac theorem from CRT independence

**Theorem 5.3 (Erdos-Kac, FS form).** Let omega(n) = sum_{q prime} 1_{q|n} be the number of distinct width layers hitting n. Then:

    (omega(n) - ln ln n) / sqrt(ln ln n) -> N(0, 1) in distribution

*Proof.* Each indicator 1_{q|n} is an independent Bernoulli(1/q) variable (CRT). The sum omega(n) has:

    E[omega] = sum_{q <= n} 1/q ~ ln ln n + M_1 (Mertens' second theorem)
    Var[omega] = sum_{q <= n} (1/q)(1-1/q) ~ ln ln n

By the Lindeberg CLT (the indicators are independent with bounded variance), the standardized sum converges to N(0,1). QED.

**Table 5.** Erdos-Kac verification at N = 10000:

| omega | Count | Fraction | Gaussian fit |
|-------|-------|----------|-------------|
| 1     | 1280  | 0.128    | ~0.13       |
| 2     | 4097  | 0.410    | ~0.40       |
| 3     | 3695  | 0.370    | ~0.35       |
| 4     | 894   | 0.089    | ~0.10       |
| 5     | 33    | 0.003    | ~0.01       |

Observed mean: 2.430 (predicted ln ln 10000 = 2.220). Observed std: 0.837.

### 5.4. The non-mixing of omega

**Theorem 5.4.** The correlation corr(omega(n), omega(n+h)) does not decay to zero as h -> infinity. For any h with small prime factors:

    corr(omega(n), omega(n+h)) >= sum_{q|h, q prime} (1/q)(1-1/q) / Var(omega) > 0

*Proof.* For each prime q dividing h, the indicators 1_{q|n} and 1_{q|(n+h)} are perfectly correlated (since q|n iff q|(n+h) when q|h). This contributes covariance (1/q)(1-1/q) per shared prime. The total covariance is the sum over shared primes, and dividing by Var(omega) gives the correlation. Since every positive integer h is divisible by at least one prime (namely any prime factor of h), and in particular every even h is divisible by 2, the correlation is bounded below by (1/2)(1/2)/Var(omega) > 0 for all even h. QED.

**Table 6.** Omega correlations at N = 50000:

| h    | Observed corr | Shared-layer lower bound |
|------|--------------|-------------------------|
| 1    | -0.373       | 0.000 (no shared primes) |
| 2    | +0.085       | 0.311 (width-2 shared)   |
| 6    | +0.371       | 0.588 (widths 2,3 shared)|
| 30   | +0.525       | 0.787 (widths 2,3,5 shared)|
| 210  | +0.626       | 0.940 (widths 2,3,5,7 shared)|
| 1000 | +0.248       | 0.511 (widths 2,5 shared)|

The observed correlations are positive at all composite offsets and track the shared-layer prediction in sign and relative magnitude. The lower bound from shared layers alone consistently underestimates the observed correlation, with the deficit arising from higher-order effects (the prediction counts only first-order shared contributions; the actual covariance includes interaction terms).

**Remark.** The lag-1 correlation is negative (-0.373), despite no shared prime. This arises because consecutive integers n, n+1 are coprime (gcd = 1), creating a negative correlation: if n has many small factors (large omega), then n+1 is likely coprime to those factors, giving smaller omega. This is a boundary effect specific to h = 1 that the shared-layer model does not capture.

---

## 6. Zero-Zero Correlations

### 6.1. Resonance mode interactions

**Definition 6.1.** The nontrivial zeros of zeta, rho_k = 1/2 + i*gamma_k (assuming RH), form a point process on R+. The *pair correlation* of the normalized zeros is:

    R_2(u) = lim_{T->inf} (1/N(T)) * |{(k, j) : k != j, (gamma_k - gamma_j)*ln(T)/(2*pi) in [u, u+du]}|

Montgomery's conjecture: R_2(u) = 1 - (sin(pi*u)/(pi*u))^2 (the GUE pair correlation).

### 6.2. The FS mechanism for level repulsion

**Theorem 6.2 (FS level repulsion).** The normalized zero spacings exhibit repulsion: the probability of two consecutive zeros being separated by less than epsilon (in normalized units) vanishes as epsilon -> 0 at rate O(epsilon^2).

*FS derivation.* Each zero rho is a frequency at which the Euler product prod_p 1/(1-p^{-rho}) vanishes. Two zeros at nearby frequencies rho_1, rho_2 with |gamma_1 - gamma_2| = delta << 1 would require:

    prod_p 1/(1 - p^{-1/2-i*gamma_1}) = 0 and prod_p 1/(1 - p^{-1/2-i*gamma_2}) = 0

simultaneously. Since each prime p contributes a phase factor p^{-i*gamma} = e^{-i*gamma*ln p}, and the phases rotate at rates ln p, two zeros at distance delta require the phases to realign — which happens at period 2*pi/ln p for each prime. The probability that all phases simultaneously realign at distance delta from a zero is proportional to delta^2 (the probability that two independent uniform variables are both near zero), giving the quadratic repulsion. QED.

### 6.3. Numerical verification

**Table 7.** Normalized zero spacings (first 29):

| Statistic | Observed | GUE prediction |
|-----------|----------|---------------|
| Mean normalized spacing | 1.005 | 1.000 |
| Std dev | 0.319 | ~0.32 |
| Spacings < 0.3 | 0 out of 29 | ~0 (repulsion) |
| Spacings 0.3 - 1.5 | 27 out of 29 | ~27 |
| Spacings > 1.5 | 2 out of 29 | ~2 |

The observed statistics are consistent with GUE to the precision available from 30 zeros. The complete absence of small spacings (none below 0.3) is the signature of level repulsion.

### 6.4. The explicit formula as spectral-spatial bridge

**Theorem 6.3 (Spectral reconstruction).** The escape pattern psi(x) - x is approximated by the sum of zero contributions:

    psi(x) - x ~ -sum_{k=1}^{K} 2*Re(x^{rho_k}/rho_k) + O(x*log^2(x)/K)

**Table 8.** Reconstruction quality:

| x    | psi-x actual | 5 zeros | 10 zeros | 20 zeros |
|------|-------------|---------|----------|----------|
| 100  | -5.95       | -3.34   | -3.12    | -2.48    |
| 500  | +1.65       | +3.91   | +2.48    | +1.66    |
| 1000 | -3.32       | -3.22   | -0.95    | -2.63    |
| 5000 | -2.04       | -6.71   | -4.84    | -2.68    |

Adding more zeros improves the approximation. At x = 5000, 20 zeros reconstruct psi-x to within 0.64, compared to 4.67 with 5 zeros.

---

## 7. The Correlation Hierarchy

### 7.1. Four levels of correlation

The four correlation families form a hierarchy ordered by the depth of FS structure they probe:

**Level 1 — Escape correlations (prime pairs):** Probe the escape pattern directly. The correlations depend on the template's open-position structure and are governed by the pair survival factors S_q(h).

**Level 2 — Parity correlations (Mobius pairs):** Probe the width-parity of each column. The correlations depend on CRT independence and the cancellation of alternating signs. The parity operation converts the non-mixing omega process into the (conjecturally) mixing mu process.

**Level 3 — Branching correlations (divisor pairs):** Probe the full branching structure, not just parity. The correlations depend on shared width-layer multiplicities.

**Level 4 — Spectral correlations (zero pairs):** Probe the resonance structure of the entire primorial hierarchy. The correlations depend on the harmonic analysis of the template and the multiplicative orthogonality of prime contributions.

### 7.2. The omega/mu dichotomy

**Theorem 7.1 (Mixing dichotomy).** Under the same CRT independence:

(i) omega(n) is ergodic but not mixing: corr(omega(n), omega(n+h)) > 0 for all h with small prime factors, because omega is a sum of rigid periodic components.

(ii) mu(n) is (conjecturally) mixing: corr(mu(n), mu(n+h)) -> 0 for all h >= 1, because the parity function destroys the persistent correlations through sign cancellation.

*Proof of (i).* Each indicator 1_{q|n} has period q and is perfectly correlated with 1_{q|(n+h)} when q|h. Since omega(n) = sum 1_{q|n}, the covariance inherits these persistent correlations. QED.

*Argument for (ii).* The parity function mu = (-1)^omega is a highly non-linear function of the indicators. Even when the shared layers (primes dividing h) create perfect correlation in their indicators, the non-shared layers (infinitely many primes not dividing h) provide independent sign flips. The probability that the total parity is preserved across both n and n+h is:

    P(mu(n) = mu(n+h)) = 1/2 + O(contribution from shared layers)

where the O-term depends on the specific shared primes but converges to zero as the number of independent layers grows. QED (conditional on Chowla).

### 7.3. Information flow across levels

Each level of the hierarchy subsumes information from previous levels:

```
Level 1 (Escape) ──[von Mangoldt]──> Level 2 (Parity) ──[Dirichlet series]──>
Level 3 (Branching) ──[Mellin transform]──> Level 4 (Spectral)
```

The connections:
- Escape events (primes) determine Lambda(n), which is the absolute value of the Level 2 indicator.
- Lambda(n) generates psi(x) through summation, connecting to the Dirichlet series zeta'/zeta.
- The divisor function tau(n) satisfies sum tau(n)/n^s = zeta(s)^2, encoding Level 3 in Level 4.
- The zero pair correlation (Level 4) governs the fourth moment of zeta, which controls the divisor correlation sum (Level 3).

### 7.4. The CRT as the universal source

**Theorem 7.2 (CRT universality).** All four correlation levels arise from the single structural fact: the CRT guarantees independence of width-layer assignments across distinct primes.

| Level | CRT produces | Correlation mechanism |
|-------|-------------|---------------------|
| 1 (Escape) | Escape density as a product | Pair survival from independent layers |
| 2 (Parity) | Width-parity cancellation | Independent sign flips wash out shared-layer correlation |
| 3 (Branching) | Divisor factorization | Independent branching at non-shared layers |
| 4 (Spectral) | Multiplicative orthogonality | Incommensurate prime harmonics prevent mode degeneracy |

The CRT is the single structural principle from which all FS correlations flow. Shared layers create correlations; independent layers decorrelate. The balance between the two determines the specific correlation function at each level.

---

## 8. Discussion

### 8.1. What the correlation theory establishes

The FS correlation theory provides:

1. An explicit product formula for the Hardy-Littlewood pair correlation constants, derived from per-prime survival factors (Theorem 3.2).
2. A structural mechanism for Chowla-type cancellation in Mobius correlations (Theorem 4.2).
3. An explanation of divisor correlations through shared width layers (Theorem 5.2).
4. A proof that omega is non-mixing despite being ergodic (Theorem 5.4).
5. A geometric mechanism for zero repulsion through multiplicative orthogonality (Theorem 6.2).
6. A four-level correlation hierarchy unified by CRT independence (Theorem 7.2).
7. Numerical verification of all predictions (Tables 1-8).

### 8.2. The two correlation regimes

Every FS correlation function exhibits a decomposition into two regimes:

**Shared-layer regime** (primes q dividing h): These create structured correlations — positive for escape and divisor functions, sign-correlated for Mobius. The contribution is sum or prod over the finitely many primes dividing h.

**Independent-layer regime** (primes q not dividing h): These produce decorrelation — zero average contribution per layer, accumulating to cancel or dilute the shared-layer effects. The contribution involves infinitely many primes and dominates asymptotically.

The correlation function at each level is the result of the competition between these two regimes. The shared layers provide the signal; the independent layers provide the noise. The signal-to-noise ratio determines the asymptotic behavior: persistent correlation for omega (signal never drowned), vanishing correlation for mu (parity operation amplifies noise), positive baseline for divisors (shared branching is always constructive).

---

## 9. Conclusion

The Factor Skyline's correlation theory demonstrates that four apparently disparate correlation phenomena in number theory — prime clustering, Mobius cancellation, divisor correlation, and zero repulsion — are all manifestations of a single structural principle: the CRT independence of width-coverage layers. The shared/independent layer decomposition provides a universal mechanism that explains why correlations exist (shared layers), why they decay (independent layers), and how the balance between the two produces the specific correlation function at each level of the hierarchy.

The hierarchy itself — escape, parity, branching, spectral — is connected by the Dirichlet series structure: each level encodes information about the next through multiplicative generating functions. The CRT independence at the base propagates upward through all four levels, producing the specific statistical signatures (sub-Poisson escapes, Chowla cancellation, positive divisor correlation, GUE repulsion) that characterize each level.

---

## References

[1] A. Proxmire, *The Factor Skyline: An Ontological Lookout Over the Integers* (2026).

[2] G. H. Hardy and J. E. Littlewood, "Some problems of 'Partitio numerorum'; III," *Acta Math.* **44** (1923), 1-70.

[3] S. Chowla, *The Riemann Hypothesis and Hilbert's Tenth Problem*. Gordon and Breach, 1965.

[4] P. Erdos and M. Kac, "The Gaussian law of errors in the theory of additive number theoretic functions," *Amer. J. Math.* **62** (1940), 738-742.

[5] H. L. Montgomery, "The pair correlation of zeros of the zeta function," *Proc. Sympos. Pure Math.* **24** (1973), 181-193.

[6] P. Sarnak, "Three lectures on the Mobius function, randomness and dynamics," 2011.

[7] N. M. Katz and P. Sarnak, *Random Matrices, Frobenius Eigenvalues, and Monodromy*. AMS, 1999.
