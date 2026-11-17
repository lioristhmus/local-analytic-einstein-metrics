---
title: "Local analytic Einstein metrics from free curvature data in four dimensions"
author: 'Lior Isthmus\textsuperscript{1}'
short-author: "Lior Isthmus"
date: "2026-11-18"
language: en
version: "1.0.2"
bibliography: references.bib
---

<div id="sec:es-abstract"></div>

## Abstract

We construct marked holomorphic Einstein four-germs from the two complete chiral curvature records at a point. For every prescribed numerical cosmological constant, a factorial growth bound on the free records is necessary and sufficient for realization by such a germ. We complete the ordered curvature jets, estimate the nonlinear horizontal derivations, and integrate them on a scale of analytic record spaces. The resulting radial curvature determines the metric through a Jacobi equation. The metric, its inverse and its normal-coordinate realization depend holomorphically on bounded record balls on common neighborhoods. The same record flows represent short point and full spin-frame changes, and the records fixed by Lorentz conjugation give the real-analytic Lorentzian Einstein germs.

\tableofcontents

\footnotetext[1]{Email: \href{mailto:lioristhmus@proton.me}{\nolinkurl{lioristhmus@proton.me}}}
\setcounter{footnote}{1}

<div id="sec:es-introduction"></div>

## 1. Introduction

In four dimensions, a factorial growth bound on the free chiral curvature derivatives at a point is necessary and sufficient for realization by a marked holomorphic Einstein metric germ. The germ is unique up to marked isometry, for every prescribed numerical cosmological constant, including zero. The free data are the separately symmetric covariant derivatives of the two Weyl spinors. Their Lorentz-real form gives exactly the marked real-analytic Lorentzian Einstein germs. The construction applies to every algebraic type of the Weyl curvature.

On each bounded ball of analytic records, the metrics and their inverses are bounded on a common normal-coordinate neighborhood and depend holomorphically on the records. Bounded holomorphic families also have common domains for the coordinate maps and radial spin frames. The record flows describe changes of base point and full spin frame, with common representatives for the conditioned finite comparison diagrams specified in §8.

The ordered coefficient bound, convergent record flows and Einstein realization were established as part of the projective twistor correspondence in @Isthmus2026Twistor [Lemma 3.2, Theorem 3.3, Proposition 4.1, Appendix A and Theorem B.4]. The flow proof there also gives holomorphic maps into smaller-radius sequence spaces. This paper develops the local realization theorem in a self-contained form. We expand the normalized diagram estimates and formulate the record-flow theorem on the analytic scale. We construct the metric directly from radial curvature by the Jacobi equation, and prove that the normal metric and its inverse depend holomorphically on the records in Banach spaces of bounded holomorphic tensors. The point and full-spin comparisons and Lorentz real form correspond to the metric statements of @Isthmus2026Twistor [§§8.3–8.4].

Let $S,S'$ be marked complex symplectic two-spaces, $V=S\otimes S'$ and $\eta$ the induced tangent form. The free record spaces are

$$
 W_r^+=\operatorname{Sym}^{r+4}S^*\otimes\operatorname{Sym}^{r}S'^*,
 \qquad W_r^-=\operatorname{Sym}^{r}S^*\otimes\operatorname{Sym}^{r+4}S'^*.
$$

For an Einstein metric these are the separately symmetric parts of $\nabla^r\Psi^\pm$ at the marked point. An analytic abstract record consists of independent $U_r^\pm\in W_r^\pm$ satisfying $\|U_r^\pm\|\le Cr!R_0^{-r}$ for some $C,R_0>0$, together with a numerical constant $\Lambda$. Equivalently it belongs to one of the Banach spaces $\mathcal B_R$ defined in §2.

The main results are summarized below and proved in Theorem [7.2](#thm:es-realization), Proposition [7.3](#prop:es-uniform-realization) and §8.

**Theorem A.** Every analytic abstract record $X=(U^+,U^-,\Lambda)$ is realized by a marked holomorphic Einstein four-germ with $\operatorname{Ric}(g)=\Lambda g$. Its entire free curvature record is the prescribed one, and it is unique up to the marked isometry. Every marked holomorphic Einstein four-germ arises in this way. For each $R,M>0$ there is a common normal-coordinate neighborhood on the record ball $\|X\|_R\le M$, with common bounds for the metric and its inverse. The normal realization, its coordinate maps and radial spin frames depend holomorphically on the records, with the spatial restrictions specified in Proposition [7.3](#prop:es-uniform-realization).

**Theorem B.** Short changes of point and full spin frame are represented by the convergent record flows. They give exactly the local isometries with their specified spin lifts, and their finite conditioned composition diagrams have common representatives on bounded record families. The Lorentz-real records are precisely those of real-analytic Lorentzian Einstein four-germs.

The conditioning in §8 bounds the spin maps and their inverses and keeps the coordinate maps and specified composites inside their assigned normal neighborhoods with uniformly positive buffer and inverse margins.

We first complete the free records to all ordered curvature derivatives. We verify the polynomial identities on analytic Einstein metrics realizing finite record prefixes. This formal completion defines the horizontal derivations corresponding to a change of base point: in a direction $a$ they act by

$$
 \mathsf H_aU_r=i_aU_{r+1}+Q_{r,a}(U,\Lambda).
$$

We use auxiliary Hermitian tensor norms to estimate the derivations on an analytic record scale. The leading shift loses radius, while the nonlinear terms come from the curvature commutators in the exact-set recursion. To integrate these derivations, we need estimates uniform in derivative order and curvature degree. Lemma [5.4](#lem:es-transfer) supplies an inverse-order factor $1/(t+1)$ whenever an order-$t$ correction is inserted into the recursion. A common contraction-diagram mass controls these insertions, and a rescaling absorbs the summable linear transfer loss. The inverse-order gain then closes the curvature-degree induction. The resulting ordered degree-$d$ coefficients satisfy

$$
 \|B^{[d]}_{r,\mathbf j}\|
 \le ab^{d-2}r\,\frac{r!}{\prod_i j_i!},
 \qquad j_1+\cdots+j_d=r+3-2d,
$$

for structural constants $a,b>0$. A scalar majorant equation gives normally convergent horizontal flows on smaller positive record radii, with holomorphic initial-value dependence.

For a small tangent vector $x$, the flow $\Phi_x^t$ of $\mathsf H_x$ gives the analytic radial curvature $\mathcal C_0(\Phi_x^tX)$. The initialized radial Jacobi equation constructs the metric in marked normal coordinates. Its Taylor series agrees with the formal normal metric determined by the completed curvature list, so the formal Einstein and curvature-readout identities become identities of this analytic metric. The uniform flow and Jacobi estimates give the common normal domains and Banach-holomorphic realization of Proposition [7.3](#prop:es-uniform-realization).

Penrose introduced exact sets and their constraint-free null-cone interpretation for interacting fields, including the Einstein equations [@Penrose1980, §§2–3]. The spinor coordinates of Anderson and Torre describe the free components of prolonged Ricci-flat jets and the leading part of their total derivatives [@AndersonTorre1996, §2C, Theorems 2.7–2.8 and Proposition 2.10]. Torre explicitly distinguishes that formal parametrization from convergence of the resulting metric series [@Torre1995, §2].

Related realization problems prescribe algebraic curvature at a point, compatible lists of curvature derivatives, or an analytic curvature map. Gasqui proves formal integrability and involutivity of the Einstein system and realizes prescribed algebraic Einstein curvature at a point, with the extension to arbitrary signatures stated after his Theorem 4.2 [@Gasqui1982, §4]. Kowalski and Belger construct analytic metrics in normal coordinates from compatible sequences of all covariant curvature derivatives satisfying growth inequalities [@KowalskiBelger1994]. The classical normal-jet correspondence expresses the normal metric jet by universal curvature polynomials; a coordinate-free formulation is given by @Jentsch2026 [Theorems 1 and 3]. Basurto-Arzate realizes an analytic curvature map satisfying a radial structure consistency identity by a torsion-free connection [@BasurtoArzate2026, Theorem 1]. Here the input is the two free chiral sequences: completion and convergent record flows supply the analytic radial curvature used in the Jacobi construction.

Friedrich proves a factorial null-data criterion at spatial infinity for static vacuum solutions with a fixed nonzero ADM mass [@Friedrich2007, Theorem 1.1 and Lemma 3.2]. Aceña extends this reconstruction to asymptotically flat stationary vacuum solutions with nonzero mass monopole [@Acena2009, Theorem 1.1]. His two null-data sequences are the symmetric trace-free derivatives of a conformally rescaled scalar potential $\phi_S$ and of the trace-free Ricci tensor of the three-dimensional conformal quotient metric. Aceña subsequently obtains a null-data characterization for three-dimensional negative-definite geometry coupled to scalar fields satisfying the coefficient conditions of his system [@Acena2010, Theorem 1.1 and §7].

In four dimensions, Friedrich identifies the corresponding symmetric vertex spinors as null data for the rescaled conformal Weyl field, determines the formal conformal-vacuum jets from them, and constructs smooth fields satisfying the equations to all orders at the vertex [@Friedrich2013, §5.1, Lemma 6.1 and Proposition 8.1]. He also remarks in §1 that the analysis simplifies for a finite cone with a regular vacuum vertex. Chruściel and Paetz prove existence and uniqueness of smooth vacuum space-times from freely prescribed cone-smooth radiation data at past null infinity [@ChruscielPaetz2013, Theorem 1.1]. The present theorem realizes two independent chiral Weyl records at a regular point by a holomorphic Einstein metric with arbitrary numerical $\Lambda$, with factorial record estimates and uniform holomorphic dependence.

Sections 2–4 establish the record spaces, universal completion and normalized horizontal recursion. Section 5 proves the coefficient estimate, §6 integrates the record fields, and §7 constructs the normal Einstein metric by the radial Jacobi equation. Section 8 gives the point and spin comparisons and the Lorentz real form. Appendix A proves finite-prefix realizability, and Appendix B records low-order forms of the recursion.

<div id="sec:es-records"></div>

## 2. Curvature records and analytic scales

Let $S,S'$ be complex symplectic two-spaces with fixed ordered bases. Put $V=S\otimes S'$ and $\eta_{AA'BB'}=\epsilon_{AB}\epsilon_{A'B'}$. Our index conventions are

$$
 \epsilon_{AB}=\epsilon_{A'B'}=
 \begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 \epsilon^{AB}=\epsilon^{A'B'}=
 \begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 v^A=\epsilon^{AB}v_B,\quad v_A=\epsilon_{AB}v^B .
$$ {#eq:es-spin-conventions}

The primed operations have the same order. A marked holomorphic metric germ consists of a metric near a point $o$ and a full spin marking: an identification of $S,S'$ with the spin spaces at $o$, inducing the tangent isometry $V\to T_oM$. A marked isometry sends the base point to the base point and intertwines these markings by its specified spin lift. Germs are identified by restriction to smaller neighborhoods. Spin lifts of comparisons are retained as part of their data. Write $\operatorname{Spin}(V,\eta)=\operatorname{SL}(S)\times\operatorname{SL}(S')$.

Our curvature operator is $R(a,b)=[\nabla_a,\nabla_b]-\nabla_{[a,b]}$, and $\operatorname{Ric}(b,c)=\operatorname{tr}(a\mapsto R(a,b)c)$. Lowering the output in the last slot gives $R_{abcd}=g(R(e_a,e_b)e_c,e_d)$. With $P=\tfrac12(\operatorname{Ric}-\operatorname{Scal}\,g/6)$, define

$$
 \begin{aligned}
 C_{abcd}&=R_{abcd}-g_{ad}P_{bc}+g_{bd}P_{ac}
                         +g_{ac}P_{bd}-g_{bc}P_{ad},\\
 C_{AA'BB'CC'DD'}
 &=-\Psi^+_{ABCD}\epsilon_{A'B'}\epsilon_{C'D'}
   -\Psi^-_{A'B'C'D'}\epsilon_{AB}\epsilon_{CD} .
 \end{aligned}
$$ {#eq:es-curvature-decomposition}

The two spinors are therefore recovered by

$$
 \begin{aligned}
 \Psi^+_{ABCD}&=-\tfrac14\epsilon^{A'B'}\epsilon^{C'D'}C_{AA'BB'CC'DD'},\\
 \Psi^-_{A'B'C'D'}&=-\tfrac14\epsilon^{AB}\epsilon^{CD}C_{AA'BB'CC'DD'} .
 \end{aligned}
$$

Throughout, $\Lambda$ is the coefficient in $\operatorname{Ric}(g)=\Lambda g$.

<div id="def:es-records"></div>

**Definition 2.1.**

For $r\ge0$ let

$$
 W_r^+=\operatorname{Sym}^{r+4}S^*\otimes\operatorname{Sym}^{r}S'^*,
 \qquad
 W_r^-=\operatorname{Sym}^{r}S^*\otimes\operatorname{Sym}^{r+4}S'^* .
$$ {#eq:es-record-spaces}

The free records of a marked Einstein metric are

$$
 U_r^+=\operatorname{Sym}_{A_1\cdots A_{r+4}}
       \operatorname{Sym}_{A'_1\cdots A'_r}
       \nabla_{A_1A'_1}\cdots\nabla_{A_rA'_r}
       \Psi^+_{A_{r+1}\cdots A_{r+4}}\big|_o,
$$ {#eq:es-free-records}

and the corresponding negative expression with the two spin factors exchanged. Symmetrization is averaging. An abstract record is a pair of arbitrary sequences $U_r^\pm\in W_r^\pm$ and a scalar $\Lambda$. A finite prefix retains $0\le r\le N$.

Give both spin spaces the auxiliary Hermitian norms for which their fixed bases are orthonormal. Symmetric tensors carry the subspace norms of full tensor powers; direct sums carry the orthogonal direct-sum norm. These norms are used for analytic estimates. Put $X_0=(U_0^+,U_0^-,\Lambda)$ and $X_r=(U_r^+,U_r^-)$ for $r>0$.

<div id="def:es-record-scale"></div>

**Definition 2.2.**

For $R>0$ the analytic record space $\mathcal B_R$ is the Banach space with norm

$$
 \|X\|_R=\sum_{r\ge0}\frac{R^r}{r!}\|X_r\|.
$$ {#eq:es-record-norm}

For $R>s>0$, write $\iota_{R,s}:\mathcal B_R\to\mathcal B_s$ for the continuous inclusion. A bounded analytic record family has a common $R>0$ and a common bound for this norm. A holomorphic family is a holomorphic map into such a space on a smaller parameter neighborhood. For a fixed numerical constant one takes the corresponding affine slice of $\mathcal B_R$.

<div id="lem:es-record-growth"></div>

**Lemma 2.3.**

An abstract record belongs to some $\mathcal B_R$ if and only if there are $C,R_0>0$ such that $\|U_r^\pm\|_{\mathrm{ev}}\le Cr!R_0^{-r}$, where

$$
 \|T\|_{\mathrm{ev}}=
 \sup_{|\xi|,|\pi|\le1}|T(\xi^p,\pi^q)|,
 \qquad T\in\operatorname{Sym}^pS^*\otimes\operatorname{Sym}^qS'^* .
$$ {#eq:es-evaluation-norm}

The two descriptions of bounded families agree after a fixed radius decrease.

*Proof.* Coherent evaluation and the unit-sphere integral give

$$
 \|T\|_{\mathrm{ev}}\le\|T\|
 \le\sqrt{(p+1)(q+1)}\,\|T\|_{\mathrm{ev}}.
$$ {#eq:es-coherent-norm}

With probability surface measure on each unit spin sphere, phase orthogonality and $\int_0^1t^j(1-t)^{p-j}\,\mathrm dt=j!(p-j)!/(p+1)!$ show that the squared coherent integral is $\|T\|^2/((p+1)(q+1))$. The first inequality is Cauchy–Schwarz. For $W_r^\pm$ the square-root factor is at most $r+3$. At $R=R_0/2$ the two series therefore have sum at most $16C$, and $\|X\|_R\le16C+|\Lambda|$. Conversely each summand in the record norm is bounded by the norm itself. ∎

For the homogeneity count in the curvature completion, assign scaling weight $r+2$ to $U_r^\pm$ and weight two to $\Lambda$. Curvature degree counts the record or scalar factors in a monomial; its input positions remain ordered and retain their spin types.

<div id="def:es-lorentz-involution"></div>

**Definition 2.4.**

Choose the Lorentz spin identification for which real vectors in $V$ are Hermitian matrices and $\eta(v,v)=2\det(v^{AA'})$, of signature $(+,-,-,-)$. Let $\mathfrak c$ conjugate coefficients, exchange the spin factors and the two chiral records, and conjugate $\Lambda$. A Lorentz-real record is fixed by $\mathfrak c$; in the fixed bases this says $U^-_r=\overline{U^+_r}$ and $\Lambda\in\mathbb R$.

<div id="sec:es-completion"></div>

## 3. Highest compatibility and curvature completion

The algebraic and differential Bianchi identities, together with the commutator of covariant derivatives, determine the part of each ordered curvature derivative complementary to the free records. We first identify the homogeneous system that occurs when the lower derivatives have been fixed. Einstein contractions are the differentiated equations $\nabla^k(\operatorname{Ric}-\Lambda g)=0$, $k\ge0$, with $\Lambda$ constant.

<div id="lem:es-highest-kernel"></div>

**Lemma 3.1.**

Fix the curvature derivatives of orders less than $r$, with the Einstein Ricci tensor $\Lambda\eta$. The homogeneous difference of two order-$r$ solutions of the differentiated curvature symmetries, Bianchi identities, Einstein contractions and derivative-commutator identities is precisely $W_r^+\oplus W_r^-$. The separately symmetric free projection restricts to the identity on this kernel.

*Proof.* At order zero the curvature decomposition [@eq:es-curvature-decomposition] gives the assertion. Suppose $r\ge1$ and let $T$ be the positive Weyl component of a highest difference. Interchanging adjacent derivative pairs changes an ordered derivative by curvature acting on a lower derivative, so those pairs commute in $T$. The Ricci derivatives in the difference vanish. The differentiated Einstein Bianchi identity therefore makes the alternating contraction between any derivative unprimed index and any of the four Weyl unprimed indices zero.

For two specified slots in a two-dimensional spin space, the convention [@eq:es-spin-conventions] gives

$$
 T_{AB\cdots}-T_{BA\cdots}
   =-\epsilon_{AB}\epsilon^{CD}T_{CD\cdots}.
$$ {#eq:es-two-slot-symmetry}

Thus the vanishing contractions make $T$ invariant under interchanging each derivative unprimed index with a Weyl unprimed index. Those interchanges, together with the symmetry of the four Weyl indices, generate every permutation of the $r+4$ unprimed slots. Hence all unprimed slots are symmetric. Since the derivative pairs are symmetric, exchanging two derivative primed slots can now be compensated by exchanging their already symmetric unprimed slots. All $r$ primed slots are consequently symmetric as well. The positive difference is an element of $\operatorname{Sym}^{r+4}S^*\otimes\operatorname{Sym}^rS'^*$.

The negative Weyl component has the factors exchanged and belongs to $W_r^-$. Conversely, a tensor in either of these separately symmetric spaces has zero alternating contractions and commuting derivative pairs, and satisfies every homogeneous highest-order identity. Its free projection is itself. ∎

At each finite order, these identities form a system between fixed finite-dimensional tensor spaces. Its coefficients use the fixed alternating tensors and tangent form; products of lower derivatives appear in the inhomogeneous terms through the derivative-commutator identities.

<div id="prop:es-completion"></div>

**Proposition 3.2.**

For every $r\ge0$ there is a unique universal polynomial tensor $\mathcal C_r(U,\Lambda)$ that completes the two free records through order $r$ to the ordered Einstein curvature derivative of order $r$. These polynomials satisfy all differentiated curvature symmetries, Bianchi identities, Einstein contractions and derivative-commutator identities. They are equivariant for the two complex spin groups and commute with the Lorentz coefficient involution.

*Proof.* At order zero use the Weyl decomposition and the prescribed Ricci part. Inductively, collect the order-$r$ identities and the specified free projection into a finite constant linear system

$$
 A_r C_r=b_r(U_0,\ldots,U_r,\Lambda).
$$ {#eq:es-finite-completion-system}

The already constructed lower-order polynomial tensors make the right-hand side polynomial. Lemma 3.1 makes $A_r$ injective, so a constant left inverse defines a candidate polynomial $\mathcal C_r$.

Lemma [A.1](#lem:es-finite-witness), proved by finite analytic Cauchy systems and a finite-dimensional inverse theorem, realizes every finite Lorentz-real prefix and every real scalar by an analytic Einstein metric. On that metric, the actual order-$r$ derivative solves the full system and has the prescribed free projection. Injectivity makes it equal to the candidate. Hence the residual $A_r\mathcal C_r-b_r$ vanishes on the real form $U^-=\overline{U^+}$, $\Lambda\in\mathbb R$.

Choose paired bases for the two chiral spaces and write $U^+=x+\mathrm i y$, $U^-=x-\mathrm i y$. A complex polynomial in $(x,y,\Lambda)$ that vanishes for all real values of these variables is identically zero. The residual therefore vanishes for independent complex records and complex $\Lambda$. The candidate satisfies the full system, and uniqueness makes it independent of the chosen left inverse.

Spin transformations preserve the defining identities and transform the free projection, so uniqueness gives equivariance of the completion. Conjugation with exchange of the two spin factors preserves the same defining equations and gives the Lorentz assertion. ∎

For a covariant tensor $T$ on $V$, write $\mathsf V_BT$ for insertion of $B\in\mathfrak{so}(V,\eta)$ into each argument, summed over all arguments. Define $\mathsf H_a$ on the free coordinates by taking the free projection of the next completed derivative with first derivative argument $a\in V$. Write $i_aU_{r+1}$ for contraction of one derivative pair of the separately symmetric record with $a$. These definitions extend by the polynomial product rule to the algebra of cylinder polynomials in the records, that is, polynomials depending on finitely many components. They fix $\Lambda$.

<div id="prop:es-polynomial-derivations"></div>

**Proposition 3.3.**

The resulting polynomial derivations satisfy

$$
 \begin{aligned}
 [\mathsf H_a,\mathsf H_b]&=-\mathsf V_{R_U(a,b)},&
 [\mathsf V_B,\mathsf H_a]&=\mathsf H_{Ba},&
 [\mathsf V_B,\mathsf V_C]&=\mathsf V_{[B,C]},\\
 \mathsf H_a\Lambda&=\mathsf V_B\Lambda=0,&
 \mathsf H_a\mathcal C_r&=\mathcal C_{r+1}(a;\,\cdot),
 \end{aligned}
$$ {#eq:es-cartan-identities}

where

$$
 R_U(a,b)c=W_U(a,b)c+
 \frac{\Lambda}{3}\bigl(a\eta(b,c)-b\eta(a,c)\bigr),
$$ {#eq:es-algebraic-curvature}

and $W_U$ is the Weyl tensor with chiral spinors $U_0^+,U_0^-$. Moreover,

$$
 \mathsf H_aU_r=i_aU_{r+1}+Q_{r,a}(U,\Lambda),\qquad Q_0=0,
$$ {#eq:es-horizontal-polynomial}

where $Q_r$ depends only on $U_0,\ldots,U_{r-1},\Lambda$. At curvature degree $d\ge2$, each ordered monomial of $Q_r$ has input record orders satisfying

$$
 j_1+\cdots+j_d=r+3-2d;
$$ {#eq:es-completion-weight}

a scalar $\Lambda$ occupies an input position of derivative order zero.

*Proof.* Each component of each displayed identity depends on a finite prefix. Realize a prefix long enough to include all derivatives appearing in that component by Lemma [A.1](#lem:es-finite-witness). Proposition 3.2 applies to the records at every point and frame of this witness. On its spin frame bundle, $\mathsf H_a$ is therefore the horizontal component readout and $\mathsf V_B$ is the frame readout. The horizontal commutator acts on every covariant slot by minus curvature insertion. The horizontal--vertical and vertical--vertical brackets give the other two commutators with the stated pullback convention. Differentiating an ordered curvature derivative gives the last identity, including its derivative slots. Thus each component identity holds on every finite Lorentz-real prefix. The polynomial continuation used in Proposition 3.2 proves all of them on independent complex records.

Under the dilation $g_s=s^{-2}\delta_s^*g$, $\delta_s(x)=sx$, the tangent metric at the mark is fixed, $U_j$ has weight $j+2$ and $\Lambda$ has weight two. The value of $\mathsf H_aU_r$ has weight $r+3$. Its linear term is $i_aU_{r+1}$: in the homogeneous linear system of Lemma 3.1, the highest derivative is the separately symmetric tensor itself, and its free projection is an average. Every remaining monomial has degree $d\ge2$ and therefore has weight $j_1+\cdots+j_d+2d$. This gives the degree relation. It implies $j_i\le r-1$ for every nonlinear input, and gives $Q_0=0$. ∎

<div id="sec:es-derivations"></div>

## 4. The Einstein Cartan derivations

Proposition [3.3](#prop:es-polynomial-derivations) defines the horizontal derivations $\mathsf H_a$ and vertical derivations $\mathsf V_B$ on cylinder polynomials. The horizontal field has the form $\mathsf H_aU_r=i_aU_{r+1}+Q_{r,a}$. Resolving the antisymmetric part of one additional covariant derivative gives the nonlinear correction.

Use the full-tensor Hermitian norms of §2, with the fixed alternating spin bases orthonormal. Symmetrizations are averaging projections. All adjoints below are adjoints of constant finite matrices; they do not introduce conjugated record variables.

Fix either chirality and write $W_r$ for its record space. For $r\ge1$, regrouping one spinor of each kind gives an isometric inclusion
$j_r:W_r\to V^*\otimes W_{r-1}$. Let $J_r=1\otimes j_r$ and let $\tau$ exchange the two outer derivative pairs after that inclusion. Set $\delta_r=(1-\tau)J_r$, without dividing by two. For the positive chirality write $n=r+4,m=r$; exchange them for the negative one. The upper and lower projections in the two spin factors are denoted by $P_{++},P_{-+},P_{+-},P_{--}$. In each spin factor, the upper summand is fully symmetric and the lower summand is its complement; §5.1 gives their polynomial normalizations.

<div id="lem:es-spencer"></div>

**Lemma 4.1.**

For the original derivation $\mathsf H_aU_r=i_aU_{r+1}+Q_{r,a}$, $r\ge0$, the initial case is $Q_0=0$. For $r\ge1$ one has the following identities, with the last sum interpreted as zero when $r=1$:

$$
 \begin{aligned}
 \ker\delta_r&=\operatorname{im}P_{++},\\
 M_r&=\frac n{n+1}P_{-+}+\frac m{m+1}P_{+-}
                         +\frac{nm}{nm-1}P_{--},\\
 Q_r&=M_rJ_r^*(\tau\,\mathsf H Q_{r-1}-K_r),\\
 K_r(a,b)&=\mathsf V_{R_U(a,b)}U_{r-1},\\
 (\mathsf H Q_{r-1})(a,b)
  &=\sum_{j=0}^{r-2}D_{U_j}Q_{r-1,b}
                         [i_aU_{j+1}+Q_{j,a}].
 \end{aligned}
$$ {#eq:es-recursion}

*Proof.* On $A\otimes\operatorname{Sym}^nA$, let $P_n$ be the orthogonal full-symmetrization projection onto $\operatorname{Sym}^{n+1}A$. Compression of an exchange of the outer slot with an inner slot is
$C_n=((n+1)P_n-1)/n$. Indeed full symmetrization is
$(1+\sum_{i=1}^n\tau_{0i})/(n+1)$, and the compressed inner exchanges agree. Its two eigenvalues are $1,-1/n$. Thus

$$
 \delta_r^*\delta_r=2(1-C_n\otimes C_m)
$$ {#eq:es-spencer-spectrum}

has nonzero eigenvalues $2(1+1/n)$, $2(1+1/m)$ and
$2(1-1/(nm))$. Their minimum is at least $8/5$.
On antisymmetric sources the complementary inverse of $\delta_r$ is
$M_rJ_r^*$.

Apply the actual commutator in Proposition [3.3](#prop:es-polynomial-derivations) to $U_{r-1}$. The completely upper $U_{r+1}$ term cancels and gives
$\delta_rQ_r=-K_r-(1-\tau)\mathsf H Q_{r-1}$.
Differentiating the constant zero-upper-projection identity for $Q_{r-1}$ gives $J_r^*\mathsf H Q_{r-1}=0$. The commutator identity places the antisymmetric source in the image of $\delta_r$. Applying its complementary inverse recovers the already defined $Q_r$ and proves the formula. Here $(\mathsf H Q_{r-1})(a,b)=\mathsf H_a(Q_{r-1,b})$ has direction slot $a$ first and the coefficient's own slot $b$ second; $J_r^*\tau$ retains $b$ and symmetrizes $a$ into the output record. The last line is the ordinary polynomial product rule; $\mathsf H_a\Lambda=0$. The curvature in $K_r$ acts on all $2r+2$ spinor slots, including the derivative slots. ∎

Appendix B displays the first three corrections and the first possible insertion of one nonlinear correction into another.

<div id="sec:es-coefficients"></div>

## 5. Uniform nonlinear coefficient estimates

The convergence argument requires coefficient bounds uniform in derivative order and curvature degree. We obtain them by measuring contraction diagrams in one mass and retaining the inverse-order gain in nonlinear insertions. Throughout this section, symmetric tensors have the full-tensor Hermitian norms of §2, and every symmetrization is an average. Structural constants depend only on the two fixed spin spaces and the curvature convention.

At curvature degree $d$, retain the order and chirality of each input position in the polynomial expansion of $Q_r$. A scalar $\Lambda$ position has order zero. The dilation weights in Proposition [3.3](#prop:es-polynomial-derivations) give

$$
 Q_{r,a}(X)=\sum_{d\ge2}\ 
 \sum_{|\mathbf j|=r+3-2d}
 B^{[d]}_{r,\mathbf j}(a;X_{j_1},\ldots,X_{j_d}).
$$ {#eq:es-ordered-expansion}

We first estimate coefficients with fixed input and output chiralities; they are grouped at the end of §5.3. Recursion ([-@eq:es-recursion]) fixes the ordered expansion: differentiation replaces an input at its existing position, and an insertion preserves the order of its own inputs. This convention determines coefficients of the commutative polynomial without a symmetric polarization or a factor $1/d!$.

<div id="sec:es-contractions"></div>

### 5.1. Normalized contractions

In one spin factor, express a symmetric tensor by its polynomial on a vector $u=(u^0,u^1)$. For a degree-$q$ polynomial with an additional covariant index, write it as $T_a(u)$. Put

$$
 (\operatorname{up}_{q+1}g)_a=\frac{\partial_ag}{q+1},\qquad
 g=u^aT_a.
$$ {#eq:es-upper-inclusion}

For $q\ge1$ also put

$$
 (\iota_qf)_0=-u^1f,\qquad
 (\iota_qf)_1=u^0f,\qquad
 \operatorname{strip}_qT
 =\frac{\partial_0T_1-\partial_1T_0}{q+1}.
$$ {#eq:es-lower-inclusion}

Then $T=\operatorname{up}_{q+1}g+\iota_q\operatorname{strip}_qT$. For $q=0$ only the upper summand occurs. The upper inclusion is the isometric inclusion of a completely symmetric tensor in the full tensor product. For $q\ge1$, the squared norm of the lower inclusion is $(q+1)/q\le2$: on the unit highest vector $(u^0)^{q-1}$ its two components have squared norms $1/q$ and $1$, and unitary equivariance gives the general formula.

A bare contraction diagram, or atom, has a fixed ordered list of symmetric inputs with their two spin valences. In each spin factor, choose a pairing of some input slots, attach the alternating tensor $\epsilon^{ab}$ to every pair with a specified orientation, and pass every remaining slot to an output of the same spin type. Average the output slots separately in the two factors. An input of scalar type $\Lambda$ has no spin slots. Each alternating tensor joins two input slots directly; there are no chains of alternating tensors or closed components.

Slot selection is normalized: choosing $h$ slots of a degree-$p$ symmetric polynomial means applying $\partial_{a_1}\cdots\partial_{a_h}/(p)_h$, where $(p)_h=p(p-1)\cdots(p-h+1)$. Thus labeled slot choices represent the same averaged tensor operation. Reversing the orientation of a contracted pair changes its sign. A contraction between two slots of the same symmetric input is zero. An atom with $c$ alternating contractions has operator norm at most $2^{c/2}$, since each alternating tensor has full-tensor norm $\sqrt2$ and slot selections and symmetrizations have norm at most one.

An output block is restored by applying $\operatorname{up}$ in its upper factors and $\iota$ in its lower factors. To compose restored diagrams, resolve each symmetrization as its average of slot permutations, and glue the matching slots. Identity tensors $\delta^a_b$ and alternating tensors then have two incident half-edges, while the uncontracted input and output slots are terminals. A *wire* is a connected component of this graph after the glued internal slots are suppressed; it is a path or a circle. An *opened wire* at a lower insertion is obtained when a selected derivative hits its raw factor $\epsilon_{bc}u^b$: compose this alternating tensor with the incident contracted pair, replace their composition by the signed identity, and pass the partner slot to the symmetric output. Lemma 5.1 records the normalization of this operation.

<div id="lem:es-opening"></div>

**Lemma 5.1.**

Replace a degree-$p$ input of a normalized contraction diagram by $(\iota_pf)_c$, and suppose that $h$ of its slots are contracted. Let $D_c(u)$ be the resulting degree-$N$ polynomial in the free output variable of this spin factor. If $E_j$ is the diagram obtained by opening the $j$th incident contraction, with its orientation sign $\varepsilon_j$, then

$$
 u^cD_c=\frac1p\sum_{j=1}^h\varepsilon_jE_j.
$$ {#eq:es-opened-edge}

For $N\ge1$ this also gives

$$
 \frac{u^c\partial_aD_c}{N}
 =\frac{N+1}{N}(\operatorname{up}_{N+1})_a
       \left(\frac1p\sum_j\varepsilon_jE_j\right)
       -\frac{D_a}{N}.
$$ {#eq:es-opened-edge-derivative}

For a linear shift, in which the input is replaced by $\operatorname{up}_{p+1}g$, contraction of the new index with $u$ has coefficient one. An old lower output has normalized coefficient bound one. For an old upper output, the lower leakage obtained by stripping has coefficients of absolute value

$$
 \frac{p_j-h_j}{N(N+1)}
$$ {#eq:es-linear-leakage-coefficient}

for the other inputs $j$, where $p_j-h_j$ is their number of free slots. The sum of these coefficients is at most $1/(N+1)$.

*Proof.* In the fixed alternating convention, $(\iota_pf)_c=\epsilon_{bc}u^bf$. The normalized product rule reads

$$
 \frac{\partial_{a_1}\cdots\partial_{a_h}
                  (\epsilon_{bc}u^bf)}{(p)_h}
 =\frac{p-h}{p}\epsilon_{bc}u^b
       \frac{\partial_{a_1}\cdots\partial_{a_h}f}{(p-1)_h}
  +\frac1p\sum_{j=1}^h\epsilon_{a_jc}
       \frac{\prod_{\ell\ne j}\partial_{a_\ell}f}{(p-1)_{h-1}}.
$$ {#eq:es-normalized-product}

The first term is omitted when $h=p$, and the sum is empty when $h=0$. Multiplication by $u^c$ kills the first term. In each remaining term the two alternating tensors at the opened contraction compose to a signed identity. If the partner input has degree $p_j$ and $h_j$ selected slots, the released derivative gives the factor $p_j-h_j+1$. Its normalization is

$$
 \frac{p_j-h_j+1}{(p_j)_{h_j}}
       =\frac1{(p_j)_{h_j-1}}.
$$ {#eq:es-partner-normalization}

This leaves precisely the normalized selection with $h_j-1$ slots. Thus the coefficient of the opened diagram is exactly $\varepsilon_j/p$, without a partner-valence factor. Differentiating $u^cD_c$ proves [@eq:es-opened-edge-derivative].

For the upper replacement, the selected polynomial derivatives are $\partial_{a_1}\cdots\partial_{a_h}\partial_cg/((p+1)(p)_h)$. Euler's identity after contraction with $u^c$ gives the multiplier

$$
 \frac{(p+1-h)(p+1)_h}{(p+1)(p)_h}=1.
$$ {#eq:es-unit-linear-shift}

To compute leakage from an old upper output, write its restored outer index as a normalized derivative. Stripping the transferred output antisymmetrizes this derivative with the new derivative index. When both derivatives land on the distinguished shifted input, their contribution vanishes. A derivative landing on another input $j$ can select any of its $p_j-h_j$ remaining free slots. The two output normalizations give the denominator $N(N+1)$ in [@eq:es-linear-leakage-coefficient]. The remaining free-slot counts sum to at most $N$, proving the total bound. Raw lower output factors are independent of the distinguished input, so an old lower output stays lower with unit bound. These arguments are tensor-valued in the other spin factor. ∎

For example, a single bare contraction of degree-$p$ and degree-$q$ inputs is $\epsilon^{ab}(\partial_aP)(\partial_bQ)/(pq)$. Replacing the first input by $\epsilon_{dc}u^df$ gives, in the alternating convention of §2,

$$
 u^c\frac{\epsilon^{ab}}{pq}
       \partial_a(\epsilon_{dc}u^df)\,\partial_bQ
 =-\frac{u^b\partial_bQ}{pq}f
 =-\frac1p fQ.
$$ {#eq:es-single-opened-edge-example}

The factor $q$ from Euler's identity cancels the partner input's normalization. This is the cancellation used at every opened contraction in Lemma 5.1.

The one-derivative space has four upper/lower blocks. The $++$ block of $Q_r$ is zero by its definition. For the positive chirality, strip the raw lower factors and retain the upper potentials in the other factors. The three remaining output blocks have valences

$$
 \begin{array}{c|ccc}
 \nu&A=-+&B=+-&C=--\\ \hline
 \text{stripped valence}&(r+3,r+1)&(r+5,r-1)&(r+3,r-1).
 \end{array}
$$ {#eq:es-stripped-valences}

The negative chirality exchanges the two spin degrees. The labels $A,B$ always refer to the physical unprimed/primed signs.

We measure diagram representations by weighted sums of the absolute values of their coefficients, so that one mass controls composition as well as the operator norm. Fix a degree $d$ and an ordered input list with $|\mathbf j|=r+3-2d$, including its types. For each block $\nu$, let $\mathcal D_{r,\nu}$ be the finite set of normalized bare contraction diagrams with those inputs and that stripped output valence, including contraction orientations. Define

$$
 m_{r,\nu}(B)=\inf\left\{
       \sum_D|b_D|:\ 
       \widetilde B_\nu=\sum_{D\in\mathcal D_{r,\nu}}b_DD
                     \right\},\qquad
 m_r(B)=2m_{r,A}(B)+2m_{r,B}(B)+m_{r,C}(B).
$$ {#eq:es-diagram-mass}

Here $\widetilde B_\nu$ is the stripped coefficient and the infimum is taken on the span of the displayed diagrams. Absent blocks have mass zero. All coefficients generated by [@eq:es-recursion] lie in these spans: the curvature formula, the projections, shifts and insertions use alternating contractions and averaged slot permutations. Pairing internal alternating tensors reduces their compositions to bare contraction diagrams of the specified final valence.

A degree-$d$ coefficient containing $\ell$ scalar inputs has total input valence

$$
 2\sum_i j_i+4(d-\ell)=2r+6-4\ell.
$$ {#eq:es-input-valence}

It follows from [@eq:es-stripped-valences] that the total number of bare contractions is $1-2\ell$ in blocks $A,B$ and $2-2\ell$ in block $C$. A negative count gives the zero space. There are consequently at most two bare contractions in any nonzero block, independently of $r$ and $d$. Restoring the raw lower factors and the isometric upper inclusions therefore gives

$$
 \|B\|_{\mathrm{op}}\le4m_r(B).
$$ {#eq:es-mass-dominates-norm}

Indeed a bare diagram has norm at most two, and at most two lower inclusions contribute an additional factor two. Taking the infimum preserves this bound. Thus $m_r$ is a norm on each of the coefficient spaces under consideration.

<div id="sec:es-transfers"></div>

### 5.2. Linear and nonlinear transfers

Linear shifts and nonlinear insertions have different effects on the coefficient mass. In the recursion, let $L_iB$ denote replacement of the $i$th input by its linear shift, and let $I_i(B,C)$ denote replacement of that input by a specified coefficient of $Q_t$. The estimate below holds for one fixed index $i$; the coefficient theorem will sum over the eligible positions.

<div id="lem:es-directed-wires"></div>

**Lemma 5.2.**

Fix a fine assignment in the insertion of one restored bare atom into another, followed by $J_r^*\tau$ and extraction of a target block. The input and output slots of every elementary operation can be placed on distinct successive boundaries so that all identity connections are directed from an earlier boundary to a later one. Cutting the alternating tensors leaves only paths. Thus every closed component of the unreduced graph contains an alternating tensor. If there are at most $q$ alternating tensors in both spin factors together, the product of the closed-component factors has absolute value at most $2^q$. The same conclusions hold for the opened terms of $u^cD_c$ in Lemma [5.1](#lem:es-opening), with their factor $1/p$ kept outside the graph.

*Proof.* Represent each operation on labeled tensor slots before averaging. Its input and output are separate copies even when they have the same valence. A fixed permutation matches these two boundaries bijectively. Tensor products place matchings side by side, and composition glues an output boundary only to a subsequent input boundary. Unchanged slots are carried by identity maps.

The insertion has a definite composition order: form and restore the inner atom, apply the restored outer atom to its selected record output, and apply $\tau$, $J_r^*$ and the target extraction. The other outer inputs and the inner derivative index are carried through the intervening stages. Expand these stages into their elementary operations. The following list accounts for all their slot connections.

- A bare atom pairs selected input slots by $\epsilon^{ab}$ and passes the others to its output.
- Upper restoration separates a selected slot from a symmetric tensor; upper-potential extraction returns the distinguished slot to the symmetric output. Both are averages of boundary matchings.
- Multiplication and symmetrization average boundary matchings; a fine assignment fixes one such matching.
- A raw lower restoration adjoins $\epsilon_{ab}$, with two outgoing slots. A lower stripping contracts two incoming slots by $\epsilon^{ab}$. All remaining slots pass forward.
- The map $\tau$ permutes slots, and $J_r^*$ symmetrizes the new derivative slots into the two spin outputs as specified in Lemma [4.1](#lem:es-spencer). Each is an average of boundary matchings. Target upper extraction uses such a matching, and target lower extraction uses the stripping just described.

Number the elementary stages by $k$. Give their input and output boundaries heights $2k$ and $2k+1$, respectively, inserting identity stages for slots carried alongside an operation. An identity connection traverses a stage from input to output; gluing successive stages also increases height. Cut each alternating tensor while retaining its incident half-edges as open ends. Every remaining internal vertex has one incoming and one outgoing identity connection, along which height strictly increases. A closed identity component would therefore be a directed cycle with strictly increasing height, which is impossible.

The two spin colors are preserved. Each closed component of the original graph consequently contains an alternating tensor, and its contraction, by the fixed alternating inverse identities, has absolute value at most two in a two-dimensional spin factor. Distinct closed components use disjoint alternating tensors, so there are at most $q$ of them. Evaluating the closed components of this unreduced graph gives the bound $2^q$.

For an opened term, the selected slot of the inner raw lower factor is paired by an outer bare contraction with a slot of another outer input. A contraction within the distinguished outer input itself is zero by symmetry. The other outer input remains an original input of the composite. Contracting the two incident alternating tensors gives a signed identity from that partner slot to the new slot passed to the symmetric output by $u^c$. This connects an input boundary to a later output boundary. All subsequent upper restorations and target extractions are among the operations above. The partner normalization in [@eq:es-partner-normalization] leaves the numerical factor $1/p$ outside this matching. Thus an opening removes two alternating tensors and preserves the directed-boundary construction, so the same closed-component bound applies. ∎

<div id="lem:es-diagram-composition"></div>

**Lemma 5.3.**

Let $D$ be a bare atom for a block $\nu$ at order $r-1$, with a specified nonscalar input of order $t$, and let $E$ be a bare atom for a block $\mu$ at order $t$ with the matching output chirality. Suppose $1\le t\le r-2$. Restore their one-derivative blocks and replace the specified input of $D$ by $E$. Give an atom in block $\lambda$ the block weight $w_\lambda$, where $w_A=w_B=2$ and $w_C=1$. Then there is a representation by target bare atoms, restored in their target blocks, such that

$$
 M_rJ_r^*\tau I_i(D,E)=\sum_F\beta_FF,\qquad
 \sum_Fw(F)|\beta_F|
 \le\frac{5C_{\mathrm w}}{t+1}
 \le\frac{K_0}{t+1}w(D)w(E),\qquad
 C_{\mathrm w}=2^{20},\quad K_0=2^{24}.
$$ {#eq:es-atomwise-insertion}

The estimate is independent of the two arities, input orders, input types and output chiralities.

*Proof.* First account for the slots selected before composition. Suppose that input $i$ has degree $q_i$, of which $k_i$ slots have already been selected, and put $p_i=q_i-k_i$. For $0\le h\le\sum_i p_i$, distributing $h$ further selections among the residual symmetric factors gives the weights

$$
 \binom h{\alpha_1,\ldots,\alpha_d}
 \frac{\prod_i(p_i)_{\alpha_i}}{(\sum_i p_i)_h},
 \qquad \sum_i\alpha_i=h.
$$ {#eq:es-assignment-weights}

The displayed weight is the total weight of the occupancy $\boldsymbol\alpha$. Conditional on that occupancy, average uniformly over its $\binom h{\alpha_1,\ldots,\alpha_d}$ allocations of the $h$ labeled selection slots. Each such fine assignment has weight $\prod_i(p_i)_{\alpha_i}/(\sum_i p_i)_h$ and specifies one slot graph. The total weights are nonnegative and sum to one by the falling-factorial Vandermonde identity; for $h=0$ the weight is one. A selection beyond the total residual valence is zero. The composite selection on input $i$ has exactly the normalization of a single selection of $k_i+\alpha_i$ slots, because

$$
 (q_i)_{k_i}(q_i-k_i)_{\alpha_i}=(q_i)_{k_i+\alpha_i}.
$$ {#eq:es-preselected-normalization}

Unavailable selections have coefficient zero. Apply this identity separately in the two spin factors. The joint assignment weights are products of the two families of nonnegative weights, and again sum to one. At each successive distribution, multiplying these conditional weights preserves their total sum. A fixed fine assignment therefore produces one slot graph with a nonnegative coefficient, and the coefficients of all assignments sum to at most one. This remains true when some graphs vanish. No count of the assignments, input positions or slot permutations enters the estimate.

The operations used here have the following normalizations. Multiplication of output polynomials is averaged symmetrization of their free slots. Upper restoration is a normalized slot selection, and extraction of its upper potential passes the distinguished slot to the symmetric output. A lower stripping on a degree-$N$ output is a normalized single-slot selection followed by an alternating contraction, with scalar factor $N/(N+1)\le1$. A raw lower restoration adds the degree-one factor $\epsilon_{bc}u^b$. Treating that factor as a further symmetric factor makes its derivative assignments instances of [@eq:es-assignment-weights]. Finally, $J_r^*$ averages the new slots into the two symmetric spin outputs and $\tau$ exchanges specified slots. Thus every one of these operations either uses the preceding nonnegative assignments, has scalar coefficient at most one, or introduces an explicit alternating tensor.

For a fixed assignment and target block, all alternating tensors come from the following operations:

| Source | Maximum number in both spin factors | Reason |
| --- | --- | --- |
| Bare contractions of $D$ | $2$ | [@eq:es-input-valence] at order $r-1$ |
| Bare contractions of $E$ | $2$ | [@eq:es-input-valence] at order $t$ |
| Raw lower restorations of $D$ | $2$ | At most one in each spin factor |
| Raw lower restorations of $E$ | $2$ | At most one in each spin factor |
| Stripping the target lower factors | $2$ | At most one in each spin factor |

The raw lower factors of the restored target atom are output data and are excluded from its stripped graph. There are at most ten internal alternating tensors. Lemma [5.2](#lem:es-directed-wires) applies to each fine assignment and bounds the closed-component contribution by $2^{10}$, evaluated on the unreduced graph. The same bound holds after a lower opening, which replaces its two incident alternating tensors by a forward boundary matching.

Reduce the open paths using the alternating inverse identities of [@eq:es-spin-conventions]. Their endpoint variances give signed identities or single alternating tensors. A path joining two slots of one symmetric input vanishes, as does a path joining two symmetric output slots. Every remaining path either contracts two different inputs or passes an input slot to the output, giving a bare target atom. Its selected-slot normalization is [@eq:es-preselected-normalization], so the reduction introduces no additional valence factor.

For each assignment the absolute reduction coefficient is therefore at most $2^{10}$. The sum of the assignment weights is at most one, so the same number bounds the total absolute coefficients in each stripped target block. The $++$ block is annihilated by $M_r$, and the remaining target weights sum to $2+2+1=5$. Each nonzero block multiplier of $M_r$ has absolute value at most $5/4$ by Lemma [4.1](#lem:es-spencer). The weighted sum after $M_r$ is consequently at most $2^{10}\cdot5\cdot(5/4)<2^{13}<C_{\mathrm w}$. This proves a coefficient estimate for both spin factors together.

The preceding reduction bounds composition uniformly. To retain the inverse-order factor, choose one lower spin factor of the inserted coefficient and track it through the final projection. The table lists all choices used in this argument:

| Inner chirality | Inner block | Chosen lower factor | Degree $p$ of its input |
| --- | --- | --- | --- |
| $+$ | $A=-+$ | unprimed | $t+4$ |
| $+$ | $B=+-$ | primed | $t$ |
| $+$ | $C=--$ | unprimed | $t+4$ |
| $-$ | $A=-+$ | unprimed | $t$ |
| $-$ | $B=+-$ | primed | $t+4$ |
| $-$ | $C=--$ | unprimed | $t$ |

There is no inner $++$ block, and $Q_0=0$. Hence $t\ge1$ and $p\ge t$. For a double-lower block the table selects the unprimed factor once. In the chosen factor the inserted output is $(\iota_pf)_c$. Formula ([-@eq:es-normalized-product]) shows that contraction with $u^c$ kills the unhit term. Each hit opens an incident bare contraction of the outer atom. There are at most two such contractions, and Lemma 5.1 gives coefficient $1/p$ for each, including the normalization on its partner input. Before any further slot distribution, [@eq:es-partner-normalization] puts the partner in normalized form with one fewer selected slot. The subsequent assignment weights therefore use these updated residual valences and again sum to one. Thus the opened coefficient sum, before the bounded wire reductions, is at most $2/p$ for a pair of bare atoms.

It remains to check that the final projection retains an inverse-order factor. The outer blocks have the following signs in the chosen factor:

| Chosen factor | Outer $A=-+$ | Outer $B=+-$ | Outer $C=--$ |
| --- | --- | --- | --- |
| unprimed | lower | upper | lower |
| primed | upper | lower | lower |

These rows apply to both outer chiralities. Suppose first that the outer sign is upper. Write its old output as $B_a=\partial_ag/(q+1)$, where $q$ is its degree in $W_{r-1}$. After inserting the chosen coefficient into $g$, retain its new derivative index $c$ and call the polynomial $D_c$. With $N=q+1$, the factor after $J_r^*\tau$ is

$$
 T'_a=\frac{u^c\partial_aD_c}{N},\qquad
 \deg D_c=N,\qquad N\in\{r,r+4\}.
$$ {#eq:es-exact-slot-map}

The multiplication by $u^c$ expresses the averaged insertion of the derivative index into the symmetric output. A nonlinear input order satisfies $1\le t\le r-2$, since $Q_{r-1}$ uses only records through order $r-2$. In particular $N\ge t+1$.

Set $G=u^cD_c$. Euler's identity gives

$$
 u^aT'_a=G,\qquad P_+T'=\operatorname{up}_{N+1}G.
$$ {#eq:es-upper-transfer-cancellation}

The upper coefficient therefore has the opened bound $2/p\le4/(t+1)$. For the lower coefficient, the mixed second derivatives cancel:

$$
 \begin{aligned}
 \partial_0(u^c\partial_1D_c)
       -\partial_1(u^c\partial_0D_c)
       &=\partial_1D_0-\partial_0D_1,\\
 \operatorname{strip}_NT'
       &=-\frac1N\operatorname{strip}_ND.
 \end{aligned}
$$ {#eq:es-lower-transfer-cancellation}

The remaining stripping is a normalized slot operation with scalar factor $N/(N+1)\le1$. Its diagram reduction is covered by the preceding uniform bound, while the factor $1/N\le1/(t+1)$ remains explicit.

If the outer sign is lower, its factor $\epsilon_{ba}u^b$ is independent of the inserted input. The resulting factor is $\epsilon_{ba}u^bG$. Its upper projection vanishes, and its lower coefficient is $G$, with the same opened bound $2/p\le4/(t+1)$. The other spin factor undergoes the normalized operations already counted. Together, the two tables and the upper/lower computations treat every inner and outer block in both chiralities.

The upper and lower contributions in the chosen factor have sum at most $2/p+1/N\le5/(t+1)$; when the outer factor is lower, only the first occurs. The normalized operations in the other factor and the target weights have already been included in $C_{\mathrm w}$. Thus the weighted target representation satisfies [@eq:es-atomwise-insertion]. Since $5C_{\mathrm w}\le2^{24}$ and both input block weights are at least one, the stated constant follows. ∎

<div id="lem:es-transfer"></div>

**Lemma 5.4.**

For $r\ge1$, put

$$
 c_r=\frac{r(r+4)}{r(r+4)-1},\qquad
 P_r=\prod_{s=1}^rc_s,
 \qquad P_0=1.
$$ {#eq:es-linear-transfer-product}

The actual recursion satisfies

$$
 \begin{aligned}
 m_r(M_rJ_r^*\tau L_iB)&\le c_rm_{r-1}(B),\\
 m_r(M_rJ_r^*\tau I_i(B,C))
     &\le\frac{K_0}{t+1}m_{r-1}(B)m_t(C),
       \qquad K_0=2^{24}.
 \end{aligned}
$$ {#eq:es-transfer-bounds}

Every typed ordered quadratic coefficient of the transferred curvature source has mass at most $C_*(r+1)$ for a structural constant $C_*$. Moreover, the product converges and

$$
 1\le P_r\le P_\infty\le\exp(11/18).
$$ {#eq:es-transfer-product-bound}

*Proof.* Lemma [5.3](#lem:es-diagram-composition) gives the nonlinear estimate on pairs of bare atoms. Choose arbitrary finite representations $B=\sum_Db_DD$ and $C=\sum_Ec_EE$, with their blocks restored. Composition is bilinear, so the atomwise representations give

$$
 m_r(M_rJ_r^*\tau I_i(B,C))
 \le\frac{K_0}{t+1}
       \left(\sum_Dw(D)|b_D|\right)
       \left(\sum_Ew(E)|c_E|\right).
$$ {#eq:es-representation-insertion}

For any $\varepsilon>0$, the two representations can be chosen independently with weighted sums at most $m_{r-1}(B)+\varepsilon$ and $m_t(C)+\varepsilon$. Letting $\varepsilon$ decrease to zero proves the nonlinear estimate in [@eq:es-transfer-bounds].

For a linear shift, we retain the coefficients of Lemma 5.1 rather than the coarser reduction bound, to obtain a summable loss. Put $n=r+4$ and $m=r$ for positive output chirality.

An $A$ atom has an unprimed lower factor and a primed upper factor. Its unchanged lower block receives the multiplier $n/(n+1)$ from $M_r$; primed lower leakage has coefficient at most $1/(m+1)$ and receives the double-lower multiplier $c_r$. Its column is therefore $(n/(n+1),0,c_r/(m+1))^{\mathsf T}$.

A $B$ atom has column $(0,m/(m+1),c_r/(n+1))^{\mathsf T}$ by the same calculation with the spin factors exchanged. A $C$ atom stays double-lower with column $(0,0,c_r)^{\mathsf T}$. Hence the transfer on the raw block masses is bounded componentwise by

$$
 \begin{pmatrix}
 n/(n+1)&0&0\\
 0&m/(m+1)&0\\
 c_r/(m+1)&c_r/(n+1)&c_r
 \end{pmatrix}.
$$ {#eq:es-linear-transfer-matrix}

Its column sums with weights $(2,2,1)$ are bounded by $c_r$ times the input weights. The two inequalities reduce to

$$
 m(n+1)\le2(m+1)^2,
 \qquad n(m+1)\le2(n+1)^2.
$$ {#eq:es-weighted-column-inequalities}

For $n=r+4,m=r$ their right-minus-left differences are $r^2-r+2$ and $r^2+15r+46$, respectively. Interchanging the spin factors interchanges $A,B$ and preserves their equal weights, proving the same estimate for negative chirality.

For the quadratic curvature source, fix its ordered curvature and record positions. First take positive output chirality, write $U=U_{r-1}^+(u,u')$, and put $p=r+3$, $p'=r-1$, $n=r+4$, $m=r$. Evaluating the symmetrized direction $b$ at $u\otimes u'$ describes $J_r^*K_r$. By [@eq:es-curvature-decomposition], its $\Psi^+=U_0^+$ contribution is, up to an overall sign, $\epsilon_{B'A'}u'^{B'}F_A$, where

$$
 F_A=\frac1{12}\epsilon^{DE}
                  (\partial_A\partial_D\Psi^+)\partial_EU.
$$ {#eq:es-source-weyl-polynomial}

The derivatives of $U$ sum the action on all its unprimed slots, including derivative slots. Euler's identity and antisymmetry give

$$
 \begin{aligned}
 u^AF_A
 &=p\,\frac{\epsilon^{DE}(\partial_D\Psi^+)\partial_EU}{4p},\\
 \operatorname{strip}_nF
 &=\frac{p(p-1)}{n+1}\,
   \frac{\epsilon^{AF}\epsilon^{DE}
       (\partial_A\partial_D\Psi^+)\partial_F\partial_EU}
        {12p(p-1)}.
 \end{aligned}
$$ {#eq:es-source-normalized-atoms}

The two quotients are normalized bare atoms with one and two contractions. In the second line, derivatives hitting $\Psi^+$ three times vanish under the alternating $A,F$ contraction. The primed factor is already a raw lower inclusion, so the two terms belong to blocks $B,C$. Multiplication by $M_r$ and the weights $(2,2,1)$ give the mass bound $S_+(r)$ below. For the $\Psi^-=U_0^-$ contribution, exchange the spin factors in this calculation. Its blocks are $A,C$, giving $S_-(r)$. When $p'=0$ the latter contribution is zero; when $p'=1$ its double-contraction term is zero. Normalized atoms requiring those vanishing derivatives are omitted.

$$
 \begin{aligned}
 S_+(r)&=2\frac{m}{m+1}p+c_r\frac{p(p-1)}{n+1},\\
 S_-(r)&=2\frac{n}{n+1}p'+c_r\frac{p'(p'-1)}{m+1}.
 \end{aligned}
$$ {#eq:es-source-weyl-masses}

For the constant-curvature part of [@eq:es-algebraic-curvature], each spin part of $R_\Lambda(a,b)$ acts on the corresponding factor of $b=u\otimes u'$ by $-\Lambda\eta(a,b)/6$. Insertion in the $p+p'=2r+2$ slots therefore gives

$$
 (J_r^*K_r^{\Lambda})_{AA'}
 =-\frac{\Lambda}{3}(r+1)
     \epsilon_{BA}u^B\epsilon_{B'A'}u'^{B'}U.
$$ {#eq:es-source-scalar-polynomial}

This is a block-$C$ atom with zero contractions and transferred mass at most $c_r(r+1)/3$. Since $c_r\le5/4$, the preceding expressions satisfy

$$
 S_+(r)\le\frac{21}{4}(r+1),\qquad
 S_-(r)\le\frac{13}{4}(r+1),\qquad
 c_r\frac{r+1}{3}\le\frac5{12}(r+1).
$$ {#eq:es-source-uniform-bound}

Thus $C_*=6$ is a valid structural choice for each typed ordered coefficient. Negative output chirality exchanges $n,m$ and the two spin factors; the equal weights of $A,B$ give the same bound.

Finally,

$$
 \log c_r\le\frac1{r(r+4)-1}\le\frac1{r(r+3)},\qquad
 \sum_{r\ge1}\frac1{r(r+3)}=\frac13\left(1+\frac12+\frac13\right)=\frac{11}{18}.
$$ {#eq:es-summable-transfer-cost}

This proves the product bound. Taking the infimum over finite representations of $B$ in the linear column estimates gives the first line of [@eq:es-transfer-bounds]. ∎

Define the rescaled mass

$$
 \gamma_r=4\frac{P_\infty}{P_r}m_r.
$$ {#eq:es-rescaled-mass}

This rescaling absorbs the accumulated linear loss: it dominates the operator norm and makes each specified linear transfer nonexpanding. For a nonlinear insertion, the factor relative to the two input masses is

$$
 \frac{P_{r-1}P_t}{4P_\infty P_r}\le\frac14.
$$ {#eq:es-insertion-rescaling}

The product rule sums the two possible intermediate record chiralities. A scalar $\Lambda$ position has derivative zero. Absorbing that sum gives one structural constant $K\le K_0$ for the rescaled insertion bound $K/(t+1)$. The arity induction below counts the eligible ordered positions.

<div id="sec:es-ordered-coefficients"></div>

### 5.3. The coefficient theorem

<div id="thm:es-coefficients"></div>

**Theorem 5.5.**

There are structural constants $a,b>0$ such that every typed ordered coefficient in [@eq:es-ordered-expansion] satisfies

$$
 \gamma_r(B^{[d]}_{r,\mathbf j}),\ 
 \|B^{[d]}_{r,\mathbf j}\|_{\mathrm{op}}
 \le ab^{d-2}r\frac{r!}{\prod_i j_i!},
 \qquad |\mathbf j|=r+3-2d,\quad d\ge2.
$$ {#eq:es-coefficient-budget}

*Proof.* For degree two, a curvature source introduced at order $s$ has ordered indices $(0,s-1)$ and rescaled mass at most $C(s+1)$. Subsequent linear shifts distribute their increments among the two existing positions. At final indices $j+k=r-1$, their total contribution is bounded by

$$
 C\sum_{s=1}^{r-j}(s+1)\binom{r-s}{j}
 =C\left\{\binom{r+1}{j+2}+\binom r{j+1}\right\}.
$$ {#eq:es-quadratic-sum}

The identity follows by summing binomial coefficients, or by writing $s+1=2+\sum_{\ell=1}^{s-1}1$ and applying the hockey-stick identity twice. Multiplication by $j!k!/r!$ bounds this by

$$
 C\left\{\frac{r+1}{(j+1)(j+2)}+\frac1{j+1}\right\}\le2Cr.
$$ {#eq:es-quadratic-normalization}

The reverse source ordering has the same bound with $j,k$ exchanged. Choose $a$ to include its finite multiplicity and the fixed source types.

Normalize each rescaled coefficient mass by multiplying by $\prod_i j_i!/r!$. Induct on the arity and, within each arity, on $r$. Suppose a normalized degree-$d$ coefficient is bounded by $A_dr$. Set $k=|\mathbf j|=r+3-2d$. A linear shift into position $i$ comes from index $j_i-1$ and contributes at most $A_d(r-1)j_i/r$. Summing over the positions gives at most $A_dk$.

For a nonlinear insertion, let the inner and outer arities be $e,f\ge2$, so that $e+f=d+1$. The order of the old outer position is

$$
 t=\sum_{\mathrm{inner}}j_i+2e-3\ge1.
$$ {#eq:es-inserted-order}

The outer factorial denominator $t!$ cancels the inner factorial numerator. After normalization by $\prod_i j_i!/r!$, Lemma [5.4](#lem:es-transfer) and [@eq:es-insertion-rescaling] give the bound

$$
 K A_fA_e\frac{(r-1)t}{r(t+1)}\le K A_fA_e.
$$ {#eq:es-normalized-insertion}

For a fixed final ordered list and fixed $e,f$, there are $f$ possible outer positions. At each position, the inner inputs are determined as its consecutive ordered sublist. Thus the product rule contributes $f$, with no further partition factor. The scalar positions contribute zero to differentiation. Since $r-k=2d-3$, the target bound leaves $(2d-3)A_d$ for the nonlinear terms. We therefore close the induction with

$$
 A_2=a,\qquad
 A_d=\frac K{2d-3}
       \sum_{\substack{e+f=d+1\\e,f\ge2}}fA_eA_f
 \le\frac{2K}{3}
       \sum_{\substack{e+f=d+1\\e,f\ge2}}A_eA_f.
$$ {#eq:es-arity-recursion}

For the last inequality, interchange $e,f$ in the sum and use $(d+1)/(2(2d-3))\le2/3$ for $d\ge3$. The Catalan recurrence then yields

$$
 A_d\le a(2Ka/3)^{d-2}\operatorname{Cat}_{d-2}
       \le ab^{d-2},\qquad b=8Ka/3.
$$ {#eq:es-catalan-bound}

The rescaled mass dominates the operator norm by [@eq:es-mass-dominates-norm] and [@eq:es-rescaled-mass]. ∎

Group the input types using the fixed direct-sum norms in [@eq:es-record-norm]. There are at most $3^d$ ordered input-type lists and two output chiralities. Hence the grouped coefficients satisfy the same estimate with

$$
 a_0=18a,\qquad b_0=3b,
 \qquad 2\cdot3^dab^{d-2}=a_0b_0^{d-2}.
$$ {#eq:es-grouped-constants}

<div id="cor:es-nonlinear-field"></div>

**Corollary 5.6.**

Write $Q_a(X)$ for the nonlinear record vector with scalar component zero, and set

$$
 \|Q(X)\|_s=\sup_{\|a\|\le1}\|Q_a(X)\|_{\mathcal B_s}.
$$ {#eq:es-nonlinear-field-norm}

Let $M=\|X\|_R$, let $0<s<R$, and suppose $\vartheta=b_0s^2M<1$. Then the nonlinear part of the original record derivation converges in $\mathcal B_s$ and satisfies

$$
 \|Q(X)\|_s
 \le a_0sM^2\left(2+\frac{s}{R-s}\right)
                    \frac{2-\vartheta}{(1-\vartheta)^2}.
$$ {#eq:es-nonlinear-bound}

It is a holomorphic map on every open input ball for which these inequalities hold uniformly with strict margins.

*Proof.* Put $c_j=R^j\|X_j\|/j!$ and $q=s/R$. In the degree-$d$ sum, $r=\sum_i j_i+2d-3$. The unweighted product sum is at most $M^d$, while

$$
 \sum_{j_1,\ldots,j_d}\left(\sum_i j_i\right)
        q^{\sum_i j_i}\prod_i c_{j_i}
 \le dM^d\frac{q}{1-q}.
$$ {#eq:es-weighted-product-bound}

Indeed $j q^j\le q/(1-q)$, and one sums the distinguished position first. Applying [@eq:es-coefficient-budget] with the grouped constants bounds the degree-$d$ contribution by $a_0sM^2d\vartheta^{d-2}(2+q/(1-q))$. Summing the identity $\sum_{d\ge2}d\vartheta^{d-2}=(2-\vartheta)/(1-\vartheta)^2$ gives [@eq:es-nonlinear-bound]. Finite input and output truncations are continuous polynomial maps. The same estimates, with a strict output-radius margin, make them converge locally uniformly in the output norm. Their limit is therefore holomorphic. ∎

<div id="sec:es-flows"></div>

## 6. Analytic record flows

We integrate the horizontal derivations on decreasing record radii. A scalar majorant controls the radius loss and yields a flow holomorphic in the initial record and direction. The canonical inclusions $\iota_{u,v}:\mathcal B_u\to\mathcal B_v$, $0<v<u$, are those of §2 and have norm at most one. The horizontal vector field is

$$
 \mathsf H_a(X)_r=i_aU_{r+1}+Q_{r,a}(X),\qquad
 \mathsf H_a\Lambda=0.
$$ {#eq:es-horizontal-vector-field}

The leading shift has norm at most $\|a\|/(u-v)$ from $\mathcal B_u$ to $\mathcal B_v$. Corollary [5.6](#cor:es-nonlinear-field) makes the full field holomorphic between suitable smaller-radius spaces on bounded input balls. The three radii in the theorem below distinguish the input space, the space containing the flow, and the smaller space where its equation and compositions are compared. The spatial normal-coordinate neighborhood is constructed in §7.

<div id="thm:es-flow"></div>

**Theorem 6.1.**

For every $R,M,A>0$, there are $0<\sigma<s<R$ and $T,C>0$ with the following properties. On an open neighborhood $\mathcal U\subset V\times\mathcal B_R$ of

$$
 \{(a,X):\|a\|\le A,\ \|X\|_R\le M\}
$$

there is a jointly holomorphic map

$$
 \Phi:\{t\in\mathbb C:|t|<T\}\times\mathcal U
                 \longrightarrow\mathcal B_s,
 \qquad \Phi(t,a,X)=\Phi_a^t(X),\qquad
 \|\Phi_a^t(X)\|_s\le C.
$$ {#eq:es-flow-map}

It is initialized by $\Phi_a^0(X)=\iota_{R,s}X$ and satisfies

$$
 \iota_{s,\sigma}\,\partial_t\Phi_a^t(X)
       =\mathsf H_a\bigl(\Phi_a^t(X)\bigr)
       \quad\text{in }\mathcal B_\sigma.
$$ {#eq:es-flow-equation}

The right side is the original polynomial record derivation, evaluated by its convergent sequence expansion. Its coordinate equations determine the analytic-time solution uniquely.

The initial-value derivative $Y_h(t)=D_X\Phi_a^t(X)[h]$ is a holomorphic $\mathcal B_s$-valued function for $h\in\mathcal B_R$. On the displayed bounded input set it has a common bound $\|Y_h(t)\|_s\le C\|h\|_R$, after increasing $C$, and

$$
 \begin{aligned}
 Y_h(0)&=\iota_{R,s}h,\\
 \iota_{s,\sigma}\,\partial_tY_h(t)
   &=D\mathsf H_a\bigl(\Phi_a^t(X)\bigr)[Y_h(t)]
                         \quad\text{in }\mathcal B_\sigma.
 \end{aligned}
$$ {#eq:es-flow-variational-equation}

After choosing $T$ smaller, compositions initialized on the intermediate space $\mathcal B_s$ are defined and satisfy, in the common space $\mathcal B_\sigma$,

$$
 \begin{aligned}
 \Phi_a^t\bigl(\Phi_a^u(X)\bigr)
       &=\iota_{s,\sigma}\Phi_a^{t+u}(X),\\
 \Phi_a^{-t}\bigl(\Phi_a^t(X)\bigr)&=\iota_{R,\sigma}X,
 \end{aligned}
$$ {#eq:es-flow-composition}

whenever $|t|,|u|,|t+u|<T$. The first expression uses the flow with initial scale $s$, followed by its inclusion in $\mathcal B_\sigma$.

Every specified finite word of horizontal flows and bounded full-spin actions has a common positive record radius, time domain and bound, also for its inverse word. These maps and their initial-value derivatives are jointly holomorphic. The coefficient involution of Definition [2.4](#def:es-lorentz-involution) satisfies

$$
 \mathfrak c\Phi_a^t(X)
   =\Phi_{\mathfrak ca}^{\bar t}(\mathfrak cX).
$$ {#eq:es-flow-reality}

Consequently Lorentz-real directions and real times, together with Lorentz-real full-spin actions, preserve the fixed locus.

*Proof.* The scalar majorant will give convergence and joint holomorphy; coefficientwise uniqueness will then give the composition laws. Choose larger bounds $\widehat M=M+1$ and $\widehat A=A+1$. We construct the flow on the product of the open balls with these bounds, retaining an open neighborhood of the original bounded set under all later restrictions.

Use the recursively ordered expansion of §5, grouped in the fixed direct-sum norms:

$$
 Q_{r,a}(X)=\sum_{d\ge2}\
 \sum_{\substack{\mathbf j\in\mathbb N_0^d\\
                  |\mathbf j|=r+3-2d}}
 B^{[d]}_{r,\mathbf j}(a;X_{j_1},\ldots,X_{j_d}).
$$ {#eq:es-grouped-expansion}

Theorem [5.5](#thm:es-coefficients) and [@eq:es-grouped-constants] give structural constants $a_0,b_0>0$ such that

$$
 \|B^{[d]}_{r,\mathbf j}(a;\cdot)\|
 \le\|a\|a_0b_0^{d-2}r\frac{r!}{\prod_i j_i!}.
$$ {#eq:es-grouped-budget}

These constants include the summable linear transfer loss:

$$
 c_r=\frac{r(r+4)}{r(r+4)-1},\qquad
 \prod_{r\ge1}c_r\le e^{11/18}.
$$ {#eq:es-transfer-product}

For formal time series with initial norm at most $\widehat M$ and $\|a\|\le\widehat A$, divide the record components by $r!$. They are majorized by the nonnegative scalar recursion

$$
 \partial_\tau F
   =\widehat A\left(F_z+z\frac{\mathrm d}{\mathrm dz}V(z,F)\right),
 \qquad V(z,w)=\frac{a_0zw^2}{1-b_0z^2w},\qquad
 F(0,z)=\frac{\widehat M}{1-z/R}.
$$ {#eq:es-flow-majorant}

Here $z$ is the generating variable for derivative order and $\tau$ is the scalar majorant time. The derivative of $V(z,F)$ is total. Indeed write $X_r(t)=\sum_{k\ge0}X_{r,k}t^k$ and $F(\tau,z)=\sum_{k,r\ge0}f_{k,r}\tau^kz^r$. Initially $\|X_{r,0}\|/r!\le\widehat M R^{-r}=f_{0,r}$. The leading shift is bounded by the corresponding coefficient of $\widehat A F_z$. If the record coefficients through time order $k$ are dominated, the degree-$d$ nonlinear term is bounded by

$$
 \begin{aligned}
 &\widehat A a_0b_0^{d-2}r
 [\tau^k]\!
 \sum_{j_1+\cdots+j_d=r+3-2d}
       \prod_{i=1}^d[z^{j_i}]F(\tau,z)\\
 &\qquad= [\tau^kz^r]\,\widehat A z\frac{\mathrm d}{\mathrm dz}
       \left(a_0b_0^{d-2}z^{2d-3}F^d\right).
 \end{aligned}
$$ {#eq:es-flow-majorization}

For fixed $r$ the sum is finite. The coefficient equations for $X_{r,k+1}$ and $f_{k+1,r}$ then give $\|X_{r,k+1}\|/r!\le f_{k+1,r}$. Induction in $k$, simultaneously for every $r$, proves formal coefficientwise domination. Each $X_{r,k}$ is a polynomial in $a$ and finitely many initial record components.

Put $W_*=4\widehat M+1$ and choose $0<\rho\le R/8$ such that $16b_0\rho^2W_*\le1$. The finite characteristic equations are

$$
 \dot z=-\widehat A(1+zV_w),\qquad
 \dot w=\widehat A zV_z,\qquad
 z(0)=\zeta,\quad w(0)=\widehat M/(1-\zeta/R).
$$ {#eq:es-characteristics}

On $|z|\le2\rho$, $|w|\le W_*$ their denominator is bounded away from zero, and

$$
 |zV_w|\le16a_0\rho^2W_*,\qquad
 |zV_z|\le5a_0\rho W_*^2.
$$

The vector field and its first derivatives are bounded in the scaled coordinates $(z/\rho,w/W_*)$. Its finite integral equation is a contraction for a common sufficiently small complex time disc, with scaled displacement less than $1/8$. For $|\zeta|\le\rho$ the initial second scaled coordinate is less than $2/7$, so these solutions remain in the displayed parent domain. On $|\zeta|=3\rho/4$ the estimate $|z(\tau,\zeta)-\zeta|\le\rho/8$ and Rouché's theorem give a unique simple inverse for $|z_*|<\rho/2$. Hence $F(\tau,z_*)=w(\tau,\zeta(\tau,z_*))$ is jointly holomorphic and bounded by $W_*$ there. Its Taylor series solves the nonnegative formal recursion above.

Take $s=\rho/4$ and restrict to a smaller positive time disc. Coefficientwise domination now gives normal convergence of the double record series in $\mathcal B_s$, with a uniform bound $C_0=2W_*$. Its finite time and output truncations are continuous polynomial maps of $(a,X)$ using finitely many initial records. On strictly smaller time discs they converge in this norm uniformly on the enlarged input balls. The scalar double-series tails tend uniformly to zero. Thus the limit is jointly Fréchet-holomorphic in $(t,a,X)$ with values in $\mathcal B_s$.

Choose $0<\sigma<s/2$ with $b_0\sigma^2(C_0+1)<1/2$. Corollary [5.6](#cor:es-nonlinear-field), applied from $\mathcal B_s$ to $\mathcal B_\sigma$, and the shift bound make $\mathsf H_a$ a holomorphic map on the ball $\|Z\|_s<C_0+1$ into $\mathcal B_\sigma$. The normally convergent time series can be differentiated in $\mathcal B_s$ on smaller time discs. Each coordinate of its derivative equals the corresponding finite polynomial coefficient of $\mathsf H_a(\Phi_a^t(X))$. Both sequences belong to $\mathcal B_\sigma$, which proves [@eq:es-flow-equation] with the original vector field.

For uniqueness, each coordinate of an analytic-time solution satisfies the finite polynomial equation for that coordinate. Differentiating successively at zero determines its time coefficients by

$$
 (k+1)X_{r,k+1}=[t^k](\mathsf H_aX(t))_r.
$$ {#eq:es-flow-time-recursion}

For fixed $r,k$, the right side uses finitely many previously determined time coefficients and record components. Two initialized analytic solutions therefore have identical coordinate Taylor series and agree near zero, hence throughout a connected common time domain. Solutions obtained from different input radii agree after their canonical inclusions whenever both are defined.

Joint holomorphy and the enlarged input ball give the initial-value Fréchet derivative into $\mathcal B_s$. Cauchy's formula on a fixed-radius initial-data disc supplies its uniform operator bound on $\|X\|_R\le M$, $\|a\|\le A$. The chain rule applied to [@eq:es-flow-equation] in $\mathcal B_\sigma$ proves [@eq:es-flow-variational-equation]. Here the differential is taken for the holomorphic map $\mathsf H_a:\mathcal B_s\to\mathcal B_\sigma$. Increasing $C$ covers both value and derivative bounds.

For composition, apply the construction a second time with input scale $s$, initial bound $C_0+1$ and direction bound $\widehat A$. It gives a positive output radius $s_1<s$ and a common time disc for all intermediate records $\Phi_a^u(X)$. Decrease $\sigma$ below $s_1$ and keep the preceding vector-field margin. Take $T$ smaller than both construction times. The curves $t\mapsto\Phi_a^{t+u}(X)$ and $t\mapsto\Phi_a^t(\Phi_a^u(X))$ solve the same initialized coordinate equations. Their common time domain $|t|<T$, $|t+u|<T$ is connected and contains zero. The uniqueness just proved gives their equality in $\mathcal B_\sigma$. Taking $u=t$ and the outer time $-t$ gives the inverse identity with $\iota_{R,\sigma}X$. This proves [@eq:es-flow-composition].

For a bounded set of full-spin matrices, their inverses are also bounded, since each spin matrix is two-dimensional with determinant one. Choose a common spin-factor norm bound $L\ge1$ for these matrices and their inverses. The action on $W_r^\pm$ has norm at most $L^{2r+4}$, so it maps a bounded $\mathcal B_u$ ball to a bounded $\mathcal B_v$ ball for $0<v<u/L^2$. Finite truncations and this strict margin prove joint holomorphy in the spin element and the record. Apply each horizontal or spin operation to the output radius and bound of the preceding one. A specified finite word and its inverse require finitely many such restrictions, leaving a positive common radius and time domain. Differentiating these holomorphic maps gives the corresponding finite-word derivatives.

Finally the polynomial tensor identities imply $\mathfrak c(\mathsf H_aX)=\mathsf H_{\mathfrak ca}(\mathfrak cX)$. Conjugating the convergent time series and applying initialized uniqueness gives [@eq:es-flow-reality]. The fixed-locus conclusion follows. ∎

<div id="sec:es-realization"></div>

## 7. Einstein realization and normal uniqueness

The radial Jacobi equation provides the passage from curvature records to a metric. Its formal solution determines the normal metric and its Einstein identities from the completed curvature list. The horizontal flow makes the radial curvature series converge; solving the same Jacobi equation analytically then gives a metric with that formal Taylor series. Write $D_\delta=\{x\in V:|x^j|<\delta,\ 1\le j\le4\}$ in the fixed marked tangent basis.

<div id="prop:es-normal-uniqueness"></div>

**Proposition 7.1.**

The completed ordered curvature list determines a unique formal metric in marked geodesic normal coordinates. Its curvature derivatives are the prescribed completion and its Ricci tensor is $\Lambda g$. The construction commutes with extension of the complex coefficient algebra. Two marked analytic Einstein metrics with equal free records and numerical constant are equal in these normal coordinates.

*Proof.* With $x\in V$ a formal spatial variable, set

$$
 R_x(t)=\sum_{r\ge0}\frac{t^r}{r!}
                  \mathcal C_r(x,\ldots,x;\,\cdot).
$$ {#eq:es-formal-radial-curvature}

Solve the formal Jacobi equation

$$
 J_x''(t;v)+R_x(t)(J_x(t;v),x)x=0,\qquad
 J_x(0;v)=0,\quad J_x'(0;v)=v,
 \qquad g_x(v,w)=\eta(J_x(1;v),J_x(1;w)).
$$ {#eq:es-formal-jacobi}

The coefficient of $J_x$ has spatial order at least two, so successive spatial degrees determine $J_x$ uniquely. At each degree the dependence on $t$ is polynomial, making evaluation at $t=1$ formally well-defined. At each fixed spatial degree, the recursion uses finitely many completed derivatives and divides only by positive integers. Each metric coefficient is therefore polynomial in a finite record prefix and $\Lambda$, as are the inverse-metric coefficients obtained by formal inversion at $g_0=\eta$. The Einstein residual $\operatorname{Ric}(g)-\Lambda g$, the normal-coordinate residual $\Gamma^k_{ij}(x)x^ix^j$, and each discrepancy between a curvature derivative at the origin and its prescribed completion all have coefficients of this kind.

For any one such coefficient, Lemma [A.1](#lem:es-finite-witness) gives an analytic Einstein metric realizing a finite Lorentz-real prefix long enough to contain every record used by it. In the parallel frame along its radial geodesic $\gamma_x$, its curvature satisfies

$$
 \left.\frac{\mathrm d^r}{\mathrm dt^r}
       P_{t\to0}R_{\gamma_x(t)}\right|_{t=0}
     =(\nabla_x^rR)_0=\mathcal C_r(x,\ldots,x;\,\cdot).
$$

The witness metric in exponential coordinates is recovered by its Jacobi fields through [@eq:es-formal-jacobi]. Its Taylor coefficients through the required degree are consequently those just constructed, and the residual coefficient is zero. Polynomial continuation from the maximal real form, as in Proposition [3.2](#prop:es-completion), proves the identity on independent complex records. This gives all prescribed curvature derivatives, the Einstein equation and marked normal coordinates. These polynomial identities remain valid over every commutative complex coefficient algebra.

Conversely, any formal metric with this completed curvature list, expressed in marked normal coordinates and a radial parallel frame, has radial curvature [@eq:es-formal-radial-curvature]. Its Jacobi equation recovers its metric by [@eq:es-formal-jacobi], proving uniqueness. Equal Taylor series give equal analytic germs. An isometry with the prescribed point and tangent map intertwines their exponential maps, so it is uniquely determined as well. ∎

<div id="thm:es-realization"></div>

**Theorem 7.2.**

Every analytic record $X$ determines a marked holomorphic Einstein four-germ by the convergent horizontal flow and a radial Jacobi equation. Its entire free record is the original one. For bounded holomorphic input families, its normal coordinates and radial spin frames have common positive domains. The construction is unique up to the prescribed marked isometry. Conversely, the free records of every marked holomorphic Einstein four-germ satisfy a factorial growth bound.

*Proof.* Fix $R,M>0$ with $\|X\|_R\le M$. Apply Theorem [6.1](#thm:es-flow) on the larger open input ball of radius $M+1$, with direction bound one. It gives a common time $T>0$, output radius $s>0$ and output bound. Fix $0<2\varepsilon<T$. For $\|a\|<\varepsilon$, put

$$
 \operatorname{Fl}_{\mathsf H_a}^{\,t}X
       :=\Phi_{a/\varepsilon}^{\varepsilon t}(X),
       \qquad |t|<2.
$$ {#eq:es-rescaled-flow}

Linearity of $\mathsf H_a$ in $a$ and initialized uniqueness in Theorem [6.1](#thm:es-flow) identify this with the original short-time flow wherever both are defined, and make it independent of $\varepsilon$ on common smaller record spaces. It is jointly holomorphic in $(t,a,X)$ and uniformly bounded there. Define the algebraic-curvature-valued holomorphic map

$$
 \widehat R_X(y)=\mathcal C_0\bigl(
           \operatorname{Fl}_{\mathsf H_y}^{\,1}X\bigr),
           \qquad \|y\|<\varepsilon.
$$ {#eq:es-analytic-radial-curvature}

For $\|x\|<\varepsilon/2$ and $|t|<2$, initialized uniqueness gives
$\operatorname{Fl}_{\mathsf H_{tx}}^{\,1}X
 =\operatorname{Fl}_{\mathsf H_x}^{\,t}X$.
The last identity of [@eq:es-cartan-identities], iterated on the polynomial completed tensors, identifies all time derivatives at zero. Hence

$$
 \widehat R_X(tx)
   =\mathcal C_0\bigl(\operatorname{Fl}_{\mathsf H_x}^{\,t}X\bigr)
   =\sum_{r\ge0}\frac{t^r}{r!}
                   \mathcal C_r(x,\ldots,x;\,\cdot).
$$ {#eq:es-convergent-radial-curvature}

This series converges on the displayed time disc and realizes the formal radial series of Proposition [7.1](#prop:es-normal-uniqueness).

Solve the analytic Jacobi equation by its integral form

$$
 J_x(t;v)=tv-
    \int_0^t(t-u)\widehat R_X(ux)(J_x(u;v),x)x\,\mathrm du,
 \qquad
 g_X(x)(v,w)=\eta(J_x(1;v),J_x(1;w)).
$$ {#eq:es-analytic-jacobi}

The flow bound gives a uniform bound for $\widehat R_X$. The norm of the linear integral operator on the right, on $|t|\le3/2$, is at most $C\|x\|^2$. A common smaller $x$-neighborhood makes this norm less than $1/2$. The Picard series therefore converges uniformly, is holomorphic in $(t,x,X)$, and gives
$J_x(1;\,\cdot)=I+O(\|x\|^2)$ uniformly on the record ball. Thus $g_X$ is a holomorphic nondegenerate metric with $g_X(0)=\eta$ and $\partial g_X(0)=0$.

Its spatial Taylor series solves the formal Jacobi recursion in Proposition [7.1](#prop:es-normal-uniqueness). By uniqueness of that recursion, it is the formal normal Einstein metric of that proposition. All Taylor coefficients of the analytic Einstein and normal-coordinate residuals consequently vanish, and every ordered curvature derivative at the mark is $\mathcal C_r$. The identity theorem gives $\operatorname{Ric}(g_X)=\Lambda g_X$ and normal coordinates, while the free projection gives the prescribed records. Proposition [7.1](#prop:es-normal-uniqueness) proves marked uniqueness. The common domain and holomorphic dependence just obtained, followed by radial spin parallel transport, give the family assertion; Proposition [7.3](#prop:es-uniform-realization) records the uniform bounds.

For the converse, take an analytic Einstein metric and parallel-transport its Weyl spinors along geodesics with initial velocities $\xi\otimes\pi$, where $\xi,\pi$ are unit spinors. Compactness of these unit spinor pairs gives a common affine time disc and curvature bound for the finite holomorphic geodesic and frame equations. Cauchy's formula bounds the coherent evaluations of the free order-$r$ record by $Cr!R_0^{-r}$. Lemma [2.3](#lem:es-record-growth) converts this to the required tensor-norm bound after a radius decrease. ∎

<div id="prop:es-uniform-realization"></div>

**Proposition 7.3.**

For every $R,M>0$ there are $\delta>0$ and $C<\infty$ such that the normal metric of Theorem [7.2](#thm:es-realization) is defined on $D_{2\delta}\subset V$ for every $\|X\|_R\le M$ and satisfies

$$
 \sup_{D_{2\delta}}(\|g_X\|+\|g_X^{-1}\|)\le C.
$$ {#eq:es-uniform-metric-bound}

On an open neighborhood of this record ball the maps $X\mapsto g_X|_{D_\delta}$ and $X\mapsto g_X^{-1}|_{D_\delta}$ are Fréchet-holomorphic maps into the Banach spaces of bounded holomorphic tensor-valued functions. The normal-coordinate maps, their inverses and radial spin frames have the same property after common restrictions. Every fixed finite spatial derivative has a uniform interior bound.

*Proof.* The enlarged input ball and common flow bounds in Theorem [7.2](#thm:es-realization) allow us to choose $\delta$ so that the Jacobi integral operator is a contraction on a neighborhood of $\overline{D_{4\delta}}$. The Picard series then converges uniformly on the product domain and is holomorphic in the Banach parameter $X$. For the endpoint operator $L_X(x)v=J_x(1;v)$, decrease $\delta$ until $\|L_X-I\|<1/2$ uniformly. The normally convergent Neumann series bounds $L_X^{-1}$ there. Since

$$
 g_X=L_X^{\mathsf T}\eta L_X,\qquad
 g_X^{-1}=L_X^{-1}\eta^{-1}(L_X^{-1})^{\mathsf T},
$$

both tensors have common bounds and holomorphic parameter dependence on the larger spatial parent.

Cauchy's formula across the remaining spatial buffer bounds every specified derivative on $D_{2\delta}$. The Christoffel and spin-connection coefficients are therefore uniformly bounded on smaller parents. The finite geodesic and parallel-spin integral equations have uniformly convergent Picard series there, giving common normal-coordinate and radial-frame maps with holomorphic parameter dependence. Each based exponential map has derivative the identity in its specified tangent frame at zero. Restricting its endpoint and initial-velocity domains makes the derivative uniformly close to that identity; the contraction proof of the finite inverse theorem gives a common inverse and its holomorphic dependence.

Finally expand each of these bounded maps in the spatial variables on a larger polydisc. Its coefficients are holomorphic in $X$, and the uniform spatial bound makes its Taylor polynomials converge locally uniformly in the bounded-function norm on a smaller polydisc. Their limit is Fréchet-holomorphic in that norm. Apply this with a final common restriction to $D_\delta$. ∎

<div id="sec:es-naturality"></div>

## 8. Point and spin-frame changes and Lorentz reality

Point and frame changes give different marked realizations of the same local geometry. Let $G=\operatorname{Spin}(V,\eta)=\operatorname{SL}(S)\times\operatorname{SL}(S')$. We write $A$ also for the induced tangent map of $A\in G$, and $A^*U$ for insertion of its two spin maps in every argument of the records. A full spin lift is retained as part of a comparison. The normal realization of a record $U$ will be denoted by $g[U]$. The coefficient $\Lambda$ is suppressed in this notation and is unchanged by each comparison. The marked exponential map of this realization identifies its normal neighborhood with a neighborhood of $0\in V$.

Use the rescaled flow of [@eq:es-rescaled-flow], on a common bounded record ball. Take $\|a\|<\varepsilon$ small enough that $ta$ lies in the common normal parent for $|t|<2$.

Put

$$
 x_a=\operatorname{Exp}^{g[U]}_o(a),\qquad
 \nu_a:V\longrightarrow T_{x_a}M,
 \qquad
 \mathcal R_{a,A}U
 =A^*\operatorname{Fl}_{\mathsf H_a}^{\,1}U,
$$ {#eq:es-point-frame-action}

where $\nu_a$ is the specified spin parallel transport along the radial geodesic from $o$ to $x_a$.

A short record comparison from $U$ to $U'$ is a pair $(a,A)$ with $U'=\mathcal R_{a,A}U$, together with representatives on which the displayed flow and normal maps are defined. A finite diagram of such comparisons is conditioned if its spin maps and inverse spin maps are bounded, and all exponential maps, inverse maps and specified finite composites have images in their assigned normal parents with uniformly positive buffer and inverse margins on the bounded family. These conditions are imposed on representatives; taking a common restriction preserves the represented local comparisons.

<div id="thm:es-physical-arrows"></div>

**Theorem 8.1.**

Short record comparisons are in bijection with short local isometries between the normal realizations with their specified full spin lifts. For $U'=\mathcal R_{a,A}U$, the associated isometry is

$$
 \Xi^U_{a,A}:g[U']\longrightarrow g[U],\qquad
 v\longmapsto
 \operatorname{Exp}^{g[U]}_{x_a}(\nu_aAv).
$$ {#eq:es-normal-isometry}

Thus the instruction $U\to U'$ corresponds to $(\Xi^U_{a,A})^{-1}$. These maps, their inverses and the comparisons in every conditioned finite diagram have common representatives for bounded holomorphic record families, and depend holomorphically on the retained parameters.

*Proof.* Along $\gamma_a(t)=\operatorname{Exp}^{g[U]}_o(ta)$, read the free records $Y_r(t)$ in the spin frame parallel-transported from the mark. Every component is holomorphic in $t$. Proposition [3.2](#prop:es-completion) identifies the ordered curvature derivatives of this Einstein metric at each point with the universal completion of its free record. Differentiation along $\gamma_a$, whose velocity has constant frame components $a$, therefore gives

$$
 \frac{\mathrm d}{\mathrm dt}Y_r(t)
       =i_aY_{r+1}(t)+Q_{r,a}(Y(t)),\qquad Y_r(0)=U_r.
$$ {#eq:es-geometric-record-flow}

The analytic-time coefficient recursion of Theorem [6.1](#thm:es-flow) determines every component from these initial values. Thus $Y(t)=\operatorname{Fl}_{\mathsf H_a}^{\,t}U$ on the common time domain. Applying the frame change $A$ at $t=1$ proves that the record at $x_a$ in the frame $\nu_aA$ is $U'$.

Rebase $g[U]$ at $x_a$ and give it that frame. Proposition [7.1](#prop:es-normal-uniqueness) identifies this rebased metric in its normal coordinates with $g[U']$. The resulting isometry is exactly [@eq:es-normal-isometry]: the new normal-coordinate representation maps into the original one. Its differential at the marked point is $\nu_aA$, and its spin lift is the one obtained from the initialized radial transport and the specified element $A$.

Conversely, let $f$ be such a local isometry from a neighborhood of the mark of $g[U']$ into a retained representative of $g[U]$. Its marked image determines $a=(\operatorname{Exp}^{g[U]}_o)^{-1}(f(0))$. Its specified spin differential, expressed relative to $\nu_a$, determines a unique full spin element $A$. Curvature and covariant differentiation are natural under an isometry, so their complete symmetric records give $U'=\mathcal R_{a,A}U$. An isometry carries affinely parametrized geodesics to affinely parametrized geodesics and preserves their initial tangent vectors. Hence it agrees with [@eq:es-normal-isometry] on a normal neighborhood. This proves both existence and uniqueness of the comparison.

Theorem [6.1](#thm:es-flow) gives common record-flow domains; Proposition [7.3](#prop:es-uniform-realization) bounds the metric, inverse metric and their finite derivatives on common normal parents. The geodesic and parallel-spin equations are finite analytic ODEs there. Their solutions and inverse exponential maps therefore have common smaller domains and holomorphic parameter dependence. For a conditioned finite diagram, the minimum of its finitely many positive buffers and inverse margins gives common domains for all representatives and specified composites. ∎

The record composition law compares a broken geodesic with the direct radial geodesic to its endpoint. Define

$$
 h_U(a,c)
 =\bigl(\operatorname{Exp}^{g[U]}_o\bigr)^{-1}
    \operatorname{Exp}^{g[U]}_{x_a}(\nu_ac).
$$ {#eq:es-endpoint-composition}

Let $\nu^{a}_c$ be spin parallel transport along the second geodesic, from $x_a$ with initial tangent $\nu_ac$, to the endpoint in [@eq:es-endpoint-composition]. With $h=h_U(a,c)$, set

$$
 K_U(a,c)=\nu_h^{-1}\nu^{a}_c\nu_a.
$$ {#eq:es-spin-holonomy}

This is the full spin rotation comparing broken radial transport with direct radial transport. Its value at a constant broken path is the identity.

<div id="prop:es-composition"></div>

**Proposition 8.2.**

For successive admissible comparisons $(a,A):U\to U'$ and $(b,B):U'\to U''$, composition and inversion are

$$
 \begin{aligned}
 (b,B)\circ(a,A)
   &=\bigl(h_U(a,Ab),\ K_U(a,Ab)AB\bigr),\\
 (a,A)^{-1}
   &=\bigl(-A^{-1}a,A^{-1}\bigr)\quad\text{at }U'.
 \end{aligned}
$$ {#eq:es-record-composition}

These operations define the local comparison groupoid and identify it with the local spin-isometry groupoid under Theorem [8.1](#thm:es-physical-arrows).

*Proof.* The composite isometry $\Xi^U_{a,A}\circ\Xi^{U'}_{b,B}$ sends the final mark to
$\operatorname{Exp}^{g[U]}_{x_a}(\nu_aAb)$. Its normal displacement from $o$ is $h_U(a,Ab)$. An isometry intertwines the spin parallel transports initialized by its spin differential. Consequently its differential at the final mark is the broken transport $\nu^{a}_{Ab}\nu_aAB$. Expressing this relative to the direct radial transport $\nu_{h_U(a,Ab)}$ gives the second component of the first formula.

The reversed first radial geodesic, expressed in the frame $\nu_aA$ at $x_a$, has initial tangent $-A^{-1}a$. Transport along that reversed segment cancels $\nu_a$. The remaining frame comparison is $A^{-1}$, giving the inverse formula with its full spin lift. The identity is $(0,1)$. Associativity follows from actual composition of the isometries and the uniqueness in Theorem [8.1](#thm:es-physical-arrows). The same uniqueness proves that these formulas agree on overlapping representatives. ∎

The element $(-1,-1)\in G$ acts trivially on $V$ and on every tensor record. It remains a distinct specified lift in the comparison groupoid. Thus the record comparison includes its spin label as well as its action on tensor components.

Fix now the Lorentz real form $V_{\mathbb R}\subset V$ of signature $(+,-,-,-)$ and its spin conjugation. On records it induces the antilinear involution $\mathfrak c$ of Definition 2.4, which also conjugates $\Lambda$. Its fixed points in the fixed spin identifications satisfy

$$
 \Lambda\in\mathbb R,\qquad
 U_r^-=\overline{U_r^+}\quad(r\ge0).
$$ {#eq:es-lorentz-records}

<div id="prop:es-lorentz-reality"></div>

**Proposition 8.3.**

The fixed records in [@eq:es-lorentz-records] correspond exactly to marked real-analytic Lorentzian Einstein four-germs. The correspondence preserves the real point comparisons and full Lorentz spin lifts of Theorem [8.1](#thm:es-physical-arrows).

*Proof.* By Proposition 3.2, curvature completion commutes with $\mathfrak c$. Hence the horizontal and vertical derivations satisfy
$\mathfrak c(\mathsf H_aX)=\mathsf H_{\mathfrak ca}(\mathfrak cX)$ and the corresponding identity for spin-frame derivations. Uniqueness of the convergent initialized flow gives

$$
 \mathfrak c\,\operatorname{Fl}_{\mathsf H_a}^{\,t}X
 =\operatorname{Fl}_{\mathsf H_{\mathfrak ca}}^{\,\bar t}
      (\mathfrak cX).
$$ {#eq:es-real-flow}

Conjugate the normal metric by the fixed antilinear map on $V$: its value at $x$ on $v,w$ is $\overline{g(\mathfrak cx)(\mathfrak cv,\mathfrak cw)}$. This is a holomorphic normal metric with the prescribed tangent form and conjugate Einstein coefficient. Its free records are $\mathfrak cX$. Proposition [7.1](#prop:es-normal-uniqueness) therefore identifies it with $g[\mathfrak cX]$. For fixed input, $g[X]$ is consequently real on $V_{\mathbb R}$. At the mark it equals the prescribed nondegenerate Lorentz form. Continuity and a restriction of the real neighborhood give the same signature throughout, and its Einstein coefficient is the real prescribed $\Lambda$.

Conversely, a real-analytic Lorentzian Einstein metric has a local holomorphic extension, obtained by complexifying its coordinate coefficients and its marked spin frame. The Einstein equation extends by the identity theorem, since it is an analytic identity in the metric, its inverse and its first two derivatives. Its free curvature derivatives satisfy [@eq:es-lorentz-records]. Their factorial estimate follows from the converse part of Theorem [7.2](#thm:es-realization). The normal realization with these records is identified with the holomorphic extension by Proposition [7.1](#prop:es-normal-uniqueness). Restriction to the real slice gives the original real-analytic metric.

For real directions and real times, [@eq:es-real-flow] preserves the fixed records. Real geodesic development and parallel transport give the real point and spin maps. Conversely a real local isometry with a prescribed Lorentz spin lift yields, by the extraction in Theorem [8.1](#thm:es-physical-arrows), precisely a real displacement and that real spin element. ∎

<div id="sec:es-finite-witnesses"></div>

## Appendix A. Finite Einstein witnesses

The completion argument requires analytic realizations of finite record prefixes. We construct them by solving analytic constraints and evolution equations, then prescribing the prefix through a finite-dimensional inverse theorem. We use the analytic Cauchy theorem in the following normal form: a finite analytic system solved for its highest derivatives transverse to a noncharacteristic analytic hypersurface, with analytic Cauchy data, has a unique local analytic solution. Additional undifferentiated finite-dimensional parameters give a jointly holomorphic solution after restriction [@Kowalevsky1875].

<div id="lem:es-finite-witness"></div>

**Lemma A.1.**

For every $N\ge0$, every finite Lorentz-real prefix $U_r^\pm$, $0\le r\le N$, and every real $\Lambda$, there is a real-analytic Lorentzian Einstein metric with this prefix, this numerical coefficient and the prescribed tangent and spin marking.

*Proof.* Choose a real orthonormal basis of the Lorentz tangent space, so that the physical flat metric is $\eta=(\mathrm dt)^2-\sum_{i=1}^3(\mathrm dy^i)^2$. We first solve analytic constraints and evolution with an auxiliary metric of signature $(-,+,+,+)$ and coefficient $\lambda$. The physical metric will be its negative and will have coefficient $\Lambda=-\lambda$. The inverse theorem will first realize small prefixes; a final dilation will reach arbitrary finite targets.

Let $A_\nu,B_\nu$ be real-analytic symmetric spatial tensors satisfying the flat transverse trace-free conditions

$$
 \operatorname{tr}A_\nu=\operatorname{tr}B_\nu=0,
 \qquad \partial^j(A_\nu)_{ij}
       =\partial^j(B_\nu)_{ij}=0.
$$ {#eq:es-finite-tt-data}

Their finite-dimensional choice will be made below. For real amplitude parameters $c_\nu$ set $\bar\gamma=\delta+\sum_\nu c_\nu A_\nu$ and let $\Sigma$ be the $\bar\gamma$-trace-free part of $\sum_\nu c_\nu B_\nu$. Put

$$
 (\bar LZ)_{ij}
 =\bar\nabla_iZ_j+\bar\nabla_jZ_i
    -\frac23\bar\gamma_{ij}\bar\nabla_kZ^k .
$$ {#eq:es-finite-conformal-killing}

Solve the two analytic systems

$$
 \overline{\operatorname{div}}\bar LZ
       =-\overline{\operatorname{div}}\Sigma,
 \qquad
 \bar\Delta\phi-\frac18R(\bar\gamma)\phi
  +\frac18|\Sigma+\bar LZ|_{\bar\gamma}^2\phi^{-7}
  +\frac{\lambda}{4}\phi^5=0
$$ {#eq:es-finite-constraints}

with $Z=\partial_1Z=0$, $\phi=1$, $\partial_1\phi=0$ on $y^1=0$. Here tensor contractions are bilinear in the complexified systems. At $c=\lambda=0$, the coefficient of $\partial_1^2 Z$ in the first system is $I+\frac13(\mathrm dy^1)^\sharp\otimes\mathrm dy^1$, with eigenvalues $1,1,4/3$. The coefficient of $\partial_1^2\phi$ in the second system is $\bar\gamma^{11}=1$. The first system is independent of $\phi$, and the second is analytic near the unit $\phi=1$. The analytic Cauchy theorem therefore gives solutions jointly holomorphic in $c,\lambda$ and $y$ near zero.

Set $T=\Sigma+\bar LZ$, $\gamma=\phi^4\bar\gamma$ and $K=\phi^{-2}T$. The conformal connection difference is
$2\phi^{-1}(\delta_i^k\partial_j\phi+\delta_j^k\partial_i\phi-\bar\gamma_{ij}\bar\gamma^{k\ell}\partial_\ell\phi)$. Substitution gives

$$
 \begin{aligned}
 R(\gamma)&=\phi^{-5}\bigl(-8\bar\Delta\phi+R(\bar\gamma)\phi\bigr),\\
 \operatorname{div}_\gamma K
   &=\phi^{-6}\overline{\operatorname{div}}T,&
 |K|_\gamma^2&=\phi^{-12}|T|_{\bar\gamma}^2,&
 \operatorname{tr}_\gamma K&=0.
 \end{aligned}
$$ {#eq:es-finite-conformal-identities}

Equations ([-@eq:es-finite-constraints]) imply the constraint equations

$$
 R(\gamma)+(\operatorname{tr}_\gamma K)^2-|K|_\gamma^2
       =2\lambda,
 \qquad
 \operatorname{div}_\gamma K
       -\mathrm d\operatorname{tr}_\gamma K=0.
$$ {#eq:es-finite-solved-constraints}

At the flat parameter, the first amplitude variations of $Z$ and $\phi-1$ vanish. Indeed their sources are respectively $\partial^j(B_\nu)_{ij}$ and $\partial_i\partial_j(A_\nu)_{ij}-\Delta\operatorname{tr}A_\nu$, and their Cauchy data are zero. Thus $\dot\gamma=A_\nu$ and $\dot K=B_\nu$ in each amplitude direction.

Write $\tau=\operatorname{tr}_\gamma K$ and evolve by

$$
 \partial_t\gamma_{ij}=2K_{ij},\qquad
 \partial_tK_{ij}
   =-\operatorname{Ric}(\gamma)_{ij}
     -\tau K_{ij}+2K_i{}^kK_{kj}
     +\lambda\gamma_{ij}.
$$ {#eq:es-finite-gaussian-evolution}

After eliminating $K$, these equations are solved for $\partial_t^2\gamma$, with right-hand sides analytic in the invertible spatial metric, its tangential derivatives through order two and its first time derivative. The analytic initial data are the $\gamma,K$ constructed above, so the analytic Cauchy theorem applies with normal coefficient the identity. Put $g_{\mathrm a}=-(\mathrm dt)^2+\gamma_{ij}\,\mathrm dy^i\mathrm dy^j$.

The time-containing Christoffel symbols are $\Gamma^0_{ij}=K_{ij}$ and $\Gamma^i_{0j}=K^i{}_j$. Consequently

$$
 \begin{aligned}
 \operatorname{Ric}(g_{\mathrm a})_{ij}
 &=\operatorname{Ric}(\gamma)_{ij}
     +\partial_tK_{ij}+\tau K_{ij}-2K_i{}^kK_{kj},\\
 \operatorname{Ric}(g_{\mathrm a})_{00}
 &=-\partial_t\tau-|K|^2,
 &\operatorname{Ric}(g_{\mathrm a})_{0i}
 &=\nabla^jK_{ij}-\partial_i\tau.
 \end{aligned}
$$ {#eq:es-finite-gaussian-ricci}

The spatial Einstein equations hold by construction. Let $\mathcal H=\operatorname{Ric}(g_{\mathrm a})_{00}+\lambda$ and $\mathcal M_i=\operatorname{Ric}(g_{\mathrm a})_{0i}$. The contracted Bianchi identity, with those spatial equations imposed, is the homogeneous normal system

$$
 \partial_t\mathcal H
 =2\nabla^i\mathcal M_i-2\tau\mathcal H,
 \qquad
 \partial_t\mathcal M_i
 =\frac12\partial_i\mathcal H-\tau\mathcal M_i.
$$ {#eq:es-finite-constraint-propagation}

The initial values vanish by [@eq:es-finite-solved-constraints]. Analytic uniqueness gives $\mathcal H=\mathcal M=0$ and hence $\operatorname{Ric}(g_{\mathrm a})=\lambda g_{\mathrm a}$. The initialized solutions are real on the real parameter and coordinate slice by conjugation and uniqueness. On a smaller real neighborhood $\gamma$ is positive definite. Therefore $g=-g_{\mathrm a}$ is Lorentzian, and $\operatorname{Ric}(g)=-\lambda g$.

It remains to prescribe the free record prefix. We choose a finite TT family whose physical free-record map is a submersion with equal source and target dimensions. For $z\in\mathbb C$ put $\kappa(z)=(1,z)$ and $k(z)_{AA'}=\kappa_A(z)\bar\kappa_{A'}(z)$. These are nonzero real null covectors. For each $r$, the tensors

$$
 \kappa(z)^{r+4}\bar\kappa(z)^r
$$ {#eq:es-finite-coherent-directions}

span $W_r^+$ over $\mathbb C$. To see this, a functional annihilating all of them gives a polynomial in $z,\bar z$ of bidegree at most $(r+4,r)$. With $z=x+\mathrm i y$, it becomes a polynomial vanishing for every real pair $(x,y)$, hence is identically zero. The substitution between $(z,\bar z)$ and $(x,y)$ is invertible over $\mathbb C$, so the original functional vanishes. A finite spanning set valid for every $r\le N$ is obtained from
$x,y\in\{0,\ldots,2N+4\}$: its polynomial degree in each real variable is at most $2N+4$, and successive one-variable interpolation proves the assertion on this grid. Choose a complex basis of $(r+5)(r+1)$ such directions for each $r$.

Choose distinct nonzero real numbers $\tau_0,\ldots,\tau_N$. The Vandermonde matrix $((\mathrm i\tau_\ell)^j)_{0\le j,\ell\le N}$ is invertible. Its inverse columns give profiles

$$
 f_r(s)=\sum_{\ell=0}^N b_\ell^{(r)}e^{\mathrm i\tau_\ell s},
 \qquad f_r^{(j)}(0)=\delta_{jr}\quad(0\le j\le N).
$$ {#eq:es-finite-profiles}

For one chosen direction write $k_{AA'}=\kappa_A\lambda_{A'}$ with $\lambda=\bar\kappa$, and choose $\mu$ with $d=\lambda_{0'}\mu_{1'}-\lambda_{1'}\mu_{0'}\ne0$. The polarization $p_{AA'}=\kappa_A\mu_{A'}$ is null and transverse to $k$. In the physical flat tangent convention the metric variation $h_{ab}=a p_ap_b e^{\mathrm i\tau k\cdot x}$ has linearized last-slot curvature

$$
 \begin{aligned}
 R^{(1)}_{abcd}(h)
 &=\frac12\bigl(
   \partial_a\partial_ch_{bd}+\partial_b\partial_dh_{ac}
   -\partial_a\partial_dh_{bc}-\partial_b\partial_ch_{ad}\bigr)\\
 &=-\frac12a\tau^2
   (k_ap_b-k_bp_a)(k_cp_d-k_dp_c)e^{\mathrm i\tau k\cdot x},\\
 \Psi^{+(1)}_{ABCD}
 &=\frac12a\tau^2d^2\kappa_A\kappa_B\kappa_C\kappa_D
       e^{\mathrm i\tau k\cdot x},
 &\Psi^{-(1)}&=0.
 \end{aligned}
$$ {#eq:es-finite-wave-readout}

The first line follows by differentiating the Christoffel formula at a constant metric. For the last line use $k_ap_b-k_bp_a=d\kappa_A\kappa_B\epsilon_{A'B'}$ and the curvature readout of [@eq:es-curvature-decomposition]. All normalization factors displayed here are nonzero.

Replace $p$ by $p-(p_0/k_0)k$. Since $k$ is a nonzero real null covector, $k_0\ne0$. This change removes $p_0$ and preserves its wedge with $k$, its nullness and its transversality. The resulting wave is temporal and its spatial initial metric and half time derivative satisfy [@eq:es-finite-tt-data]. Pair it with its Lorentz conjugate to obtain a real TT wave. Use the negative of this real wave for the auxiliary initial data, so that the physical metric variation after $g=-g_{\mathrm a}$ is the displayed wave and its conjugate.

For each frequency divide its amplitude by $\tau_\ell^2d^2/2$ and combine with [@eq:es-finite-profiles]. The positive linearized Weyl spinor is then $c\kappa^4f_r(k\cdot x)$, its negative spinor is its Lorentz conjugate, and its order-$j$ free record at the origin is

$$
 \delta_{jr}c\kappa^{r+4}\bar\kappa^r
 \qquad(0\le j\le N).
$$ {#eq:es-finite-wave-record}

Real and imaginary parts of $c$ supply two real amplitude directions. Put $d_N=2\sum_{r=0}^N(r+5)(r+1)$. The chosen bases and profiles therefore give $d_N$ real amplitudes and an invertible derivative onto the real space of Lorentz-real prefixes.

Read the nonlinear family in an analytic orthonormal spin frame $\nu(c,\lambda)$ at the origin, identified with the prescribed marking. Such a frame and its local spin lift are obtained by analytic orthonormalization near the flat frame. At the flat parameter, all background Weyl derivatives vanish, so point-frame and connection variations contribute nothing to the first variation of the free-record map. Linearization of [@eq:es-finite-gaussian-evolution] has precisely the TT wave with its prescribed initial data, by analytic uniqueness. The analytic map to the real prefix space is

$$
 \begin{aligned}
 \mathcal F_N:\mathbb R^{d_N}\times\mathbb R
    &\longrightarrow
    \left(\bigoplus_{r=0}^N(W_r^+\oplus W_r^-)^{\mathfrak c}\right)
       \times\mathbb R,\\
 (c,\lambda)&\longmapsto
    \bigl((U_r(g(c,\lambda),\nu(c,\lambda)))_{r=0}^N,-\lambda\bigr),\\
 D\mathcal F_N(0,0)&=
       \begin{pmatrix}L_N&*\\0&-1\end{pmatrix},
       \qquad L_N\text{ a real linear isomorphism}.
 \end{aligned}
$$ {#eq:es-prefix-submersion}

The finite-dimensional analytic inverse theorem realizes every sufficiently small real prefix and scalar. For an arbitrary finite target choose $s>0$ so large that $(s^{-r-2}U_r,s^{-2}\Lambda)_{0\le r\le N}$ lies in this neighborhood. If $h$ realizes the scaled target, set $g=s^{-2}\delta_s^*h$ with $\delta_s(x)=sx$. The pullback contributes $s^{r+4}$ on the $r+4$ covariant curvature-derivative slots, and the constant metric scaling contributes $s^{-2}$. Thus the tangent metric is unchanged, the order-$r$ marked curvature derivative is multiplied by $s^{r+2}$, and the Einstein coefficient by $s^2$. It realizes the requested prefix and coefficient. ∎

This construction uses finitely many analytic equations and finite-dimensional parameters. Its neighborhood may depend on the length and values of the prescribed prefix. Proposition [3.2](#prop:es-completion) uses this finite-prefix existence to verify polynomial identities; common analytic domains are obtained separately from the record-flow and Jacobi estimates.

<div id="sec:es-low-orders"></div>

## Appendix B. The first nonlinear corrections

The first three corrections show how linear shifts lead to the first nonlinear insertion. Recursion ([-@eq:es-recursion]) gives finite tensor formulas at each fixed order, using the same compatible Spencer inverse $M_rJ_r^*$ as in §4. For a polynomial coefficient $F_b$ let $D_jF_b[Z]$ mean its differential with respect to the two chiral components of $U_j$; the scalar $\Lambda$ is held fixed. The two outer derivative arguments in the following formulas are $a,b$.

Since $Q_0=0$, the first correction is

$$
 Q_1=-M_1J_1^*K_1,\qquad
 K_1(a,b)=\mathsf V_{R_U(a,b)}U_0.
$$ {#eq:es-q-one}

It is quadratic in $(U_0,\Lambda)$. Define the two-argument tensor

$$
 (T_2)_{a,b}=D_0Q_{1,b}[i_aU_1],
 \qquad Q_2=M_2J_2^*(\tau T_2-K_2),
 \qquad K_2(a,b)=\mathsf V_{R_U(a,b)}U_1.
$$ {#eq:es-q-two}

Every term of $Q_2$ has curvature degree two and total input order one. At the next order put

$$
 \begin{aligned}
 (T_3^{[2]})_{a,b}
     &=D_0Q_{2,b}[i_aU_1]+D_1Q_{2,b}[i_aU_2],\\
 (T_3^{[3]})_{a,b}
     &=D_1Q_{2,b}[Q_{1,a}],\\
 Q_3^{[2]}&=M_3J_3^*(\tau T_3^{[2]}-K_3),\\
 Q_3^{[3]}&=M_3J_3^*\tau T_3^{[3]},\qquad
 Q_3=Q_3^{[2]}+Q_3^{[3]}.
 \end{aligned}
$$ {#eq:es-q-three}

Here $K_3(a,b)=\mathsf V_{R_U(a,b)}U_2$. The quadratic inputs have total order two, while the cubic inputs all have order zero. The last line exhibits the first possible nonlinear insertion: a coefficient of $Q_1$ replaces the order-one position of $Q_2$. Both output chiralities and both possible intermediate record chiralities are included in the differential $D_1$. Differentiation of a scalar position contributes zero.

These formulas follow by applying the polynomial product rule in [@eq:es-recursion]. The weight relation [@eq:es-completion-weight] permits only degree two for $r=1,2$ and degrees two and three for $r=3$, so the displayed formulas contain every term at these orders. The bounds for all orders are given by Theorem [5.5](#thm:es-coefficients).

The recursion can also be checked directly on the Ricci-flat Kasner metric

$$
 g=\mathrm dt^2-\sum_{i=1}^3t^{2p_i}(\mathrm dx^i)^2,
 \qquad (p_1,p_2,p_3)=(-2/7,3/7,6/7).
$$

In its orthonormal frame, compute the ordered curvature derivatives through order four at $t=1$ and project to the two chiral records. Evaluate $Q_r=\nabla U_r-iU_{r+1}$ and $\mathsf H Q_{r-1}$ by covariant differentiation of these geometric records, and $K_r$ by curvature action. Applying the Spencer inverse to the right side of [@eq:es-recursion] agrees with $Q_r$ in all 520 components for $1\le r\le3$, with zero fully symmetric projection. These are exact equalities over $\mathbb Q(\mathrm i)$ after a common spin-basis rescaling. The companion archive, [`exact-set-checks-v1.0.2.zip`](https://github.com/lioristhmus/local-analytic-einstein-metrics/raw/refs/tags/v1.0.2/paper/exact-set-checks-v1.0.2.zip), is included with the source and computational supplements and supplies these calculations, their exact output and checksums. Its SageMath 10.9 entry point is `check_kasner_recursion.py --max-r 3`; the accompanying README specifies the spin-basis rescaling, curvature convention and isolated execution environment.

<div id="sec:es-ai-use"></div>

## AI-use disclosure {.unnumbered .unlisted}

AI systems were used extensively throughout this research and the preparation of this manuscript. The models used were GPT-6 Pro, gpt-6.1-sol (xhigh), and Claude Opus 5.5 (xhigh). Selected finite algebraic identities and explicit metric examples were checked using SageMath and independent Python implementations; the code, inputs, computational environments and recorded results are provided in the [computational supplement](https://github.com/lioristhmus/local-analytic-einstein-metrics/tree/v1.0.2/computations).
