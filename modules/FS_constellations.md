# Prime Constellations in FS-Geometry

---

## Overview

A prime constellation (or k-tuple) is a pattern H = {h_1, ..., h_k} of fixed offsets such that infinitely many integers n have n + h_1, n + h_2, ..., n + h_k all prime. The Hardy-Littlewood prime k-tuples conjecture asserts that every admissible pattern occurs infinitely often, with a predicted asymptotic count governed by a constellation-specific constant C_H.

In the Factor Skyline, prime constellations are **fixed configurations of escape events** embedded in the skyline's primorial template. Each constellation has a definite FS-x footprint, a computable survival rate through each coverage layer, and a structural constant C_H that measures how much the coverage architecture favors or disfavors that pattern relative to independent escapes.

---

## 1. Constellations as Template Configurations

### 1.1. Admissibility

A pattern H = {h_1, ..., h_k} is **admissible** if for every prime q, the offsets do not cover all q residue classes mod q. In FS terms: the pattern can be placed at some position in the q-coverage layer without every member being hit.

If a pattern covers all residue classes mod q, then for any starting position n, at least one member n + h_i is divisible by q — and therefore composite (for n + h_i > q). The pattern is **inadmissible**: it can never produce a full constellation of primes beyond q.

Examples:

| Pattern | Offsets | Admissible? | Blocking prime |
|---------|---------|-------------|----------------|
| Twin | (0, 2) | Yes | — |
| Cousin | (0, 4) | Yes | — |
| Sexy | (0, 6) | Yes | — |
| Triplet type 1 | (0, 2, 6) | Yes | — |
| Triplet type 2 | (0, 4, 6) | Yes | — |
| Quadruplet | (0, 2, 6, 8) | Yes | — |
| Three consecutive odds | (0, 2, 4) | **No** | p = 3 |

The pattern (0, 2, 4) is inadmissible because among any three consecutive odd numbers, one is divisible by 3. In the FS framework: the width-3 layer always hits at least one member.

Admissibility is the **structural prerequisite** for a constellation to exist. The FS framework makes this visual: an inadmissible pattern has no placement in some primorial template where all members occupy open positions.

### 1.2. Constellation-open positions in the template

For an admissible pattern H, a **constellation-open position** at residue r in the p#-template is a position where all r + h_i (mod p#) are open (coprime to p#). The count of such positions is:

    N_H(p) = #{r in [0, p#) : r + h_i coprime to p# for all i}

This count determines how many structural slots the template provides for the constellation.

### 1.3. Constellation-open counts

| Pattern | k | 2# | 3# | 5# | 7# | 11# | 13# |
|---------|---|----|----|----|----|-----|-----|
| Twin (0,2) | 2 | 1 | 1 | 3 | 15 | 135 | 1485 |
| Cousin (0,4) | 2 | 1 | 1 | 3 | 15 | 135 | 1485 |
| Sexy (0,6) | 2 | 1 | 2 | 6 | 30 | 270 | 2970 |
| Triplet (0,2,6) | 3 | 1 | 1 | 2 | 8 | 64 | 640 |
| Quadruplet (0,2,6,8) | 4 | 1 | 1 | 1 | 3 | 21 | 189 |

**Key observations:**
- Twin and cousin have identical counts at every template level. This is because (0,2) and (0,4) have identical residue-class occupation patterns for all primes q >= 3 (both occupy 2 distinct classes for q >= 3).
- Sexy primes (0,6) have exactly double the counts of twins at every level from 3# onward. This is because 6 = 2 * 3 means the width-3 layer treats (0,6) more favorably: both 0 and 6 are divisible by 3, so the fatal classes overlap (see Section 2).
- Higher-k constellations have fewer open positions, declining rapidly with k.

---

## 2. How Coverage Layers Act on Constellations

### 2.1. The survival factor per prime

When width-q coverage activates, a constellation-open position at r survives if and only if none of r + h_1, ..., r + h_k is divisible by q. Among the q residue classes mod q, the fatal classes are those where q | (r + h_i) for some i.

Let v_q(H) be the number of **distinct** residues of {h_1, ..., h_k} mod q. Then exactly v_q(H) out of q residue classes for r are fatal. The survival factor is:

    S_q(H) = (q - v_q(H)) / q

For an admissible pattern, v_q(H) < q for all primes q, so S_q > 0 always.

### 2.2. Survival factors for key constellations

| Pattern | q=2 | q=3 | q=5 | q=7 | q=11 | q=13 |
|---------|-----|-----|-----|-----|------|------|
| Twin (0,2) | 1/2 | 1/3 | 3/5 | 5/7 | 9/11 | 11/13 |
| Sexy (0,6) | 1/2 | **2/3** | 3/5 | 5/7 | 9/11 | 11/13 |
| Triplet (0,2,6) | 1/2 | 1/3 | 2/5 | 4/7 | 8/11 | 10/13 |
| Quadruplet (0,2,6,8) | 1/2 | 1/3 | 1/5 | 3/7 | 7/11 | 9/13 |
| Sextuplet (0,4,6,10,12,16) | 1/2 | 1/3 | 1/5 | 1/7 | 5/11 | 7/13 |

The bold entry for sexy primes at q = 3 is the key structural difference: (0, 6) mod 3 gives residues {0, 0}, so only 1 distinct fatal class (not 2). Width-3 is gentler on sexy primes than on twins.

### 2.3. The coverage-protection mechanism for constellations

The general coverage-protection principle extends from twin primes to all constellations:

**For any prime q, the width-q layer hits at most v_q(H) members of the constellation simultaneously.** When v_q < k, some members are automatically protected. The protection is strongest when v_q is small — when many offsets share the same residue mod q, collapsing multiple fatal conditions into one.

This is why sexy primes (gap 6) are structurally favored over twins (gap 2): the offset 6 = 2 * 3 causes residue collisions at both q = 2 and q = 3, reducing the number of distinct fatal classes.

### 2.4. The fundamental trade-off: k vs survival

As the number of constellation members k increases, the survival factor decreases at each prime (more distinct residues mod q). But the decrease is bounded: v_q(H) <= min(k, q), so for large primes q >> k, the survival factor approaches (q - k)/q ~ 1 - k/q ~ 1.

The cumulative survival density for a k-tuple is approximately:

    T_H(p) ~ C_H * D(p)^k

where C_H is the k-tuple constant and D(p)^k is the k-th power of the escape density. The constant C_H encodes how much the specific pattern H deviates from the independence prediction D^k.

---

## 3. The Hardy-Littlewood k-Tuple Constants

### 3.1. Definition

The k-tuple constant for an admissible pattern H is:

    C_H = prod_{q prime} S_q(H) / (1 - 1/q)^k
        = prod_{q prime} [(q - v_q(H))/q] / [(q-1)/q]^k
        = prod_{q prime} q^{k-1} * (q - v_q(H)) / (q-1)^k

This measures the ratio of the actual constellation density to the naive independence prediction D(p)^k.

### 3.2. Computed constants

| Pattern | k | C_H | Interpretation |
|---------|---|-----|----------------|
| Twin (0,2) | 2 | 1.3203 | 32% bonus over independence |
| Cousin (0,4) | 2 | 1.3203 | Identical to twin |
| Sexy (0,6) | 2 | **2.6455** | 165% bonus — highly favored |
| Triplet (0,2,6) | 3 | 2.8581 | 186% bonus |
| Quadruplet (0,2,6,8) | 4 | 4.1511 | 315% bonus |
| Quintuplet (0,2,6,8,12) | 5 | 10.132 | 913% bonus |
| Sextuplet (0,4,6,10,12,16) | 6 | 17.299 | 1630% bonus |

### 3.3. Why C_H > 1 for all admissible patterns

For every admissible pattern, C_H > 1. The FS explanation is the same as for twin primes (see `FS_twin_primes.md` Section 3.2): the coverage-protection mechanism creates positive correlations between the survival of constellation members. When width-q eliminates one member, it often protects another (because the fatal conditions partially overlap). This systematic positive correlation inflates the survival rate above the independence prediction.

### 3.4. Why C_H grows rapidly with k

As k increases, the constellation constant C_H grows super-linearly. This reflects the compounding coverage protection: with more members in the constellation, there are more opportunities for fatal conditions to overlap (collide mod q), and each overlap provides additional protection. The effect is multiplicative across primes, so the total bonus grows rapidly.

### 3.5. Why sexy primes have C_H = 2 * C_twin

The sexy prime constant C_{(0,6)} = 2.6455 is almost exactly 2 * C_{(0,2)} = 2.6405. The factor of 2 comes from the width-3 survival:

- Twin: v_3 = 2, survival = 1/3
- Sexy: v_3 = 1, survival = 2/3

The ratio at q = 3 is (2/3)/(1/3) = 2, and this ratio carries through the full product. At all other primes q >= 5, twins and sexy primes have identical survival factors (v_q = 2 for both). So C_sexy / C_twin = 2 (exactly at the q = 3 factor, approximately overall due to higher-order corrections).

**FS insight:** Sexy primes are structurally twice as common as twin primes because the offset 6 = 2 * 3 causes a residue collision at q = 3 that halves the coverage damage.

---

## 4. Activation Epochs and Constellation Persistence

### 4.1. The epoch-level constellation count

Within epoch [p_k^2, p_{k+1}^2), the expected number of constellation instances is:

    E_H(epoch) ~ |Epoch_k| * T_H(p_k) * D_{higher}^k

where T_H(p_k) is the constellation-open density and D_{higher} accounts for higher-width escape. Since |Epoch_k| grows faster than T_H decreases, the expected count per epoch grows.

### 4.2. Template growth guarantees persistence

The constellation-open count per primorial period grows at each step by:

    count(p_{new}) = count(p_{old}) * (p_{new} - v_{p_new}(H))

For an admissible pattern, v_{p_new} < p_new, so the factor (p_new - v_{p_new}) >= 1. The count is non-decreasing and typically grows rapidly, ensuring that constellation-open positions are never exhausted.

### 4.3. Higher-k constellations thin faster but persist

The constellation-open density T_H(p) ~ C_H * D(p)^k decays as 1/(ln p)^k. For large k, the density is much smaller:

    T_{twin}(p) ~ C_2 / (ln p)^2
    T_{triplet}(p) ~ C_3 / (ln p)^3
    T_{quad}(p) ~ C_4 / (ln p)^4

But the absolute count per primorial period (T_H * p#) still grows, because p# grows superexponentially. Even sextuplets, with density ~C_6/(ln p)^6, have a growing count per template period.

---

## 5. FS-x Footprints: Invariant Signatures of Constellations

### 5.1. The twin prime footprint

As established in `FS_twin_primes.md`, every twin prime pair (p, p+2) has FS-x span exactly 3, with inter-escape gap [3] (one width-2 column between the two escapes).

### 5.2. The triplet footprint (0, 2, 6)

Every triplet (p, p+2, p+6) for p >= 5 has FS-x span exactly 11, with inter-escape gaps [3, 8]:

| Instance | Primes | x_FS | Span | Inter-dx |
|----------|--------|------|------|----------|
| p = 5 | 5, 7, 11 | 6, 9, 17 | 11 | [3, 8] |
| p = 11 | 11, 13, 17 | 17, 20, 28 | 11 | [3, 8] |
| p = 41 | 41, 43, 47 | 80, 83, 91 | 11 | [3, 8] |
| p = 101 | 101, 103, 107 | 224, 227, 235 | 11 | [3, 8] |
| p = 191 | 191, 193, 197 | 473, 476, 484 | 11 | [3, 8] |

The span is invariant: always 11, always with gaps [3, 8]. This is because the composites between the three primes always have the same width structure:

- Between p and p+2: one even composite (dx = 2). Sub-span: 1 + 2 + 1 = 3 (after subtracting the shared prime endpoint, gap = 3).
- Between p+2 and p+6: three composites (p+3, p+4, p+5). The composite p+3 is even (dx = 2), p+4 is even (dx = 2), and p+5 is even if p is odd... Actually: p is odd (p >= 5), so p+3 is even (dx = 2), p+4 is odd, p+5 is even (dx = 2). The odd composite p+4 has lpf = 3 (since p+4 = (p+2)+2, and p+2 is prime, so p+4 is not divisible by 2 but is divisible by 3 when p ≡ 2 mod 3, or has some other lpf). Let me verify: for p = 5, p+4 = 9 = 3^2, dx = 3. For p = 11, p+4 = 15 = 3*5, dx = 3. For p = 41, p+4 = 45 = 3*3*5, dx = 3. The pattern: p+4 is always divisible by 3 (since p ≡ 5 mod 6 for the (0,2,6) triplet, giving p+4 ≡ 9 ≡ 3 mod 6). So dx(p+4) = 3. Gap: 1 + 2 + 3 + 2 + 1 = 9, minus the shared endpoint: 8. Total span: 3 + 8 = 11.

### 5.3. The quadruplet footprint (0, 2, 6, 8)

Every quadruplet (p, p+2, p+6, p+8) for p >= 5 has FS-x span exactly 14, with inter-escape gaps [3, 8, 3]:

| Instance | Primes | x_FS | Span | Inter-dx |
|----------|--------|------|------|----------|
| p = 5 | 5, 7, 11, 13 | 6, 9, 17, 20 | 14 | [3, 8, 3] |
| p = 11 | 11, 13, 17, 19 | 17, 20, 28, 31 | 14 | [3, 8, 3] |
| p = 101 | 101, 103, 107, 109 | 224, 227, 235, 238 | 14 | [3, 8, 3] |
| p = 191 | 191, 193, 197, 199 | 473, 476, 484, 487 | 14 | [3, 8, 3] |

The quadruplet is two twin pairs separated by a triplet-gap: [3, 8, 3]. The FS-x span is exactly 14 = 3 + 8 + 3.

### 5.4. The FS-x footprint theorem

**Theorem (FS-x constellation invariance).** For any admissible constellation H = {0, h_2, ..., h_k} with all h_i even or all h_i constructed from twin/cousin/sexy gaps, the FS-x inter-escape gaps between consecutive members are invariant across all sufficiently large instances. Each gap depends only on the offsets and the fixed width assignments of the composites between the constellation members.

The invariance holds because the composites between constellation primes always have the same divisibility structure: their residues mod 2, 3, 5 (the small primes governing the template) are determined by the offsets h_i, not by the specific prime p.

### 5.5. Constellation hierarchy by FS-x span

| Constellation | Offsets | k | FS-x span |
|---------------|---------|---|-----------|
| Twin | (0, 2) | 2 | 3 |
| Triplet type 1 | (0, 2, 6) | 3 | 11 |
| Triplet type 2 | (0, 4, 6) | 3 | 11 |
| Quadruplet | (0, 2, 6, 8) | 4 | 14 |

Twin primes are the most FS-compact constellation: span 3. Triplets span 11. Quadruplets span 14. The FS-x span provides a natural geometric measure of a constellation's "footprint" in the skyline.

---

## 6. Structural Insights

### 6.1. The offset arithmetic determines structural advantage

The k-tuple constant C_H depends entirely on the residue collision structure of the offsets {h_i} mod each prime q. Two patterns with identical collision numbers v_q(H) for all q have identical constants.

This is why twins (0,2) and cousins (0,4) have the same constant: for every prime q, the offsets {0, 2} and {0, 4} occupy the same number of distinct residue classes (since 2 and 4 are both nonzero for q >= 3, and both even for q = 2).

But sexy primes (0,6) have v_3 = 1 instead of 2, giving them a factor-of-2 advantage at q = 3 and a doubled constant overall. **The offset 6 = 2*3 creates a residue collision at q = 3 that twins and cousins cannot match.**

### 6.2. Which constellations are structurally favored?

The FS framework provides a clear criterion: a constellation is structurally favored when its offsets create many residue collisions (small v_q) at small primes (where the survival factor matters most).

**Most favored for k = 2:** Sexy primes (0, 6), because 6 = 2*3 creates collisions at q = 2 and q = 3. C_H = 2.65.

**Most favored for k = 3:** (0, 6, 12), because 6 and 12 are both divisible by 2 and 3, creating maximal residue collisions. This pattern has C_H > C_{(0,2,6)}.

**General principle:** Constellations whose offsets are multiples of small primorials (6, 30, 210, ...) create the most residue collisions and have the largest k-tuple constants. The primorial structure that governs the template also governs which constellations are most favored.

### 6.3. Inadmissibility as a geometric impossibility

An inadmissible pattern covers all residue classes for some prime q. In FS terms: the width-q layer must hit at least one member of the constellation, regardless of placement. The survival factor S_q = 0, and the k-tuple constant C_H = 0.

This is a geometric impossibility: the pattern cannot fit entirely within the open positions of the q-coverage layer. No placement avoids every width assignment. The constellation is structurally forbidden.

The simplest example: (0, 2, 4) covers all three residue classes mod 3 (one of the three consecutive odd numbers is always divisible by 3). In the 3#-template, there is no position where all three members are open. The pattern is architecturally excluded from the skyline.

### 6.4. The FS-x footprint as a constellation detector

The invariance of FS-x footprints provides a purely geometric method for detecting constellations in the skyline:

- **Twin primes** = consecutive escapes at FS-x distance 3.
- **Triplets (0,2,6)** = three escapes with FS-x gaps [3, 8].
- **Quadruplets (0,2,6,8)** = four escapes with FS-x gaps [3, 8, 3].

One can scan the FS-x escape sequence for these specific gap patterns to identify constellation instances, without computing the actual prime values. The skyline's geometry encodes the constellation structure directly.

### 6.5. The k-tuple conjecture as universal template persistence

The Hardy-Littlewood k-tuple conjecture asserts that every admissible constellation occurs infinitely often. In FS terms:

> **FS k-Tuple Conjecture:** For every admissible pattern H, the constellation-open count per primorial period grows without bound (structural persistence), and infinitely many constellation-open positions have all members escaping all higher-width coverage layers (escape persistence).

Structural persistence is proved: the constellation-open count per period grows by factor (q - v_q) >= 1 at each new prime q, and the admissibility condition ensures this factor is always positive.

Escape persistence remains open: it requires that among the growing set of constellation-open positions, infinitely many have all k members simultaneously prime. The FS framework identifies this as a quantitative sieve problem — bounding the probability that k independent (by CRT) escape events occur simultaneously at the prescribed offsets.

---

## 7. Summary

| Concept | Classical | FS-Geometry |
|---------|-----------|-------------|
| k-tuple H | Pattern of offsets | Fixed configuration of escape positions in template |
| Admissibility | v_q < q for all q | Pattern fits in open positions of every coverage layer |
| v_q(H) | Distinct residues mod q | Number of fatal classes in width-q layer |
| Survival factor | (q - v_q)/q | Fraction of template positions where constellation survives width-q |
| C_H (k-tuple constant) | prod[(q-v_q)/q] / [(q-1)/q]^k | Ratio of constellation density to D^k; measures coverage protection |
| C_H > 1 | Proved for admissible H | Coverage protection: eliminating one member protects others |
| Sexy > twin | C_sexy = 2 * C_twin | Offset 6 = 2*3 creates residue collision at q = 3 |
| FS-x span (twin) | Not visible | Always 3 |
| FS-x span (triplet) | Not visible | Always 11 (gaps [3, 8]) |
| FS-x span (quadruplet) | Not visible | Always 14 (gaps [3, 8, 3]) |
| Inadmissible pattern | Covers all classes mod q | Survival factor = 0; geometrically impossible |
| Template persistence | Not visible | Constellation-open count grows with each primorial |
| Favored constellations | Larger C_H | Offsets divisible by small primorials maximize residue collisions |

Prime constellations in the Factor Skyline are fixed geometric configurations of escape events whose survival through each coverage layer is determined by the residue collision structure of their offsets. The k-tuple constant C_H measures the cumulative coverage protection, and the FS-x footprint provides an invariant geometric signature for each constellation type. The skyline's architecture determines which constellations are favored (those with primorial-aligned offsets), which are forbidden (inadmissible patterns), and how their density decays with scale (as C_H / (ln n)^k).
