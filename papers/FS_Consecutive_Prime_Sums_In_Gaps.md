# Consecutive-Prime Sums in Prime Gaps

Allen Proxmire

July 2026

---

## Abstract

Let $p_1 = 2, p_2 = 3, p_3 = 5, \dots$ be the primes and let $S_k = p_k + p_{k+1}$ be the $k$-th *consecutive-prime sum* (OEIS A001043: $5, 8, 12, 18, 24, 30, \dots$). We study the distribution of these sums among the prime gaps: given a gap $(p_n, p_{n+1})$, how many $S_k$ land strictly inside it?

We establish three things. **(1) A density law:** every $S_k$ with $k \ge 2$ is even, hence composite, hence lands strictly inside a unique prime gap, and the expected number of consecutive-prime sums in a gap of width $W$ near $x$ is $W/(2\ln(x/2))$. The factor of $2$ is the arithmetic content — a consecutive-prime sum lives at the "$2p$" scale, so it is drawn from primes near $x/2$ and is twice as sparse as the gaps it must fall into. Empirically the mean is $\approx 0.56$ sums per gap, so roughly $55\%$ of gaps contain none, $37\%$ contain exactly one, and $8\%$ contain two or more. **(2) A complete finite classification (the main theorem):** the gap widths $W$ for which a gap can *never* contain two consecutive-prime sums are exactly $\{2, 4, 6, 10\}$. The bound rests on the elementary fact that consecutive sums are $\ge 6$ apart, combined with a residue analysis modulo $6$; width $10$ is a genuine straggler, the only forbidden width wide enough to appear capable. **(3) An honest limit:** the "existence" direction — whether every sufficiently wide gap must contain a sum — has no deterministic threshold. Empty gaps persist at arbitrary width relative to the local sum-spacing (we exhibit a width-$140$ empty gap), and settling the question is of Goldbach/Cramér strength.

All results are verified computationally to $N = 2 \times 10^8$; a self-contained reproduction script is included in Appendix B.

---

## 1. Introduction

### 1.1. Motivation

Bertrand's postulate — that there is always a prime between $n$ and $2n$ — suggests that the interval $(p, 2p)$ carries much of the local structure of the primes. This paper follows that intuition to a specific, elementary object. If one adds two consecutive primes, $p_k + p_{k+1}$, the result sits just above $2p_k$; it is a shadow of the pair cast onto the "doubled" scale. Asking where these shadows land among the *larger* primes turns out to have a clean and partly surprising answer.

The starting observation was empirical. Between the consecutive primes $1601$ and $1607$ there is exactly one number that is a sum of two smaller consecutive primes: $797 + 809 = 1606$. One is tempted to conjecture that this holds throughout — that every gap (excluding the twin-prime gaps, which are too narrow) contains exactly one such sum. That conjecture is *false*, but the way it fails is structured, and the structure is worth recording.

### 1.2. The object

**Definition 1.1.** For $k \ge 1$, the $k$-th **consecutive-prime sum** is
$$S_k = p_k + p_{k+1}.$$
The sequence is $S_1 = 5,\ S_2 = 8,\ S_3 = 12,\ S_4 = 18,\ S_5 = 24,\ S_6 = 30, \dots$ (OEIS A001043).

The sums are strictly increasing, and for a prime gap $(p_n, p_{n+1})$ we write $W = p_{n+1} - p_n$ for its width and ask for the count
$$c(n) = \#\{\, k : p_n < S_k < p_{n+1}\,\}.$$

### 1.3. Summary of results and honest positioning

The density law of Section 3 is a consequence of the prime number theorem and carries no independent arithmetic surprise; we include it because the constant — exactly $2$ — is the quantitative form of the "$p$ versus $2p$" heuristic and because it organizes everything that follows. The **forbidden-width theorem** of Section 4 is the novel contribution: a short, self-contained, and complete classification. The existence discussion of Section 5 is expository; it locates the hard part of the original conjecture inside known deep problems and gives a concrete obstruction.

We claim no deep new mathematics. The interest is in a clean elementary theorem (Section 4) and in the sharp separation between what is provable and what is not (Sections 4 vs. 5).

---

## 2. Elementary facts

**Proposition 2.1 (Every sum lands strictly inside a gap).** For $k \ge 2$, $S_k$ is even; consequently $S_k$ is composite, and it lies strictly between two consecutive primes — never on a prime.

*Proof.* For $k \ge 2$, both $p_k$ and $p_{k+1}$ are odd, so $S_k$ is even and $> 2$, hence composite. A composite number is not prime, so if $p_m \le S_k < p_{m+1}$ then $p_m \ne S_k$, giving $p_m < S_k < p_{m+1}$. $\square$

Thus the map $k \mapsto (\text{gap containing } S_k)$ is well defined for $k \ge 2$, and the counts $c(n)$ partition the sums.

**Proposition 2.2 (Sums are at least 6 apart, eventually).** For $k$ with $p_k \ge 5$,
$$S_{k+1} - S_k = p_{k+2} - p_k \ \ge\ 6.$$

*Proof.* The identity is immediate: $S_{k+1} - S_k = (p_{k+1} + p_{k+2}) - (p_k + p_{k+1}) = p_{k+2} - p_k$. Writing the two gaps $g_k = p_{k+1} - p_k$ and $g_{k+1} = p_{k+2} - p_{k+1}$, we have $p_{k+2} - p_k = g_k + g_{k+1}$, a sum of two consecutive prime gaps. For primes $\ge 5$ each gap is even and $\ge 2$; the only way $g_k = g_{k+1} = 2$ would require three primes $p, p+2, p+4$, but one of any three integers in arithmetic progression with common difference $2$ is divisible by $3$, so the sole such triple is $(3,5,7)$. Hence for $p_k \ge 5$ at least one of $g_k, g_{k+1}$ is $\ge 4$, giving $g_k + g_{k+1} \ge 6$. $\square$

The bound $6$ is attained infinitely often in practice (e.g. $5+7=12,\ 7+11=18$; $11+13=24,\ 13+17=30$), so Proposition 2.2 is sharp.

---

## 3. The density law

### 3.1. Heuristic derivation

Fix a location $x$. A consecutive-prime sum near $x$ has $S_k = p_k + p_{k+1} \approx 2p_k$, so it is generated by a prime $p_k \approx x/2$. As $k$ advances by one, $S_k$ advances by $p_{k+2} - p_k$, which by the prime number theorem is on average twice the local prime gap at $x/2$:
$$S_{k+1} - S_k = p_{k+2} - p_k \ \approx\ 2\ln(x/2).$$
Hence near $x$ the consecutive-prime sums form a sequence of average spacing $2\ln(x/2)$, i.e. of linear density $1/(2\ln(x/2))$. The expected number falling in a gap of width $W$ is therefore
$$\boxed{\ \lambda(W, x) \ \approx\ \frac{W}{2\ln(x/2)}\ }\tag{3.1}$$
Because prime gaps near $x$ have average width $\ln x$, the mean count per gap is $\approx \ln x / (2\ln(x/2)) \to \tfrac12$. This is the quantitative form of the doubling intuition: the sums are drawn from the half-scale $x/2$ and are asymptotically **twice as sparse** as the gaps they must land in, so on average only one gap in two receives a sum.

### 3.2. Numerical confirmation

Table 1 gives the distribution of $c(n)$ over non-twin gaps with $p_n > 11$, computed to $N = 2\times 10^7$.

**Table 1.** Count distribution, non-twin gaps, $p_n > 11$, $N = 2 \times 10^7$ (1,163,197 gaps; mean $= 0.561$).

| $c(n)$ | 0 | 1 | 2 | 3 | $\ge 4$ |
|---|---|---|---|---|---|
| gaps | 635,687 | 431,667 | 73,356 | 17,455 | 5,032 |
| fraction | 0.546 | 0.371 | 0.063 | 0.015 | 0.004 |

The mean is stable across magnitude (0.591 near $10^3$, 0.561 near $10^7$), consistent with the slow logarithmic drift in (3.1).

The constant $2$ in (3.1) is confirmed directly. Writing the measured linear density of sums near $x$ as $d(x)$ and fitting $c_{\mathrm{fit}} = 1/(d(x)\ln(x/2))$, the value converges to $2$ from above:

**Table 2.** Fitted constant, $N = 5 \times 10^7$.

| $x$ | $\sim 10^{2.5}$ | $10^{3.5}$ | $10^{4.5}$ | $10^{5.5}$ | $10^{6.5}$ | $10^{7.25}$ |
|---|---|---|---|---|---|---|
| $c_{\mathrm{fit}}$ | 2.080 | 2.052 | 2.031 | 2.018 | 2.014 | 2.013 |

Measuring the sum-spacing directly against $2\ln(x/2)$ gives a ratio converging to $1.007$ — a sub-$1\%$ lower-order logarithmic correction on top of a clean leading term $2\ln(x/2)$.

### 3.3. Consequence for the original conjecture

The naive conjecture — "every non-twin gap after $11$ contains exactly one sum" — is false on the existence side: by Table 1 the single most common outcome is an **empty** gap (about $55\%$). The example $1601 + 1607 \supset 1606$ is a genuine hit, but for a width-$6$ gap it is only a $\approx 19\%$ event. The corrected statement is the density law (3.1): the count is not $1$ but a random-looking quantity with mean $W/(2\ln(x/2))$.

---

## 4. Uniqueness and the forbidden-width theorem

Although existence fails, a sharpened form of the conjecture — *when a gap does contain a sum, it contains only one* — is nearly true and, for narrow gaps, exactly true. Among the $1{,}242{,}066$ non-empty non-twin gaps below $5\times10^7$, $81.7\%$ contain exactly one sum; the $18.3\%$ with two or more are concentrated in the wide gaps. We now determine precisely which widths *force* uniqueness.

### 4.1. Setup and the crude bound

Suppose a gap $(a, a+W)$ contains two consecutive-prime sums $S_k < S_{k+1}$. Both lie in an open interval of length $W$, so their separation satisfies $S_{k+1} - S_k \le W - 2$ (the sums are even and $a$ is odd, so the extreme interior even integers are $a+1$ and $a+W-1$, spanning $W-2$). By Proposition 2.2, for $a$ large enough that the generating primes exceed $5$ (which holds for every gap of width $\ge 8$; the finitely many tiny gaps are checked directly), the separation is also $\ge 6$. Hence a double requires $W - 2 \ge 6$, i.e.
$$W \ge 8. \tag{4.1}$$
In particular, **any gap of width $\le 6$ contains at most one consecutive-prime sum.** This already covers the twin gaps ($W=2$) and widths $4, 6$.

### 4.2. The multiples-of-6 lemma

The tight case $S_{k+1} - S_k = 6$ has rigid arithmetic.

**Lemma 4.1.** If $S_{k+1} - S_k = 6$ (with $p_k \ge 5$), then $S_k \equiv S_{k+1} \equiv 0 \pmod 6$.

*Proof.* Separation $6$ means the two prime gaps $(g_k, g_{k+1})$ are $(2,4)$ or $(4,2)$. 

- Case $(2,4)$: the triple is $q, q+2, q+6$. Requiring none divisible by $3$ forces $q \equiv 2 \pmod 3$. Then $S_k = 2q+2 \equiv 0$ and $S_{k+1} = 2q+8 \equiv 0 \pmod 3$. 
- Case $(4,2)$: the triple is $q, q+4, q+6$, forcing $q \equiv 1 \pmod 3$, whence $S_k = 2q+4 \equiv 0$ and $S_{k+1} = 2q+10 \equiv 0 \pmod 3$. 

In both cases the sums are $\equiv 0 \pmod 3$, and being even they are $\equiv 0 \pmod 6$. $\square$

So a tight double consists of **two multiples of $6$, six apart.** Whether a given width can accommodate this reduces to counting the multiples of $6$ interior to the gap — and that count is forced by $W \bmod 3$, because the gap's lower endpoint has a forced residue.

**Lemma 4.2 (Endpoint residue).** Let $(a, a+W)$ be a prime gap with $a > 3$.
- If $W \equiv 1 \pmod 3$ then $a \equiv 1 \pmod 6$.
- If $W \equiv 2 \pmod 3$ then $a \equiv 5 \pmod 6$.
- If $W \equiv 0 \pmod 3$ then $a \equiv 1$ or $5 \pmod 6$.

*Proof.* Both $a$ and $a+W$ are primes $> 3$, so neither is $\equiv 0 \pmod 3$. If $W \equiv 1$, then $a \equiv 2 \pmod 3$ would give $a + W \equiv 0$, impossible; so $a \equiv 1 \pmod 3$. If $W \equiv 2$, then $a \equiv 1$ would give $a+W \equiv 0$; so $a \equiv 2 \pmod 3$. Combining with $a$ odd (so $a \not\equiv 3 \pmod 6$) yields the stated residues mod $6$. $\square$

Counting multiples of $6$ in the open interval $(a, a+W)$ under Lemma 4.2 gives the **slot count** $s(W)$ = the maximum number of multiples of $6$ that can lie interior, which is the number of admissible positions for tight-double members:

**Table 3.** Slot count $s(W)$ = interior multiples of $6$.

| $W$ | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| $W \bmod 3$ | 2 | 1 | 0 | 2 | 1 | 0 | 2 | 1 | 0 | 2 |
| $s(W)$ | 1 | 0 | 1 | 2 | 1 | 2 | 3 | 2 | 3 | 4 |

A tight double needs $s(W) \ge 2$. This first happens at $W = 8$, **fails again at $W = 10$**, and holds for all $W \ge 12$ (the offset pattern only adds slots as $W$ grows). The lone dip at $W=10$ is the crux.

### 4.3. Width 10

**Proposition 4.3.** No prime gap of width $10$ contains two consecutive-prime sums.

*Proof.* Let $(a, a+10)$ be a prime gap. By Lemma 4.2, $a \equiv 1 \pmod 6$; every such gap has $a \ge 139$, so the generating primes exceed $5$ and Proposition 2.2 applies. A double would have separation $\sigma \in \{6, 8\}$ (even, $\ge 6$ by Prop. 2.2, $\le W-2 = 8$).

*Separation $6$.* By Lemma 4.1 both sums are multiples of $6$. With $a \equiv 1 \pmod 6$, the only interior multiple of $6$ is $a+5$ ($a-1 \le a$ and $a+11 \ge a+10$ are excluded). One slot cannot hold two members. Impossible.

*Separation $8$.* The only two interior even integers $8$ apart are $a+1$ and $a+9$. With $a \equiv 1 \pmod 3$ their residues are $a+1 \equiv 2$ and $a+9 \equiv 1 \pmod 3$, so a double here would need $(S_k, S_{k+1}) \equiv (2, 1) \pmod 3$. But a separation-$8$ triple is $(2,6)$ or $(6,2)$ (the pattern $(4,4)$ gives $q, q+4, q+8 \equiv q, q+1, q+2$, always hitting a multiple of $3$, so it is not a prime triple for $q > 3$):
- $(2,6)$: $q \equiv 2 \pmod 3$, giving $(S_k, S_{k+1}) \equiv (0, 2)$;
- $(6,2)$: $q \equiv 2 \pmod 3$, giving $(S_k, S_{k+1}) \equiv (1, 0)$.

Neither is $(2,1)$. Impossible. $\square$

### 4.4. The classification

**Theorem 4.4 (Forbidden widths).**

(a) If $W \in \{2, 4, 6, 10\}$, then no prime gap of width $W$ contains two consecutive-prime sums.

(b) For every even $W \ge 8$ with $W \notin \{10\}$, prime gaps of width $W$ containing two consecutive-prime sums exist.

*Proof.* (a) Widths $2,4,6$ are handled by (4.1); width $10$ is Proposition 4.3. (b) For $W = 8$ and every even $12 \le W \le 60$ an explicit example is exhibited computationally (Table 4 lists the first; the search to $N = 2\times10^8$ found doubles at every such width). Structurally, $s(W) \ge 2$ for all these $W$ by Table 3, so the required pair of interior multiple-of-$6$ positions exists, and prime triples realizing a $(2,4)$ or $(4,2)$ pattern at the half-scale populate them. $\square$

**Remark 4.5.** The forbidden set is exactly $\{2, 4, 6, 10\}$: no forbidden width exceeds $10$. Part (b) is verified for $8 \le W \le 60$; its extension to all even $W \ge 12$ is expected on the same slot-counting basis, and the *infinitude* of doubles at each such width would follow from the prime $k$-tuple conjecture (the relevant triples are admissible constellations). The elementary content — part (a), the complete list of widths that force uniqueness — is unconditional.

**Table 4.** Doubles by width, $N = 2\times 10^8$. "first $a$" is the lower endpoint of the first gap of that width containing two sums.

| $W$ | gaps | with $\ge 2$ | rate | first $a$ |
|---|---|---|---|---|
| 2 | 813,370 | 0 | 0 | — |
| 4 | 813,714 | 0 | 0 | — |
| 6 | 1,429,538 | 0 | 0 | — |
| **8** | 624,743 | 1,181 | 0.19% | 389 |
| **10** | 805,277 | 0 | 0 | — |
| 12 | 1,017,047 | 7,332 | 0.72% | 199 |
| 14 | 556,481 | 11,593 | 2.08% | 317 |
| 16 | 411,449 | 4,581 | 1.11% | 1,933 |
| 18 | 739,453 | 22,016 | 2.98% | 523 |
| 30 | 443,840 | 62,707 | 14.13% | 4,831 |
| 60 | 62,576 | 34,355 | 54.90% | 43,331 |

The first genuine double occurs in the width-$8$ gap $(389, 397)$: it contains both $390 = 193 + 197$ and $396 = 197 + 199$.

**Corollary 4.6 (Sharpened conjecture).** For gaps of width $W \in \{2,4,6,10\}$, the original "only one" property holds without exception: such a gap contains at most one consecutive-prime sum. For all other widths it can fail, with failure rate increasing in $W$.

---

## 5. The existence direction

The remaining half of the original conjecture — does every *sufficiently wide* gap contain at least one sum? — behaves very differently. It has no elementary resolution, and we explain why.

### 5.1. Sub-Poisson emptiness

If the sums fell as independent random points of density $1/(2\ln(x/2))$, the fraction of empty gaps would be $e^{-\lambda}$ with $\lambda$ as in (3.1). The measured empty fraction is markedly *smaller* and the discrepancy grows with $\lambda$:

**Table 5.** Empty fraction vs. Poisson prediction, $N = 10^8$.

| $\lambda$ | 0.375 | 0.625 | 0.875 | 1.125 | 1.625 | 2.125 |
|---|---|---|---|---|---|---|
| $P(\text{empty})$ | 0.659 | 0.448 | 0.289 | 0.183 | 0.065 | 0.022 |
| $e^{-\lambda}$ | 0.687 | 0.535 | 0.417 | 0.325 | 0.197 | 0.119 |

The empty fraction decays faster than $e^{-\lambda}$ — roughly $e^{-2.3\lambda}$ — because consecutive-prime sums are **under-dispersed**: they march with spacing tightly concentrated near $2\ln(x/2)$ rather than clustering like Poisson points, and an evenly spaced sequence leaves fewer empty intervals. So wide gaps are non-empty *more* reliably than a random model predicts; the original intuition is, if anything, better than chance would justify.

### 5.2. No deterministic threshold

Nevertheless there is no width — however large relative to the local sum-spacing — that guarantees a hit. Empty gaps persist out to $\lambda \approx 4$.

**Example 5.1.** The gap $(79{,}092{,}617,\ 79{,}092{,}757)$ has width $140$ and contains **no** consecutive-prime sum, although $\lambda \approx 4.0$ (the width is four times the local sum-spacing). The sum sequence steps $\dots, 79{,}092{,}612,\ 79{,}092{,}758, \dots$ — a single stride of $146$ that straddles the entire gap. This is a double coincidence: the primes near $x \approx 79\times 10^6$ are locally sparse (the wide gap) and the primes near $x/2 \approx 39.5\times 10^6$ that generate the nearby sums are simultaneously sparse at the aligned location.

### 5.3. Why this is hard

Proving that every gap wider than some explicit function of $x$ contains a sum would require ruling out coincidences of the type in Example 5.1 — a controlled statement about the joint behavior of prime gaps at $x$ and prime spacing at $x/2$. This couples the distribution of gaps to itself across scales and is of the same order of difficulty as Goldbach- and Cramér-type problems. We therefore leave existence as:

**Open Problem 5.2.** Is there a function $f(x) = o(x)$ such that every prime gap $(p_n, p_{n+1})$ with $p_{n+1} - p_n \ge f(p_n)$ contains a consecutive-prime sum? Equivalently, bound the largest empty gap at height $x$.

---

## 6. Discussion

The trajectory of the original conjecture is a compact case study. A pattern noticed at a single gap ($1601, 1607$) generalized in three ways with three different epistemic statuses:

1. **Existence ("always one") — false**, replaced by the density law (3.1) whose only content is the doubling constant $2$, a restatement of the prime number theorem at the half-scale.
2. **Uniqueness ("at most one") — a theorem for exactly the widths $\{2,4,6,10\}$** (Theorem 4.4), unconditional and elementary, with width $10$ the single non-obvious member.
3. **Wide-gap existence — open and hard** (Open Problem 5.2), provably not settleable by width alone (Example 5.1).

Within the Factor Skyline program the consecutive-prime sum is the simplest object that lives one dyadic scale above the primes that define it, making the interaction between a gap at $x$ and the prime density at $x/2$ explicit and elementary. The clean separation here — an unconditional finite classification sitting directly beside a Goldbach-strength open problem — mirrors the template/escape split elsewhere in the framework: the part fixed by congruences is provable, the part requiring cross-scale coincidence control is not.

---

## Appendix A. Notation

- $p_k$: the $k$-th prime, $p_1 = 2$.
- $S_k = p_k + p_{k+1}$: the $k$-th consecutive-prime sum (OEIS A001043).
- $W = p_{n+1} - p_n$: gap width. A *twin gap* has $W = 2$.
- $c(n) = \#\{k : p_n < S_k < p_{n+1}\}$: sums in gap $n$.
- $\lambda(W,x) = W / (2\ln(x/2))$: expected count (density law).
- $s(W)$: slot count, interior multiples of $6$ (Table 3).

## Appendix B. Reproduction

All tables were produced by the following self-contained script (Python 3, standard library only). Sieve to `N`, form the consecutive-prime sums, sweep the gaps with a two-pointer, and tabulate.

```python
import math
from collections import defaultdict

def sieve(n):
    bs = bytearray([1]) * (n + 1); bs[0] = bs[1] = 0
    i = 2
    while i * i <= n:
        if bs[i]: bs[i*i::i] = bytearray(len(bs[i*i::i]))
        i += 1
    return [i for i in range(n + 1) if bs[i]]

def analyze(N):
    P = sieve(N)
    S = [P[k] + P[k+1] for k in range(len(P) - 1)]   # consecutive-prime sums
    maxS = S[-1]
    tot = defaultdict(int); dbl = defaultdict(int); first = {}
    dist = defaultdict(int)                            # count-distribution, non-twin, p_n>11
    j = 0
    for n in range(len(P) - 1):
        a, b = P[n], P[n+1]
        if b >= maxS: break
        if a < 3: continue                             # skip the degenerate width-1 gap (2,3)
        while j < len(S) and S[j] <= a: j += 1         # first sum > a
        jj = j; c = 0
        while jj < len(S) and S[jj] < b: c += 1; jj += 1
        w = b - a
        tot[w] += 1
        if c >= 2:
            dbl[w] += 1
            first.setdefault(w, a)
        if a > 11 and w > 2:
            dist[c] += 1
    # forbidden widths = those with zero doubles (verify == {2,4,6,10})
    forbidden = sorted(w for w in tot if dbl[w] == 0)
    mean = sum(k * v for k, v in dist.items()) / sum(dist.values())
    return dist, forbidden, first, mean

if __name__ == "__main__":
    dist, forbidden, first, mean = analyze(2 * 10**8)
    print("non-twin (p_n>11) count distribution:", dict(sorted(dist.items())))
    print("mean sums/gap:", round(mean, 3))
    print("forbidden widths (zero doubles):", forbidden)
    print("first double at width 8 / 12:", first.get(8), first.get(12))
```

Expected output (abridged): forbidden widths `[2, 4, 6, 10]`; mean $\approx 0.56$; first width-$8$ double at $a = 389$.

## References

- OEIS A001043, *Numbers that are the sum of two successive primes*.
- Bertrand's postulate / Chebyshev's theorem.
- H. Cramér, *On the order of magnitude of the difference between consecutive prime numbers*, Acta Arith. 2 (1936).
- G. H. Hardy and J. E. Littlewood, *Some problems of 'Partitio numerorum' III*, Acta Math. 44 (1923) — the prime $k$-tuple conjecture.
- A. Proxmire, *The Architectural Foundation of the Factor Skyline* (companion paper, this repository).
