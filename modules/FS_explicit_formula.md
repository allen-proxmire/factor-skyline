# The Explicit Formula in FS-Geometry

---

## Overview

The classical explicit formula for psi(x) is:

    psi(x) = x - sum_{rho} x^{rho}/rho - log(2*pi) - (1/2)*log(1 - x^{-2})

where the sum runs over the non-trivial zeros rho of zeta(s). This formula decomposes the prime-counting function into a smooth main term (x), a sum of oscillatory corrections (one per zero), and small constant/remainder terms.

In the Factor Skyline, the explicit formula becomes a **decomposition of escape geometry**: the cumulative height of structural events (escapes and activations) equals a smooth corridor-collapse term plus a sum of oscillatory modes that encode how escape positions deviate from the predictions of the escape density product.

This document derives the FS-geometric meaning of each term.

---

## 1. Escape Events and Activation Events as Geometric Impulses

### 1.1. The von Mangoldt impulse train

The von Mangoldt function Lambda(n) is nonzero exactly at structurally significant integers:

    Lambda(n) = { log(p)   if n = p^k for some prime p and k >= 1
                { 0         otherwise

In the Factor Skyline, these structurally significant integers are of two types:

**Escape events (primes, k = 1):** A prime p has dx = 1 and y_FS = p. It contributes an impulse of weight log(p) = log(y_FS(p)). This is a narrow spire in the skyline, and the impulse weight equals the logarithm of its height.

**Activation events (prime powers, k >= 2):** A prime power p^k has dx = lpf(p^k) = p and y_FS = p^{k-1}. It contributes an impulse of weight log(p). At the activation threshold p^2 specifically, y_FS = p and the impulse weight equals log(y_FS(p^2)) -- the logarithm of the activation column's height.

All other integers (composites that are not prime powers) are structurally silent: Lambda(n) = 0. They are ordinary coverage columns, carrying no structural information beyond their width assignment.

### 1.2. The impulse train in the skyline

The psi function is the cumulative sum of these impulses:

    psi(x) = sum_{n <= x} Lambda(n) = sum_{structural events n <= x} log(p_n)

Walking along the skyline from n = 1 to n = x, psi accumulates a log(p) token at each escape event and each activation event. Between these events, psi is flat (no tokens). The graph of psi(x) is a **staircase** that rises at each escape or activation by the corresponding log(p).

The impulse train has a characteristic pattern visible in the data:

```
n:   2     3     4     5     7     8     9    11    13    16    17 ...
Lam: 0.69  1.10  0.69  1.61  1.95  0.69  1.10  2.40  2.56  0.69  2.83 ...
type: esc   esc  act   esc   esc  act   act   esc   esc  act   esc  ...
```

Escape impulses grow (log(p) increases with p). Activation impulses are sparser and smaller (they recycle log(p) from primes already seen, at their squares and higher powers).

### 1.3. The FS-x impulse view

In FS-x coordinates, the impulse train is unevenly spaced. Escape events contribute dx = 1, so consecutive escapes are spaced 1 unit apart in FS-x. Composites between escapes contribute dx = lpf(n) >= 2, stretching the FS-x gap between consecutive escape impulses.

The FS-x spacing between escape impulse k and escape impulse k+1 is:

    Delta_x = 2 + sum_{composites in gap} lpf(n)

This spacing is the **FS-x gap** analyzed in `FS_prime_gaps.md`. The impulse train, viewed in FS-x, has a quasi-periodic structure modulated by the width spectrum of the composite corridors between escapes.

---

## 2. The Smooth Term: Corridor Collapse

### 2.1. The main term psi(x) ~ x

The explicit formula's main term is simply x. In FS-geometry, this is the **smooth corridor-collapse prediction**: the total structural weight accumulated up to x, predicted by the escape density product.

The derivation (from `FS_Chebyshev.md`):

- There are ~x/ln(x) escape events up to x, each contributing average weight ~ln(x).
- The total escape weight is ~(x/ln(x)) * ln(x) = x.
- Activation events contribute ~sqrt(x), asymptotically negligible.
- Therefore psi(x) ~ x.

This is the **conservation law**: the escape density thins the escapes, but each escape grows taller by exactly the compensating amount. The smooth term x records the cumulative effect of this conservation.

### 2.2. The smooth term as corridor integration

More precisely, the smooth term represents the integral of the coverage architecture over [2, x]:

    x = integral from 2 to x of 1 dt

The integrand "1" is the **local structural weight density**: at every point on the number line, the expected structural weight (from escapes and activations combined) is 1 per unit length. This unit density is the FS conservation law expressed infinitesimally.

The escape density D(sqrt(t)) predicts ~1/ln(t) escapes per unit length near t, each of weight ~ln(t), giving a local weight density of ~1. The activation density adds a correction of O(1/sqrt(t)), giving a total density that converges to 1.

### 2.3. Numerical structure: psi(x) - x oscillates near zero

| x     | psi(x)  | psi - x  | (psi-x)/sqrt(x) |
|-------|---------|----------|------------------|
| 50    | 49.49   | -0.51    | -0.073           |
| 100   | 94.05   | -5.95    | -0.596           |
| 500   | 501.65  | +1.65    | +0.074           |
| 1000  | 996.68  | -3.32    | -0.105           |
| 5000  | 4997.96 | -2.04    | -0.029           |
| 10000 | 10013.4 | +13.40   | +0.134           |

Unlike theta(x) - x (which is persistently negative), psi(x) - x oscillates around zero. The activation contribution (~sqrt(x)) partially compensates the negative escape error (~-sqrt(x)), bringing psi closer to its smooth prediction. The ratio (psi-x)/sqrt(x) stays bounded and oscillates -- the signature of square-root-scale fluctuations.

---

## 3. The Oscillatory Terms: Zeros as Escape-Pattern Resonances

### 3.1. The classical oscillatory sum

The explicit formula's oscillatory part is:

    -sum_{rho} x^{rho}/rho

where rho = beta + i*gamma ranges over the non-trivial zeros of zeta(s). Each zero contributes:

    -x^{rho}/rho = -x^{beta} * e^{i*gamma*ln(x)} / rho

This is a **damped oscillation** with:
- amplitude envelope x^{beta} (how large the oscillation is)
- frequency gamma (how fast it oscillates as x varies)
- phase and normalization from 1/rho

### 3.2. FS-geometric meaning of each zero

In the Factor Skyline, each non-trivial zero corresponds to a **resonant mode of the escape pattern** -- a frequency at which the positions of escape events deviate systematically from the smooth prediction.

**The frequency gamma:** The escape positions are constrained by the primorial template, which has period p# for primes up to p. The template creates a quasi-periodic pattern of open and covered positions. The Fourier analysis of this pattern produces a discrete spectrum. As the template grows (incorporating more primes), the spectrum fills out. The imaginary parts gamma of the zeros are the frequencies in this spectrum.

**The amplitude x^{beta}:** The damping rate beta determines how rapidly each mode's influence decays as x grows. RH asserts beta = 1/2 for all zeros, meaning every mode decays at rate x^{1/2}. In FS terms, every resonance of the coverage architecture is damped at the activation-horizon scale.

**The superposition:** The total oscillatory correction is the superposition of all these damped oscillations. Near any given x, a finite number of modes contribute significantly (those whose frequencies are commensurate with x), producing the local fluctuations in psi(x) - x.

### 3.3. How oscillations appear in the impulse train

The oscillatory terms modulate the spacing and density of structural impulses. In windows of size 100, the total Lambda weight fluctuates:

| Window       | Escapes | Activations | sum Lambda | Lambda/100 |
|-------------|---------|-------------|------------|------------|
| [0, 99]     | 25      | 10          | 94.05      | 0.94       |
| [100, 199]  | 21      | 4           | 112.10     | 1.12       |
| [200, 299]  | 16      | 3           | 93.09      | 0.93       |
| [300, 399]  | 16      | 2           | 98.60      | 0.99       |
| [400, 499]  | 17      | 0           | 103.82     | 1.04       |
| [500, 599]  | 14      | 2           | 92.26      | 0.92       |
| [600, 699]  | 16      | 1           | 105.10     | 1.05       |

The density Lambda/100 oscillates around the smooth prediction of 1.00. Windows with density > 1 have "excess escapes" (a local prime-rich region); windows with density < 1 have a local prime deficit. These fluctuations are the real-space manifestation of the oscillatory terms in the explicit formula.

### 3.4. Activation events as impulse corrections

At each activation event p^2, the impulse train receives a log(p) bump:

```
  n = 49 (= 7^2):  psi jumps by log(7) = 1.946
  n = 121 (= 11^2): psi jumps by log(11) = 2.398
  n = 169 (= 13^2): psi jumps by log(13) = 2.565
```

These activation impulses are visible in the local behavior of psi(x) - x: the error term receives a positive kick of size log(p) at each p^2. Between activations, the error drifts downward (as the smooth term x grows by 1 per integer, but psi only grows at escape events, which are sparser than 1 per integer in most intervals).

The sawtooth pattern of psi(x) - x -- upward kicks at structural events, downward drift between them -- is the time-domain (real-space) form of the oscillatory sum. The explicit formula decomposes this sawtooth into its frequency components.

---

## 4. The Decomposition of Escape Geometry

### 4.1. The full FS decomposition

The explicit formula, translated into FS-geometry, is:

```
psi(x)  =   x                              [smooth corridor-collapse term]
           - sum_{rho} x^{rho}/rho          [oscillatory escape-pattern resonances]
           - log(2*pi)                      [constant: normalization of the corridor]
           - (1/2)*log(1 - x^{-2})          [remainder: boundary correction]
```

Each term has a precise geometric meaning:

**Term 1: x (the smooth prediction).**
The total structural weight that would accumulate if escapes were distributed exactly according to the escape density product D(sqrt(x)), with no fluctuations. This is the corridor-collapse integral -- the smooth envelope of the escape staircase.

**Term 2: -sum x^{rho}/rho (the oscillatory corrections).**
The deviations of actual escape positions from the smooth prediction. Each zero rho contributes one oscillatory mode. The superposition of all modes produces the actual fluctuation pattern E(x) = psi(x) - x. These oscillations encode the fine structure of the primorial template -- the specific pattern of open and covered positions that modulates the escape density at different frequencies.

**Term 3: -log(2*pi) (the constant).**
A small negative constant (~-1.84) that represents the normalization offset between the continuous prediction and the discrete impulse train. In FS terms, this is the correction for the fact that the corridor-collapse integral starts from an idealized continuous model, while the actual structural events are discrete.

**Term 4: -(1/2)*log(1 - x^{-2}) (the boundary term).**
A negligible correction that accounts for the trivial zeros of zeta (at s = -2, -4, -6, ...). In FS terms, these correspond to the ultraviolet structure of the coverage pattern -- the behavior at the finest scales of the primorial template, which contributes only O(1/x^2) to the total.

### 4.2. The escape-activation balance

The decomposition reveals a fundamental balance in the skyline. Rewrite psi(x) - x using the escape/activation decomposition:

    psi(x) - x = [theta(x) - x] + [psi(x) - theta(x)]

where:
- theta(x) - x is the **escape error**: typically negative (~-sqrt(x) scale), reflecting the Legendre sieve overcounting.
- psi(x) - theta(x) is the **activation contribution**: always positive (~sqrt(x) scale), reflecting the cumulative weight of prime-power activations.

Numerically:

| x     | theta-x  | psi-theta | psi-x   | psi-theta / sqrt(x) |
|-------|----------|-----------|---------|---------------------|
| 100   | -16.27   | +10.32    | -5.95   | 1.03                |
| 500   | -25.45   | +27.10    | +1.65   | 1.21                |
| 1000  | -43.75   | +40.44    | -3.32   | 1.28                |
| 5000  | -88.30   | +86.26    | -2.04   | 1.22                |
| 10000 | -104.01  | +117.41   | +13.40  | 1.17                |

The escape error and the activation contribution are both O(sqrt(x)), and they nearly cancel. The total error psi-x is the small residual of this near-cancellation. In FS terms:

**The negative escape bias (primes slightly undercounting the density prediction) is almost exactly compensated by the positive activation weight (prime powers adding structural impulses).** The explicit formula's oscillatory terms encode the residual imbalance after this cancellation.

### 4.3. The escape staircase and its Fourier structure

The function psi(x) is a staircase that rises by log(p) at each structural event and is flat elsewhere. The explicit formula is the **Fourier decomposition** of this staircase:

- The smooth term x is the DC component (the average rise rate).
- Each zero rho contributes an AC component (an oscillation at frequency Im(rho)).
- The superposition reconstructs the staircase from its harmonic content.

In FS-geometry, this Fourier decomposition has a physical meaning:

- **DC component (x):** The conservation law. Escape height accumulates at unit rate.
- **AC components (zeros):** The resonances of the primorial template. Each frequency corresponds to a periodic modulation of the escape pattern, arising from the interaction of coverage layers at different scales.

The explicit formula is therefore the statement that the **escape staircase is completely determined by the conservation law plus the template resonances.** There is no additional structure -- the zeros of zeta capture all the information about how escapes deviate from the smooth prediction.

---

## 5. Structural Insights

### 5.1. The explicit formula as a completeness theorem for escape geometry

The most profound FS interpretation of the explicit formula is as a **completeness theorem**:

> The escape pattern of the Factor Skyline is completely determined by:
> 1. The conservation law (psi ~ x).
> 2. The resonant spectrum (the zeros of zeta).
> 3. A normalization constant (log 2*pi).
>
> No other information is needed to reconstruct the positions of all primes and prime powers.

This means the zeros of zeta are not merely analytic curiosities -- they are the **complete set of parameters** describing how the escape pattern deviates from the smooth prediction. The FS architecture (activation, coverage, escape) produces a staircase whose harmonic content is exactly the zero spectrum of zeta.

### 5.2. The impulse response at activations

Each activation event at p^2 produces a characteristic local response in psi(x) - x:

1. Immediately before p^2: psi-x has been drifting downward (composites contribute no Lambda weight, but the smooth term x increases by 1 per integer).
2. At p^2: psi jumps by log(p) (the activation impulse).
3. After p^2: the new coverage layer removes fraction 1/p of the remaining corridor, slightly increasing the rate of downward drift (fewer escapes per unit interval in the newly narrowed corridor).

The activation impulse partially compensates the preceding downward drift, creating the sawtooth pattern. The explicit formula says this sawtooth can be decomposed into a finite number of dominant oscillatory modes plus a tail of rapidly damped higher frequencies.

### 5.3. The FS meaning of "truncating the zero sum"

In practice, the explicit formula is used with a truncated sum -- only zeros with |Im(rho)| <= T are included. The truncation error is O(x * log^2(x) / T). In FS terms:

- Including zeros up to height T captures the oscillatory modes with periods down to ~2*pi/T in the log-scale.
- Higher-frequency modes correspond to finer structure in the primorial template -- modulations at the scale of individual open positions rather than blocks of positions.
- Truncating at T corresponds to **coarse-graining the primorial template** -- averaging over the fine structure and retaining only the large-scale modulations.

This gives an FS recipe for approximating the escape pattern at different resolutions: use more zeros for finer resolution of escape positions, fewer zeros for a smooth large-scale picture.

### 5.4. The FS content of the Riemann-von Mangoldt formula

The Riemann-von Mangoldt formula counts the number of zeros with 0 < Im(rho) <= T:

    N(T) ~ (T/2*pi) * log(T/2*pi) - T/2*pi

In FS terms, this counts the **number of resonant modes** of the coverage architecture below frequency T. The count grows as T*log(T), meaning the resonance spectrum becomes denser at higher frequencies (but each mode is more rapidly damped).

This growing density of resonances reflects the increasing complexity of the primorial template as more primes are incorporated. Each new prime p adds O(log p) new resonant frequencies to the spectrum, arising from the interaction of the width-p layer with all previously active layers.

### 5.5. What the explicit formula reveals about the FS architecture

The explicit formula, read through the FS lens, says:

1. **The coverage architecture is spectrally complete.** The zeros of zeta capture all the information about escape-pattern deviations. The skyline's structure is entirely encoded in the conservation law plus the zero spectrum.

2. **Activation events are impulses; zeros are resonances.** The sawtooth pattern of psi(x) at structural events is the time-domain signal. The zeros are its frequency-domain representation. The explicit formula is the bridge between these two views.

3. **The escape-activation balance is structural.** The near-cancellation between the negative escape error and the positive activation contribution is not accidental -- it is enforced by the conservation law. The residual error after cancellation is the oscillatory part, which RH bounds at sqrt(x).

4. **Resolution and truncation have geometric meaning.** Including more zeros resolves finer primorial-template structure. The trade-off between resolution and smoothness is the trade-off between local escape-position accuracy and large-scale density prediction.

---

## 6. Summary

| Concept | Classical | FS-Geometry |
|---------|-----------|-------------|
| psi(x) | sum of Lambda(n) for n <= x | Cumulative structural impulse train |
| Lambda(n) = log(p) at p^k | von Mangoldt weight | Log-height of escape or activation column |
| Main term x | Smooth approximation | Conservation law: structural weight accumulates at unit rate |
| Oscillatory sum -sum x^{rho}/rho | Zero contributions | Resonant modes of the primorial template |
| Individual zero rho | Analytic object | One oscillatory mode of the escape pattern |
| Im(rho) = frequency | Oscillation rate | Template modulation frequency |
| Re(rho) = damping | Amplitude envelope | Decay rate of the resonance (RH: all at sqrt(x)) |
| -log(2*pi) | Constant | Normalization offset between continuous and discrete |
| Trivial zeros | s = -2, -4, ... | Ultraviolet template structure (negligible) |
| Truncation at T zeros | Approximation | Coarse-graining the primorial template |
| N(T) ~ T*log(T) | Zero count | Resonance density of coverage architecture |
| Escape-activation balance | theta-x + (psi-theta) = psi-x | Negative escape bias nearly canceled by positive activation weight |
| Completeness | Explicit formula | Zeros + conservation law = full escape pattern |

The explicit formula is the statement that the Factor Skyline's escape pattern is completely characterized by a smooth conservation law and a discrete spectrum of oscillatory resonances. The conservation law says escape height accumulates at unit rate. The resonances say how the actual escape positions deviate from this smooth prediction. Together, they reconstruct the full impulse train of primes and prime powers -- the complete structural event sequence of the Factor Skyline.
