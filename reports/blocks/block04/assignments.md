# BLOCK 4: 2D/3D Continuum Mechanics Theory

**Time:** 35-45 hours  
**Timeline:** 6-8 weeks at 6h/week

---

## Required Reading

1. **Simo & Hughes Ch 1.1-1.6** (15-18h)
2. **Belytschko Ch 3** (10-12h)
3. **Holzapfel Ch 1-2** (as needed)

---

## ASSIGNMENT 4.1: Tensor Fundamentals & Stress Tensor (12-15h)

**Deliverable:** `reports/blocks/block04_tensor_fundamentals.md`

**Reading:** Simo §1.1-1.3, Belytschko §3.1-3.3

### Section 1: Index Notation (3-4h)

1. Free vs dummy indices
2. Kronecker delta properties, derive δ_ij a_j = a_i and δ_ii = 3
3. Permutation symbol, derive ε_ijk ε_imn = δ_jm δ_kn - δ_jn δ_km
4. Einstein summation: 5 examples

### Section 2: Stress Tensor (4-5h)

1. Derive Cauchy theorem: t_i = σ_ij n_j
2. Prove σ_ij = σ_ji
3. Physical meaning of components
4. Derive transformation: σ'_ij = R_ik R_jl σ_kl

### Section 3: Strain Tensor (5-6h)

1. Deformation gradient F_ij = ∂x_i/∂X_j
2. Derive Green-Lagrange: E_ij = 1/2(F_ki F_kj - δ_ij)
3. Derive small strain: ε_ij = 1/2(∂u_i/∂x_j + ∂u_j/∂x_i)
4. All 6 components for 3D, 2D plane strain, 2D plane stress

### Hand Calculations

**Problem 1:** Given σ = [[100,50,0],[50,80,0],[0,0,60]] MPa, rotate 45° about z. Find σ'.

**Problem 2:** Given u_1 = 0.001x_1, u_2 = 0.002x_2, u_3 = 0. Find all ε_ij.

**Problem 3:** From Problem 1, find traction on n = [1/√2, 1/√2, 0].

---

## ASSIGNMENT 4.2: Principal Stresses & Invariants (10-12h)

**Deliverable:** `reports/blocks/block04_principal_stresses.md`

**Reading:** Simo §1.4, Belytschko §3.4-3.5

### Section 1: Eigenvalue Problem (3-4h)

1. Derive λ³ - I₁λ² + I₂λ - I₃ = 0 from det(σ - λI) = 0
2. Prove principal stresses real (use symmetry)
3. Prove principal directions orthogonal

### Section 2: Invariants (4-5h)

1. Derive I₁ = σ₁ + σ₂ + σ₃
2. Derive I₂ = σ₁σ₂ + σ₂σ₃ + σ₃σ₁, prove equivalent to I₂ = 1/2(σ_ij σ_ji) - 1/2(σ_kk)²
3. Derive I₃ = σ₁σ₂σ₃ = det(σ)

### Section 3: Deviatoric Stress (3-4h)

1. Define s_ij = σ_ij - 1/3(σ_kk)δ_ij
2. Prove J₁ = tr(s) = 0
3. Define J₂ = 1/2 s_ij s_ij
4. Derive J₂ = 1/6[(σ₁-σ₂)² + (σ₂-σ₃)² + (σ₃-σ₁)²]
5. Physical meaning

### Hand Calculations

**Problem 1:** Given σ = [[200,100,0],[100,150,0],[0,0,100]] MPa. Find principal stresses, principal directions, verify orthogonality.

**Problem 2:** Calculate I₁, I₂, I₃ from components and from principal stresses. Verify match. Find J₂.

**Problem 3:** For 2D σ = [[100,50],[50,60]] MPa. Draw Mohr's circle, find principal stresses graphically, find max shear, verify analytically.

---

## ASSIGNMENT 4.3: Voigt Notation & Plane Stress/Strain (8-10h)

**Deliverable:** `reports/blocks/block04_voigt_plane_theory.md`

**Reading:** Simo §1.5, Belytschko §3.6-3.7

### Section 1: Voigt Notation (3-4h)

1. Map σ_ij → {σ₁₁, σ₂₂, σ₃₃, σ₁₂, σ₂₃, σ₁₃}ᵀ
2. Map ε_ij → {ε₁₁, ε₂₂, ε₃₃, 2ε₁₂, 2ε₂₃, 2ε₁₃}ᵀ, explain factor of 2
3. Derive 6×6 D for isotropic material
4. Write D for: isotropic, cubic, transversely isotropic, orthotropic

### Section 2: Plane Stress (2-3h)

1. Assumptions: σ₃₃ = σ₁₃ = σ₂₃ = 0, explain why ε₃₃ ≠ 0
2. Derive 3×3 D_ps = E/(1-ν²) [...]
3. Write all 6 stress-strain equations

### Section 3: Plane Strain (2-3h)

1. Assumptions: ε₃₃ = ε₁₃ = ε₂₃ = 0, derive σ₃₃ = ν(σ₁₁ + σ₂₂)
2. Derive 3×3 D_pε = E/((1+ν)(1-2ν)) [...]
3. Compare stiffness: plane stress vs plane strain

### Hand Calculations

**Problem 1:** Given σ = [[100,50,30],[50,80,20],[30,20,60]] MPa. Write Voigt vector. Calculate strain (E=200 GPa, ν=0.3). Convert back.

**Problem 2:** Plane stress, E=200 GPa, ν=0.3, ε₁₁=0.001, ε₂₂=0.0005, γ₁₂=0.0002. Find σ₁₁, σ₂₂, σ₁₂, ε₃₃, verify energy.

**Problem 3:** Plane strain, E=200 GPa, ν=0.3, σ₁₁=200 MPa, σ₂₂=150 MPa, σ₁₂=50 MPa. Find ε₁₁, ε₂₂, γ₁₂, σ₃₃.

---

## ASSIGNMENT 4.4: Von Mises Yield & 3D Return Mapping (5-8h)

**Deliverable:** `reports/blocks/block04_von_mises_3d.md`

**Reading:** Simo §1.6, §2.3

### Section 1: Von Mises (2-3h)

1. Define f = √(3J₂) - σ_y, derive σ_e = √(1/2[(σ₁-σ₂)² + (σ₂-σ₃)² + (σ₃-σ₁)²])
2. Derive Voigt form: σ_e = √(σ₁₁² + σ₂₂² + σ₃₃² - σ₁₁σ₂₂ - σ₂₂σ₃₃ - σ₃₃σ₁₁ + 3(σ₁₂² + σ₂₃² + σ₁₃²))
3. Plane stress and plane strain forms
4. Sketch yield surface in principal space

### Section 2: Flow Rule (2-3h)

1. Associative: dε^p/dt = λ̇ ∂f/∂σ
2. Derive n_ij = 3/2(s_ij/σ_e)
3. Prove tr(dε^p) = 0

### Section 3: 3D Return Mapping (1-2h)

1. Principal stress approach concept
2. Spectral decomposition
3. Differences from 1D

### Hand Calculations

**Problem 1:** σ_y=250 MPa. Check yielding for: (a) σ=[200,100,50] MPa, (b) σ=[300,0,0] MPa, (c) σ=[150,150,150] MPa.

**Problem 2:** Given σ=[[100,50,0],[50,80,0],[0,0,60]] MPa. Find deviatoric s, σ_e, flow direction n, verify tr(n)=0.

**Problem 3:** Plane stress σ₁₁=200 MPa, σ₂₂=100 MPa, σ₁₂=50 MPa. Find σ_e, check if yielding (σ_y=180 MPa), find flow direction.

---

## FINAL SUMMARY (8-10h)

**Deliverable:** `reports/blocks/block04_continuum_mechanics_summary.md`

### Part 1: Equation Reference (3-4h)

Complete reference sheet with:
1. Tensor operations and identities
2. Stress/strain all forms
3. Invariants
4. Elasticity (3D, plane stress, plane strain, all D matrices)
5. Plasticity (Von Mises all forms, flow rule)

### Part 2: Worked Problems (3-4h)

5 comprehensive problems:
1. Full 3D stress analysis
2. Principal stress + transformation
3. Plane stress elasticity
4. Plane strain elasticity
5. Von Mises + flow direction

### Part 3: Conceptual Essays (2-3h)

1-2 paragraphs each:
1. Why tensors vs matrices
2. Stress vs strain fundamental differences
3. Principal stress space utility
4. Plane stress vs plane strain
5. Von Mises vs Tresca

---

## Submission Checklist

- [ ] `block04_tensor_fundamentals.md`
- [ ] `block04_principal_stresses.md`
- [ ] `block04_voigt_plane_theory.md`
- [ ] `block04_von_mises_3d.md`
- [ ] `block04_continuum_mechanics_summary.md`
- [ ] Hand calculations (scanned PDF)
- [ ] Journal entries

---

## Grading

| Component | Weight |
|-----------|--------|
| 4.1 | 25% |
| 4.2 | 25% |
| 4.3 | 20% |
| 4.4 | 20% |
| Summary | 10% |

---

## Timeline

**6h/week:** 8 weeks  
**10h/week:** 5 weeks  
**Total:** 35-45 hours