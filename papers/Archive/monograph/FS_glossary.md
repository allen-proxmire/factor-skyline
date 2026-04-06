# Glossary of Core Terms

---

## I. Architectural Terms

**Activation.**
The entry of a new width layer into the skyline geometry; prime p activates at the integer p², the smallest integer with lpf(n) = p.
*Introduced in Part I, Ch. 1 (Definition I.5).*
Cross-references: *Epoch, Coverage, Escape density, Activation horizon.*

**Activation horizon.**
The largest prime whose coverage layer is active at scale N, equal to the largest prime p ≤ √N; equivalently, the threshold below which all composites n ≤ N have their least prime factor.
*Introduced in Part I, Ch. 4 (Theorem I.12).*
Cross-references: *Activation, Escape density, Square window, Geometric PNT.*

**Column.**
The recursive width decomposition of an integer n: the ordered sequence W(n) = (lpf(n), lpf(n/lpf(n)), ..., 1) of widths obtained by iterating the lpf function, terminating at 1.
*Introduced in Part I, Ch. 1 (Definition I.4).*
Cross-references: *Width, Height, Branching complexity, Divisor functions.*

**Coverage.**
The cumulative process by which activated width layers claim integers; width-p claims every integer with lpf(n) = p, removing fraction 1/p of the integers not already claimed by smaller widths.
*Introduced in Part I, Ch. 1 (Definition I.7).*
Cross-references: *Activation, Escape, Escape density, Template.*

**Epoch.**
An activation epoch is the interval [p_k², p_{k+1}²) between consecutive prime-square activations; within each epoch the set of active coverage layers is frozen and the escape density is constant.
*Introduced in Part I, Ch. 1 (Definition I.6).*
Cross-references: *Activation, Escape density, Template, Square window.*

**Escape.**
An integer n escapes if lpf(n) = n, i.e., n is prime; in the skyline, escape events are columns with dx = 1 and y_FS = n (narrow spires).
*Introduced in Part I, Ch. 1 (Definition I.8).*
Cross-references: *Coverage, Escape density, Width, Sub-Poisson.*

**Escape density.**
The fraction of integers that escape all coverage layers activated by primes up to p, given by the product D(p) = ∏_{q ≤ p, q prime}(1 − 1/q); the central quantitative object of the FS framework.
*Introduced in Part I, Ch. 1 (Definition I.7).*
Cross-references: *Coverage, Geometric PNT, Renormalization flow, Mertens' theorem.*

**FS-x footprint.**
The invariant sequence of FS-x inter-escape gaps between consecutive members of a prime constellation; for example, every twin prime pair (p, p+2) with p ≥ 5 has FS-x footprint [3].
*Introduced in Part I, Ch. 3 (Theorem I.11).*
Cross-references: *Constellation, Template persistence, Admissibility, Width.*

**Height.**
The vertical extent of an integer's column in the skyline: h(n) = n/lpf(n) for composites, h(p) = p for primes.
*Introduced in Part I, Ch. 1 (Definition I.2).*
Cross-references: *Width, Column, Conservation law, Chebyshev functions.*

**Template.**
The primorial template T_p is the periodic function with period p# = 2·3·...·p that classifies each residue class as open (coprime to p#) or covered (sharing a factor with p#); the deterministic blueprint of the skyline at each activation level.
*Introduced in Part I, Ch. 2 (Definition I.9).*
Cross-references: *Primorial, Epoch, Template persistence, Coverage.*

**Template persistence.**
The property that the number of constellation-open positions per primorial period grows without bound for every admissible k-tuple H; established by the growth factor (p_{k+1} − v_{p_{k+1}}) ≥ 1 at each template extension.
*Introduced in Part I, Ch. 3 (Theorem I.10).*
Cross-references: *Admissibility, Survival factor, k-tuple constant, Parity barrier.*

**Width.**
The horizontal extent of an integer's column in the skyline: w(n) = lpf(n), the least prime factor; primes have width 1, composites have width ≥ 2.
*Introduced in Part I, Ch. 1 (Definition I.2).*
Cross-references: *Height, Column, Coverage, FS-x footprint.*

---

## II. Statistical Terms

**Admissibility.**
A k-tuple H = {h₁, ..., h_k} is admissible if for every prime q, the offsets occupy fewer than q distinct residue classes modulo q (v_q(H) < q); admissibility is the structural prerequisite for a constellation to occur infinitely often.
*Introduced in Part I, Ch. 3 (Definition I.11).*
Cross-references: *Survival factor, k-tuple constant, Template persistence, FS-x footprint.*

**Conservation law.**
The Chebyshev identity θ(x) = Σ_{p ≤ x} ln p ∼ x, stating that cumulative logarithmic escape height accumulates at unit rate; escape events thin (~1/ln x density) but grow taller (height ~x), and the two effects exactly compensate.
*Introduced in Part I, Ch. 5 (Theorem I.21).*
Cross-references: *Escape, Height, Geometric PNT, Chebyshev functions.*

**Entropy budget.**
The decomposition of the FS-x increment sequence's total Shannon entropy (2.48 bits/int) into template information (1.70 bits, 68.5%) and escape + activation uncertainty (0.78 bits, 31.5%), with the escape layer alone carrying ~0.26 bits/int of irreducible uncertainty.
*Introduced in Part II, Ch. 8 (Theorem II.13).*
Cross-references: *Parity barrier, Sub-Poisson, Template, Incompressible core.*

**k-tuple constant.**
The Hardy-Littlewood constant C_H = ∏_q S_q(H)/(1−1/q)^k for an admissible k-tuple H; satisfies C_H > 1 for all admissible patterns, measuring the coverage-protection premium (how much more common the constellation is than the independence prediction D(p)^k).
*Introduced in Part I, Ch. 3 (Theorem I.9).*
Cross-references: *Survival factor, Admissibility, Coverage protection, Shared-layer decomposition.*

**Shared-layer / independent-layer decomposition.**
The master decomposition principle: for any offset h, each prime q is either shared (q | h, creating structured correlation) or independent (q ∤ h, contributing decorrelation by CRT); the balance between the two determines every arithmetic correlation function.
*Introduced in Part II, Ch. 6 (Theorem II.1).*
Cross-references: *CRT independence, k-tuple constant, Correlation hierarchy, Chowla mechanism.*

**Sub-Poisson.**
The property that the variance-to-mean ratio of prime counts in windows is strictly less than 1 (observed ~0.46), compared to 1.0 for a Poisson process; the suppression arises from the template's deterministic spacers between escape candidates.
*Introduced in Part II, Ch. 7 (Theorem II.9).*
Cross-references: *Template, Escape, Entropy budget, Randomness principle.*

**Survival factor.**
The fraction of constellation-open positions that survive the activation of width-q: S_q(H) = (q − v_q(H))/q, where v_q(H) is the number of distinct residue classes occupied by the offsets modulo q.
*Introduced in Part I, Ch. 3 (Theorem I.7).*
Cross-references: *Admissibility, k-tuple constant, Coverage protection, Template persistence.*

---

## III. Dynamical and Universal Terms

**Correlation hierarchy.**
The four-level ordering of arithmetic correlations: Level 1 (escape: prime pairs), Level 2 (parity: Möbius pairs), Level 3 (branching: divisor pairs), Level 4 (spectral: zero pairs); each level subsumes information from the previous through Dirichlet series.
*Introduced in Part II, Ch. 6 (Theorem II.7).*
Cross-references: *Shared-layer decomposition, Mixing dichotomy, CRT independence, Zero repulsion.*

**Mixing dichotomy.**
The structural phenomenon in which ω(n) is ergodic but not mixing (persistent positive correlations at all composite lags from shared rigid width-layer indicators), while μ(n) = (−1)^{ω(n)} is conjecturally mixing (the parity function destroys persistent correlations through independent sign flips).
*Introduced in Part II, Ch. 7 (Theorem II.12).*
Cross-references: *CRT independence, Chowla mechanism, Quasi-ergodicity, Correlation hierarchy.*

**Quasi-ergodicity.**
The dynamical character of the dx(n) sequence: 73.3% rigid (template-determined, periodic) and 26.7% mixing (escape-determined, ergodic); asymptotically rigid (D(p) → 0 shrinks the mixing fraction) but permanently ergodic (D(p) > 0 always).
*Introduced in Part III, Ch. 10 (Theorem III.9).*
Cross-references: *Template, Escape, Renormalization flow, Entropy–ergodicity correspondence.*

**Renormalization flow.**
The multiplicative renormalization group defined by template extension p_k# → p_{k+1}#, with escape density D(p) as the running coupling constant: D(p_{k+1}) = D(p_k) · (1 − 1/p_{k+1}); the flow is deterministic, irreversible, and monotonically decreasing toward the fixed point D = 0.
*Introduced in Part III, Ch. 11 (Theorem III.16).*
Cross-references: *Escape density, Template, Universality classes, Corridor collapse.*

**Triple correspondence.**
The alignment of entropy, ergodicity, and universality: zero-entropy components are rigid and universal; positive-entropy components are ergodic and system-specific; maximum-entropy components are GUE-mixing and universal (for Class I incommensurate systems).
*Introduced in Part III, Ch. 11 (Theorem III.17).*
Cross-references: *Entropy budget, Quasi-ergodicity, Universality classes, Renormalization flow.*

**Universality classes.**
The three classes of (A1)–(A4) systems determined by the asymptotic behavior of the escape density: Class I (logarithmic thinning, D ∼ C/ln x, e.g. ℤ), Class II (constant density, D → c > 0, e.g. 𝔽_q[x]), Class III (degenerate, rapid collapse, finitely many escapes).
*Introduced in Part III, Ch. 11 (Theorem III.11).*
Cross-references: *Escape density, Renormalization flow, Axioms (A1)–(A4), GUE statistics.*

---

## IV. Meta-Structural Terms

**Axioms (A1)–(A4).**
The four universality axioms defining the class of systems that produce a Factor Skyline: (A1) countable generators with unique factorization, (A2) activation at generator squares, (A3) CRT independence of generators, (A4) escape = complement of coverage.
*Introduced in Part III, Ch. 11.*
Cross-references: *Universality classes, Meta-axioms (M1)–(M3), T_FS, Universal parity barrier.*

**CRT independence.**
The Chinese Remainder Theorem guarantee that divisibility by distinct primes constitutes independent events; the single structural fact from which all FS correlations, randomness, entropy decompositions, and universality results derive.
*Introduced in Part I, Ch. 1 (Theorem I.2).*
Cross-references: *Shared-layer decomposition, Randomness principle, Entropy budget, Mixing dichotomy.*

**Emergence hierarchy.**
The four-level stratification of FS results: Primitive (lpf) → First-order (width, height, D(p), templates) → Second-order (PNT, Chebyshev, persistence, protection) → Third-order (explicit formula, zero spectrum, GUE); each level depends on the previous.
*Introduced in Part IV, Ch. 12 (Theorem IV.3).*
Cross-references: *lpf primitive, Meta-axioms (M1)–(M3), Computational hierarchy, Renormalization flow.*

**Incompressible core.**
The ~0.26 bits per integer of escape entropy that cannot be eliminated by template conditioning; the information-theoretic content of the parity barrier, representing the distinction between primes (ω = 1) and squarefree composites with odd ω ≥ 3 at template-open positions.
*Introduced in Part II, Ch. 8 / Part III, Ch. 9 (Theorem III.5).*
Cross-references: *Entropy budget, Parity barrier, Pseudo-randomness, Template.*

**lpf primitive.**
The least prime factor function lpf(n) = min{p : p | n, p prime}, the single function from which all five FS concepts (width, height, activation, coverage, escape) derive; the irreducible primitive of the entire framework.
*Introduced in Part IV, Ch. 12 (Theorem IV.1).*
Cross-references: *Meta-axioms (M1)–(M3), Width, Emergence hierarchy, Computability.*

**Meta-axioms (M1)–(M3).**
The three minimal structural requirements for the lpf function: (M1) a total order on generators, (M2) a multiplicative structure, (M3) unique factorization; none can be dropped without destroying the framework.
*Introduced in Part IV, Ch. 12 (Theorem IV.2).*
Cross-references: *lpf primitive, Axioms (A1)–(A4), T_FS, Emergence hierarchy.*

**Parity barrier.**
The fundamental limitation of the coverage-based approach: the architecture determines which template positions are open but cannot distinguish primes (ω = 1) from squarefree composites with odd ω ≥ 3 among those open positions; measured as ~0.26 bits/int of irreducible entropy; methodological (not Gödelian), universal across all (A1)–(A4) systems.
*Introduced in Part I, Ch. 10 (Discussion) / Part III, Ch. 9 (Theorem III.5) / Part IV, Ch. 13 (Theorem IV.5).*
Cross-references: *Incompressible core, Template persistence, Entropy budget, Boundary characterization.*

**Pseudo-randomness.**
The property of the escape layer having low Kolmogorov complexity (K = O(log N), generated by a short sieve program) but high Shannon entropy (H ∼ 0.26N bits, statistically indistinguishable from filtered-Bernoulli); the gap K ≪ H is the hallmark of deterministic sequences that appear random.
*Introduced in Part IV, Ch. 13 (Theorem IV.4).*
Cross-references: *Incompressible core, CRT independence, Randomness principle, Sub-Poisson.*

**T_FS.**
The first-order theory defined by axioms (A1)–(A4) in the language of ordered multiplicative structures; has multiple non-isomorphic models (ℤ, ℤ[i], 𝔽_q[x], abstract monoids) and is therefore incomplete; a result is universal if and only if it is provable from T_FS.
*Introduced in Part IV, Ch. 13 (Theorems IV.7–IV.8).*
Cross-references: *Axioms (A1)–(A4), Universality classes, Meta-axioms (M1)–(M3), Parity barrier.*
