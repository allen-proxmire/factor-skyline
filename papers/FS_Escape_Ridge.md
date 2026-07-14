# The Escape Ridge of the Factor Skyline

Allen Proxmire

July 2026

---

## Abstract

Plotting the primes at their true Factor Skyline coordinates — cumulative $x_{FS}$ against value — traces an "escape ridge" whose shape was first measured empirically by cubic and power regression ($y \approx 0.966\,x^{0.86}$, $R^2 = 0.9993$). This note derives that shape from first principles. The horizontal coordinate grows as
$$x_{FS}(N) \sim 4e^{-\gamma}\,\frac{N^{3/2}}{\ln^2 N},$$
and the extra half-power over linear comes **entirely from the $p^2$ activation of the sieve sweeps** — a composite can only carry least prime factor $p$ once $p^2 \le n$, so the sweep sum is cut at $p \le \sqrt N$. Inverting gives an escape ridge $y \sim X^{2/3}$ with a slow upward logarithmic drift, so the *local* power falls from $\approx 0.85$ at $N \sim 10^3$ toward $2/3$ as $N \to \infty$. The empirical $x^{0.86}$ fit is a dead-on match at its scale, and the drift explains why a cubic outfit a single power law. The regression was not a curve-fit fishing for a number; it was measuring where the sieve turns its sweeps on.

---

## 1. The escape ridge

Recall the Factor Skyline coordinate: $x_{FS}(1) = 1$, and for $n \ge 2$,
$$x_{FS}(n) = x_{FS}(n-1) + dx(n), \qquad dx(n) = \begin{cases} 1 & n \text{ prime} \\ \mathrm{lpf}(n) & n \text{ composite.}\end{cases}$$
Every composite advances the horizontal coordinate by its least prime factor; every prime advances it by 1. The **escape ridge** is the locus of primes on this canvas: the points $\big(x_{FS}(p),\ p\big)$ for $p$ prime. This is the object plotted in the "Factor Skyline 1000" Desmos sheet, whose table entries — e.g. $(x_{FS}, p) = (1496, 521)$, $(1499, 523)$ — the derivation below must reproduce (and does, exactly).

## 2. Growth of the horizontal coordinate

Summing the step sizes,
$$x_{FS}(N) \approx \pi(N) + \sum_{\substack{n \le N \\ \text{composite}}} \mathrm{lpf}(n).$$
The number of $n \le N$ with least prime factor exactly $p$ is $\approx N \cdot \tfrac1p \prod_{q<p}(1 - \tfrac1q)$. A **composite** with $\mathrm{lpf} = p$ requires $p^2 \le n \le N$, i.e. $p \le \sqrt N$ — this is the sieve-of-Eratosthenes activation point, where prime $p$ first begins crossing out numbers it is the smallest factor of. Each such composite contributes $p$, so

$$\sum_{\text{comp}} \mathrm{lpf}(n) \approx N \sum_{p \le \sqrt N} p \cdot \frac1p \prod_{q<p}\Big(1 - \frac1q\Big) = N \sum_{p \le \sqrt N} \prod_{q<p}\Big(1 - \frac1q\Big).$$

By Mertens' third theorem $\prod_{q<p}(1 - 1/q) \sim e^{-\gamma}/\ln p$, and by the prime number theorem $\sum_{p \le y} 1/\ln p \sim y/\ln^2 y$. With $y = \sqrt N$,

$$\sum_{\text{comp}} \mathrm{lpf}(n) \sim N \cdot e^{-\gamma} \cdot \frac{\sqrt N}{\ln^2 \sqrt N} = 4e^{-\gamma}\,\frac{N^{3/2}}{\ln^2 N}.$$

This dominates $\pi(N) \sim N/\ln N$, giving

$$\boxed{\ x_{FS}(N) \ \sim\ 4e^{-\gamma}\,\frac{N^{3/2}}{\ln^2 N}, \qquad 4e^{-\gamma} \approx 2.2458.\ }$$

**The $\sqrt N$ is the $p^2$ sweep.** The half-power over linear is not incidental: it is the length of the sweep range $p \le \sqrt N$. Without the $p^2$ activation wall the sum would run over all $p \le N$ and the skyline would grow differently; cutting it at $\sqrt N$ is exactly what produces the $N^{3/2}$ ridge.

**Numerical confirmation.** The construction reproduces the Desmos table exactly ($x_{FS}(521) = 1496$, $x_{FS}(523) = 1499$). The local log-log slope of $x_{FS}$ vs $N$ climbs toward $3/2$:

| $N$ | ~$10^2$ | ~$10^3$ | ~$10^4$ | ~$10^5$ | ~$10^6$ |
|---|---|---|---|---|---|
| exponent | 1.18 | 1.17 | 1.24 | 1.29 | 1.33 |

and the constant ratio $x_{FS}\cdot\ln^2 N / N^{3/2}$ descends toward $4e^{-\gamma} = 2.25$ (from $4.9$ at $N\sim500$ to $3.2$ at $N=10^7$; the approach is slow, held back by the $\ln^2$ correction — see `graphics/FS_escape_ridge.png`, left panel).

## 3. The ridge and its drifting exponent

Inverting $X = x_{FS}(N) \sim C\,N^{3/2}/\ln^2 N$ for the prime value $y = N$ as a function of $X$:
$$y \sim \Big(\frac{X}{C}\Big)^{2/3} (\ln y)^{4/3}.$$
The leading behavior is $y \sim X^{2/3}$, with a slowly-growing $(\ln y)^{4/3}$ factor. Because that log factor inflates the *effective* exponent at finite scale, the **local** power $b$ in $y \sim X^{b}$ is not $2/3$ until very large $N$; it drifts down toward it:

| range of $N$ | up to $10^3$ | $10^4$ | $10^5$ | $10^6$ | $\to \infty$ |
|---|---|---|---|---|---|
| ridge power $b$ | 0.84–0.85 | 0.81 | 0.78 | 0.75 | $2/3 \approx 0.667$ |

(see `graphics/FS_escape_ridge.png`, right panel).

## 4. The regression, explained

The "Factor Skyline 1000" sheet fit the ridge with a power law $y = 0.966\,x^{0.86}$ and a cubic ($R^2 = 0.9993$). Both are now accounted for:

- **The power $0.86$** matches the computed local ridge exponent $\approx 0.85$ at $N \sim 10^3$ to within measurement — the fit was correct, and it was measuring the ridge at that scale.
- **Why the cubic fit better.** The true exponent is not constant; it slides from $\approx 0.85$ toward $2/3$. A single power law can only match locally, whereas a cubic is a flexible local stand-in for a power law with a slowly-varying exponent — hence the near-perfect $R^2$.

So the empirical regression was a faithful measurement of a real curve: the escape ridge $y \sim X^{2/3}$, reading $\approx X^{0.85}$ at the scale of a few thousand because of the logarithmic drift. And the curve's bend is the signature of the sieve's $p^2$ sweeps — the same activation-at-the-square that the wheel is built from.

---

## Appendix. Reproduction

```python
def spf_sieve(n):
    spf = list(range(n + 1)); i = 2
    while i * i <= n:
        if spf[i] == i:
            for j in range(i*i, n + 1, i):
                if spf[j] == j: spf[j] = i
        i += 1
    return spf

def factor_skyline(N):
    spf = spf_sieve(N)
    x = 1; ridge = []                 # (x_FS, prime value)
    for n in range(2, N + 1):
        x += 1 if spf[n] == n else spf[n]   # dx: 1 for primes, lpf for composites
        if spf[n] == n:
            ridge.append((x, n))
    return ridge

r = factor_skyline(1000)
print([X for X, p in r if p == 521])   # -> [1496], matching the Desmos table
```

## References

- A. Proxmire, *The Architectural Foundation of the Factor Skyline* (this repository) — the $x_{FS}$ coordinate and activation at prime squares.
- A. Proxmire, *Synthesis — Two Operations on the Factor Skyline* (this repository) — the wheel, the sweeps, and doubling.
- Mertens' third theorem; the prime number theorem.
- Figure: `graphics/FS_escape_ridge.png`.
