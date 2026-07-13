# Synthesis — Two Operations on the Factor Skyline: Doubling and the Wheel

Allen Proxmire

July 2026

---

## Abstract

This note synthesizes a connected body of exploratory work — consecutive-prime sums in gaps, the $2p$ bracket construction, the Seven Sisters, and their relation to jumping champions — by placing all of it on the Factor Skyline (FS). The claim is simple: every object studied is a motion on **one canvas** built from two features, the **escape diagonal** (primes) and the **wheel-fan** (the width-rays $y = n/\mathrm{lpf}(n)$), and the whole program is governed by **two operations** — **doubling** ($p \mapsto 2p$, geometrically the top width-2 ray) and **the wheel** (the primorials $2,3,5,7,\dots$, geometrically the fan of lower rays). Primes are exactly what escape both. The master diagram (`graphics/FS_master_synthesis.png`) is the visual spine. The synthesis also serves as an honest ledger: what proved real, what was a small-number mirage, and what runs into famous open problems.

---

## 1. The canvas

The Factor Skyline assigns each integer $n$ a height $y_{FS}(n) = n/\mathrm{lpf}(n)$ (with $y_{FS} = n$ when $n$ is prime). Plotting $n$ against $y_{FS}(n)$ produces a **fan of rays**:

- the **escape diagonal** $y = n$, where primes sit (they have no proper least prime factor, so they "escape" to full height);
- the **width-$p$ rays** $y = n/p$ — the width-2 ray ($y=n/2$, all even numbers), width-3 ($y=n/3$), width-5, width-7, … — where each composite lands on the ray of its least prime factor.

A number is prime **iff it dodges every width-ray and reaches the diagonal.** The rays *are* the primorial wheel: "divisible by 3" is not a fact about $n$ so much as a location — "on the width-3 ray."

Two features, two operations:

- **Doubling = the top ray.** Every object in this program — consecutive-prime sums $p+q$, the doublings $2p$, twin sums, the ladders — is even, so it lives entirely on the **width-2 ray**. The investigation is one ray resonating against the diagonal.
- **The wheel = the fan.** The lower rays sieve out composites; which offsets and gaps survive is decided by which rays they avoid.

See `graphics/FS_master_synthesis.png` (master canvas), `graphics/FS_wheel_fan.png` (the fan alone), and `graphics/FS_seven_sisters_escape.png` (the wheel as forbidden diagonals).

## 2. The dissolved question: sum = average

The investigation began oscillating between two views of the same object — is the thing to study the **sum** $p+q$ of consecutive primes, or their **average** $\tfrac{p+q}{2}$? The FS answers by identity. A consecutive-prime sum is even, so
$$y_{FS}(p+q) = \frac{p+q}{2} = \text{the average}.$$
On the canvas the sum is a single point on the width-2 ray: its **position** is the sum, its **height** is the average. The duality was never a choice — they are the $x$ and $y$ of one dot. Moreover the height (the average) lies strictly between the two parent primes, so a consecutive-prime sum's height "nestles in the gap" between its parents' escape peaks (master diagram, $31+37=68$ at height $34$).

## 3. Each thread as a motion on the canvas

| thread (companion paper) | what it is on the FS canvas |
|---|---|
| sum vs. average | the **same point** — position vs. height on the top ray (§2) |
| consecutive-prime sums in gaps | top-ray points whose height lands among the escape peaks |
| the density law $\lambda = W/(2\ln(x/2))$ | the "$2$" is the **reciprocal slope of the top ray** |
| forbidden widths $\{2,4,6,10\}$ | spacing constraints on top-ray points, mod-6 = the $2\cdot3$ wheel |
| the $2p$ bracket signature | Seven Sisters offsets: probes around the top-ray point $2p$ |
| the mirror law / centering | top-ray points whose double is again a top-ray sum |
| Seven Sisters coverage + wheel | escapes near $2p$, gated by which width-rays the offset avoids |
| jumping champions ($6, 30, 210$) | which escape-gaps are commonest — the primorial rays |

**The density-law constant.** A consecutive-prime sum at position $S$ has height $S/2$; its *height* points down to the half-scale $S/2$ where the primes that generated it live, while its *position* sits up among the primes that bracket it. The factor of 2 in $\lambda = W/(2\ln(x/2))$ is precisely the slope $1/2$ of the ray everything lives on — the doubling made into geometry.

**Forbidden widths.** Consecutive sums are $\ge 6$ apart (two consecutive prime gaps, minimally $2+4$, since $2+2$ forces the triple $3,5,7$). Hence gaps of width $\le 6$ hold at most one sum; width 10 is a straggler forbidden by a mod-6 residue argument; the complete forbidden set is $\{2,4,6,10\}$ — a clean, unconditional theorem. On the canvas this is a statement about the minimum spacing of top-ray points, and the mod-6 that drives it is the first two rays of the wheel.

**The Seven Sisters and the wheel.** From a prime $p$, the offset $2p + k$ either escapes (prime) or falls to a width-ray. An offset $k \equiv 0 \pmod 3$ can never land on the width-3 ray ($3 \nmid 2p+k$), so those offsets stay eligible for every prime; offsets divisible by $15 = 3\cdot5$ dodge two rays. The escape map (`FS_seven_sisters_escape.png`) shows the wheel as forbidden diagonal stripes, with the multiple-of-3 rows stripe-free and roughly twice as dense with escapes. Extending the Sisters means extending along the wheel — $\pm15, \pm45, \pm75, \pm105$ — not adding weak mod-3 conditionals.

## 4. Honest ledger

Exploratory work earns its keep by being clear about status. This program produced all three kinds of result.

**Proved (unconditional).**
- Every consecutive-prime sum ($k \ge 2$) is even, hence composite, hence lands strictly inside a prime gap.
- Consecutive sums are $\ge 6$ apart for $p_k \ge 5$; **gaps of width $\{2,4,6,10\}$ contain at most one sum** (complete forbidden-width classification).
- Every twin-prime sum is a multiple of 12.
- **Sum = average** in FS (height identity), and centered $\iff 2s$ is again a consecutive-prime sum.
- Wheel eligibility: $3 \mid k \Rightarrow 3 \nmid 2p+k$; $15 \mid k \Rightarrow 3,5 \nmid 2p+k$.

**Empirical laws (heuristic + verified to $10^8$–$2\times10^8$).**
- Density law $\lambda \approx W/(2\ln(x/2))$, constant fitted to $2$; $\approx 55\%$ of non-twin gaps empty, $37\%$ hold one.
- Centered sums $\approx 8\%$ overall, $\approx 12.5\%$ among multiples of 12 (a mod-6 bias, not a rule).
- Seven Sisters coverage drifts $92\% \to 62\%$ across five decades; greedy extension follows the wheel.

**Mirages (looked like structure, dissolved under scale).**
- The multiplier sequence $n = s/12$ of centered multiples of 12 is **pseudo-random** — the "nice" small values were a small-number artifact.
- **Primorials do not seed the long doubling ladders.** The record ladder (length 6) is seeded by $2362974 = 2\cdot3\cdot23\cdot17123$; among small primorials only $30$ is even a working sum. $30 \to 60 \to 120 \to 240$ was a charm, not a law.
- "Multiples of 12 show the mirror pattern" → the real trigger is **centering**; divisibility only nudges the odds.

**Open / hard (Goldbach– or Cramér–strength).**
- Wide-gap existence: does every sufficiently wide gap contain a consecutive-prime sum? (No deterministic threshold — a width-140 empty gap exists.)
- Seven Sisters 100% coverage: impossible for any finite offset set, because prime gaps are unbounded; the required offset grows like $(\ln 2p)^2$.
- Jumping-champion crossovers ($6 \to 30 \to 210$): conditional on the Hardy–Littlewood $k$-tuple conjecture.

Knowing which of these is which — and that two seductive patterns were mirages — is itself the main return on the exploration.

## 5. The synthesis

On the number line, these threads look unrelated: a fact about prime gaps here, a prime-generating formula there, a note on primorials elsewhere. On the Factor Skyline they are one picture. **Primes are what escape.** **The wheel is the fan of rays that catch everything else.** **Doubling is the top ray**, where every object in the program lives, one reciprocal-slope away from the primes that made it. Consecutive-prime sums, the Seven Sisters, jumping champions, the forbidden widths, the mirror law — each is a specific way the top ray meets the diagonal, refereed by the wheel.

Two operations, two geometric objects. Doubling sets the stage; the wheel decides the survivors; primes are the escapes. That is the whole thing.

---

## Companion documents

- *Consecutive-Prime Sums in Prime Gaps* — density law, forbidden-width theorem (this repository).
- *The 2p Bracket Construction* — signature, mirror law, centering, doubling ladders (this repository).
- *Extending the Seven Sisters: the Wheel and the 100% Asymptote* (this repository).
- *The Seven Sisters: Prime Generation based on the Form $2p+k$* (companion note, this repository: `papers/FS_Seven_Sisters_2p_plus_k.pdf`; data & code: https://github.com/allen-proxmire/seven-sisters).
- Odlyzko, Rubinstein, Wolf, *Jumping champions*, Experimental Math. 8 (1999).
- Figures: `graphics/FS_master_synthesis.png`, `FS_wheel_fan.png`, `FS_seven_sisters_escape.png`, `FS_consec_prime_arithmetic.png`.
