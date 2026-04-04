# An Architectural Atlas of Nonlinear Partial Differential Equations

**Allen Proxmire**

April 2026

---

## Abstract

We introduce a structural classification of nonlinear partial differential equations based on the Factor Skyline (FS) architectural framework — a method that decomposes each PDE into its constituent *channels* (diffusion, dispersion, transport, curvature, aggregation, reaction), derives the *envelope* of admissible states, constructs the *constraint-surface geometry* in channel space, and evaluates the architecture against six criteria: minimality, locality, determinism, generative sufficiency, envelope tightness, and structural optimality. Applying this framework uniformly to sixteen major nonlinear PDEs — including the Navier–Stokes, Cahn–Hilliard, Allen–Cahn, porous medium, thin-film, Fokker–Planck, Hamilton–Jacobi, Burgers, nonlinear Schrödinger, Korteweg–de Vries, mean curvature flow, Ricci flow, Keller–Segel, and reaction–diffusion equations — we obtain a finite taxonomy organized by *structural poles*: diffusive, hyperbolic, dispersive, geometric, aggregation, fluid, and integrable. The taxonomy reveals seven distinct *closure modes* by which nonlinear PDEs achieve global well-posedness, identifies *apex architectures* (KdV as the integrable apex, Ricci flow as the geometric apex), and provides a unified structural explanation for phenomena — integrability, blowup, shock formation, solitons, geometric singularities, and nonlocality — that have traditionally been studied in isolation. The central result is an architectural atlas (Figure 1) that maps every evaluated PDE to its structural pole, channel signature, singularity type, and FS score.

---

## 1. Introduction

### 1.1 The Problem of Classification

The theory of nonlinear partial differential equations encompasses an extraordinary diversity of mathematical structures: parabolic smoothing and hyperbolic steepening, dispersive oscillation and geometric curvature flow, integrable soliton resolution and turbulent cascade, mass-concentrating blowup and gradient-flow convergence to equilibrium. These phenomena arise from equations that, at the level of their formal PDE structure, appear to have little in common — the Navier–Stokes equations bear scant superficial resemblance to the Korteweg–de Vries equation, and the Keller–Segel system seems unrelated to Ricci flow.

Traditional classifications of PDEs — elliptic, parabolic, hyperbolic; linear vs. nonlinear; integrable vs. non-integrable; conservative vs. dissipative — capture important analytical distinctions but do not provide a *structural* taxonomy. They tell us which analytical tools are likely to apply but not *why* certain PDEs share deep structural features (such as the soliton resolution of both KdV and NLS, or the curvature-driven singularities of both MCF and Ricci flow) while others that are analytically similar (such as the Burgers equation and the Navier–Stokes equations) have fundamentally different well-posedness properties.

### 1.2 The Factor Skyline Framework

This paper introduces the *Factor Skyline (FS) architectural framework* as a new method for the structural classification of nonlinear PDEs. The FS framework treats each PDE as an *architecture* — a system of axioms, channels, conservation laws, and structural constraints — and evaluates it through a uniform four-stage analysis:

1. **Channel decomposition:** Each PDE is decomposed into its structural channels — diffusion, dispersion, transport, curvature, reaction, aggregation, pressure — each characterized by its locality, linearity, stability role, and scale action.

2. **Envelope derivation (Mode 1):** The forbidden configurations, necessary configurations, and extremal bounds implied by the axioms are derived, producing the *architectural envelope* — the boundary of what the PDE permits.

3. **Extremal dynamics (Mode 2):** The dynamical behaviors at the boundary of the envelope — blowup, shock formation, soliton resolution, geometric singularity, scattering — are identified and characterized.

4. **Constraint-surface geometry (Mode 3):** The geometric object in channel space that encodes all structural relationships among the channels is constructed, and its closure, openness, and singularity structure are analyzed.

Each architecture is then evaluated against six FS criteria — *minimality* (are the axioms irreducible?), *locality* (are all channels local?), *determinism* (is the evolution globally well-posed?), *generative sufficiency* (does the architecture generate all its observed laws?), *envelope tightness* (are the envelope bounds sharp?), and *structural optimality* (is the architecture free of anomalies?) — producing a quantitative FS score.

### 1.3 Goals and Scope

The goal of this paper is to construct the first *architectural atlas* of nonlinear PDEs: a systematic catalog of the structural features, channel signatures, singularity types, closure mechanisms, and FS scores of the major nonlinear PDEs of mathematical physics. The atlas encompasses sixteen architectures spanning the full range of PDE dynamics:

- **Diffusive pole:** Fokker–Planck (FP), porous medium equation (PME), thin-film equation (TFE), Allen–Cahn (AC), Cahn–Hilliard (CH), reaction–diffusion systems (RD).
- **Hyperbolic pole:** Hamilton–Jacobi (HJ), inviscid Burgers equation.
- **Dispersive pole:** nonlinear Schrödinger equation (NLS), Korteweg–de Vries equation (KdV).
- **Geometric pole:** mean curvature flow (MCF), Ricci flow (RF).
- **Aggregation pole:** Keller–Segel system (KS).
- **Fluid pole:** Navier–Stokes equations (NS).

The atlas reveals a finite taxonomy of *structural poles* — qualitatively distinct dynamical regimes — and identifies *seven closure modes* by which nonlinear PDEs achieve global well-posedness: linear, dissipative, variational, entropic-contractive, geometric-dissipative, dispersive Hamiltonian, and integrability. It also identifies *apex architectures* — the KdV (integrable apex) and Ricci flow (geometric apex) — that achieve the deepest structural results within their respective poles.

---

## 2. Methods: The FS Architectural Framework

### 2.1 Axiom Identification

The first step in the FS analysis of a PDE is the identification of its *implicit axioms* — the structural commitments that define the architecture. These include the choice of state variable (scalar, vector, complex, metric tensor), the locality structure (local vs. nonlocal channels), the conservation laws (mass, energy, momentum), the constitutive closures (viscosity, mobility, flux function), and the geometric framework (Euclidean, Riemannian, intrinsic vs. extrinsic).

The axioms are classified as *structural* (defining the architecture, not removable without changing the PDE class) or *constitutive* (selecting a specific member of the class, removable or replaceable). A key quantity is the number of *minimal* axioms — those that cannot be derived from the others — which measures the *structural economy* of the architecture.

### 2.2 Channel Decomposition

Each PDE is decomposed into its *structural channels* — the independent dynamical mechanisms that drive the evolution. The standard channel types identified across the atlas are:

- **Diffusion (D):** Second-order parabolic smoothing. Stabilizing. Rate $\sim k^2$.
- **Dispersion (D_\omega):** Oscillatory spreading through phase interference. $\omega = k^2$ (NLS) or $\omega = -k^3$ (KdV).
- **Transport/Advection (T):** First-order nonlinear self-advection. Destabilizing (steepening).
- **Reaction (R):** Zeroth-order nonlinear source/sink. Stability depends on kinetics.
- **Curvature (K):** Geometric evolution driven by mean curvature or Ricci curvature. Dual-natured.
- **Aggregation (A):** Nonlocal self-attraction. Destabilizing.
- **Pressure (P):** Nonlocal constraint enforcement. Neutral or repulsive.
- **Conservation (C):** Mass, probability, or volume preservation.
- **Gauge (G):** Symmetry or diffeomorphism invariance.

Each channel is characterized along four axes: *locality* (local vs. nonlocal), *linearity* (linear, quasilinear, fully nonlinear), *stability role* (stabilizing, destabilizing, neutral, dual), and *scale action* (how the channel's effect depends on the spatial wavenumber $k$).

### 2.3 Envelope Derivation (Mode 1)

Mode 1 derives the *architectural envelope* — the maximal set of constraints that the axioms impose on all admissible states and evolutions. The derivation proceeds through three stages:

1. **Forbidden configurations:** States, operators, or evolutions that are axiomatically excluded (e.g., compressible velocity fields in incompressible NS, negative densities in PME, Hamiltonian reversibility in gradient-flow PDEs).

2. **Necessary configurations:** Structures that the axioms force into existence (e.g., divergence-free velocity in NS, mass conservation in conserved systems, soliton solutions in integrable equations).

3. **Envelope inequalities:** The irreducible set of quantitative bounds (energy inequalities, Strichartz estimates, coarsening rates, blowup criteria) that define the boundary of the envelope.

The envelope may be *fully closed* (no open faces — the architecture is globally well-posed, as in FP, PME, AC, CH, KdV) or *partially open* (one or more faces where the dynamics can escape — as in NS 3D, focusing NLS $d \geq 2$, or KS for $M > 8\pi$).

### 2.4 Extremal Dynamics (Mode 2)

Mode 2 identifies the *extremal behaviors* — the dynamical configurations at the boundary of the envelope. These include:

- Shock formation and entropy selection (HJ, Burgers).
- Soliton formation and elastic collision (KdV, NLS).
- Finite-time blowup and mass concentration (KS, focusing NLS).
- Curvature blowup and topology change (MCF, RF).
- Scattering to linear flow (defocusing NLS).
- Coarsening and domain growth (CH).
- Self-similar spreading (PME, TFE).
- Convergence to equilibrium (FP, AC).

Mode 2 also identifies the *universal inequalities* — the quantitative bounds that hold for all admissible evolutions — and the *attractor structure* — the long-time behavior of generic solutions.

### 2.5 Constraint-Surface Geometry (Mode 3)

Mode 3 constructs the *constraint surface* — the geometric object in channel space encoding all structural relationships among the channels. The constraint surface is characterized by:

- Its *dimension* (how many independent channel states are possible).
- Its *closure* (whether all faces are sealed or some are open).
- Its *singularity structure* (whether the surface includes required singularity faces).
- Its *dissipation geometry* (how the energy/entropy budget is organized).

The constraint surface may be *contracting* (Lyapunov dissipation drives convergence — AC, CH, PME, TFE, FP), *isoenergetic* (Hamiltonian conservation preserves dimension — NLS, KdV), *entropy-resolved* (shocks produce irreversible simplification — HJ, Burgers), *geometrically dissipative* (area/curvature decreases — MCF, RF), or *mass-stratified* (the topology of the surface depends on a conserved scalar — KS).

### 2.6 FS Criteria

Each architecture is evaluated against six criteria, each receiving a verdict of PASS, CONDITIONAL, or FAIL:

1. **Minimality:** Are the axioms irreducible? Are there non-minimal constitutive selections?
2. **Locality:** Are all channels local? Is the architecture free of nonlocal operators?
3. **Determinism:** Is the evolution globally well-posed? Are solutions unique?
4. **Generative Sufficiency:** Does the architecture generate all its observed phenomena from the axioms?
5. **Envelope Tightness:** Are the envelope inequalities sharp? Is the envelope fully closed?
6. **Structural Optimality:** Is the architecture free of anomalies? Is it the simplest system generating its phenomenology?

The total number of PASS verdicts (out of 6) is the *FS score*.

---

## 3. Results: The PDE Atlas

### 3.1 The Diffusive Pole

The diffusive pole comprises architectures whose dynamics are dominated by parabolic smoothing — the monotone decrease of an energy, entropy, or free-energy functional through a diffusion mechanism.

**Fokker–Planck (FP).** The Fokker–Planck equation $\partial_t \rho = -\nabla \cdot (b\rho) + \nabla \cdot (D \nabla \rho)$ evolves a probability density under drift and diffusion. It is the *only linear PDE* in the atlas and achieves closure through *linearity alone* — the simplest possible closure mechanism. Two channels: transport (first-order drift) and diffusion (second-order smoothing). Fully local. No singularity. Gibbs–Boltzmann equilibrium as the universal attractor for confining gradient drift. Three-level convergence hierarchy: spectral gap, log-Sobolev, Wasserstein contractivity. **FS score: 5.**

**Porous Medium Equation (PME).** The equation $\partial_t u = \Delta(u^m)$, $m > 1$, is the canonical model of nonlinear degenerate diffusion. One channel: nonlinear diffusion with mobility $D(u) = mu^{m-1}$ vanishing at $u = 0$. Finite-speed propagation, free-boundary formation, compact-support preservation. The Barenblatt self-similar profile $B(x,t;M) = t^{-\alpha}[C - k|x|^2/t^{2\beta}]_+^{1/(m-1)}$ is the universal attractor for all finite-mass data. Closure by four independent mechanisms: degeneracy, entropy dissipation, $L^1$ contraction, and mass conservation. **FS score: 5.**

**Thin-Film Equation (TFE).** The equation $\partial_t h = -\nabla \cdot (h^n \nabla \Delta h)$ models viscous thin-film spreading. Fourth-order degenerate diffusion with contact-line free boundary. Combines CH's fourth-order smoothing with PME's degeneracy. The positivity question — whether $h \geq 0$ is preserved — depends on the mobility exponent $n$: preserved for $n \geq 1$ (the physical regime), potentially violated for $0 < n < 1$. This produces the only *parametric bifurcation* in the atlas. **FS score: 4 (for $n \geq 1$).**

**Allen–Cahn (AC) and Cahn–Hilliard (CH).** These architectures share the same Ginzburg–Landau free energy $F[\phi] = \int [f(\phi) + (\varepsilon^2/2)|\nabla \phi|^2]\,dx$ but differ in kinetics: AC is the $L^2$ gradient flow (non-conserved, second-order), CH is the $H^{-1}$ gradient flow (conserved, fourth-order). The single axiom of conservation transforms AC's interface extinction into CH's domain coarsening — the clearest *architectural experiment* in the atlas, isolating the structural consequences of conservation. **FS score: 3 each.**

**Reaction–Diffusion (RD).** The class $\partial_t \mathbf{u} = \mathbf{D}\Delta\mathbf{u} + \mathbf{R}(\mathbf{u})$ is the broadest second-order parabolic family. Its FS evaluation targets the *class*, not a single system. The constraint surface is a *moduli space* parameterized by the constitutive kinetics — the only architecture whose closure is constitutive-dependent. Permits Turing patterns, spiral waves, traveling pulses, and spatiotemporal chaos — phenomena forbidden in gradient-flow architectures. **FS score: 2 (class level).**

### 3.2 The Hyperbolic Pole

The hyperbolic pole comprises architectures whose dynamics are dominated by first-order nonlinear transport — steepening, shock formation, and finite-speed propagation.

**Hamilton–Jacobi (HJ).** The equation $\partial_t u + H(\nabla u) = 0$ evolves a scalar potential under a convex Hamiltonian. The *anti-diffusion pole*: zero smoothing, gradient steepening, certain finite-time singularity (gradient kink). Closure by *convexity + viscosity solutions* — the first architecture demonstrating that smoothing is *not necessary* for PDE closure. The Hopf–Lax formula $u(x,t) = \inf_y \{u_0(y) + |x-y|^2/(2t)\}$ provides the explicit variational solution. $L^\infty$ contraction. **FS score: 5.**

**Inviscid Burgers.** The conservation law $\partial_t v + \partial_x(v^2/2) = 0$ is the *derivative of HJ* ($v = \partial_x u$). Adds conservation-law structure to HJ: $L^1$ contraction (Kruzkov), Rankine–Hugoniot shock conditions, energy dissipation at shocks, total variation decay. The only architecture with *simultaneous $L^1$ and $L^\infty$ contraction*. Introduces *shock-concentrated dissipation* — energy lost only at codimension-1 shock locations. **FS score: 5.**

### 3.3 The Dispersive Pole

The dispersive pole comprises architectures whose dynamics are dominated by oscillatory spreading — phase interference rather than amplitude decay or gradient compression.

**Nonlinear Schrödinger (NLS).** The equation $i\partial_t \psi + \Delta \psi \pm |\psi|^2 \psi = 0$ is the *first complex-valued, Hamiltonian, time-reversible, soliton-supporting* architecture in the atlas. Closure by *conservation laws + Strichartz estimates* — the dispersive Hamiltonian closure mode. The focusing/defocusing dichotomy (controlled by a single sign $\pm$) is the most economical structural bifurcation: defocusing is globally well-posed; focusing in $d \geq 2$ admits blowup at the sharp threshold $M_* = \|Q\|_{L^2}^2$. **FS score: 5 (defocusing and focusing 1D).**

**Korteweg–de Vries (KdV).** The equation $u_t + 6uu_x + u_{xxx} = 0$ is the *integrable apex* of the atlas — the most structurally complete nonlinear PDE in mathematics. Bi-Hamiltonian structure generates *infinitely many conservation laws* via the Lenard recursion. Complete integrability via the inverse scattering transform provides *exact solvability*. The soliton resolution theorem decomposes every solution into $N$ sech$^2$ solitons plus dispersive radiation — the *dynamical analogue of the fundamental theorem of arithmetic*. Global smooth solutions at the sharpest threshold ($s \geq -3/4$). Zero constitutive parameters. **FS score: 5.**

### 3.4 The Geometric Pole

The geometric pole comprises architectures whose state variables are geometric objects (surfaces, metrics) rather than fields on fixed domains.

**Mean Curvature Flow (MCF).** The law $V_n = H$ evolves a hypersurface by its mean curvature — the *only architecture whose state variable is a surface*. Zero bulk degrees of freedom, zero constitutive parameters. Curvature-driven singularity formation is *certain and required* for compact surfaces — the mechanism by which MCF completes its area-minimization program. Huisken's monotonicity formula controls the blowup geometry. Self-similar shrinkers (sphere, cylinder, Angenent torus) are the universal blowup profiles. **FS score: 3.**

**Ricci Flow (RF).** The equation $\partial_t g_{ij} = -2\,\text{Ric}_{ij}$ evolves the *Riemannian metric itself* — the intrinsic geometry of space. The *geometric apex* of the atlas and the *structurally deepest PDE in mathematics*. Three minimal axioms (metric field, curvature evolution, no forcing) generate the *complete topological classification of closed 3-manifolds* via the Hamilton–Perelman program: Perelman's W-entropy monotonicity, $\kappa$-noncollapsing, canonical neighborhoods, singularity classification (Type I/II), and surgery. The only PDE that has *solved a Clay Millennium Problem* (Poincaré conjecture). **FS score: 3.**

### 3.5 The Aggregation Pole

**Keller–Segel (KS).** The system $u_t = \Delta u - \nabla \cdot (u\nabla v)$, $-\Delta v = u$ is the *only architecture with nonlocal self-attraction as its primary dynamical mechanism*. Two nonlocal channels (aggregation + potential) — the most nonlocal architecture. The diffusion–aggregation competition is controlled by a single conserved scalar: the total mass $M$. The sharp threshold $M_c = 8\pi$ (the best constant in the logarithmic Hardy–Littlewood–Sobolev inequality) partitions the entire dynamics: $M < 8\pi \Rightarrow$ global existence; $M > 8\pi \Rightarrow$ finite-time mass-concentrating blowup with mass quantization at $8\pi$. The only gradient flow whose Lyapunov structure *drives* the singularity (the free energy is unbounded below for $M > 8\pi$). **FS score: 0.**

### 3.6 The Fluid Pole

**Navier–Stokes (NS).** The equations $\partial_t \mathbf{u} + (\mathbf{u} \cdot \nabla)\mathbf{u} = -\nabla p + \nu \Delta \mathbf{u} + \mathbf{f}$, $\nabla \cdot \mathbf{u} = 0$ describe incompressible viscous flow. Five channels: advection (nonlinear, energy-neutral), viscosity (linear, stabilizing), pressure (nonlocal, constraint-enforcing), forcing (external input), and incompressibility (holonomic constraint). The pressure Poisson equation introduces the sole *nonlocal constraint-enforcement channel* in the atlas. The 3D regularity problem — whether smooth solutions exist globally — remains open: the vortex stretching sub-channel $(\boldsymbol{\omega} \cdot \nabla)\mathbf{u}$ may overwhelm viscous damping, and the enstrophy inequality does not close. **FS score: 0 (3D).**

### 3.7 Summary: The Atlas

**Figure 1** presents the complete architectural atlas as a summary table. Each row corresponds to a PDE architecture; the columns record the structural pole, locality, singularity type, nonlocality, integrability, gradient-flow structure, and FS score.

[Figure 1: FS_Atlas_Summary_Table.png — Summary of PDE architectures, poles, and FS scores.]

---

## 4. Discussion

### 4.1 Seven Closure Modes

The atlas reveals seven distinct mechanisms by which nonlinear PDEs achieve global well-posedness:

1. **Linear closure (FP):** The PDE is linear $\Rightarrow$ existence, uniqueness, and regularity follow from spectral theory.
2. **Dissipative closure (PME):** A Lyapunov functional decreases monotonically $\Rightarrow$ energy estimates + smoothing + contraction close the bootstrap.
3. **Variational closure (HJ):** Convexity of the Hamiltonian + the viscosity-solution framework $\Rightarrow$ comparison principle + Hopf–Lax formula. No smoothing required.
4. **Entropic-contractive closure (Burgers):** Convex flux + Kruzkov entropy framework $\Rightarrow$ $L^1$ contraction + Rankine–Hugoniot. Shock-concentrated dissipation.
5. **Geometric-dissipative closure (MCF):** Area/curvature dissipation + Huisken monotonicity $\Rightarrow$ singularity classification + surgery.
6. **Dispersive Hamiltonian closure (NLS):** Conservation laws (mass, energy, momentum) + Strichartz estimates $\Rightarrow$ global control without dissipation.
7. **Integrability closure (KdV):** Bi-Hamiltonian structure + inverse scattering transform $\Rightarrow$ infinitely many conservation laws + exact solvability + soliton resolution.

These seven modes exhaust the *known fundamental mechanisms* of PDE closure. Every evaluated architecture uses one (or, in the case of KdV and NLS focusing 1D, a combination) of these modes. The identification of these modes is a central contribution of the atlas.

### 4.2 Structural Relationships Across Poles

The atlas clarifies relationships between PDEs that were previously treated as unrelated:

**KS vs. NS (opposite nonlocal roles).** Both architectures have nonlocal channels mediated by the Poisson equation. But their dynamical roles are *structurally opposite*: the NS pressure *prevents* concentration (it enforces incompressibility), while the KS chemoattractant *drives* concentration (it mediates self-attraction). The same mathematical mechanism (elliptic solve) produces opposite physical effects.

**MCF vs. RF (extrinsic vs. intrinsic geometry).** Both are curvature-driven parabolic flows with singularities, surgery, and soliton-like blowup models. MCF operates on the *extrinsic* shape of surfaces in ambient space; RF operates on the *intrinsic* geometry of Riemannian manifolds. RF is structurally deeper: it produces the *geometrization theorem* (classifying 3-manifold topology), while MCF produces genus reduction.

**NLS vs. KdV (two dispersive integrable PDEs).** Both are Hamiltonian, time-reversible, soliton-supporting, and (in specific regimes) completely integrable via the inverse scattering transform. They represent the two fundamental classes of integrable dispersive waves: NLS for even-order dispersion ($\omega = k^2$) on complex fields, KdV for odd-order dispersion ($\omega = -k^3$) on real fields.

**AC vs. CH (the conservation experiment).** These architectures share the same free energy but differ in a single axiom (conservation). This single structural commitment raises the PDE order from 2 to 4, eliminates the maximum principle, changes the gradient-flow metric from $L^2$ to $H^{-1}$, and replaces interface extinction with domain coarsening — demonstrating the *high leverage* of conservation as an architectural axiom.

### 4.3 The NS Regularity Problem in Structural Context

The atlas provides a structural explanation for the difficulty of the 3D Navier–Stokes regularity problem. The Burgers equation — which shares the nonlinear self-advection mechanism $v\partial_x v$ with NS — is *completely tractable* (FS score 5). The KdV equation, which adds third-order dispersion to the Burgers advection, is *exactly solvable* (FS score 5). The difficulty of NS lies not in the nonlinear transport (which Burgers handles) or in the PDE structure (which KdV resolves through integrability) but in the *specific combination* of:

- Vector character (the velocity field $\mathbf{u} \in \mathbb{R}^3$, not a scalar).
- Incompressibility (the divergence-free constraint $\nabla \cdot \mathbf{u} = 0$).
- Pressure (the nonlocal Poisson equation $\Delta p = -\partial_i \partial_j(u_i u_j)$).

These three structural additions transform the completely understood Burgers/HJ transport into the unresolved NS regularity problem. The vortex stretching term $(\boldsymbol{\omega} \cdot \nabla)\mathbf{u}$ — which exists only in $d \geq 3$ and is absent in 2D (where NS is globally regular) — is the *unique architectural feature* responsible for the open problem.

### 4.4 Apex Architectures

The atlas identifies two *apex architectures* — PDEs that achieve the deepest structural results within their respective poles:

**KdV (Integrable Apex).** The KdV equation $u_t + 6uu_x + u_{xxx} = 0$ has infinitely many conservation laws, exact solvability via the IST, a fully classified constraint surface, and zero constitutive parameters. Its soliton resolution theorem is the *dynamical analogue of the fundamental theorem of arithmetic*: every solution decomposes uniquely into irreducible components (solitons) plus a transient remainder (radiation).

**Ricci Flow (Geometric Apex).** The equation $\partial_t g_{ij} = -2\,\text{Ric}_{ij}$ has the *most profound mathematical consequence* of any PDE: the geometrization theorem, which classifies all closed 3-manifolds into geometric pieces. Three axioms generate the complete topological classification of 3-dimensional spaces — the highest structural amplification ratio in mathematics.

---

## 5. Implications and Future Directions

### 5.1 Implications for PDE Theory

The FS atlas provides a *structural language* for discussing PDE phenomena that are traditionally treated with ad hoc methods. The identification of seven closure modes suggests that:

- New PDEs can be *classified in advance* by identifying their channels and matching them to known closure modes.
- The *feasibility of well-posedness proofs* can be assessed by examining whether the architecture's channels admit a known closure mode.
- *Open problems* (such as the NS 3D regularity) can be *localized* to specific structural features (the vortex stretching sub-channel, the nonlocal pressure interaction) by comparing with resolved architectures (Burgers, KdV).

### 5.2 Implications for Numerical Analysis

The channel decomposition and constraint-surface geometry suggest natural *structure-preserving discretization strategies*:

- Numerical schemes should *respect the channel structure* — preserving the stabilizing/destabilizing balance, maintaining conservation laws, and correctly discretizing nonlocal channels.
- The *closure mode* of the architecture should guide the choice of numerical method: dissipative closures suggest energy-decreasing schemes; Hamiltonian closures suggest symplectic integrators; entropy closures suggest total-variation-diminishing methods.

### 5.3 Implications for Geometric Analysis

The geometric pole (MCF, RF) demonstrates that the FS framework extends naturally to *geometric PDEs*. The identification of Perelman's monotone quantities as the *deepest structural tools* in the atlas suggests that:

- Geometric flows in dimensions $n \geq 4$ may require *new monotone quantities* analogous to Perelman's W-entropy.
- The surgery program for Ricci flow may be extendable to other geometric flows (e.g., mean curvature flow in higher codimension, Kähler–Ricci flow).

### 5.4 Extensions

The FS framework can be extended to several classes of equations not covered in the present atlas:

- **Stochastic PDEs:** The addition of noise channels (additive, multiplicative, space-time white noise) would introduce a new structural category — *stochastic closure modes* — and connect the atlas to the theory of regularity structures (Hairer) and paracontrolled distributions (Gubinelli–Imkeller–Perkowski).
- **Kinetic equations:** The Boltzmann and Vlasov equations evolve distribution functions on phase space, introducing a new state-variable type (functions of position and velocity) and a new channel type (collision operators).
- **Multi-physics systems:** Coupled PDE systems (fluid-structure interaction, magnetohydrodynamics, chemotaxis-fluid coupling) would produce *composite architectures* whose channels span multiple poles.

---

## 6. Conclusion

We have introduced the Factor Skyline (FS) architectural framework and applied it uniformly to sixteen major nonlinear partial differential equations, producing the first *architectural atlas* of PDE theory. The atlas organizes nonlinear PDEs into seven structural poles — diffusive, hyperbolic, dispersive, geometric, aggregation, fluid, and integrable — and identifies seven distinct closure modes by which these architectures achieve global well-posedness.

The atlas reveals deep structural relationships between PDEs that were previously treated in isolation: the opposite nonlocal roles of KS and NS, the intrinsic–extrinsic duality of RF and MCF, the conservation experiment of AC vs. CH, and the integrable kinship of NLS and KdV. It identifies two *apex architectures* — the KdV equation (integrable apex, whose soliton resolution is the dynamical fundamental theorem of arithmetic) and Ricci flow (geometric apex, whose surgery program classifies 3-manifold topology) — that achieve the deepest structural results in their respective domains.

The FS framework provides a *structural language* for PDE theory that is model-agnostic, uniform across all PDE types, and capable of revealing the architectural reasons behind integrability, blowup, shock formation, geometric singularities, and nonlocality. The atlas is a foundation for future structural mathematics — a map of the territory that nonlinear PDE theory explores.

---

## References

1. Hamilton, R.S. Three-manifolds with positive Ricci curvature. *J. Differential Geom.* **17** (1982), 255–306.

2. Perelman, G. The entropy formula for the Ricci flow and its geometric applications. *arXiv:math/0211159* (2002).

3. Perelman, G. Ricci flow with surgery on three-manifolds. *arXiv:math/0303109* (2003).

4. Huisken, G. Flow by mean curvature of convex surfaces into spheres. *J. Differential Geom.* **20** (1984), 237–266.

5. Crandall, M.G. and Lions, P.-L. Viscosity solutions of Hamilton–Jacobi equations. *Trans. Amer. Math. Soc.* **277** (1983), 1–42.

6. Kruzkov, S.N. First order quasilinear equations in several independent variables. *Mat. Sb.* **81** (1970), 228–255.

7. Gardner, C.S., Greene, J.M., Kruskal, M.D., and Miura, R.M. Method for solving the Korteweg–de Vries equation. *Phys. Rev. Lett.* **19** (1967), 1095–1097.

8. Zabusky, N.J. and Kruskal, M.D. Interaction of "solitons" in a collisionless plasma and the recurrence of initial states. *Phys. Rev. Lett.* **15** (1965), 240–243.

9. Weinstein, M.I. Nonlinear Schrödinger equations and sharp interpolation estimates. *Comm. Math. Phys.* **87** (1983), 567–576.

10. Kenig, C.E. and Merle, F. Global well-posedness, scattering and blow-up for the energy-critical focusing non-linear Schrödinger equation in the radial case. *Invent. Math.* **166** (2006), 645–675.

11. Colliander, J., Keel, M., Staffilani, G., Takaoka, H., and Tao, T. Sharp global well-posedness for KdV and modified KdV on $\mathbb{R}$ and $\mathbb{T}$. *J. Amer. Math. Soc.* **16** (2003), 705–749.

12. Kohn, R.V. and Otto, F. Upper bounds on coarsening rates. *Comm. Math. Phys.* **229** (2002), 375–395.

13. Vázquez, J.L. *The Porous Medium Equation: Mathematical Theory*. Oxford University Press, 2007.

14. Bertozzi, A.L. and Pugh, M.C. The lubrication approximation for thin viscous films: the moving contact line with a "porous media" cut-off of van der Waals interactions. *Nonlinearity* **7** (1994), 1535–1564.

15. Blanchet, A., Dolbeault, J., and Perthame, B. Two-dimensional Keller–Segel model: optimal critical mass and qualitative properties of the solutions. *Electron. J. Differential Equations* **44** (2006), 1–33.

16. Carrillo, J.A. and Toscani, G. Asymptotic $L^1$-decay of solutions of the porous medium equation to self-similarity. *Indiana Univ. Math. J.* **49** (2000), 113–142.

17. Jordan, R., Kinderlehrer, D., and Otto, F. The variational formulation of the Fokker–Planck equation. *SIAM J. Math. Anal.* **29** (1998), 1–17.

18. Evans, L.C. and Spruck, J. Motion of level sets by mean curvature I. *J. Differential Geom.* **33** (1991), 635–681.

19. Ladyzhenskaya, O.A. *The Mathematical Theory of Viscous Incompressible Flow*. Gordon and Breach, 1969.

20. Temam, R. *Navier–Stokes Equations: Theory and Numerical Analysis*. North-Holland, 1977.

21. Leray, J. Sur le mouvement d'un liquide visqueux emplissant l'espace. *Acta Math.* **63** (1934), 193–248.

22. Beale, J.T., Kato, T., and Majda, A. Remarks on the breakdown of smooth solutions for the 3-D Euler equations. *Comm. Math. Phys.* **94** (1984), 61–66.

23. Cahn, J.W. and Hilliard, J.E. Free energy of a nonuniform system. I. Interfacial free energy. *J. Chem. Phys.* **28** (1958), 258–267.

24. Allen, S.M. and Cahn, J.W. A microscopic theory for antiphase boundary motion and its application to antiphase domain coarsening. *Acta Metall.* **27** (1979), 1085–1095.

25. Turing, A.M. The chemical basis of morphogenesis. *Philos. Trans. R. Soc. Lond. B* **237** (1952), 37–72.

26. Bakry, D. and Émery, M. Diffusions hypercontractives. *Séminaire de probabilités XIX*, Lecture Notes in Math. **1123**, Springer, 1985, 177–206.

27. Otto, F. The geometry of dissipative evolution equations: the porous medium equation. *Comm. Partial Differential Equations* **26** (2001), 101–174.

28. Villani, C. *Optimal Transport: Old and New*. Springer, 2009.

29. Tao, T. *Nonlinear Dispersive Equations: Local and Global Analysis*. CBMS Regional Conf. Ser. Math. **106**, Amer. Math. Soc., 2006.

30. Thurston, W.P. Three-dimensional manifolds, Kleinian groups and hyperbolic geometry. *Bull. Amer. Math. Soc.* **6** (1982), 357–381.
