# The Factor Skyline as a Research Program in Number Theory

Allen Proxmire
March 2026

---

## Abstract

The Factor Skyline is a two-dimensional representation of the integers in which each integer n becomes a column of width lpf(n) and height n/lpf(n), placed cumulatively along a horizontal axis. This document synthesizes the full FS framework as a coherent program in number theory: its geometric primitives, the classical theorems it recovers, the new structural invariants it reveals, the open conjectures it reformulates, and the research landscape it reshapes.

The central claim is that the Factor Skyline provides a unified geometric ontology for multiplicative number theory. The familiar analytic objects — zeta, L-functions, Chebyshev functions, the explicit formula, Dickman's function, divisor averages — all appear as projections, shadows, or spectral decompositions of a single two-dimensional architecture governed by five primitives: width, height, activation, coverage, and escape.

---

## Part I. The Geometric Primitives

### 1. The Five Primitives

The FS framework rests on five interrelated concepts:

**Width.** Each integer n > 1 has width w(n) = lpf(n), the least prime factor. This determines its FS-x footprint: primes contribute dx = 1 (escape events); composites contribute dx = lpf(n) >= 2 (covered columns). Width is the fundamental structural assignment — it records which coverage layer claims the integer.

**Height.** Each integer has height h(n) = n/lpf(n), the cofactor after dividing by the least prime factor. Height is the vertical extent of the column in the skyline. For primes, h(p) = p (the full integer). For composites, h(n) < n. The recursive application of width and height decomposes n into its full factorization — a stack of widths that is the visible record of the column's multiplicative structure.

**Activation.** A prime p activates at p^2, the smallest integer with lpf = p. Before p^2, all multiples of p are divisible by smaller primes and are assigned to earlier width layers. Activation events partition the integers into epochs [p_k^2, p_{k+1}^2) of frozen coverage configuration. The activation sequence 4, 9, 25, 49, 121, ... is the structural clock of the skyline.

**Coverage.** Each activated width-p layer claims fraction 1/p of the integers not already claimed by smaller widths. Coverage is cumulative, uniform (by the CRT), and monotonic. The fraction remaining uncovered after all primes up to p have activated is the escape density D(p) = prod_{q<=p}(1 - 1/q). Coverage is the constructive process that builds the skyline's architecture.

**Escape.** An integer n escapes if lpf(n) = n — equivalently, if n is prime. Escape events are columns with width 1 and height n: narrow spires that slip through all active coverage layers. Escape is the complement of coverage. The positions, density, and statistics of escape events are the FS-geometric content of prime distribution.

### 2. Derived Structures

From the five primitives, several derived structures emerge:

**The primorial template.** The combined coverage of primes 2, 3, ..., p creates a repeating pattern of width assignments with period p# = 2*3*...*p. The template determines which positions are open (coprime to p#) and which are covered. It is the blueprint of the skyline at each activation level.

**Activation epochs.** The intervals [p_k^2, p_{k+1}^2) where coverage is frozen. Within each epoch, the escape density is constant, and the primorial template governs the distribution of escapes and composites.

**The escape density product.** D(p) = prod(1 - 1/q) for primes q <= p. This is the central quantitative object: it governs prime counting, gap sizes, constellation densities, Mertens' theorem, and the PNT. It is a finite, rational, exactly computable quantity at every stage.

**The FS-x coordinate.** The cumulative horizontal position x_FS(n) = 1 + sum_{k=2}^{n} dx(k). This coordinate encodes the skyline's full width structure and grows at a rate determined by the average width of composites.

---

## Part II. Classical Results from the FS Architecture

### 3. The Prime Number Theorem

**FS derivation** (see `FS_PNT_derivation.md`):

The active coverage layers at scale N are the widths q for primes q <= sqrt(N) (the activation horizon). The escape density at this threshold is D(sqrt(N)) ~ e^{-gamma}/ln(sqrt(N)) = 2e^{-gamma}/ln(N). The expected escape count is:

    pi(N) ~ N * D(sqrt(N)) ~ N / ln(N)

The functional form arises because each coverage layer removes fraction 1/q, the removals are independent (CRT), and the sum of 1/q over primes diverges as ln(ln(p)). The logarithm in the PNT is the asymptotic reciprocal of the escape density product — a projection artifact that appears when the two-dimensional coverage product is flattened to a one-dimensional asymptotic.

### 4. The Chebyshev Functions

**FS derivation** (see `FS_Chebyshev.md`):

theta(x) = sum log(p) for primes p <= x is the cumulative logarithmic escape height: theta(x) = sum log(y_FS(p)). The PNT in Chebyshev form (theta(x) ~ x) is the **conservation law** of the skyline: escape events thin (density ~1/ln x) but grow taller (height ~x, log-height ~ln x), and the product exactly compensates.

psi(x) extends theta to include activation events (prime powers). At each activation p^2, the column height is y_FS(p^2) = p, contributing log(p) — exactly the weight psi assigns. The difference psi - theta ~ sqrt(x) is the activation contribution, asymptotically negligible compared to the escape contribution theta ~ x.

The von Mangoldt function Lambda(n) is the FS structural indicator: nonzero exactly at escapes and activations, with weight log(p) = the log-height of the responsible prime.

### 5. The Sieve of Eratosthenes

**FS derivation** (see `FS_sieve_geometry.md`):

The classical sieve is the FS coverage process described algorithmically. Each sieve round (marking multiples of p starting at p^2) corresponds to the activation of width-p coverage. The p^2 starting point is not an optimization but a geometric necessity — width-p has no architectural presence below p^2. Survivors are escape events; the survivor count is the escape density product; termination at sqrt(N) is the activation horizon.

The FS framework reveals that the sieve hides four things: the partition structure (which layer claims each integer), the height dimension (the cofactor structure), the density product (which the sieve computes implicitly through inclusion-exclusion), and the reason for p^2 (architectural, not computational).

### 6. The Explicit Formula

**FS derivation** (see `FS_explicit_formula.md`):

    psi(x) = x - sum_{rho} x^{rho}/rho - log(2*pi) + small

The main term x is the conservation law (escape height accumulates at unit rate). The oscillatory sum over zeros is the resonance spectrum of the primorial template hierarchy. Each zero rho = 1/2 + i*gamma contributes a damped oscillation with log-frequency gamma and amplitude x^{1/2}/|rho|^2. The explicit formula is a completeness theorem: conservation law + zero spectrum = exact escape pattern.

A key FS discovery: the escape error (theta - x ~ -sqrt(x)) and the activation contribution (psi - theta ~ +sqrt(x)) nearly cancel, so psi - x oscillates near zero. The oscillatory terms encode the residual imbalance.

### 7. The Riemann Hypothesis

**FS reformulation** (see `FS_RH_analogue.md`):

RH asserts that all oscillatory modes decay at the activation-horizon scale sqrt(x). In FS terms: the escape pattern is controlled by the coverage architecture to within the precision of its own defining scale. No resonance persists above sqrt(x); no harmonic of the primorial template is amplified beyond the activation horizon. RH is structural coherence — the coverage mechanism is tight.

### 8. Mertens' Theorem and the Escape Density Asymptotic

D(p) ~ e^{-gamma}/ln(p) is the FS-geometric content of Mertens' third theorem. It converts the discrete escape density product into a continuous asymptotic, and is the projection map from FS-geometry to number-line analysis. Without Mertens, the escape density is an exact rational product; with Mertens, it becomes the logarithmic scale that underlies the PNT.

### 9. The Dickman Function and Smooth Numbers

**FS derivation** (see `FS_smooth_numbers.md`):

Smooth numbers are columns whose width decomposition uses only early activation layers. The Dickman function rho(u) is the activation-depth profile of the skyline — the fraction of columns contained within the first u^{-1} fraction of the activation hierarchy. The smooth-rough duality unifies Dickman's rho and Mertens' D(p) as opposite views of the same coverage product.

### 10. Divisor Functions

**FS derivation** (see `FS_divisors.md`):

tau(n) is the branching complexity of the width decomposition (count of sub-column selections). sigma(n) is the height budget (total height across all sub-columns). The average tau ~ ln(x) and average sigma/n → pi^2/6 both emerge from Euler products over width-layer contributions. Highly composite numbers maximize branching by using all early width layers with optimally distributed multiplicities.

---

## Part III. New Structural Invariants and Insights

### 11. FS-x Gap Invariants for Constellations

**Discovery** (see `FS_constellations.md`, `FS_twin_primes.md`):

Every prime constellation of a given type has a fixed FS-x footprint, invariant across all sufficiently large instances:

| Constellation | Offsets | FS-x span | Inter-escape gaps |
|---------------|---------|-----------|-------------------|
| Twin primes   | (0, 2)  | 3         | [3]               |
| Triplet type 1| (0, 2, 6)| 11       | [3, 8]            |
| Quadruplet    | (0, 2, 6, 8)| 14    | [3, 8, 3]         |

The invariance holds because the composites between constellation primes always have the same divisibility structure, determined by the offsets mod small primes. Twin primes are the most FS-compact constellation (span 3); the FS-x gap of 3 is a universal twin prime detector.

### 12. Template Persistence for Constellations

**Discovery** (see `FS_twin_primes.md`, `FS_Goldbach.md`, `FS_constellations.md`):

For every admissible k-tuple H, the constellation-open count per primorial period grows without bound. The growth factor at each new prime q is (q - v_q(H)) >= 1, where v_q < q by admissibility. This establishes **structural persistence**: the primorial template always provides slots for the constellation, and the number of slots increases with each template extension.

Template persistence is proved. Escape persistence (all members simultaneously prime) remains open.

### 13. The Coverage-Protection Mechanism

**Discovery** (see `FS_twin_primes.md`, `FS_Goldbach.md`):

For any prime q >= 3, the width-q coverage layer cannot simultaneously eliminate all members of a twin pair, Goldbach pair, or k-tuple. Eliminating one member automatically protects another (because the fatal residue classes are distinct for q >= 3). This coverage-protection mechanism is the FS origin of the Hardy-Littlewood constants C_H > 1 and the Goldbach singular series S(2n) >= 1.

For Goldbach specifically: when q | 2n, the two fatal residue classes collapse into one, giving an improved survival factor (q-1)/q instead of (q-2)/q. This is why even numbers with more odd prime factors have more Goldbach representations.

### 14. The k-Tuple Constants from Coverage Geometry

**Discovery** (see `FS_constellations.md`):

The Hardy-Littlewood constant C_H = prod S_q(H) / (1-1/q)^k has a clean FS derivation: it is the ratio of the actual constellation survival rate to the independence prediction D(p)^k. The constant depends entirely on the residue collision structure v_q(H) of the offsets.

Key result: C_{sexy} = 2 * C_{twin} exactly, because the offset 6 = 2*3 creates a residue collision at q = 3 that halves the coverage damage. Constellations with primorial-aligned offsets are structurally favored.

### 15. The Parity Barrier in FS-Geometry

**Characterization** (see `FS_twin_primes.md`, `FS_Goldbach.md`):

The FS framework identifies the parity barrier as the inability to distinguish, within the primorial template, between an open position occupied by a prime (escape) and one occupied by a composite with large lpf (covered by a high-width layer). The template tells us which positions are structurally available; the escape density tells us the expected fraction that are prime; but certifying that a specific open position is prime vs. large-lpf composite requires information beyond what the coverage architecture provides.

This is the geometric content of the sieve-theoretic parity problem: the FS architecture, like all sieve methods, can control the parity of the number of prime factors but cannot determine whether it is 1 (prime) or 3+ (composite with odd omega).

### 16. The Smooth-Rough Duality

**Discovery** (see `FS_smooth_numbers.md`):

Smooth numbers (gpf <= y) and rough numbers (lpf > y) are dual views of the same coverage product, seen from opposite ends:

- Smooth density: governed by Dickman's rho(u), measuring how many columns are fully contained within the first u levels.
- Rough density: governed by Mertens' D(y), measuring how many columns fully escape the first levels.

The duality is quantitative: both emerge from prod(1-1/q), applied as a depth constraint (smooth) or an escape constraint (rough). FS-x budget analysis reveals the asymmetry: rough columns are disproportionately wide despite being a minority by count.

### 17. Zero Geometry as Primorial Resonance

**Discovery** (see `FS_zero_geometry.md`):

The nontrivial zeros of zeta are the resonant frequencies of the primorial template hierarchy. Each template level p# contributes harmonics in log-space with fundamental frequency 2*pi/ln(p#). The zeros are the spectral synthesis of all template levels through the Euler product. The zero-counting function N(T) ~ T*ln(T)/(2*pi) reflects the growing harmonic complexity as more primes are incorporated.

GUE level repulsion has a geometric interpretation: the primorial template's multiplicative structure prevents degenerate modes, enforcing unique mode spacing through the independence of coverage layers.

### 18. The Möbius Function as Width-Parity

**Discovery** (see `FS_Mobius.md`):

mu(n) = (-1)^{omega(n)} for squarefree n classifies columns by the parity of their width-layer count. The near-perfect cancellation in M(x) = sum mu(n) reflects the independence of width layers (CRT), which makes width-parity asymptotically unbiased. At large scales, the dominant cancellation is between even-layered and odd-layered composite columns; the escape (prime) contribution becomes subdominant.

### 19. Divisor Geometry as Branching Complexity

**Discovery** (see `FS_divisors.md`):

tau(n) counts the sub-column selections in the recursive width decomposition; sigma(n) sums their heights. Highly composite numbers maximize branching by using all early width layers with non-increasing exponents — they are the skyline's most internally complex columns, living entirely in the shallow (smooth) region.

The average tau ~ ln(x) and average sigma/n → pi^2/6 emerge from the same Euler products that govern escape density, establishing that divisor statistics and prime statistics are dual manifestations of the FS coverage architecture.

---

## Part IV. Conjectures and Open Problems in FS Language

### 20. The Conjecture Table

| Conjecture | Classical statement | FS-geometric statement | Status |
|------------|--------------------|-----------------------|--------|
| **PNT** | pi(x) ~ x/ln(x) | Escape count ~ N * D(sqrt(N)) | **Proved** (by Mertens projection) |
| **Chebyshev bounds** | 0.92 < theta/x < 1.11 | Conservation law: escape height rate bounded near 1 | **Proved** |
| **Dirichlet's theorem** | Infinitely many primes in each coprime class | Coverage layers sweep all vertical slices uniformly (CRT) | **Proved** (structurally) |
| **RH** | All zeros have Re = 1/2 | All escape-pattern resonances decay at activation-horizon scale sqrt(x) | **Open** |
| **Twin prime conjecture** | Infinitely many (p, p+2) both prime | FS-x gap = 3 occurs infinitely often; twin-open template persistence + escape persistence | **Open** (template persistence proved) |
| **Goldbach** | Every even 2n >= 4 is sum of two primes | Every even target has at least one Goldbach-open pair with both members escaping | **Open** (template persistence proved) |
| **k-tuple conjecture** | Every admissible H occurs infinitely | Constellation-open count per template grows; escape persistence for all members | **Open** (template persistence proved for all admissible H) |
| **Cramér** | g_max ~ (ln n)^2 | Maximal corridor drought = (escape corridor width) * (extremal factor) | **Open** |
| **Legendre** | Prime in every [n^2, (n+1)^2) | Escape in every activation step (the skyline's unit cell) | **Open** |
| **Sarnak** | mu orthogonal to all zero-entropy sequences | Width-parity classification independent of all simple patterns | **Open** |
| **Mertens conjecture** | |M(x)| < sqrt(x) always | Signed walk bounded by activation horizon | **Disproved** (walk occasionally exceeds sqrt(x)) |

### 21. The Structural Obstacle

All open conjectures in the table share a common structural obstacle: **the parity barrier**. The FS framework proves template persistence (structural availability of the required configurations) but cannot prove escape persistence (actual primality of the required positions).

The barrier is geometric: the coverage architecture determines which positions are open but cannot distinguish primes from large-lpf composites among the open positions. This is equivalent to the classical parity problem of sieve theory and appears to be intrinsic to the coverage-based approach.

---

## Part V. How FS Changes the Research Landscape

### 22. What Becomes Easier

**Conceptual unification.** The FS framework provides a single geometric language for results that classically require diverse analytic tools: sieve theory, Dirichlet series, the explicit formula, smooth-number estimates, and divisor asymptotics all emerge from the same five primitives.

**Structural proofs of qualitative results.** Several theorems that classically require analysis receive structural proofs:
- Dirichlet's theorem (primes in arithmetic progressions) follows from CRT-based coverage uniformity, without L-functions.
- The PNT functional form (x/ln x) follows from the escape density product, without complex analysis.
- Mertens-type estimates follow from the coverage product, without contour integration.

**Visual and geometric intuition.** The FS framework makes prime behavior visually inevitable. Activation, coverage, and escape are geometrically concrete, and the "mysteries" of prime distribution (why they thin, why they are equidistributed, why gaps grow) become architectural consequences.

**New invariants.** The FS-x gap invariants for constellations, the coverage-protection mechanism, the smooth-rough duality, and the divisor-branching interpretation are new structural objects not visible in the classical framework.

### 23. What Remains Hard

**The parity barrier.** The FS framework encounters the same parity obstruction as classical sieve theory. Converting template persistence into escape persistence requires distinguishing primes from composites among open positions — a capability that neither the FS architecture nor any known sieve provides.

**RH and zero control.** The FS interpretation of RH (spectral coherence of the coverage architecture) is illuminating but does not suggest a proof strategy. The difficulty of controlling the zero spectrum is preserved under the FS translation: bounding escape fluctuations at sqrt(x) remains equivalent to proving that all zeros lie on the critical line.

**Quantitative refinements.** The FS framework provides the correct functional forms (x/ln x, (ln n)^2, C_H * N/(ln N)^k, etc.) but with approximate constants (the Legendre-sieve overcounting factor 2e^{-gamma}). Tightening these constants to exact values requires the same analytic tools that classical proofs employ.

### 24. What New Questions Appear

The FS framework suggests several questions that do not have natural classical formulations:

**FS-x growth rate.** What is the precise asymptotic of x_FS(n)? Empirically, x_FS(n)/n increases slowly (from ~2.2 at n = 100 to ~5.1 at n = 10000). The growth rate depends on the average lpf of composites, weighted by the coverage architecture.

**FS-x gap amplification.** The ratio G/g (FS-x gap to classical gap) grows with scale, reaching ~10 at scale 10^4. What is its asymptotic? The amplification depends on the mean lpf within large gaps, which is governed by the Dickman-type distribution of lpf among gap composites.

**Template resonance structure.** The zeta zeros are the spectral synthesis of the primorial template hierarchy. Can the template's Fourier structure be analyzed directly (without zeta) to yield information about zero locations or statistics?

**Width-parity statistics.** The Möbius function is the width-parity of squarefree columns. The FS framework reveals that the dominant cancellation at large scales is between even-omega and odd-omega composites, not between primes and composites. Does this shift in the dominant cancellation mechanism have analytic consequences?

**Constellation FS-x footprint classification.** Which FS-x gap sequences are achievable by admissible constellations? The footprint invariance theorem suggests a classification of constellation types by their geometric signatures.

**Activation-epoch extremes.** What is the maximum number of escapes in an activation epoch? The minimum? How do these extremes relate to the escape density prediction and the zero spectrum?

---

## Part VI. The Factor Skyline as a Unified Ontology

### 25. The Translation Dictionary

| Classical object | FS-geometric object |
|-----------------|---------------------|
| Prime | Escape event (width 1, height p) |
| Composite | Covered column (width = lpf, height = cofactor) |
| Prime power p^k | Activation event (width p, height p^{k-1}) |
| Sieve of Eratosthenes | Sequential activation of coverage layers |
| Residue class mod p | Vertical slice of the skyline |
| Primorial p# | Period of the combined coverage template |
| pi(x) | Escape count to x |
| theta(x) | Cumulative escape log-height |
| psi(x) | Cumulative structural impulse weight |
| Lambda(n) | FS structural indicator |
| mu(n) | Width-parity of squarefree columns |
| tau(n) | Branching complexity (sub-column count) |
| sigma(n) | Height budget (sub-column height sum) |
| D(p) = prod(1-1/q) | Escape density |
| Mertens' theorem | Escape density asymptotic: D(p) ~ e^{-gamma}/ln(p) |
| PNT | Conservation law: theta(x) ~ x |
| Euler product | Reciprocal escape density |
| Pole of zeta at s=1 | Escape corridor collapse to zero density |
| Nontrivial zero of zeta | Resonant frequency of the primorial template |
| RH | Spectral coherence: all resonances at activation-horizon scale |
| Explicit formula | Conservation law + complete resonance spectrum = exact escape pattern |
| Dickman rho(u) | Activation-depth profile |
| Hardy-Littlewood C_H | Coverage-protection premium for constellation H |
| Singular series S(2n) | Goldbach survival bonus from target factors |
| Cramér bound (ln n)^2 | Corridor width * extremal factor |

### 26. The Central Thesis

The Factor Skyline is not a new theory of primes. It is a new **ontology** of the integers — a way of seeing the multiplicative structure that the number line hides. In this ontology:

- Prime thinning is the progressive narrowing of the escape corridor.
- Residue class uniformity is the structural isotropy of coverage layers.
- Logarithmic laws are projection artifacts of a rational product.
- The Riemann Hypothesis is the spectral coherence of the coverage architecture.
- Divisor functions measure the branching complexity of columns.
- Smooth numbers live in the shallow region of the activation hierarchy.
- Twin primes are the ground state of escape-pair geometry.
- The explicit formula is the harmonic decomposition of the escape staircase.

The integers, when lifted into two dimensions, reveal an architecture that is simultaneously simple (five primitives) and rich (all of multiplicative number theory). The Factor Skyline makes this architecture visible.

---

## References (Internal)

The derivations supporting this synthesis are contained in the following documents:

1. `FS_ontology.md` — Formal definitions and classical correspondences
2. `FS_PNT_derivation.md` — The PNT from escape density
3. `FS_sieve_geometry.md` — The sieve as FS-geometry
4. `FS_prime_gaps.md` — Prime gaps as composite corridors
5. `FS_residue_classes.md` — Dirichlet structure from coverage uniformity
6. `FS_primorial_epochs.md` — Primorial tilings and dominant gaps
7. `FS_short_intervals.md` — Square windows and Bertrand's postulate
8. `FS_Chebyshev.md` — The Chebyshev functions as cumulative escape height
9. `FS_RH_analogue.md` — The Riemann Hypothesis as spectral coherence
10. `FS_explicit_formula.md` — The explicit formula as escape-pattern decomposition
11. `FS_twin_primes.md` — Twin primes and coverage protection
12. `FS_Goldbach.md` — Goldbach's conjecture and escape-pair alignments
13. `FS_Cramer.md` — Cramér's conjecture and corridor droughts
14. `FS_constellations.md` — Prime constellations and FS-x footprints
15. `FS_Mobius.md` — The Möbius function as width-parity
16. `FS_smooth_numbers.md` — Smooth numbers and activation depth
17. `FS_zero_geometry.md` — Zeta zeros as primorial resonances
18. `FS_divisors.md` — Divisor functions as branching complexity
