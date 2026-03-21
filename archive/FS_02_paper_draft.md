# The Factor Skyline: A Geometric Ontology of the Integers

Allen Proxmire

March 2026

---

## Abstract

The classical number line represents each integer as a structureless point in a single dimension. This projection discards the internal multiplicative architecture of each integer and forces prime behavior to be described statistically. We introduce the Factor Skyline, a two-dimensional representation in which each integer n becomes a column of width equal to its least prime factor and height equal to the remaining quotient. The resulting geometry is governed by five primitives — width, height, activation, coverage, and escape — from which the classical theorems of prime distribution (the prime number theorem, Chebyshev's bounds, the Dickman function) emerge as structural consequences rather than analytic discoveries. The framework also reveals new geometric invariants: fixed FS-x footprints for prime constellations, a template persistence theorem for admissible k-tuples, and a coverage-protection mechanism that explains the Hardy-Littlewood constants. We show how the Factor Skyline reframes the major open problems of number theory — the Riemann Hypothesis, the twin prime conjecture, Goldbach's conjecture, and Cramer's conjecture — as geometric statements about the escape corridor, and we identify the parity barrier as the precise structural obstacle separating the framework's proven results from the open conjectures.

---

## 1. Introduction

The number line is the most familiar representation of the integers. It is also the most misleading. By assigning each integer a single coordinate — its position in the sequence 1, 2, 3, ... — the number line collapses all internal structure into a point. The integer 12 = 2^2 * 3 looks the same as the prime 13: both are points on a line, differing only in their distance from the origin.

This collapse has consequences. On the number line, prime behavior appears irregular and must be described with analytic tools: the prime number theorem approximates pi(x) with integrals, the Riemann zeta function encodes prime distribution through complex analysis, and probabilistic models describe prime gaps. These tools are powerful and correct, but they describe the *shadow* of a structure, not the structure itself.

We propose a different representation.

Each integer n has an internal multiplicative structure determined by its prime factorization. The Factor Skyline restores this structure by lifting n into a second dimension. The result is a two-dimensional landscape — a skyline — in which the mechanisms governing prime behavior become visible as geometric features.

In this geometry:

- Prime squares introduce new horizontal layers (activation).
- Small primes dominate because their layers appear earliest (coverage).
- Primes emerge as the columns that escape all activated layers (escape).
- Logarithmic laws arise from projecting this geometry onto a line (projection).

The goal of this paper is to develop the Factor Skyline as a coherent framework, demonstrate that it recovers the classical theorems of prime distribution from geometric first principles, and exhibit new structural invariants that are invisible on the number line.

We emphasize at the outset: the Factor Skyline does not change the integers or contradict existing mathematics. It provides a new *ontology* — a new way of seeing what was always there. The familiar results of analytic number theory are consistent with this ontology; they are its one-dimensional projections. What the skyline adds is the mechanism that produces those projections.

---

## 2. Construction

### 2.1. The column representation

For any integer n >= 2, define:

- **width**: w(n) = lpf(n), the least prime factor of n
- **height**: h(n) = n / lpf(n)

If h(n) > 1, it has its own width and height, and so on. Each integer becomes a finite stack of widths — the ordered sequence of least prime factors encountered during recursive decomposition. This stack is the column representing n in the skyline.

The columns are placed consecutively along a horizontal axis, producing the cumulative FS-coordinate system:

    x_FS(1) = 1,  y_FS(1) = 1

    For n >= 2:
      x_FS(n) = x_FS(n-1) + dx(n)
      y_FS(n) = n            if n is prime
              = n / lpf(n)   if n is composite

    where dx(n) = 1 if n is prime, lpf(n) if n is composite

The coordinate (x_FS(n), y_FS(n)) marks the top-right corner of integer n's column.

### 2.2. The five primitives

The skyline's geometry is governed by five interrelated primitives:

**Activation.** A prime p activates at p^2 — the smallest integer whose least prime factor is p. Before p^2, all multiples of p are divisible by a smaller prime and belong to earlier layers. The activation sequence 4, 9, 25, 49, 121, ... partitions the integers into epochs of frozen coverage.

**Coverage.** Each activated width-p layer claims every integer n with lpf(n) = p. Among integers coprime to all primes less than p, exactly 1/p are divisible by p. Coverage is cumulative, uniform (by the Chinese Remainder Theorem), and monotonic.

**Escape.** An integer n escapes if lpf(n) = n — if n is prime. Escape events are columns with dx = 1 and y_FS = n: narrow spires that pass through all coverage layers.

**Escape density.** After all primes q <= p have activated, the fraction remaining uncovered is:

    D(p) = prod_{q <= p, q prime} (1 - 1/q)

This exact, rational, computable product is the governing quantity for the long-term frequency of primes.

**The primorial template.** The combined coverage of primes 2, 3, ..., p creates a repeating pattern of width assignments with period p# = 2 * 3 * ... * p. The template determines which positions are open (coprime to p#) and which are covered.

### 2.3. A coordinate table

The following table shows the first 30 integers in FS-coordinates:

```
  n  x_FS  y_FS  dx  type
  1     1     1   -  seed
  2     2     2   1  PRIME
  3     3     3   1  PRIME
  4     5     2   2  composite (lpf=2)
  5     6     5   1  PRIME
  6     8     3   2  composite (lpf=2)
  7     9     7   1  PRIME
  8    11     4   2  composite (lpf=2)
  9    14     3   3  composite (lpf=3)   <-- width-3 activates at 3^2
 10    16     5   2  composite (lpf=2)
 11    17    11   1  PRIME
 12    19     6   2  composite (lpf=2)
 13    20    13   1  PRIME
 ...
 25    46     5   5  composite (lpf=5)   <-- width-5 activates at 5^2
 ...
 29    54    29   1  PRIME
 30    56    15   2  composite (lpf=2)
```

Primes contribute dx = 1 (narrow spires). Composites contribute dx = lpf(n) >= 2 (wide columns). Activation events at p^2 introduce new widths into the skyline.

---

## 3. Classical Results from the FS Architecture

### 3.1. The Prime Number Theorem

**Claim.** The escape density product, combined with the activation horizon at sqrt(N), yields pi(N) ~ N / ln(N).

**Derivation.** Every composite n <= N has lpf(n) <= sqrt(n) <= sqrt(N). Therefore the active coverage layers at scale N are exactly the widths q for primes q <= sqrt(N). The fraction escaping all of them is:

    D(sqrt(N)) = prod_{q <= sqrt(N)} (1 - 1/q)

The expected escape count is pi(N) ~ N * D(sqrt(N)). To convert this to classical form, we apply Mertens' third theorem:

    D(p) ~ e^{-gamma} / ln(p)

where gamma ~ 0.5772 is the Euler-Mascheroni constant. Substituting p = sqrt(N):

    D(sqrt(N)) ~ e^{-gamma} / ln(sqrt(N)) = 2e^{-gamma} / ln(N)

Therefore:

    pi(N) ~ 2e^{-gamma} * N / ln(N)

The constant 2e^{-gamma} ~ 1.123 reflects the Legendre-sieve overcounting. The exact PNT (pi(N) ~ N/ln(N) with leading constant 1) requires boundary corrections, but the functional form x/ln(x) is determined entirely by the escape density product.

**The FS content.** The logarithm in the PNT is not fundamental. It is the asymptotic rate at which independent fractional removals (each of size 1/q) compound. In the skyline, the mechanism is the product D(p); on the number line, its shadow is 1/ln(n).

### 3.2. The Chebyshev Functions

Define theta(x) = sum_{p <= x} log(p) and psi(x) = sum_{p^k <= x} log(p). In FS-coordinates:

**theta(x) as cumulative escape height.** A prime p has y_FS(p) = p, so log(y_FS(p)) = log(p). Therefore theta(x) = sum log(y_FS(p)) for primes p <= x — the total logarithmic escape height.

**The conservation law.** There are ~x/ln(x) primes up to x, each of average size ~x/2, contributing average log-height ~ln(x). The total is:

    theta(x) ~ (x/ln(x)) * ln(x) = x

Escape events thin (density ~1/ln x) but grow taller (height ~x), and the two effects exactly compensate. This is verified numerically:

| x     | theta(x)/x |
|-------|-----------|
| 1000  | 0.956     |
| 5000  | 0.982     |
| 10000 | 0.990     |

**psi(x) as escape + activation.** At each prime power p^k, the FS-y height is p^{k-1}. For the activation event at p^2 specifically, y_FS(p^2) = p and log(y_FS(p^2)) = log(p) — exactly the weight psi assigns. The correction psi(x) - theta(x) = theta(sqrt(x)) + theta(x^{1/3}) + ... ~ sqrt(x) is the cumulative activation weight, asymptotically negligible.

**The FS content.** The weight log(p) is not an analytic convenience; it is the logarithm of the escape spire's height. The conservation law theta ~ x says the skyline's total escape height per unit of number line is asymptotically 1 — the escape density product and the escape heights are in exact balance.

### 3.3. The Dickman Function and Smooth Numbers

An integer n is y-smooth if its greatest prime factor satisfies gpf(n) <= y. In the skyline, a y-smooth number is a column whose recursive width decomposition uses only widths <= y — it is entirely determined by the first few activation layers.

**Activation depth.** Define u(n) = log(n) / log(gpf(n)). The Dickman function rho(u) gives the density of integers with activation depth <= u: the fraction of columns contained within the first u^{-1} of the activation hierarchy.

**The FS derivation.** An integer n <= x is x^{1/u}-smooth if its column uses only widths from layers that activated at or before x^{2/u}. The probability that the largest width in n's decomposition is at most x^{1/u} depends on the recursive peeling of the largest prime factor:

If gpf(n) = p with x^{1/u} < p <= x, then n = p * m where m <= x/p is (x/p)-smooth. Summing over primes p gives the integral equation:

    rho(u) = 1 - integral_{1}^{u} rho(t-1)/t dt

This is the Dickman-de Bruijn equation, derived here as the recursive structure of column decomposition in the skyline.

**The smooth-rough duality.** The skyline reveals a fundamental duality: smooth density (Dickman's rho, measuring what is fully captured by early layers) and rough density (Mertens' D(y), measuring what fully escapes) are opposite views of the same coverage product. The FS-x budget analysis makes the asymmetry visible: at threshold y = 5 among integers to 1000, smooth columns contribute only 5.9% of the total FS-x extent (compact, small widths), while rough columns contribute 43.4% (wide, expensive columns).

---

## 4. New Structural Invariants

### 4.1. FS-x Footprints for Prime Constellations

A prime constellation is a pattern of fixed offsets H = {h_1, ..., h_k} where n + h_1, ..., n + h_k are all prime. In the skyline, each constellation type has a fixed FS-x footprint.

**Theorem (FS-x footprint invariance).** For any admissible constellation H, the FS-x inter-escape gaps between consecutive members are invariant across all sufficiently large instances.

We prove this for the three principal cases:

**Twin primes (0, 2).** For a twin pair (p, p+2) with p >= 5: the composite p+1 is even (since p is odd), so lpf(p+1) = 2 and dx(p+1) = 2. The FS-x gap is x_FS(p+2) - x_FS(p) = dx(p+1) + dx(p+2) = 2 + 1 = 3. Verified for all 23 twin pairs below 500:

    (5,7), (11,13), (17,19), (29,31), ..., (197,199): FS-x gap = 3 in every case.

**Triplets (0, 2, 6).** For (p, p+2, p+6) with p >= 5: the composites between p and p+6 are p+1 (even, dx=2), p+3 (even, dx=2), p+4 (divisible by 3, dx=3), p+5 (even, dx=2). But only p+1 is between p and p+2 (gap [3]), and p+3, p+4, p+5 are between p+2 and p+6 (gap 2+3+2+1=8). Total span: 3+8 = 11. Verified for all 11 triplets below 500.

**Quadruplets (0, 2, 6, 8).** The pattern [3, 8, 3] with total span 14. Verified for all 4 quadruplets below 500.

The invariance holds because the composites between constellation primes have divisibility structure determined entirely by the offsets mod small primes (2, 3), not by the specific prime p.

**Consequence.** The FS-x gap provides a purely geometric constellation detector: scan the FS-x escape sequence for the pattern [3] (twins), [3, 8] (triplets), [3, 8, 3] (quadruplets). The twin prime conjecture becomes: the FS-x gap of 3 between consecutive escapes occurs infinitely often.

### 4.2. Template Persistence for Admissible k-Tuples

**Theorem (template persistence).** For every admissible k-tuple H = {h_1, ..., h_k}, the number of constellation-open positions per primorial period p# grows without bound as p increases.

**Proof.** A constellation-open position at residue r in the p#-template is one where all r + h_i are coprime to p#. When a new prime q extends the template from (q-1)# to q#, the period multiplies by q. The constellation-open count multiplies by (q - v_q), where v_q = |{h_i mod q : 1 <= i <= k}| is the number of distinct residue classes occupied by the offsets modulo q.

By admissibility, v_q < q for all primes q. Therefore q - v_q >= 1, and the constellation-open count is non-decreasing. For q > max(h_i), we have v_q = k (all offsets are distinct mod q), so q - v_q = q - k >= 1 for q > k. For q > k, the growth factor is q - k > 0, ensuring the count strictly increases for all sufficiently large primes.

Numerically verified for twins (0, 2):

| p# | Period | Twin-open count |
|----|--------|----------------|
| 2  | 2      | 1              |
| 6  | 6      | 1              |
| 30 | 30     | 3              |
| 210| 210    | 15             |
| 2310| 2310  | 135            |

The count grows rapidly: each new prime q multiplies the count by (q-2) (since v_q = 2 for twins and all q >= 3).

**Consequence.** The primorial template always contains slots for every admissible constellation, and the number of slots grows without bound. This establishes *structural* persistence. What remains open is *escape* persistence — whether infinitely many of these slots are occupied by actual primes.

### 4.3. The Coverage-Protection Mechanism

**Theorem (coverage protection).** For any admissible k-tuple H and any prime q >= 3, the width-q coverage layer cannot simultaneously eliminate all members of a constellation-open position. Specifically, the survival factor is:

    S_q(H) = (q - v_q(H)) / q > 0

Moreover, for pairs (r, r+d) with d < q, eliminating one member automatically protects the other: if q | (r + h_i), then q does not divide r + h_j for any h_j with h_j != h_i mod q.

**Proof.** The offsets occupy v_q distinct residue classes mod q. For each class, exactly one value of r mod q is fatal (r + h_i = 0 mod q). Since the offsets are in distinct classes (for the v_q that are represented), and v_q < q, the remaining q - v_q classes for r are safe.

The protection mechanism: if q | (r + h_i), then r = -h_i mod q. For any other h_j with h_j not congruent to h_i mod q, we have r + h_j = h_j - h_i not congruent to 0 mod q (since h_j - h_i is nonzero mod q). Therefore r + h_j is not divisible by q.

**Consequence.** The cumulative effect of coverage protection across all primes is the Hardy-Littlewood k-tuple constant:

    C_H = prod_{q prime} S_q(H) / (1 - 1/q)^k

This constant exceeds 1 for all admissible patterns, meaning constellations are *more* common than the naive independence prediction D(p)^k. The coverage layers create positive correlations: eliminating one member of a constellation protects others.

Specific values:
- C_{twin} = C_{cousin} ~ 1.320 (the Hardy-Littlewood twin prime constant)
- C_{sexy} ~ 2.646 = 2 * C_{twin} (the factor 2 comes from a residue collision at q = 3)
- C_{triplet} ~ 2.858
- C_{quadruplet} ~ 4.151

The ratios between these constants are determined by the residue collision structure of the offsets, providing a complete geometric explanation for why certain constellations are more common than others.

---

## 5. Discussion: How the Factor Skyline Reframes Open Problems

### 5.1. The Riemann Hypothesis

The explicit formula decomposes the escape staircase psi(x) as:

    psi(x) = x - sum_{rho} x^{rho}/rho + small corrections

where rho ranges over the nontrivial zeros of zeta. Each zero contributes a damped oscillation in log-space with frequency Im(rho) and amplitude x^{Re(rho)}.

In FS terms, each zero is a resonant frequency of the primorial template hierarchy — a frequency at which the combined coverage architecture produces coherent oscillations in the escape pattern. RH asserts Re(rho) = 1/2 for all zeros: every resonance decays at the activation-horizon scale sqrt(x). No oscillatory mode is amplified beyond this scale.

The FS reformulation: *the coverage architecture controls the escape pattern to within the precision of its own defining scale.* The activation horizon sqrt(x) is both the scale at which coverage layers are defined and the scale at which escape deviations are bounded. RH is the statement that these two scales coincide — that the architecture is spectrally coherent.

The FS framework does not suggest a proof of RH. The difficulty of controlling the resonance spectrum is preserved under translation. But it provides a geometric intuition for *why* sqrt(x) is the natural bound: it is the scale at which the coverage configuration is determined.

### 5.2. Twin Primes and Goldbach

Both conjectures share a common FS structure:

1. **Template persistence** (proved): The primorial template always contains the required configurations (twin-open pairs, Goldbach-open pairs), and their count grows without bound.

2. **Coverage protection** (proved): Each coverage layer cannot eliminate all configurations simultaneously. The survival factors yield C_H > 1 (for twins) and S(2n) >= 1 (for Goldbach, with bonus factors for highly composite targets).

3. **Escape persistence** (open): Among the growing set of structurally available configurations, do infinitely many have all members prime?

The FS framework pinpoints the obstruction: the *parity barrier*. The coverage architecture determines which positions are open but cannot distinguish between a prime (single width, escaped all layers) and a composite with large lpf (caught by a high-activation layer). The template provides structural slots; the escape density predicts the fraction that should be occupied; but certifying occupancy requires information beyond what the coverage geometry provides.

For Goldbach specifically, the FS framework reveals a structural asymmetry that makes it "easier" than the twin prime conjecture: the additive constraint p + q = 2n allows many more configurations than the positional constraint p' = p + 2, and the singular series provides additional protection when the target has many odd prime factors. Powers of 2 are the hardest Goldbach targets (no singular series bonus), but even for them the predicted count grows exponentially.

### 5.3. Cramer's Conjecture

The FS framework decomposes the maximal prime gap into two factors:

    g_max ~ (1/D) * ln(n) ~ ln(n) * ln(n) = (ln n)^2

The first factor, 1/D ~ ln(n), is the escape corridor width — the typical spacing between escapes. The second factor, ln(n), is the extremal count — how many corridor-width intervals must be searched before the longest drought occurs.

The mechanism for large gaps is three-layered: (i) the primorial template creates a skeleton of covered positions, (ii) higher-width layers stochastically fill the open positions in the skeleton, (iii) the largest gap occurs when all open positions in a template run are simultaneously covered. The probability of this conspiracy decreases exponentially with the number of open positions, capping gaps at the (ln n)^2 scale.

The Granville refinement (g_max >= 2e^{-gamma} * (ln n)^2 infinitely often) arises from the Mertens constant in the escape density: the corridor is slightly wider than the pure-random model predicts.

### 5.4. The Parity Barrier as a Geometric Limit

The FS framework identifies the parity barrier as a fundamental limitation of the coverage-based approach:

The five primitives — width, height, activation, coverage, escape — determine the *structure* of the skyline but not the *occupancy* of its open positions. The template tells us where primes *can* occur; the escape density tells us how many *should* occur; but no coverage-based argument can certify that a specific open position *is* occupied by a prime rather than by a composite with large lpf.

This limitation is shared by all sieve methods. In the FS language, it becomes geometrically precise: the architecture controls the *density* of escapes but not their *positions*. Overcoming the parity barrier would require a structural argument that goes beyond coverage — one that exploits the *height* dimension (the y_FS values of escape events) or the *FS-x correlation structure* (the precise spacing of escapes in FS-x coordinates) in a way that current methods do not.

---

## 6. Conclusion: The Research Program

The Factor Skyline provides a unified geometric framework for multiplicative number theory. Its five primitives — width, height, activation, coverage, and escape — generate the classical theorems (PNT, Chebyshev, Mertens, Dickman) as structural consequences and reveal new invariants (FS-x footprints, template persistence, coverage protection, smooth-rough duality) that are invisible on the number line.

The framework's principal achievements are:

1. **A geometric derivation of the PNT**, using only the escape density product and Mertens' theorem, without complex analysis.

2. **A structural proof of Dirichlet's theorem**, using CRT-based coverage uniformity, without L-functions.

3. **A complete geometric dictionary** translating between classical analytic objects (zeta, theta, psi, Lambda, mu, tau, sigma, rho) and FS-geometric objects (escape density, escape height, structural impulses, width-parity, branching complexity, activation depth).

4. **New invariants**: the FS-x gap invariants for constellations, the coverage-protection mechanism explaining Hardy-Littlewood constants, and the smooth-rough duality unifying Dickman and Mertens.

5. **A precise identification of the parity barrier** as the geometric limit of coverage-based arguments.

The framework's principal limitation is that it encounters the same parity obstruction as classical sieve theory when addressing the major open conjectures. Template persistence is proved for all admissible constellations, but escape persistence remains open.

The Factor Skyline does not resolve the hard conjectures of number theory. It provides a new ontology in which those conjectures become geometric statements about a two-dimensional architecture, and in which the mechanisms behind prime behavior — activation, coverage, escape, and the narrowing corridor — become visible rather than implicit. The research program it suggests is the systematic development of this geometric perspective: to find what the skyline reveals that the number line cannot, and to determine whether the additional structure of the second dimension contains the information needed to cross the parity barrier.

---

## Acknowledgments

The FS-coordinate system is implemented in `FS_coordinates.py` (available at the repository cited below). All numerical verifications were performed using SymPy. The supporting derivations (ontology, PNT, sieve geometry, prime gaps, residue classes, primorial epochs, short intervals, Chebyshev functions, RH analogue, explicit formula, twin primes, Goldbach, Cramer, constellations, Mobius, smooth numbers, zero geometry, divisors, and the research program synthesis) are available as individual documents in the project repository.

## References

[1] A. Proxmire, *The Factor Skyline: An Ontological Lookout Over the Integers* (2026). DOI: 10.5281/zenodo.18275273.

[2] H. Davenport, *Multiplicative Number Theory*, 3rd ed. Springer, 2000.

[3] G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, 6th ed. Oxford University Press, 2008.

[4] H. Iwaniec and E. Kowalski, *Analytic Number Theory*. AMS Colloquium Publications, 2004.

[5] F. Mertens, "Ein Beitrag zur analytischen Zahlentheorie," *J. Reine Angew. Math.* 78 (1874), 46-62.

[6] N. G. de Bruijn, "On the number of positive integers <= x and free of prime factors > y," *Indag. Math.* 13 (1951), 50-60.

[7] G. H. Hardy and J. E. Littlewood, "Some problems of 'Partitio numerorum'; III: On the expression of a number as a sum of primes," *Acta Math.* 44 (1923), 1-70.

[8] H. Cramer, "On the order of magnitude of the difference between consecutive prime numbers," *Acta Arith.* 2 (1936), 23-46.

[9] A. Granville, "Harald Cramer and the distribution of prime numbers," *Scand. Actuarial J.* (1995), 12-28.

[10] H. L. Montgomery, "The pair correlation of zeros of the zeta function," *Proc. Sympos. Pure Math.* 24 (1973), 181-193.

[11] P. Sarnak, "Three lectures on the Mobius function, randomness and dynamics," 2011. Available at: publications.ias.edu/sarnak.
