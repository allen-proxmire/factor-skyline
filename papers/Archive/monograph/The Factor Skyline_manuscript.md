**The Factor Skyline: a 2-Dimensional View of the Number Line**

Allen Proxmire  
16JAN26

**Abstract**

The classical number line presents the integers as isolated points arranged in a single dimension. In that view, each integer appears structureless, and the behavior of primes must be described statistically. This is why logarithmic laws dominate the study of prime distribution: they are the best analytic fit to patterns that appear irregular when seen in one dimension.

We propose a different perspective.

Each integer has an internal multiplicative structure that is lost when the integers are flattened onto the number line. When that structure is restored by lifting the integers into a second dimension, prime behavior becomes a geometric consequence rather than a statistical phenomenon.

In this two‑dimensional representation — the Factor Skyline — each integer is a column whose width is determined by its least prime factor and whose height is the remaining quotient. Prime squares introduce new horizontal layers; composite numbers are covered by the activation of smaller widths; primes appear as the columns that escape all activated widths.

In this geometry:

* prime thinning arises from the cumulative effect of coverage layers  
* the dominance of small primes follows from early activation  
* uniformity across residue classes reflects identical horizontal sweeps  
* unique factorization is the visible structure of each column

The logarithmic laws of prime distribution are not fundamental. They are artifacts of projecting this two‑dimensional geometry onto a one‑dimensional line.

This framework does not replace the integers. It restores the structure that the number line hides.

**1\. Introduction — Why the Number Line Misleads Us**

The number line presents the integers as isolated points arranged in a single dimension. In that view, each integer appears structureless, and the behavior of primes must be described statistically. This is why logarithmic laws dominate the study of prime distribution: they are the best analytic fit to patterns that look irregular when seen in one dimension.

But the number line is a projection.

It collapses the internal multiplicative structure of each integer into a point and hides the layered geometry that governs how the integers populate the natural numbers. When multiplicative depth is flattened into linear distance, logarithmic patterns appear. When a two‑dimensional structure is sliced into parallel sequences, residue classes appear uniform. When coverage layers are compressed into a single axis, prime thinning looks like a slow decay.

None of these phenomena originate on the line. They are artifacts of the projection.

To understand prime behavior, we need to restore the structure that the number line removes. The Factor Skyline provides that structure. It lifts each integer into a second dimension and represents it as a column whose width is determined by its least prime factor and whose height is the remaining quotient. In this geometry, classical features of prime distribution become architectural consequences:

* prime squares activate new horizontal layers

* small primes dominate because their widths appear earliest

* coverage layers sweep across the skyline

* primes emerge as the columns that escape all activated widths

* residue classes become vertical slices of a uniform structure

* unique factorization becomes the visible blueprint of each column

The number line shows us the results of these processes but not their causes.

The Factor Skyline reveals the geometry that produces them.

The goal of this framework is not to replace the integers but to recover the structure that the projection hides. Once that structure is visible, the familiar mysteries of prime behavior stop looking like analytic accidents and start looking like the inevitable consequences of a deeper geometry.

**2\. Construction — Lifting the Integers Into Two Dimensions**

To recover the structure that the number line removes, we represent each integer as a column built from unit squares. This construction introduces a second dimension that records multiplicative depth directly, rather than compressing it into a single coordinate.

For any integer *n*:

* its **width** is the least prime factor of *n*

* its **height** is the quotient *n*/width

If the height is composite, it has its own width and height, and so on. Each integer therefore becomes a finite stack of widths, each one determined by the next prime factor in its decomposition. This representation makes the internal structure of the integer visible rather than implicit.

Graphic 1: The Factor Skyline

![][image1]

The Factor Skyline changes the number coordinates from 1 \= (1,1), 2 \= (2,2), etc to a dynamic fluctuation. Above are the new and classic coordinates from 1 to 100\. Coordinates are taken from the top-right of each “number column”. So, 3 \= (3,3), 4 \= (5,2), 5 \= (6,5), 6 \= (8,3) and so on. 

Python to generate the new coordinates here: [https://github.com/allen-proxmire/factor-skyline](https://github.com/allen-proxmire/factor-skyline)

Prime squares introduce new horizontal layers.

When a prime *p* reaches its square *p*2, a new width‑*p* layer becomes active across the skyline. Every multiple of *p* receives a width‑*p* assignment at the appropriate height. These layers accumulate as *p* increases, producing a sequence of horizontal coverage bands that sweep across the geometry.

Small primes dominate the early structure because their squares appear earliest. Width‑2 activates first, covering half of all columns. Width‑3 activates next, covering a third of what remains. Width‑5, width‑7, and higher widths activate later and cover progressively smaller fractions. This sequence of activations creates a layered geometry in which each width removes a predictable portion of the available space.

In this construction, primes appear as the columns that escape all activated widths. A prime *p* is the first column in its width‑*p* layer that has no smaller width assigned at any height. Its position is determined by the cumulative effect of all earlier layers.

This two‑dimensional representation does not change the integers. It reveals the architecture that the number line hides.

Once the integers are lifted into this geometry, the mechanisms behind prime behavior become visible and can be analyzed directly.

**3\. Activation — When a Prime Square Enters the Geometry**

In the Factor Skyline, each prime *p* introduces structure only when its square *p*2 is reached. Before *p*2, the width‑*p* layer has no place to attach: there is no integer whose least prime factor is *p* until the first multiple of *p* that is not divisible by any smaller prime.

The moment *p*2 appears, the width‑*p* layer becomes active.

This activation has two immediate consequences:

**A new horizontal layer is created at height** *p***.**  

1. Every integer of the form *p*⋅*k* receives a width‑*p* assignment at the appropriate height, provided *k* has no smaller width.

**A new coverage sweep begins.**  

2. The width‑*p* layer removes a fraction 1/*p* of the remaining available columns, independent of their position on the number line.

This process is uniform across all primes.

Width‑2 activates first at 22 \= 4, covering half of all columns.

Width‑3 activates next at 32 \= 9, covering a third of what remains.

Width‑5 activates at 25, width‑7 at 49, and so on.

Each activation reduces the available space for future primes.

The skyline becomes progressively more constrained as more widths enter the geometry. The cumulative effect of these activations determines the long‑term density of escape points — the positions where primes can appear.

Activation is therefore the mechanism that initiates the structure behind prime thinning.

It is not a statistical trend but a geometric consequence of how widths enter the skyline. Once a width is active, its coverage is fixed and predictable, and the remaining space for primes is determined by the interaction of all activated layers.

This activation sequence is the foundation for the coverage and escape dynamics that follow.

**4\. Coverage — How Activated Widths Remove Available Space**

Once a width‑*p* layer becomes active at *p*2, it begins covering the skyline. Coverage is the process by which each activated width removes a fixed fraction of the remaining columns, independent of their position on the number line.

For a given prime *p*:

* the width‑*p* layer covers every column whose least prime factor is *p*

* these columns occur with natural density 1/*p* among the integers not already covered by smaller widths

* coverage is uniform across the skyline because it depends only on divisibility, not on location

Coverage is cumulative.

Width‑2 removes half of all columns.

Width‑3 removes a third of what remains.

Width‑5 removes a fifth of what remains after that.

Each new width reduces the available space for future primes by a predictable amount.

This cumulative reduction produces a narrowing corridor of available columns. The skyline becomes progressively more constrained as more widths activate. The remaining space is not random; it is the intersection of all uncovered positions after each width has removed its share.

Coverage therefore determines the long‑term density of escape points.

A prime *p* can only appear where all smaller widths have failed to assign coverage. The probability that a column escapes all activated widths up to *p* is the product of the remaining fractions:

![][image2]

This product decreases as more widths activate, reflecting the shrinking availability of uncovered columns. Prime thinning is the direct consequence of this cumulative coverage.

Coverage is not a statistical trend. It is a geometric process that removes space in fixed proportions.

Once a width is active, its effect is determined entirely by divisibility and does not vary across the skyline.

This mechanism sets the stage for escape, the process that identifies which columns become primes.

**5\. Escape — How Primes Emerge From the Coverage Process**

In the Factor Skyline, a prime appears when a column escapes all activated widths. Escape is the complement of coverage: it identifies the positions that remain unassigned after every active width has removed its share of the skyline.

For a prime *p*, escape occurs at the column whose least prime factor is *p*. This column must satisfy two conditions:

**It is not divisible by any smaller prime.**  

1. It must avoid all coverage layers created by widths 2,3,5,…, *p*−1.

**It is the first such column after the activation of width‑**p**.**  

2. Once width‑*p* activates at *p*2, the first uncovered column in the width‑*p* corridor becomes the prime *p*.

Escape is therefore a deterministic outcome of the cumulative coverage process. The position of each prime is determined by the interaction of all previously activated widths. The more widths that are active, the narrower the corridor of available columns becomes, and the farther apart escape events occur.

The probability that a column escapes all activated widths up to *p* is:

![][image2]

This product decreases as more primes activate, reflecting the shrinking availability of uncovered columns. Prime thinning is the direct result of this narrowing corridor. The gaps between primes grow because the space in which escape can occur becomes progressively smaller.

Escape also explains the uniformity of primes across residue classes.

Each residue class modulo *p* corresponds to a vertical slice of the skyline. Coverage layers sweep across all slices uniformly, and escape occurs wherever a slice remains uncovered. No residue class receives special treatment; the geometry enforces uniformity.

In this framework, primes are not anomalies or statistical outliers. They are the columns that remain after all structural constraints have been applied. Their distribution follows from the geometry of widths, activations, and coverage, not from randomness or analytic approximation.

Escape completes the mechanism that produces prime behavior.

With activation, coverage, and escape in place, the Factor Skyline provides a structural explanation for the classical patterns observed on the number line.

**6\. Density — How Coverage Determines the Long‑Term Frequency of Primes**

The cumulative effect of coverage layers determines the long‑term density of escape points. Each activated width removes a fixed fraction of the remaining columns, and the product of these removals defines how much space is left for primes.

For a prime *p*, the available space after all smaller widths have activated is:

![][image2]

This product decreases as more primes activate.

Each new width reduces the remaining corridor by a predictable proportion, independent of position. The narrowing of this corridor is the geometric origin of prime thinning.

This density product has two important properties:

**It decreases slowly.**  

1. Even after many widths have activated, a non‑zero fraction of columns remains uncovered. The corridor narrows, but it does not collapse.

**It decreases in a way that matches classical prime density.**  

The reciprocal of the density product grows approximately like log⁡*p*.

2. This is not because primes “follow logs,” but because the cumulative effect of removing fractions 1/2,1/3,1/5,… produces a corridor whose width shrinks at a rate comparable to 1/log⁡*p*.

In the Factor Skyline, this correspondence is structural rather than analytic.

The density of primes is not derived from integrals or asymptotics. It emerges from the geometry of widths and the fixed proportions they remove.

This framework also explains why prime density is stable across residue classes.

Each residue class modulo *p* corresponds to a vertical slice of the skyline. Coverage layers sweep across all slices uniformly, and the density product applies equally to each slice. No residue class receives more or less coverage; the geometry enforces uniformity.

The density of primes is therefore the visible consequence of:

* the order in which widths activate

* the fixed fractions they remove

* the cumulative narrowing of the escape corridor

Prime thinning is not a statistical trend. It is the direct result of how multiplicative structure occupies space in two dimensions.

With density established, the next step is to examine how this geometry produces the classical analytic approximations observed on the number line.

**7\. Approximation — Why Logarithms Appear on the Number Line**

When the Factor Skyline is projected back onto the number line, the geometric mechanisms of activation, coverage, and escape collapse into a single dimension. This flattening removes the structure that governs prime behavior and replaces it with a statistical appearance. Logarithmic laws arise from this projection, not from the underlying geometry.

The key quantity is the density of uncovered columns after all widths less than *p* have activated:

![][image2]

This product decreases slowly and behaves asymptotically like *e* − γ/log⁡*p*, where γ is the Euler–Mascheroni constant. The reciprocal of the density therefore grows approximately like log⁡*p*. This correspondence is the source of the classical logarithmic approximations for prime distribution.

On the number line, this appears as:

* the prime number theorem

* the logarithmic thinning of primes

* the use of log*⁡x* as the natural scale for prime gaps

* the appearance of logarithmic integrals in prime counting

In the Factor Skyline, these patterns are structural rather than analytic.

The density product shrinks at a rate that happens to match the reciprocal of a logarithm because removing fractions 1/2,1/3,1/5,… produces a corridor whose width decreases like 1/log*⁡p*. The logarithm is not the cause of prime thinning; it is the one‑dimensional expression of a two‑dimensional coverage process.

This explains why logarithmic approximations are accurate but incomplete.

They describe the projection of the geometry, not the geometry itself. They capture the long‑term trend of the density product but cannot express the layered structure that produces it. Error terms, fluctuations, and local irregularities arise because the projection hides the discrete activations and coverage sweeps that shape the skyline.

In this framework:

* logarithms measure the visible effect of cumulative coverage

* the prime number theorem reflects the long‑term narrowing of the escape corridor

* analytic fluctuations correspond to the discrete activation of new widths

* residue class uniformity follows from uniform coverage across slices

The classical analytic results are therefore consistent with the Factor Skyline, but they describe only the shadow of the structure. The geometry provides the mechanism; the logarithms record its projection.

With approximation understood, we can now examine how the skyline encodes the internal structure of each integer and how unique factorization becomes visible in two dimensions.

**FS–Number Line Translation.** *When the classical prime sequence is expressed in FS‑coordinates, the resulting skyline is well‑approximated by a sublinear power law. This reflects the geometric compression induced by composite widths: the FS x‑coordinate grows more slowly than the natural numbers, so the prime heights trace a curve of the form* p ∼ Cxα *with* α \< 1*. This curve is the FS analogue of the prime number theorem, providing a direct translation between classical number‑line behavior and the coverage architecture of the skyline.*

**8\. Structure — How the Skyline Makes Factorization Visible**

In the Factor Skyline, each integer is represented as a column built from its prime factors. This construction makes the internal structure of the integer visible in two dimensions. Unique factorization, which is implicit on the number line, becomes explicit in the geometry.

For any integer *n*:

* its **width** is its least prime factor

* its **height** is the quotient after dividing by that width

* if the height is composite, the process repeats

* the column is the ordered sequence of widths produced by this decomposition

This representation produces a skyline in which each column is the visible record of its factorization. The skyline therefore encodes the multiplicative structure of the integers directly, without requiring symbolic notation or analytic interpretation.

Several structural consequences follow:

**Prime columns are minimal.**  

A prime *p* has width 1 and height *p*.

1. Its column consists of a single width, and it appears exactly where escape occurs.

**Prime powers form vertical stacks.**  

A prime power *pk* produces a column with repeated width *p*.

2. These stacks align horizontally at the activation height of width‑*p*.

**Composite numbers inherit structure from their factors.**  

A composite *n* \= *p*⋅*m* begins with width *p* and continues with the structure of *m*.

3. The skyline therefore displays factorization as a sequence of visible layers.

**Residue classes become vertical slices.**  

Each residue class modulo *p* corresponds to a vertical slice of the skyline.

4. Coverage layers sweep across all slices uniformly, and the structure within each slice reflects the same rules.

**Unique factorization is geometric.**  

No two columns share the same sequence of widths.

5. The skyline contains no ambiguity: each column has a unique shape determined by its prime factors.

This structural visibility explains why the skyline can express prime behavior more directly than the number line. The number line collapses all of this information into a single coordinate, making factorization invisible and forcing prime behavior to be described statistically. The skyline restores the structure, allowing prime behavior to be understood as the outcome of geometric constraints.

With the structure of individual columns established, the final step is to examine how the skyline behaves as a whole and how its global geometry produces the classical patterns observed in prime distribution.

**9\. Global Behavior — How the Skyline Produces the Classical Patterns**

The Factor Skyline is not a collection of isolated columns. It is a global structure shaped by the interaction of all activated widths. The behavior of primes emerges from this interaction, not from local irregularities or statistical fluctuations. Once the skyline is viewed as a whole, the classical patterns of prime distribution follow directly from its geometry.

Several global features are especially important:

1\. The skyline becomes increasingly constrained.

Each activated width removes a fixed fraction of the remaining columns. As more widths activate, the available corridor narrows. This narrowing is monotonic and cumulative. The skyline therefore becomes more structured as it grows, not more chaotic.

2\. Escape events occur at predictable frequencies.

The density of uncovered columns after all widths less than *p* have activated is:

![][image2]

This density determines how often escape can occur. The long‑term frequency of primes is therefore governed by the cumulative effect of coverage, not by randomness. The skyline enforces the thinning of primes through its geometry.

3\. Residue classes behave uniformly.

Each residue class modulo *p* corresponds to a vertical slice of the skyline. Coverage layers sweep across all slices identically. Escape occurs wherever a slice remains uncovered. No slice receives preferential treatment. Uniformity across residue classes is a structural consequence of the geometry.

4\. Prime gaps reflect the narrowing corridor.  
As more widths activate, the corridor of uncovered columns shrinks. The distance between escape events increases because fewer positions remain available. Large gaps occur when the corridor becomes temporarily sparse; small gaps occur when several escape opportunities cluster. Both behaviors follow from the same geometric mechanism.

5\. Primorial Gaps as an Architectural Consequence

In the Factor Skyline ontology, the progression of dominant prime gaps follows directly from the coverage architecture of the number line. Each prime p occupies a repeating corridor of width p, and the smallest primes claim the most real estate: 2 removes every other number, 3 removes every third, 5 removes every fifth, and so on. The surviving integers are those that simultaneously avoid all these corridors, and their pattern repeats with period equal to the product of the active primes. As the primes thin out and the typical gap grows, the dominant gap becomes the largest primorial still smaller than the ambient scale: first 6=2⋅3, then 30=2⋅3⋅5, and eventually 210=2⋅3⋅5⋅7. What appears empirically as a shifting “most common gap” is simply the unfolding of the primorial tiling imposed by the small primes. The primorials are not anomalies or curiosities — they are the structural skeleton of the number line revealed at increasing scales.

6\. Local fluctuations arise from discrete activations.

When a new width activates at *p*2, it removes a fraction 1/*p* of the remaining columns. This discrete event produces a visible change in the skyline. On the number line, these changes appear as fluctuations in prime counts and deviations from smooth approximations. In the skyline, they are structural transitions.

7\. The skyline encodes both global trends and local detail.

The long‑term thinning of primes follows from the cumulative narrowing of the corridor. The short‑term irregularities follow from the discrete activation of new widths. Both behaviors are visible in the geometry and arise from the same rules.

8\. The classical analytic results describe the projection of this structure.

When the skyline is flattened onto the number line:

* the density product becomes a logarithmic scale

* discrete activations become analytic fluctuations

* uniform coverage becomes residue class uniformity

* escape events become primes

The analytic patterns are therefore consistent with the skyline but incomplete. They record the visible effects of a geometry that is hidden by projection.

**10\. Projection — Why the Number Line Loses the Geometry**

The Factor Skyline is a two‑dimensional structure. When it is projected onto the number line, most of its geometry is lost. The number line records only the horizontal order of the integers and discards the vertical structure that determines how widths activate, how coverage accumulates, and where escape occurs.

This projection has several consequences:

1\. Multiplicative depth collapses into a single coordinate.

On the skyline, each integer has a visible sequence of widths.

On the number line, this sequence becomes invisible. All integers appear as identical points, regardless of their internal structure.

2\. Coverage becomes statistical.

Coverage layers remove fixed fractions of the skyline.

When projected, these removals appear as thinning patterns that must be described with analytic approximations. The deterministic geometry becomes a probabilistic trend.

3\. Escape becomes irregular.

On the skyline, escape occurs wherever a column avoids all activated widths.

On the number line, these escape events appear as primes with irregular spacing. The geometry that determines their positions is no longer visible.

4\. Activations become fluctuations.

Each new width activates at *p*2 and removes a fraction 1/*p* of the remaining columns.

On the number line, these discrete events appear as deviations from smooth approximations, contributing to the error terms in prime‑counting functions.

5\. Uniformity across residue classes becomes a theorem.

In the skyline, residue classes are vertical slices that receive identical coverage.

On the number line, this uniformity must be proved analytically because the geometric mechanism is hidden.

6\. Logarithmic laws replace geometric ones.

The density product

![][image2]

shrinks at a rate comparable to 1/log⁡*p*.

When the skyline is flattened, this correspondence becomes the prime number theorem. The logarithm is not the cause of prime thinning; it is the one‑dimensional expression of a two‑dimensional process.

7\. The skyline explains what the number line can only measure.

The number line captures the outcomes of activation, coverage, and escape but not the mechanisms. Analytic tools describe the projection; the skyline reveals the structure that produces it.

**11\. Interpretation — What the Skyline Explains That the Line Cannot**

The Factor Skyline provides a structural account of prime behavior. It replaces statistical descriptions with geometric mechanisms and shows how classical patterns arise from the interaction of widths, activations, coverage, and escape. This section summarizes what the skyline makes explicit and how it reframes the familiar results of analytic number theory.

1\. Prime thinning is geometric.

On the number line, prime thinning appears as a gradual decline in density that must be described with logarithmic functions.

In the skyline, thinning follows from the cumulative removal of space by activated widths. Each width removes a fixed fraction of the remaining columns, and the narrowing of the escape corridor is the direct cause of thinning.

2\. Prime gaps follow from corridor width.

On the number line, prime gaps appear irregular and require probabilistic models to describe.

In the skyline, gaps reflect the local width of the uncovered corridor. When the corridor is sparse, gaps are large; when it is dense, gaps are small. Both behaviors follow from the same coverage process.

3\. Residue class uniformity is structural.

On the number line, uniform distribution across residue classes is a theorem proved analytically.

In the skyline, each residue class is a vertical slice that receives identical coverage. Uniformity is built into the geometry.

4\. Logarithmic laws are projection artifacts.

Analytic results such as the prime number theorem arise from flattening the skyline onto the number line.

The density product shrinks at a rate comparable to 1/log*⁡p*, and this correspondence becomes a logarithmic law when the geometry is projected. The logarithm records the effect of coverage; it does not generate it.

5\. Fluctuations reflect discrete activations.

On the number line, deviations from smooth approximations appear as error terms.

In the skyline, these deviations correspond to the activation of new widths at *p*2. Each activation removes a fraction 1/*p* of the remaining columns, producing visible structural transitions.

6\. Unique factorization becomes visible.

The skyline displays the factorization of each integer as a sequence of widths.

This makes multiplicative structure explicit and shows how composite numbers inherit their geometry from their prime factors.

7\. The skyline unifies global trends and local detail.

The long‑term thinning of primes follows from the cumulative narrowing of the corridor.

Short‑term irregularities follow from discrete activations.

Both behaviors arise from the same rules and are visible in the geometry.

8\. The number line measures outcomes; the skyline reveals causes.

The projection of the skyline is described with analytic tools. 

The skyline provides the mechanisms that produce the patterns those tools measure.

**12\. Conclusion — Restoring the Geometry Behind Prime Behavior**

The Factor Skyline provides a geometric account of the integers that the number line cannot express. By lifting each integer into a second dimension, the skyline makes multiplicative structure visible and reveals the mechanisms that govern prime behavior. Activation, coverage, escape, and density are not analytic constructs or statistical approximations; they are the direct consequences of how widths occupy space in this geometry.

Several conclusions follow from this framework:

1\. Prime behavior is structural, not statistical.

The thinning of primes, the growth of gaps, and the uniformity across residue classes arise from deterministic coverage processes. These patterns do not require randomness to explain.

2\. Logarithmic laws describe the projection, not the mechanism.

The correspondence between the density product and 1/log⁡*p* explains why logarithms appear in classical results. They measure the visible effect of cumulative coverage after the geometry has been flattened.

3\. Local irregularities reflect discrete activations.

Fluctuations in prime counts and deviations from smooth approximations correspond to the activation of new widths at *p*2. These transitions are structural events in the skyline.

4\. Unique factorization becomes a geometric property.

Each column has a unique sequence of widths, and no two columns share the same structure. The skyline displays factorization directly.

5\. The skyline unifies global trends and local detail.

Long‑term density, short‑term fluctuations, residue class behavior, and prime gaps all follow from the same geometric rules. The skyline provides a single framework that accounts for both large‑scale patterns and fine‑scale structure.

6\. The number line is a projection of this geometry.

The number line records the order of the integers but not their structure. It collapses the internal multiplicative structure of each integer into a point that disguises its own architectural geometry. The skyline does not change the integers; it changes what we can see. The skyline reveals the mechanisms that produce the projection.  Analytic tools describe this projection.

[image1]: <data:image/png;base64,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vjhBdExdu3YVf8V9swZslcedVxz5Al70xd/85onjecMGsxMvLXXL1671FV52mTljBxYudPd4v/BC58MPzUmFJ5N1ZNUqr+UnTTKnhkn/DHznO+ZU5JVoAl6qrKzs3r276J6KEkTYmzVgn0w6L5yQyMX77nNee80sPxFfwJ99tq93bmnxVVX0LJG3999PThLPQRWK7wHISCbryG9/67X8179uTg2T/sGYMMGcirwSZcCLRC8pKRExX5oYQBjj+IqKiiOwz+bNm80idE7l2LEtn/2s7FKbfvQjc3KH9uzZs337dnGnQoSKP7YrJ0wwa7fSq7V88Yv6pPpLLmn81a9q77lHL0QgQdeRii1bjPfueEmJWSksx2fMqLvuusZf/vLY3LnmNERNj8h0RBPwItFPOeUUeX9/guOeMrK7rxIyow/CHn7YnNppmYxOIOnJqk6dlnoEcFWVb64OHdFH8Po5tMWtg9/mZ892j3r48Y/dR0cg6uR67e+EmMk6op/LT9z08/UCmYom4EWWy83yJ598stpET8Bnh5EWU6aYFTonk86rEKxY4Uye7F6pogPqtOfi9m//lix87TXzLdu71zdXh3wBP368bznIuu3bfS38xBNmhYRM1pFXX/UW+7e/mVOBjEQT8MghIy2uv96s0DmZdF6xd+WVydb+2tfa/UbV2Oh84hO+t0aOnlM2rZszdsgX8MKsWc6//qtz+unsipwT/fv73qkf/9iskJDhOvL737vnfDzjDLMcyBQBHztGWjz2mFmhczLsvOJhwIBkq376016hOhHvCRPa2Ayr78U2cKDzuc+5wRxwD2oz4AvE3r3Oaaclm/Hss82puTNxou8dvPBCs0JCQa8jsAkBHztf+YrXAf3Lv2T9x7xC6byWLzevMCYGx3rnPn9+slwvlLf2PP+8VydLW1YKNODPOiutBs8F/XHnzTOnJhTKOgLrEfCxs26de9mPT33KvTpTDq7sUhCd109+kuzBH3jAKzSuSXrrrcnyn//cV95x3vzsZ26Fb37TLM9UIQZ8yj7n7uXkQ3P77e536E9+0vz+pymIdQT5gIC3zznnJLut++83J1kgjzuv3buTbfuJT3TUtmPH+sKj9XAP5+67feV69r/yilvts591brrJqanxynPP9oCfNi3ZXFk8tru83PdGFLVz6vvo5PE6gs74z/9MfiCHDjUnRYSA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>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGcAAAA0CAIAAAAYObH3AAAD20lEQVR4Xu2Z/UsUQRjH/VOCqCvRMENFRQURI0VTFCPKClOiRFPTKAqksjLSMl/wJS0jiYzEshSVC6RIRUy0rMxOTdPLd04yuh/75taw7HOne5N328rA54fdZ+bmZj87MzvPrpt1eUngKG40JFgTYY0HYY0HYY0HYY0HYY0HYY0HYY0Hx6xlZ6YbNm/igDalaxyzJuGxbUt5SRGNK5AU97x+SYv0Do+1kEA/9damJ8dpkd7hsRYWEqTe2uLcNC3SO8IaD8IaD8IaDxpbq62ujI+JonEnkZl2IiEuhsZBbFTEw/u1NG4TLa2Nj3xGnfkZs3T687vlbV9vZVkxrameZcvCk4ZHfT1dtAiEBgfW1lTSOEA30Bl0iRZRNLN2Kfd8fGw0OzW2Ng8NDvR2d6pp2SY/lhbz8y7g4kuLCm1am5ueOn0qA/eGFjGiI8ILr12mcQWaWQsO8KW3HVerpuXVQQs2rXW96njR1kLjctAljEcaV6CNNdzw8NAQ8/ioIu48ayOfPsh1YNz5+3hjgH98149Nu2novRRHl9Ax2qYCbawhmLg/gRbZs+azc4c8q2XQFqx2rB09fBCPAukYaiJ3h1nmZ6wra+v1q3msmr2OKdCHNYewac1vlxebnh3GdqTS7Lj1+VNWzV7HFGhjzcUzFH9UVJDPTm9XlBr+vobx8fJcmP3GiibHTLg6+W9too0168qkoyMCmwY85rB7oPVVgt+iBbQjDzY+rh/sf8NOpbGGmi1NjQf2xctr4onh5bFd0SZFM2vYeeAxT+PrDu4NpieNSyiKsN791zsPLMPo4r8MK5VgbuKPaNy6slDIMxN0Jm5vpHlijNZUoJk1CSQxzs6osHLZezOK+YiFAttjHKMb+sio9IuwxoOwxgOPNaQgZ3OyaFxBStIhg/huwMBmJyEuBqkcLZKDJxes0U3ZBsAxa9KkY7Q1N9E6AHF5NYP4HiqwCmt8rJs1PCvvVJVnZ6QNDQ7Q0g2GA9aQfwT5+7lv3XzuTLai6ItpODjAt/hGgSI+OzWBODJnbNBdk3W6BrXWkJ2xy85KT2XxyTFTdUXZKunknrDQhvoH1pUnCS3VKWqtdRjbpRdPyNrq7tawOAZg8pHEVfLw+NhobNlmzV+dnW+6ErXWjK3N2Nxirl25mDsxOkwr2FzX4PR4SpJlfgZaK0pv0V/pFLXWsKfFmCq5WVBfd29pYZZWkGhveZZ6LJmdYpTlZJ309nSvKi+xNxj1iFprEr8nmuwj5ppgRRN56J/3otLXHTUgXe3t7qRxveOYNYGEsMaDsMaDsMaDsMaDsMaDsMaDsMbDL6PC/wq0R9QcAAAAAElFTkSuQmCC>