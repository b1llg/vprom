# BLOCK 4: CONTINUUM MECHANICS THEORY
## Assignment Structure for LaTeX Book

**Goal:** Master tensor formulation and continuum mechanics for large displacement analysis

**Deliverable:** One LaTeX book with 8 chapters + introduction + conclusion

**Time Estimate:** 40-50 hours (7-8 weeks at 6h/week)

---

## INTRODUCTION CHAPTER

### Content to Write:
- Motivation for studying continuum mechanics
- Overview of large displacement framework
- Connection to your PhD goals (viscoplasticity, ROM, high-temperature components)
- Brief preview of all 8 chapters
- How this prepares you for MFEM implementation

**Length:** 2-3 pages

---

## CHAPTER 1: Tensor Fundamentals AND EINSTEIN SUMMATION CONVENTION

### Required Reading:
- https://www.continuummechanics.org/tensornotationbasic.html
- https://www.continuummechanics.org/tensornotationadvanced.html

### Theory Topics to Cover:

**1.1 Einstein Summation Convention**
- Repeated index implies summation
- Free vs dummy indices
- Valid vs invalid expressions

**1.2 Kronecker Delta δᵢⱼ**
- Definition
- Properties
- Key identities

**1.3 Permutation Symbol εᵢⱼₖ**
- Definition
- Connection to cross products
- Key identities

**1.4 Common Tensor Operations**
- Dot product: aᵢbᵢ
- Matrix-vector: yᵢ = Aᵢⱼxⱼ
- Matrix-matrix: Cᵢₖ = AᵢⱼBⱼₖ
- Trace: Aᵢᵢ
- Double contraction: AᵢⱼBᵢⱼ

### Problems to Solve:

**Problem 1.1:** Given a = [2, -1, 3], b = [1, 4, -2], calculate aᵢbᵢ showing all terms

**Problem 1.2:** Given matrix A and vector x, calculate yᵢ = Aᵢⱼxⱼ for each component

**Problem 1.3:** Verify δᵢⱼδⱼₖ = δᵢₖ for specific values of i, k

**Problem 1.4:** Calculate cross product using (a × b)ᵢ = εᵢⱼₖaⱼbₖ

**Problem 1.5:** Calculate trace using Aᵢᵢ notation

### Python Exercise:
Implement all problems using numpy.einsum (include code and output in chapter)

---

## CHAPTER 2: DEFORMATION GRADIENT AND MOTION

### Required Reading:
- https://www.continuummechanics.org/deformationgradient.html
- https://www.continuummechanics.org/polardecomposition.html
- Belytschko §3.2.2-3.2.3 (pages 79-80)
- Belytschko §3.2.6 (pages 83-84)
- Belytschko §3.7.1 (page 130)

### Theory Topics to Cover:

**2.1 Material vs Spatial Description**
- Lagrangian coordinates X
- Eulerian coordinates x
- Motion: x = φ(X, t)
- Displacement: u = x - X

**2.2 Deformation Gradient**
- Definition: FᵢJ = ∂xᵢ/∂XJ
- Physical meaning: maps line elements
- Examples: translation, rotation, stretch

**2.3 Jacobian Determinant**
- J = det(F)
- Physical meaning: volume ratio
- Constraint: J > 0

**2.4 Polar Decomposition**
- F = R·U (right decomposition)
- F = V·R (left decomposition)
- R: rotation, U: right stretch, V: left stretch
- Why it matters for plasticity

### Problems to Solve:

**Problem 2.1:** Calculate F for x = 1.2X, y = 0.8Y, z = Z. Find J and interpret.

**Problem 2.2:** Calculate F for 30° rotation about z-axis. Verify det(F) = 1 and F^T F = I.

**Problem 2.3:** Given F = [[1.3, -0.375], [0.75, 0.65]], compute polar decomposition (calculate C, U, R).

**Problem 2.4:** Calculate volume change for F = diag(1.5, 1.2, 0.8).

### Python Exercise:
Implement deformation gradient calculations and polar decomposition using scipy.linalg.polar

---

## CHAPTER 3: STRAIN MEASURES (SMALL AND FINITE)

### Required Reading:
- https://www.continuummechanics.org/smallstrain.html
- https://www.continuummechanics.org/greenstrain.html
- Belytschko §3.3.1 (pages 95-97)

### Theory Topics to Cover:

**3.1 Small Strain Tensor**
- Definition: εᵢⱼ = ½(∂uᵢ/∂xⱼ + ∂uⱼ/∂xᵢ)
- Physical interpretation
- Engineering vs tensorial shear
- When it fails (large rotation, not large strain!)

**3.2 Green Strain Tensor**
- Definition: E = ½(F^T F - I)
- Component form with quadratic terms
- Frame invariance property
- Why quadratic terms matter

**3.3 Comparison**
- When to use small strain
- When to use Green strain
- Examples where small strain fails

### Problems to Solve:

**Problem 3.1:** Given u = 0.01x, v = 0.02y, w = 0, calculate all εᵢⱼ components.

**Problem 3.2:** Given F for 30° pure rotation, calculate E and verify E = 0.

**Problem 3.3:** Given F = [[1.3, -0.375], [0.75, 0.65]], calculate Green strain E.

**Problem 3.4:** For small displacement (u = 0.001x, v = -0.0005y, w = 0), show E ≈ ε.

### Python Exercise:
Implement small strain and Green strain functions. Compare for pure rotation, pure stretch, and combined cases.

---

## CHAPTER 4: STRESS TENSOR FUNDAMENTALS

### Required Reading:
- https://www.continuummechanics.org/stress.html
- https://www.continuummechanics.org/tractionvector.html
- https://www.continuummechanics.org/stressintroduction.html
- Belytschko §3.4.1-3.4.2 (pages 104-107)

### Theory Topics to Cover:

**4.1 Cauchy Stress Tensor**
- Physical meaning
- Traction vector: t = σ·n
- Symmetry: σᵢⱼ = σⱼᵢ
- Normal and shear components

**4.2 Multiple Stress Measures**
- Cauchy stress σ (force per current area)
- 1st Piola-Kirchhoff P
- 2nd Piola-Kirchhoff S (work conjugate to E)
- Transformations between them

**4.3 When to Use Each**
- Cauchy for equilibrium
- 2nd PK for constitutive laws
- Importance for large displacement

### Problems to Solve:

**Problem 4.1:** Given σ and normal vector n, calculate traction t, normal stress σₙ, and shear stress τ.

**Problem 4.2:** Derive stress symmetry (σₓᵧ = σᵧₓ) from moment balance.

**Problem 4.3:** Calculate traction on planes at different orientations for uniaxial tension.

**Problem 4.4:** Transform Cauchy stress σ to 2nd PK stress S for given F.

### Python Exercise:
Implement traction calculation and stress transformations (Cauchy ↔ 2nd PK).

---

## CHAPTER 5: PRINCIPAL STRESSES AND INVARIANTS

### Required Reading:
- https://www.continuummechanics.org/principalstress.html
- https://www.continuummechanics.org/hydrodeviatoricstress.html

### Theory Topics to Cover:

**5.1 Principal Stresses**
- Eigenvalue problem
- Characteristic equation
- Principal directions

**5.2 Stress Invariants**
- I₁ = tr(σ)
- I₂ = ½[(tr σ)² - tr(σ²)]
- I₃ = det(σ)
- Why "invariant"?

**5.3 Hydrostatic-Deviatoric Decomposition**
- Hydrostatic: p = ⅓I₁
- Deviatoric: s = σ - pI
- J₂ = ½s:s
- Physical meaning

### Problems to Solve:

**Problem 5.1:** Given 2D stress tensor, find principal stresses and directions.

**Problem 5.2:** Calculate I₁, I₂, I₃ for 3D stress tensor. Verify using principal stresses.

**Problem 5.3:** Calculate hydrostatic pressure p, deviatoric stress s, and J₂.

**Problem 5.4:** For pure shear stress, calculate principal stresses and J₂.

### Python Exercise:
Implement principal stress calculation using scipy.linalg.eigh and invariant calculations.

---

## CHAPTER 6: VON MISES STRESS AND YIELD CRITERION

### Required Reading:
- https://www.continuummechanics.org/vonmisesstress.html

### Theory Topics to Cover:

**6.1 Von Mises Stress Definition**
- σᵥₘ = √(3J₂)
- Alternative forms (principal stresses, components)
- All equivalent!

**6.2 Yield Criterion**
- f = σᵥₘ - σᵧ ≤ 0
- Physical meaning
- Why J₂ not I₁?

**6.3 Connection to 1D Work**
- 1D: f = |σ| - σᵧ
- 3D: f = √(3J₂) - σᵧ
- Same conceptual structure

**6.4 Special Cases**
- Uniaxial: σᵥₘ = σ
- Pure shear: σᵥₘ = √3 τ
- Hydrostatic: σᵥₘ = 0

### Problems to Solve:

**Problem 6.1:** Calculate von Mises stress for general 3D stress state using multiple formulas.

**Problem 6.2:** Verify special cases (uniaxial, pure shear, biaxial).

**Problem 6.3:** Check yield condition: given σ and σᵧ, is material yielding?

### Python Exercise:
Implement von Mises function and yield surface visualization.

---

## CHAPTER 7: VOIGT NOTATION AND ELASTICITY

### Required Reading:
- https://www.continuummechanics.org/hookeslaw2.html

### Theory Topics to Cover:

**7.1 Voigt Notation Mapping**
- Stress vector {σ} (6×1)
- Strain vector {ε} (6×1)
- **CRITICAL:** Factor of 2 on shear strains
- Why? Energy equivalence

**7.2 Elasticity Tensor**
- General: 6×6 matrix [C]
- Isotropic: 2 parameters (E, ν)
- Lamé parameters: λ, μ

**7.3 Plane Stress vs Plane Strain**
- When to use each
- 3×3 reduced matrices

### Problems to Solve:

**Problem 7.1:** Given σ and ε tensors, verify energy equivalence σ:ε = {σ}^T{ε}.

**Problem 7.2:** Construct 6×6 isotropic elasticity matrix for given E and ν. Calculate stress for given strain.

**Problem 7.3:** Derive 3×3 plane stress elasticity matrix from 6×6.

### Python Exercise:
Implement Voigt conversions and elasticity matrix generation.

---

## CHAPTER 8: SYNTHESIS - 3D RETURN MAPPING ALGORITHM

### Required Reading:
- Review all previous chapters
- Review your Block 2-3 return mapping (1D)

### Theory Topics to Cover:

**8.1 Review of 1D Return Mapping**
- Algorithm from Block 2
- Elastic predictor
- Plastic corrector

**8.2 Extension to 3D: Conceptual Design**
- Key differences 1D vs 3D
- Algorithm in principal stress space
- Spectral decomposition
- Hydrostatic preservation
- Deviatoric return

**8.3 Complete 3D Algorithm**
- Step-by-step pseudocode
- Working in principal space
- Transform back to Cartesian

**8.4 Connection to Large Displacement**
- Material vs spatial formulation
- Frame invariance
- Extension to viscoplasticity (preview)

**8.5 Preparation for MFEM**
- What you're ready for
- How algorithm integrates with FE
- Dimension-agnostic implementation

### Questions to Answer:

**Question 8.1:** Why do we need different strain measures? When is small strain adequate vs when must you use Green strain?

**Question 8.2:** Explain frame invariance in plasticity. How does polar decomposition help?

**Question 8.3:** What does "work conjugate" mean? Why use S with E?

**Question 8.4:** Why is von Mises better than Tresca for metals? Why is J₂ invariant important?

**Question 8.5:** How will return mapping fit into MFEM? What data structures make sense?

**Question 8.6:** For your PhD (large displacement viscoplasticity at high temps), which formulation will you use and why?

### Python Exercise:
Complete 3D von Mises return mapping implementation. Test cases:
1. Elastic loading
2. Uniaxial tension (plastic)
3. General stress with shear (plastic)
4. Pure hydrostatic (should not yield)
5. Compare 1D vs 3D for uniaxial case

---

## CONCLUSION CHAPTER

### Content to Write:

**Summary of Accomplishments**
- What you learned in each chapter
- Key insights gained
- Connections between topics

**Preparation for MFEM (Block 5)**
- What you're ready for
- Tensor operations mastered
- Algorithm design complete
- Dimension-agnostic understanding

**Connection to PhD Goals**
- Large displacement framework established
- Frame invariance understood
- Path to viscoplasticity clear
- Foundation for ROM work

**Reflection**
- What was most challenging?
- What surprised you?
- What would you do differently?

**Length:** 2-3 pages

---

## DELIVERABLE STRUCTURE

Your LaTeX book should have:

```
Title Page
Abstract
Table of Contents

Introduction (2-3 pages)

Chapter 1: Tensor Fundamentals (theory + 5 problems + Python)
Chapter 2: Deformation Gradient (theory + 4 problems + Python)
Chapter 3: Strain Measures (theory + 4 problems + Python)
Chapter 4: Stress Tensor (theory + 4 problems + Python)
Chapter 5: Principal Stresses (theory + 4 problems + Python)
Chapter 6: Von Mises (theory + 3 problems + Python)
Chapter 7: Voigt Notation (theory + 3 problems + Python)
Chapter 8: Synthesis (theory + 6 questions + Python implementation)

Conclusion (2-3 pages)

Bibliography
```

**Total Problems:** 31 (27 hand calculations + 4 conceptual questions + 8 Python implementations)

**Estimated Length:** 100-130 pages

---

## GRADING CRITERIA

**Theory (40%):** Complete, correct derivations with clear explanations

**Problems (30%):** All solved with work shown and verified

**Python (20%):** Working implementations with outputs included

**Synthesis (10%):** Clear connections, preparation for MFEM demonstrated

---

**Start when ready. Complete at your pace (7-8 weeks at 6h/week).**