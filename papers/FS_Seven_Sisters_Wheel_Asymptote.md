# Extending the Seven Sisters: The Wheel and the 100% Asymptote

Allen Proxmire

July 2026

---

## Abstract

The *Seven Sisters* note studies the offsets $k \in \{+1, +3, -3, -5, +7, +9, -9\}$ applied to $2p$, asking how often $2p + k$ is prime. This companion memo answers the natural follow-up: **can we add offsets and reach 100% coverage** — i.e. guarantee that *every* prime $p$ yields a prime by some offset? The answer is **no**, but the way it fails is clean and useful:

1. **Coverage drifts down with scale.** The seven-offset "at least one prime" rate falls from $\approx 92\%$ near $10^3$ to $\approx 62\%$ near $10^7$, because the primes near $2p$ thin out.
2. **100% is an asymptote, not a target.** Because prime gaps are unbounded, for any fixed finite offset set there are primes $p$ whose neighborhood of $2p$ contains no prime within the set's reach. The maximum offset actually needed grows with scale ($15 \to 29 \to 51 \to 73 \to 99$ across five decades), tracking the maximal local prime gap $\sim (\ln 2p)^2$.
3. **The efficient way to climb is the wheel.** The most valuable offsets to add are those divisible by $15 = 3\cdot 5$ (then by $105 = 3\cdot5\cdot7$), because they can never be killed by 3 or 5 and so remain *eligible* for the largest share of primes. Greedy extension along this wheel reaches $99\%$ with a dozen additions; the original seven's weak members ($+1, -5, +7$) are the mod-3 "conditional" offsets and should not be the template for growth.

All figures verified by sieve to $6\times 10^7$.

---

## 1. The question

The Seven Sisters generate primes from the doubled scale $2p$. Empirically the set covers a strong majority of primes but leaves a persistent tail uncovered ($\approx 35\%$ over the first million primes). It is natural to ask whether *adding* offsets — reaching for the second, third, … nearest primes above and below $2p$ — can close the gap entirely. This memo settles the ceiling and identifies which offsets are worth adding.

Throughout, all offsets are odd (since $2p$ is even, $2p + k$ can be prime only for odd $k$). We say offset $k$ **covers** prime $p$ if $2p + k$ is prime, and a set covers $p$ if some member does.

## 2. Coverage drifts down with scale

The seven-offset coverage is not scale-invariant; it decays as the primes near $2p$ grow sparser (density $\sim 1/\ln 2p$).

**Table 1.** Seven-Sister coverage and the offset actually needed, by magnitude of $p$.

| prime band | "$\ge 1$ prime" coverage | max $|k|$ needed | mean $|k|$ |
|---|---|---|---|
| $10^3$–$3\times10^3$ | 91.60% | 15 | 3.59 |
| $10^4$–$3\times10^4$ | 83.68% | 29 | 4.42 |
| $10^5$–$3\times10^5$ | 73.99% | 51 | 5.70 |
| $10^6$–$3\times10^6$ | 67.32% | 73 | 6.79 |
| $10^7$–$3\times10^7$ | 61.52% | 99 | 7.89 |

(The $\approx 65\%$ figure of the Seven Sisters note corresponds to the first million primes, i.e. up to $\approx 1.5\times10^7$, consistent with the trend.) The mean offset needed grows like $\ln 2p$ — the average nearest-prime distance — while the *maximum* grows far faster.

## 3. Why 100% is unreachable

**Claim.** No finite set of offsets covers every prime.

**Reason.** Let $K$ be a finite offset set and $M = \max_{k\in K} |k|$. Offset set $K$ covers $p$ only if the window $[\,2p - M,\ 2p + M\,]$ contains a prime. Since prime gaps are unbounded, there exist even numbers $2p$ (with $p$ prime) sitting in a prime gap wider than $2M$, far enough from both ends that the window is prime-free; such $p$ are uncovered. Empirically this is unmistakable: the maximum offset required does not saturate but climbs with scale (Table 1, last column: $15 \to 29 \to 51 \to 73 \to 99$), tracking the maximal local gap $\sim (\ln 2p)^2$. Hence the number of offsets required to cover all primes up to $x$ grows without bound (like $(\ln x)^2$), and **100% is an asymptote approached but never attained** by any fixed set.

*Rigor note.* That coverage $\to 100\%$ as the offset window widens is immediate; that no *finite* window suffices is certain in practice and rests on the unboundedness of the nearest-prime distance from $2p$ — a statement of the same character as the wide-gap-existence problem in the companion paper, and not claimed here as a formal proof.

## 4. The efficient extension: the wheel

Although 100% is unreachable, one can approach it, and the *order* in which offsets pay off is dictated entirely by divisibility — the primorial wheel.

**Eligibility lemma.** For any prime $p > 3$:
- if $3 \mid k$, then $3 \nmid (2p + k)$;
- if $15 \mid k$ (and $p > 5$), then $3 \nmid (2p+k)$ **and** $5 \nmid (2p+k)$.

*Proof.* Every prime $p > 3$ has $2p \equiv 1$ or $2 \pmod 3$ (never $0$); adding $k \equiv 0 \pmod 3$ preserves this, so $3 \nmid (2p+k)$. Likewise $2p \not\equiv 0 \pmod 5$ for $p > 5$, so $5 \nmid (2p+k)$ when $5 \mid k$. $\square$

The consequence is a strict eligibility hierarchy — the fraction of primes for which an offset is *not* automatically killed by a small prime:

| offset class | killed by 3? | killed by 5? | eligible share |
|---|---|---|---|
| $15 \mid k$ (e.g. $\pm15, \pm45, \pm75$) | never | never | highest |
| $3 \mid k,\ 5 \nmid k$ (e.g. $\pm21, \pm63$) | never | $\approx \tfrac14$ of $p$ | middle |
| $3 \nmid k$ (e.g. $+1, -5, +7, -11$) | $\approx \tfrac12$ of $p$ | some | lowest |

Greedy extension confirms the hierarchy exactly — every early addition is a multiple of 15, then the multiples of 3, and the mod-3 conditionals never appear:

**Table 2.** Greedy offset additions beyond the seven (primes to $2\times10^6$).

| add | coverage | | add | coverage |
|---|---|---|---|---|
| (7 Sisters) | 70.29% | | $-75$ | 95.46% |
| $+15$ | 78.25% | | $-21$ | 96.54% |
| $-15$ | 84.21% | | $+21$ | 97.39% |
| $+45$ | 88.46% | | $+63$ | 98.04% |
| $-45$ | 91.61% | | $-63$ | 98.54% |
| $+75$ | 93.85% | | $-39$ | 98.88% |
| | | | $-27$ | 99.14% |

The winners $\pm15, \pm45, \pm75$ are all divisible by $15$; $\pm21, \pm63$ (divisible by 3, not 5) come next; the conditionals do not make the list. A multiple-of-15 offset covers roughly $\tfrac43\times$ as many primes as a multiple-of-3-only offset and about $2\times$ as many as a mod-3 conditional, purely from eligibility.

For reference, the *idealized* ceiling — coverage if one could use **every** odd offset out to $\pm M$ — shows the diminishing returns directly:

**Table 3.** Coverage by "all odd offsets within $\pm M$" (primes to $2\times10^6$).

| $M$ | 9 | 15 | 21 | 31 | 45 | 63 |
|---|---|---|---|---|---|---|
| coverage | 81.5% | 94.3% | 98.0% | 99.6% | 99.98% | 100%\* |

\*100% on *this* sample only; the required $M$ grows with scale (§3).

**The extended Sisters.** The natural family to grow into is therefore the odd multiples of 3, weighted toward the multiples of 15 and 105:
$$\{\pm3,\ \pm9,\ \pm15,\ \pm21,\ \pm27,\ \pm33,\ \pm39,\ \pm45,\ \pm63,\ \pm75,\ \pm105,\ \dots\}.$$
These are the *strong* Sisters — the ones the wheel keeps eligible. The original seven's members $+1, -5, +7$ are weak (mod-3 conditional) and were included only because they are small; they are not the template for extension.

## 5. The two operations

This closes a loop across the whole program. Two operations organize everything:

- **Doubling** ($p \mapsto 2p$) sets the stage — it lifts a prime to the scale where the Sisters, the consecutive-prime sums, and Bertrand's postulate all live.
- **The wheel** ($3, 5, 7, \dots$ — the primorials) decides who survives — which gaps are common (jumping champions), which sums are centered (the mod-6 bias), and here, which offsets stay eligible.

The Seven Sisters sit exactly at this intersection: $2p$ chooses the neighborhood, the wheel chooses the winners. Reaching for 100% fails not because the method is weak but because the primes themselves thin out and gap without bound — the same unbounded-gap wall met in the consecutive-sum work. The reachable goal is not 100% but a wheel-optimal family that approaches it as closely as one likes.

---

## Appendix. Reproduction

```python
def sieve(n):
    b = bytearray([1]) * (n + 1); b[0] = b[1] = 0
    i = 2
    while i * i <= n:
        if b[i]: b[i*i::i] = bytearray(len(b[i*i::i]))
        i += 1
    return b

B = sieve(60_000_000)
sisters = [1, 3, -3, -5, 7, 9, -9]

def covers(p, K):                       # does offset set K yield a prime from 2p?
    return any(B[2*p + k] for k in K)

def nearest(p):                         # min |k| (odd) with 2p+k prime
    x = 2*p; du = 1
    while not B[x + du]: du += 1
    dd = 1
    while not B[x - dd]: dd += 1
    return min(du, dd)

# coverage drift + max offset needed, by band
for lo, hi in [(10**3,3*10**3),(10**6,3*10**6),(10**7,3*10**7)]:
    ps = [i for i in range(lo, hi) if B[i]]
    cov = sum(covers(p, sisters) for p in ps)
    rs  = [nearest(p) for p in ps]
    print(lo, f"{100*cov/len(ps):.2f}%", "maxk", max(rs))
```

## References

- A. Proxmire, *The Seven Sisters: Prime Generation based on the Form $2p + k$* (companion note, this repository: `papers/FS_Seven_Sisters_2p_plus_k.pdf`; data & code: https://github.com/allen-proxmire/seven-sisters).
- A. Proxmire, *The 2p Bracket Construction* (companion note, this repository).
- A. Proxmire, *Consecutive-Prime Sums in Prime Gaps* (companion paper, this repository) — the wide-gap-existence wall.
- A. M. Odlyzko, M. Rubinstein, M. Wolf, *Jumping champions*, Experimental Math. 8 (1999) — primorial gaps and the wheel.
