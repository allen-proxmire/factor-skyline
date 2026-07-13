# The 2p Bracket Construction: Seven Sisters, Consecutive-Prime Sums, and Doubling Ladders

Allen Proxmire

July 2026

---

## Abstract

This is a companion note linking two earlier pieces of work: *The Seven Sisters* (prime generation via the form $2p + k$) and *Consecutive-Prime Sums in Prime Gaps*. Starting from a single construction on a consecutive-prime pair $(p, q)$ — form the two doublings $2p, 2q$ and the sum $s = p+q$, then measure how far the doublings sit from the primes bracketing the sum — we obtain a four-number signature $(a, b, c, d)$. We show:

1. **The signature *is* the Seven Sisters.** The four offsets are exactly the values of $k$ for which $2p + k$ or $2q + k$ lands on the two primes flanking the sum; the dominant offsets ($\pm 3, \pm 9$) are the ones the Seven Sisters analysis proved are never divisible by 3.
2. **A mirror law.** The signature takes the antisymmetric form $(-x, +y, -y, +x)$ **exactly when the sum is centered between its bracketing primes** — not, as first guessed, when the sum is a multiple of 12. Divisibility by 12 only *raises the odds* of centering (~12.5% vs ~8%), a mod-6 symmetry effect.
3. **A clean characterization and doubling ladders.** A sum $s$ is centered iff $2s$ is *again* a sum of two consecutive primes; equivalently $s$ is simultaneously a consecutive-prime **sum** and a consecutive-prime **average**. Iterating the flank-and-sum map produces geometric ladders $s \to 2s \to 4s \to \cdots$ of centered sums, e.g. $30 \to 60 \to 120 \to 240$, seeded at $30 = 2\cdot 3 \cdot 5$.

All numerical claims verified to $N = 5 \times 10^6$ (signatures, centering rates) and $N = 2\times 10^6$ (ladders). This note is exploratory; proven statements are marked as such.

---

## 1. The construction

**Definition 1.1.** Let $(p, q)$ be consecutive primes, $q = p_{n+1}$, $p = p_n$. Form three numbers
$$2p, \qquad s = p + q, \qquad 2q,$$
and let $L < s < U$ be the primes immediately below and above the sum ($L = \text{prevprime}(s)$, $U = \text{nextprime}(s)$). The **bracket signature** of $(p,q)$ is the quadruple
$$a = L - 2p, \quad b = U - 2p, \quad c = L - 2q, \quad d = U - 2q.$$

**Worked example.** $p = 31,\ q = 37$: $2p = 62,\ s = 68,\ 2q = 74$; bracket $(L, U) = (67, 71)$.
$$a = 67 - 62 = +5, \quad b = 71 - 62 = +9, \quad c = 67 - 74 = -7, \quad d = 71 - 74 = -3.$$
Signature $(+5, +9, -7, -3)$. Note $2p$ sits *below* both bracket primes (both offsets positive) and $2q$ sits *above* both (both negative); this is forced, since $2p = s - g$ and $2q = s + g$ straddle the sum symmetrically at distance $g = q - p$.

## 2. The signature is the Seven Sisters

Since $2p + a = L$ and $2p + b = U$ are both prime, $a$ and $b$ are precisely the offsets $k$ for which the Seven Sisters form $2p + k$ lands on the two primes flanking the sum; $c, d$ do the same for $2q + k$. The construction is therefore a structured *source* of Seven Sisters hits.

**Elementary identities.** Writing $g = q - p$, $d_L = s - L$, $d_U = U - s$, and $W = U - L = d_L + d_U$ (the bracketing gap width):
$$a = g - d_L, \quad b = g + d_U, \quad c = -(g + d_L), \quad d = d_U - g. \tag{2.1}$$
Consequently
$$a - c = b - d = 2g, \qquad b - a = d - c = W. \tag{2.2}$$
So the four offsets form a rectangle: horizontally spaced by the *bracket width* $W$, vertically by *twice the original gap* $2g$.

**Which offsets dominate.** Tabulating the signature over consecutive pairs with $p \in [29, 73]$ reproduces the offsets one sees most often:

| column | meaning | most frequent values ($p \in [29,73]$) |
|---|---|---|
| $a$ | $2p \to L$ | $+3$ |
| $b$ | $2p \to U$ | $+7,\ +9$ |
| $c$ | $2q \to L$ | $-7,\ -9$ |
| $d$ | $2q \to U$ | $-3$ |

The prevalence of $\pm 3, \pm 9$ (and to a lesser extent $\pm 7$) is exactly the Seven Sisters mod-3 result: for $k \in \{+3, -3, +9, -9\}$ the candidate $2p + k$ is **never** divisible by 3 (Group 1), so those offsets land on primes far more often than the "filter-affected" offsets $\{+1, +7, -5\}$, whose candidates are forced composite for half of all primes. The bracket construction inherits this bias directly.

## 3. The mirror law

**Observation.** For certain pairs the signature is antisymmetric, of the form $(-x, +y, -y, +x)$ — i.e. $a = -d$ and $b = -c$. Examples:
$$60 = 29+31 \to (+1, +3, -3, -1), \qquad 120 = 59+61 \to (-5, +9, -9, +5).$$

**Proposition 3.1 (Mirror law).** The signature satisfies $a = -d$ and $b = -c$ **if and only if** the sum is centered in its bracket, $L + U = 2s$ (equivalently $d_L = d_U$).

*Proof.* From (2.1), $a = -d \iff g - d_L = -(d_U - g) \iff d_L = d_U$, and $b = -c \iff g + d_U = g + d_L \iff d_L = d_U$; both conditions are the same, and $d_L = d_U \iff L + U = 2s$. $\square$

When centered, writing $t = d_L = d_U = W/2$, (2.1) collapses to
$$(a, b, c, d) = \big(g - t,\ g + t,\ -(g+t),\ -(g-t)\big) = (-x, +y, -y, +x), \quad x = t - g,\ y = t + g. \tag{3.1}$$
For $120$: $t = 7,\ g = 2 \Rightarrow (x, y) = (5, 9) \Rightarrow (-5, +9, -9, +5)$, as claimed.

### 3.1. Why "multiples of 12" was the wrong trigger

The mirror was first noticed among sums divisible by 12, and there is a real reason it clusters there — but divisibility is not the cause.

**Proposition 3.2 (proven).** Every twin-prime sum is a multiple of 12. *Proof.* A twin lower member $p \ge 5$ satisfies $p \equiv 5 \pmod 6$, so $s = 2p + 2 = 2(p+1)$ with $p + 1 \equiv 0 \pmod 6$; hence $12 \mid s$. $\square$ (Verified: all $17{,}936$ twin sums below $5\times10^6$ are divisible by 12. Multiples of 12 also arise from wider gaps $g \equiv \pm 2 \pmod{12}$, so the multiple-of-12 set is strictly larger than the twin-sum set.)

But being a multiple of 12 does **not** force centering:

| $s$ | pair | mult. of 12? | bracket | centered? | signature |
|---|---|---|---|---|---|
| $60$ | $29+31$ | yes | $(59, 61)$ | yes | $(+1,+3,-3,-1)$ mirror |
| $120$ | $59+61$ | yes | $(113, 127)$ | yes | $(-5,+9,-9,+5)$ mirror |
| $144$ | $71+73$ | yes | $(139, 149)$ | yes | $(-3,+7,-7,+3)$ mirror |
| $84$ | $41+43$ | yes | $(83, 89)$ | **no** ($1$ below, $5$ above) | $(+1,+7,-3,+3)$ — no mirror |
| $204$ | $101+103$ | yes | $(199, 211)$ | **no** ($5$ below, $7$ above) | $(-3,+9,-7,+5)$ — no mirror |

The correct statement is a mild **bias**: centered sums are $\approx 8\%$ of all consecutive-prime sums, but $\approx 12.5\%$ of those divisible by 12 (measured to $5\times10^6$) — about $1.5\times$ enriched. The mechanism is mod-6 geometry: every prime $> 3$ lies at $6k \pm 1$, symmetrically flanking each multiple of 6, so a multiple of 12 (hence of 6) is structurally more likely to have equidistant neighbors. It is a tendency, never a guarantee; $84$ and $204$ are among the $\approx 87\%$ of multiples of 12 that miss.

## 4. The characterization and doubling ladders

**Proposition 4.1 (proven).** A consecutive-prime sum $s$ is centered $\iff 2s$ is itself a sum of two consecutive primes. Equivalently, $s$ is simultaneously a consecutive-prime **sum** ($s = p + q$) and a consecutive-prime **average** ($s = (L+U)/2$).

*Proof.* Centered means $L + U = 2s$ with $L, U = \text{prevprime}(s), \text{nextprime}(s)$, which are consecutive primes; so $2s = L + U$ is a consecutive-prime sum. Conversely, if $2s = L' + U'$ for consecutive primes $L' < U'$, then $L' < s < U'$, so $L', U'$ are exactly the primes bracketing $s$, i.e. $s$ is centered. $\square$

This makes the flank-and-sum map $T(s) = \text{prevprime}(s) + \text{nextprime}(s)$ natural: $s$ is centered precisely when $T(s) = 2s$. When the image $2s$ is *itself* centered, the doubling continues, producing a **ladder** $s \to 2s \to 4s \to \cdots$ of centered sums.

**The multipliers carry no pattern.** For centered sums divisible by 12, the multiplier $n = s/12$ runs
$$1, 5, 10, 12, 20, 24, 25, 50, 58, 69, 77, 87, 95, 110, 119, 135, 136, 139, \dots$$
with successive differences $4, 5, 2, 8, 4, 1, 25, 8, 11, \dots$ — no arithmetic progression, no modular cycle. The apparent "niceness" of the first few ($5, 10, 12$) is a small-number artifact: round integers are simply dense among small values. The multiplier sequence is as pseudo-random as the prime gaps that generate it.

**The ladders do.** The pretty structure lives in the doubling map, not the multipliers. Searching to $N = 2\times10^6$:

| length | ladder |
|---|---|
| 4 | $30 \to 60 \to 120 \to 240$ |
| 4 | $36120 \to 72240 \to 144480 \to 288960$ |
| 4 | $44202 \to 88404 \to 176808 \to 353616$ |
| 3 | $810 \to 1620 \to 3240$ |
| 3 | $1320 \to 2640 \to 5280$ |
| 3 | $3330 \to 6660 \to 13320$ |

The seed ladder is transparent:
$$30 = 13+17 \xrightarrow{\ 29+31\ } 60 = 29+31 \xrightarrow{\ 59+61\ } 120 = 59+61 \xrightarrow{\ 113+127\ } 240 = 113+127,$$
each term the sum of the two primes flanking the previous, each exactly double its predecessor, until $240 \to 480$ falls off center and the ladder ends. The root $30 = 2\cdot3\cdot5$ is the second primorial.

## 5. Summary

The construction unifies the two prior notes. A consecutive-prime pair casts two shadows onto the doubled scale ($2p, 2q$); their offsets to the primes bracketing the sum $p+q$ are Seven Sisters values, biased toward $\pm 3, \pm 9$ by the same mod-3 law. The signature mirrors ($-x, +y, -y, +x$) exactly when the sum is centered in its bracket — a property equivalent to "$2s$ is again a consecutive-prime sum," enriched but not caused by divisibility by 12. Centered sums chain under doubling into short geometric ladders rooted at clean seeds. Throughout, the organizing operation is the same one that runs through Bertrand's postulate, the Seven Sisters, and the density law of the companion paper: **doubling**.

---

## Appendix. Reproduction

Signatures, centering rates, and ladders were computed with a sieve to $N$, `prevprime`/`nextprime` by linear scan, and the flank-and-sum map $T(s)$; a working (centered) sum satisfies $T(s) = 2s$, and ladders are maximal runs with $T(2^i s) = 2^{i+1} s$. See the companion paper *Consecutive-Prime Sums in Prime Gaps* (this repository) for the sieve harness; the additions here are:

```python
def prevp(n, B):
    n -= 1
    while not B[n]: n -= 1
    return n
def nextp(n, B):
    n += 1
    while not B[n]: n += 1
    return n

def signature(p, q, B):
    s = p + q; L = prevp(s, B); U = nextp(s, B)
    return (L - 2*p, U - 2*p, L - 2*q, U - 2*q)      # (a, b, c, d)

def centered(s, B):
    return prevp(s, B) + nextp(s, B) == 2*s           # mirror <=> 2s is a consec-prime sum
```

## References

- A. Proxmire, *The Seven Sisters: Prime Generation based on the Form $2p + k$* (companion note, this repository: `papers/FS_Seven_Sisters_2p_plus_k.pdf`; data & code: https://github.com/allen-proxmire/seven-sisters).
- A. Proxmire, *Consecutive-Prime Sums in Prime Gaps* (companion paper, this repository).
- OEIS A001043, *Numbers that are the sum of two successive primes*.
