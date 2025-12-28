# BLOCK 4: CONTINUUM MECHANICS THEORY

**Goal:** Master tensor formulation and continuum mechanics fundamentals for large displacement analysis, preparing for dimension-agnostic MFEM implementation.

**Primary References:**
- **Website:** https://www.continuummechanics.org (free, accessible)
- **Textbook:** Belytschko et al., "Nonlinear Finite Elements for Continua and Structures", Chapter 3 (when you need deeper theory)

**Philosophy:** 
- Build solid tensor mathematics foundation
- Understand large displacement framework (not just small strain)
- Use Python exercises to cement theory (numpy/scipy, not custom libraries)
- Prepare for dimension-agnostic MFEM implementation

**Total Estimated Time:** 40-50 hours (7-8 weeks at 6h/week)

---

## ASSIGNMENT 4.1: Index Notation and Einstein Summation Convention

**Time Estimate:** 6-8 hours

### Reading

**Primary:**
- https://www.continuummechanics.org/tensornotationbasic.html
- https://www.continuummechanics.org/tensornotationadvanced.html (skim, focus on coordinate transforms)

**Optional (for deeper understanding):**
- Belytschko §3.2.1 Definitions (pages 78-79, ~1 page)

### Theory Work (3-4 hours)

**Deliverable:** `reports/block04/assignment_4_1_index_notation.md`

Write in your own words (no copy-paste). Include:

#### 1. Einstein Summation Convention (1 hour)
- What does "repeated index" mean?
- Automatic summation rule
- Free vs dummy indices
- Valid vs invalid expressions
- 3 examples of valid expressions
- 2 examples of INVALID expressions (explain why)

#### 2. Kronecker Delta δᵢⱼ (45 min)
- Definition: δᵢⱼ = 1 if i=j, 0 otherwise
- Write out full 3×3 matrix
- **Derive:** δᵢⱼaⱼ = aᵢ (show the summation explicitly)
- **Derive:** δᵢᵢ = 3 (show why)
- Physical meaning: identity tensor

#### 3. Permutation Symbol εᵢⱼₖ (45 min)
- Definition for all 27 combinations
- Which combinations = +1? Which = -1? Which = 0?
- Relation to determinants
- Connection to cross products: (a × b)ᵢ = εᵢⱼₖaⱼbₖ

#### 4. Common Tensor Operations in Index Notation (45 min)
Write these operations in both conventional and index notation:

- Dot product: a·b
- Matrix-vector product: A·v
- Matrix-matrix product: A·B
- Trace: tr(A)
- Transpose: Aᵀ
- Tensor contraction: A:B (double dot product)

### Hand Calculations (2-3 hours)

**Deliverable:** Scanned PDF `reports/block04/handwork_4_1.pdf`

**Problem 1:** Given vectors a = [2, -1, 3] and b = [1, 4, -2]
- Calculate aᵢbᵢ (dot product) using index notation
- Show all terms in the summation explicitly

**Problem 2:** Given matrix A and vector x:
```
A = [[2, -1, 0],
     [1,  3, 2],
     [0,  1, 4]]
     
x = [1, 2, -1]
```
- Calculate yᵢ = Aᵢⱼxⱼ by hand
- Show the summation for each component (y₁, y₂, y₃)

**Problem 3:** Verify δᵢⱼδⱼₖ = δᵢₖ
- Expand for i=1, k=1
- Expand for i=1, k=2
- Explain why this identity works

**Problem 4:** Cross product using permutation symbol
- Given a = [1, 0, 0] and b = [0, 1, 0]
- Calculate (a × b)ᵢ = εᵢⱼₖaⱼbₖ for i=1,2,3
- Verify result matches standard cross product

**Problem 5:** Trace in index notation
- Given matrix A from Problem 2
- Calculate tr(A) = Aᵢᵢ
- Show the summation explicitly

### Python Exercise (1-2 hours)

**Deliverable:** `code/block04/ex4_1_index_notation.py`

**Purpose:** Get comfortable with numpy array operations that mirror tensor notation

```python
import numpy as np

# Problem 1: Dot product using Einstein summation
a = np.array([2, -1, 3])
b = np.array([1, 4, -2])

# Using np.einsum (Einstein summation in numpy)
result = np.einsum('i,i->', a, b)
# Verify against np.dot
print(f"Dot product: {result}")
print(f"Verification: {np.dot(a, b)}")

# Problem 2: Matrix-vector product
A = np.array([[2, -1, 0],
              [1,  3, 2],
              [0,  1, 4]])
x = np.array([1, 2, -1])

# Using einsum: y_i = A_ij x_j
y = np.einsum('ij,j->i', A, x)
print(f"Matrix-vector product: {y}")
print(f"Verification: {A @ x}")

# Problem 3: Trace
trace = np.einsum('ii->', A)
print(f"Trace: {trace}")
print(f"Verification: {np.trace(A)}")

# Problem 4: Matrix-matrix product
B = np.array([[1, 0],
              [0, 1],
              [2, -1]])
# C_ik = A_ij B_jk
C = np.einsum('ij,jk->ik', A, B)
print(f"Matrix product:\n{C}")
print(f"Verification:\n{A @ B}")
```

**Your task:** 
1. Run this code and verify all results
2. Add Problem 5: Calculate A:B (Frobenius inner product) for two 3×3 matrices using `einsum('ij,ij->', A, B)`
3. Add comments explaining what each einsum operation does

---

## ASSIGNMENT 4.2: Deformation Gradient and Motion

**Time Estimate:** 7-9 hours

### Reading

**Primary:**
- https://www.continuummechanics.org/deformationgradient.html
- https://www.continuummechanics.org/polardecomposition.html

**Required (for rigorous treatment):**
- Belytschko §3.2.2 Eulerian and Lagrangian Coordinates (pages 79-80, ~1 page)
- Belytschko §3.2.3 Motion (page 80, ~1 page)
- Belytschko §3.2.6 Deformation Gradient (pages 83-84, ~1 page)
- Belytschko §3.7.1 Polar Decomposition Theorem (page 130, ~1 page)

### Theory Work (4-5 hours)

**Deliverable:** `reports/block04/assignment_4_2_deformation_gradient.md`

#### 1. Material vs Spatial Description (1 hour)
- Lagrangian (material) coordinates: X
- Eulerian (spatial) coordinates: x
- Motion: x = φ(X, t)
- Displacement: u = x - X
- Why both descriptions matter

#### 2. Deformation Gradient F (1.5 hours)
- Definition: Fᵢⱼ = ∂xᵢ/∂Xⱼ
- Matrix form
- **Physical meaning:** Maps material line elements to spatial line elements: dx = F·dX
- det(F) = J: volume ratio
- **Derive:** J = dV/dV₀ (volume change)

#### 3. Types of Deformations Through F (1 hour)
Study these cases from continuummechanics.org:

- Rigid translation: F = I (no deformation)
- Pure rotation: F = R (det(F) = 1, orthogonal)
- Pure stretch: F = diagonal matrix
- Combined: rotation + stretch

**Key insight:** F generally contains BOTH rotation and deformation - we need to separate them!

#### 4. Polar Decomposition (1.5 hours)
- F = R·U (material description)
- F = V·R (spatial description)
- R: rotation tensor (orthogonal)
- U: right stretch tensor (symmetric, material frame)
- V: left stretch tensor (symmetric, spatial frame)

**Why this matters:** 
- Rotations don't cause stress
- Only stretches (U or V) matter for constitutive equations
- This is THE key to large displacement analysis

### Hand Calculations (2-3 hours)

**Deliverable:** Add to `reports/block04/handwork_4_2.pdf`

**Problem 1:** Simple deformation
Given mapping: x = 1.2X, y = 0.8Y, z = Z

- Calculate F
- Calculate det(F)
- Interpret: what type of deformation is this?

**Problem 2:** Rotation
Given mapping: x = X cos(30°) - Y sin(30°), y = X sin(30°) + Y cos(30°), z = Z

- Calculate F
- Verify det(F) = 1
- Verify FᵀF = I (orthogonal matrix)
- This is pure rotation - no deformation!

**Problem 3:** Combined deformation and rotation
Given:
```
F = [[1.3, -0.375],
     [0.75,  0.65]]
```
(This is from continuummechanics.org example)

- Calculate det(F)
- Calculate C = FᵀF (right Cauchy-Green tensor)
- This will be used in polar decomposition
- Does this contain rotation? (Check if F = Fᵀ)

**Problem 4:** Volume change
- Initial cube: 1×1×1 mm³
- Deformation: F = diag(1.5, 1.2, 0.8)
- Calculate J = det(F)
- Calculate final volume
- Verify Vf = J·V₀

### Python Exercise (1-2 hours)

**Deliverable:** `code/block04/ex4_2_deformation_gradient.py`

```python
import numpy as np
from scipy.linalg import polar

# Problem 1: Calculate deformation gradient from displacement field
def deformation_gradient_1d_example():
    """
    Simple 1D stretch: x = 1.2*X
    """
    F = np.array([[1.2]])
    J = np.linalg.det(F)
    print(f"1D deformation gradient: {F}")
    print(f"Volume ratio: {J}")
    
# Problem 2: 2D example with rotation and stretch
def deformation_gradient_2d():
    """
    Example from continuummechanics.org
    """
    F = np.array([[1.300, -0.375],
                  [0.750,  0.650]])
    
    J = np.linalg.det(F)
    print(f"Deformation gradient:\n{F}")
    print(f"Determinant (volume ratio): {J:.4f}")
    
    # Polar decomposition: F = R @ U
    R, U = polar(F, side='right')
    
    print(f"\nRotation tensor R:\n{R}")
    print(f"Right stretch tensor U:\n{U}")
    
    # Verify: F = R @ U
    F_reconstructed = R @ U
    print(f"\nReconstructed F:\n{F_reconstructed}")
    print(f"Match: {np.allclose(F, F_reconstructed)}")
    
    # Verify R is orthogonal: R^T @ R = I
    I_check = R.T @ R
    print(f"\nR^T @ R (should be I):\n{I_check}")
    print(f"R is orthogonal: {np.allclose(I_check, np.eye(2))}")
    
    return F, R, U

# Problem 3: Demonstrate pure rotation has det(F) = 1
def pure_rotation_example():
    """
    30 degree rotation about z-axis
    """
    theta = np.radians(30)
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    
    print(f"Rotation matrix (30°):\n{R}")
    print(f"Determinant: {np.linalg.det(R):.6f}")
    print(f"R^T @ R:\n{R.T @ R}")

if __name__ == "__main__":
    deformation_gradient_1d_example()
    print("\n" + "="*50 + "\n")
    deformation_gradient_2d()
    print("\n" + "="*50 + "\n")
    pure_rotation_example()
```

**Your task:**
1. Run this code and understand each output
2. Add a 3D example with F = diag(1.5, 1.2, 0.8)
3. Perform polar decomposition on the 3D case
4. Verify all properties

---

## ASSIGNMENT 4.3: Strain Measures (Small and Finite)

**Time Estimate:** 8-10 hours

### Reading

**Primary:**
- https://www.continuummechanics.org/smallstrain.html
- https://www.continuummechanics.org/greenstrain.html

**Required:**
- Belytschko §3.3.1 Green Strain Tensor (pages 95-97, ~2 pages)
- Belytschko §3.3.3 Rate-of-Deformation in Terms of Rate of Green Strain (pages 98-104, ~6 pages) - SKIM for now, focus on strain definitions

### Theory Work (5-6 hours)

**Deliverable:** `reports/block04/assignment_4_3_strain_measures.md`

#### 1. Small Strain Tensor ε (1.5 hours)
- Definition: εᵢⱼ = (1/2)(∂uᵢ/∂xⱼ + ∂uⱼ/∂xᵢ)
- Or: εᵢⱼ = (1/2)(uᵢ,ⱼ + uⱼ,ᵢ) in index notation
- Symmetry: εᵢⱼ = εⱼᵢ
- Physical meaning of diagonal terms: normal strains
- Physical meaning of off-diagonal terms: shear strains
- Engineering shear strain: γᵢⱼ = 2εᵢⱼ (for i≠j)

**CRITICAL:** Small strain assumes:
- ||∇u|| << 1 (displacement gradients small)
- **Actually limitation is small ROTATION**, not small strain!

#### 2. Green Strain Tensor E (2 hours)
- Motivation: Small strain fails for large rotations
- Definition: Eᵢⱼ = (1/2)(Fᵢₖ Fⱼₖ - δᵢⱼ)
- Or: E = (1/2)(FᵀF - I) = (1/2)(C - I), where C = FᵀF
- Expanded form:
  ```
  E_xx = ∂u/∂X + (1/2)[(∂u/∂X)² + (∂v/∂X)² + (∂w/∂X)²]
  E_xy = (1/2)(∂u/∂Y + ∂v/∂X) + (1/2)[∂u/∂X ∂u/∂Y + ∂v/∂X ∂v/∂Y + ∂w/∂X ∂w/∂Y]
  ```

**Why Green strain:**
- Frame-invariant (independent of rigid rotations!)
- Works for large rotations AND large strains
- Quadratic terms capture geometric nonlinearity

#### 3. Relationship Between ε and E (1 hour)
- When ||∇u|| << 1, neglect quadratic terms
- Then: E ≈ ε (Green strain reduces to small strain)
- **Work through the algebra** to show this

#### 4. Physical Interpretation (1.5 hours)

Study the continuummechanics.org examples:

**Pure rotation (25°):**
- Small strain ε shows spurious shear (WRONG!)
- Green strain E = 0 (CORRECT - no deformation)

**Pure shear:**
- Small strain: diagonal terms = 0
- Green strain: diagonal terms ≠ 0 (stretching due to shear!)

**Write in your notes:**
- When to use small strain
- When you MUST use Green strain
- Why quadratic terms matter

### Hand Calculations (2-3 hours)

**Deliverable:** Add to `reports/block04/handwork_4_3.pdf`

**Problem 1:** Small strain for simple displacement
Given: u = 0.01x, v = 0.02y, w = 0

- Calculate all εᵢⱼ components by hand
- Which are normal strains? Which are shears?

**Problem 2:** Green strain for pure rotation
Given: F for 30° rotation from Assignment 4.2

- Calculate C = FᵀF
- Calculate E = (1/2)(C - I)
- Verify E = 0 (pure rotation has no strain!)

**Problem 3:** Green strain for stretch + rotation
Given F from Assignment 4.2 Problem 3:
```
F = [[1.3, -0.375],
     [0.75,  0.65]]
```

- Calculate C = FᵀF
- Calculate E = (1/2)(C - I)
- Compare to U from polar decomposition (should be related!)

**Problem 4:** Verify small strain approximation
Given displacement: u = 0.001x, v = -0.0005y, w = 0

- Calculate small strain ε
- Calculate F (F = I + ∇u)
- Calculate Green strain E
- Show E ≈ ε (quadratic terms negligible)

### Python Exercise (1-2 hours)

**Deliverable:** `code/block04/ex4_3_strain_measures.py`

```python
import numpy as np

def small_strain(u_grad):
    """
    Calculate small strain tensor from displacement gradient
    ε_ij = 0.5 * (∂u_i/∂x_j + ∂u_j/∂x_i)
    
    Parameters:
    u_grad: 3x3 array, displacement gradient tensor
    
    Returns:
    epsilon: 3x3 small strain tensor
    """
    return 0.5 * (u_grad + u_grad.T)

def green_strain(F):
    """
    Calculate Green strain tensor
    E = 0.5 * (F^T F - I)
    
    Parameters:
    F: deformation gradient
    
    Returns:
    E: Green strain tensor
    """
    C = F.T @ F  # Right Cauchy-Green tensor
    I = np.eye(len(F))
    E = 0.5 * (C - I)
    return E

# Test case 1: Pure rotation (should give E = 0)
theta = np.radians(30)
F_rotation = np.array([[np.cos(theta), -np.sin(theta), 0],
                       [np.sin(theta),  np.cos(theta), 0],
                       [0,              0,             1]])

E_rotation = green_strain(F_rotation)
print("Pure rotation:")
print(f"F:\n{F_rotation}")
print(f"Green strain E (should be ~0):\n{E_rotation}")
print(f"Max error: {np.max(np.abs(E_rotation)):.2e}\n")

# Test case 2: Pure stretch (no rotation)
F_stretch = np.diag([1.1, 0.95, 1.05])
E_stretch = green_strain(F_stretch)
print("Pure stretch:")
print(f"F:\n{F_stretch}")
print(f"Green strain E:\n{E_stretch}")

# Compare to small strain approximation
u_grad = F_stretch - np.eye(3)  # ∇u = F - I for small deformations
epsilon = small_strain(u_grad)
print(f"Small strain ε:\n{epsilon}")
print(f"Difference (E - ε):\n{E_stretch - epsilon}")
print(f"Relative error: {np.max(np.abs((E_stretch - epsilon)/E_stretch)):.2%}\n")

# Test case 3: Combined rotation and stretch
F_combined = np.array([[1.3, -0.375, 0],
                       [0.75,  0.65, 0],
                       [0,     0,    1]])
E_combined = green_strain(F_combined)
print("Combined rotation + stretch:")
print(f"F:\n{F_combined}")
print(f"Green strain E:\n{E_combined}\n")

# Compare small vs Green strain for this case
u_grad_combined = F_combined - np.eye(3)
epsilon_combined = small_strain(u_grad_combined)
print(f"Small strain ε (WRONG for large rotation):\n{epsilon_combined}")
print(f"Difference shows effect of rotation:\n{E_combined - epsilon_combined}")
```

**Your task:**
1. Run and understand all test cases
2. Add a case with small displacement (max 0.1%) and verify E ≈ ε
3. Add a case with large rotation (60°) and show small strain is wrong
4. Plot: for rotation angle 0-90°, show max error in small strain vs Green strain

---

## ASSIGNMENT 4.4: Stress Tensor Fundamentals

**Time Estimate:** 7-9 hours

### Reading

**Primary:**
- https://www.continuummechanics.org/stress.html
- https://www.continuummechanics.org/tractionvector.html
- https://www.continuummechanics.org/stressintroduction.html

**Required:**
- Belytschko §3.4.1 Definitions of Stresses (pages 104-105, ~1 page)
- Belytschko §3.4.2 Transformation between Stresses (pages 105-107, ~2 pages)

### Theory Work (4-5 hours)

**Deliverable:** `reports/block04/assignment_4_4_stress_tensor.md`

#### 1. Cauchy Stress Tensor σ (1.5 hours)
- Physical meaning: force per current area
- Traction vector: t = σ·n (Cauchy stress formula)
- In index notation: tᵢ = σᵢⱼnⱼ
- Symmetry: σᵢⱼ = σⱼᵢ (from moment balance)
- 9 components → 6 independent

**Components:**
- Normal stresses: σ_xx, σ_yy, σ_zz
- Shear stresses: σ_xy, σ_yz, σ_xz
- Sign convention: tension positive

#### 2. Why Multiple Stress Measures? (1.5 hours)

This is CRITICAL for large displacement analysis!

**Cauchy stress σ:**
- Force per CURRENT area
- Easy to measure
- Used in equilibrium equations

**First Piola-Kirchhoff stress P:**
- Force per INITIAL area  
- Connects Eulerian (spatial) and Lagrangian (material)
- NOT symmetric!

**Second Piola-Kirchhoff stress S:**
- Force per initial area, "pulled back" to material frame
- Symmetric
- Work conjugate to Green strain E
- Used in constitutive equations

**Relationship:**
- P = J σ F⁻ᵀ
- S = J F⁻¹ σ F⁻ᵀ
- Or: σ = (1/J) F S Fᵀ

**For small deformations:** σ ≈ P ≈ S (all equivalent)

#### 3. Traction Vector and Stress (1 hour)

- Traction t: force per area on a surface
- Depends on surface orientation (normal n)
- Stress tensor σ: relates traction to normal
- **Derive** Cauchy formula from force balance

#### 4. When to Use Which Stress (1 hour)

**Cauchy σ:**
- Spatial description
- Equilibrium equations
- Physical interpretation

**2nd PK S:**
- Material description  
- Constitutive laws (σ vs E)
- Finite element formulation

**Your research (viscoplasticity, ROM):**
- Will primarily use S and E (material frame)
- Transform to σ when needed for output

### Hand Calculations (2-3 hours)

**Deliverable:** Add to `reports/block04/handwork_4_4.pdf`

**Problem 1:** Traction vector
Given stress state:
```
σ = [[100, 30, 0  ],
     [30,  80, 10 ],
     [0,   10, 60 ]] MPa
```
Plane with normal n = [1/√2, 1/√2, 0]

- Calculate traction t = σ·n
- Calculate normal stress: σ_n = t·n
- Calculate shear stress: τ = ||t - σ_n n||

**Problem 2:** Stress symmetry
- Draw 2D stress element with σ_xx, σ_yy, σ_xy
- Apply moment balance about center
- Derive σ_xy = σ_yx

**Problem 3:** Uniaxial tension
- σ_xx = 100 MPa, all other components = 0
- Calculate traction on plane with n = [1, 0, 0]
- Calculate traction on plane with n = [cos(45°), sin(45°), 0]

**Problem 4:** Stress transformation
Given F = diag(1.1, 1.0, 0.95) and σ = diag(100, 80, 60) MPa

- Calculate J = det(F)
- Calculate S = J F⁻¹ σ F⁻ᵀ (2nd Piola-Kirchhoff)
- Verify σ = (1/J) F S Fᵀ

### Python Exercise (1-2 hours)

**Deliverable:** `code/block04/ex4_4_stress_tensor.py`

```python
import numpy as np

def traction_vector(sigma, normal):
    """
    Calculate traction vector on a surface
    t = σ · n
    """
    return sigma @ normal

def normal_shear_stress(sigma, normal):
    """
    Decompose traction into normal and shear components
    """
    t = traction_vector(sigma, normal)
    sigma_n = np.dot(t, normal)  # Normal stress
    tau = np.linalg.norm(t - sigma_n * normal)  # Shear stress
    return sigma_n, tau, t

def cauchy_to_pk2(sigma, F):
    """
    Transform Cauchy stress to 2nd Piola-Kirchhoff stress
    S = J F^{-1} σ F^{-T}
    """
    J = np.linalg.det(F)
    F_inv = np.linalg.inv(F)
    S = J * F_inv @ sigma @ F_inv.T
    return S

def pk2_to_cauchy(S, F):
    """
    Transform 2nd Piola-Kirchhoff to Cauchy stress
    σ = (1/J) F S F^T
    """
    J = np.linalg.det(F)
    sigma = (1/J) * F @ S @ F.T
    return sigma

# Test case 1: Traction vector
sigma = np.array([[100, 30, 0],
                  [30,  80, 10],
                  [0,   10, 60]])

normal = np.array([1/np.sqrt(2), 1/np.sqrt(2), 0])
sigma_n, tau, t = normal_shear_stress(sigma, normal)

print("Traction vector problem:")
print(f"Stress tensor σ:\n{sigma}")
print(f"Normal vector n: {normal}")
print(f"Traction vector t: {t}")
print(f"Normal stress: {sigma_n:.2f} MPa")
print(f"Shear stress: {tau:.2f} MPa\n")

# Test case 2: Stress transformation (pure stretch)
F = np.diag([1.1, 1.0, 0.95])
sigma_initial = np.diag([100, 80, 60])

S = cauchy_to_pk2(sigma_initial, F)
sigma_reconstructed = pk2_to_cauchy(S, F)

print("Stress transformation:")
print(f"F:\n{F}")
print(f"Cauchy stress σ:\n{sigma_initial}")
print(f"2nd PK stress S:\n{S}")
print(f"Reconstructed σ:\n{sigma_reconstructed}")
print(f"Match: {np.allclose(sigma_initial, sigma_reconstructed)}\n")

# Test case 3: For small deformation, σ ≈ S
F_small = np.eye(3) + 0.01 * np.random.rand(3, 3)
F_small = 0.5 * (F_small + F_small.T)  # Symmetrize
sigma_test = np.diag([100, 80, 60])

S_test = cauchy_to_pk2(sigma_test, F_small)
print("Small deformation (σ ≈ S):")
print(f"σ:\n{sigma_test}")
print(f"S:\n{S_test}")
print(f"Difference:\n{S_test - sigma_test}")
print(f"Relative error: {np.max(np.abs((S_test - sigma_test)/sigma_test)):.2%}")
```

**Your task:**
1. Run all test cases
2. Add case with large deformation (F = diag(1.5, 0.8, 1.2)) and show σ ≠ S
3. Verify symmetry of S for all cases
4. Add visualization: plot how S/σ ratio changes with stretch

---

## ASSIGNMENT 4.5: Principal Stresses and Invariants

**Time Estimate:** 6-8 hours

### Reading

**Primary:**
- https://www.continuummechanics.org/principalstress.html
- https://www.continuummechanics.org/hydrodeviatoricstress.html

**Optional:**
- Belytschko §3.7 Polar Decomposition and Frame-Invariance (pages 123-142) - SKIM, focus on invariance concepts

### Theory Work (3-4 hours)

**Deliverable:** `reports/block04/assignment_4_5_principal_stresses.md`

#### 1. Eigenvalue Problem (1 hour)
- Principal stresses: eigenvalues of σ
- Principal directions: eigenvectors of σ  
- Characteristic equation: det(σ - λI) = 0
- Expanded: λ³ - I₁λ² + I₂λ - I₃ = 0

**Physical meaning:**
- On principal planes: pure normal stress, zero shear
- Maximum normal stresses occur on principal planes

#### 2. Stress Invariants (1.5 hours)

**First invariant I₁:**
- I₁ = σ₁ + σ₂ + σ₃ = tr(σ) = σᵢᵢ
- Related to volume change

**Second invariant I₂:**
- I₂ = σ₁σ₂ + σ₂σ₃ + σ₃σ₁
- I₂ = (1/2)[(tr σ)² - tr(σ²)]

**Third invariant I₃:**
- I₃ = σ₁σ₂σ₃ = det(σ)

**Why "invariant"?**
- Same value in ANY coordinate system
- Fundamental property of the stress state
- Used in yield criteria

#### 3. Hydrostatic and Deviatoric Decomposition (1.5 hours)

**Hydrostatic (volumetric) stress:**
- p = (1/3)I₁ = (1/3)tr(σ)
- Scalar quantity
- Tensor form: p𝐈 = (1/3)I₁ 𝐈

**Deviatoric stress:**
- s = σ - p𝐈
- sᵢⱼ = σᵢⱼ - (1/3)δᵢⱼσₖₖ
- Trace-free: tr(s) = 0

**J₂ invariant (second invariant of deviatoric stress):**
- J₂ = (1/2)sᵢⱼsᵢⱼ = (1/2)s:s
- Alternative form: J₂ = (1/6)[(σ₁-σ₂)² + (σ₂-σ₃)² + (σ₃-σ₁)²]

**Why this decomposition matters:**
- Hydrostatic: volume change (no yielding in metals!)
- Deviatoric: shape change (causes plastic yielding)
- **J₂ is basis for von Mises yield criterion**

### Hand Calculations (2-3 hours)

**Deliverable:** Add to `reports/block04/handwork_4_5.pdf`

**Problem 1:** Principal stresses (2D)
Given:
```
σ = [[100, 50 ],
     [50,  80 ]]
```

- Write characteristic equation det(σ - λI) = 0
- Solve for λ (principal stresses)
- Find principal directions (eigenvectors)
- Verify: σ₁ + σ₂ = I₁ = tr(σ)

**Problem 2:** Invariants (3D)
Given:
```
σ = [[100, 30, 0  ],
     [30,  80, 10 ],
     [0,   10, 60 ]]
```

- Calculate I₁ = tr(σ)
- Calculate I₂ = (1/2)[(tr σ)² - tr(σ²)]
- Calculate I₃ = det(σ)
- Find principal stresses numerically
- Verify: σ₁ + σ₂ + σ₃ = I₁

**Problem 3:** Hydrostatic-deviatoric decomposition
Using σ from Problem 2:

- Calculate p = (1/3)tr(σ)
- Calculate deviatoric stress s = σ - p𝐈
- Verify tr(s) = 0
- Calculate J₂ = (1/2)s:s = (1/2)sᵢⱼsᵢⱼ

**Problem 4:** Pure shear
Given:
```
σ = [[0,  50, 0],
     [50, 0,  0],
     [0,  0,  0]]
```

- Calculate principal stresses
- Calculate p (should it be zero?)
- Calculate deviatoric stress s
- Calculate J₂

### Python Exercise (1-2 hours)

**Deliverable:** `code/block04/ex4_5_principal_stresses.py`

```python
import numpy as np
from scipy.linalg import eigh

def principal_stresses(sigma):
    """
    Calculate principal stresses and directions
    Returns eigenvalues (principal stresses) and eigenvectors (principal directions)
    """
    # eigh for symmetric matrices (more stable than eig)
    eigenvalues, eigenvectors = eigh(sigma)
    # Sort in descending order
    idx = eigenvalues.argsort()[::-1]
    return eigenvalues[idx], eigenvectors[:, idx]

def stress_invariants(sigma):
    """
    Calculate I1, I2, I3
    """
    I1 = np.trace(sigma)
    I2 = 0.5 * (I1**2 - np.trace(sigma @ sigma))
    I3 = np.linalg.det(sigma)
    return I1, I2, I3

def deviatoric_stress(sigma):
    """
    Calculate deviatoric stress tensor
    s = σ - (1/3)tr(σ)I
    """
    p = np.trace(sigma) / 3
    s = sigma - p * np.eye(len(sigma))
    return s, p

def J2_invariant(s):
    """
    Calculate J2 = (1/2) s:s
    """
    return 0.5 * np.einsum('ij,ij->', s, s)

# Test case 1: 3D stress state
sigma = np.array([[100, 30, 0],
                  [30,  80, 10],
                  [0,   10, 60]])

print("3D stress tensor:")
print(sigma)

# Principal stresses
principals, directions = principal_stresses(sigma)
print(f"\nPrincipal stresses: {principals}")
print(f"Principal directions:\n{directions}")

# Invariants
I1, I2, I3 = stress_invariants(sigma)
print(f"\nInvariants:")
print(f"I1 = {I1:.2f}")
print(f"I2 = {I2:.2f}")
print(f"I3 = {I3:.2f}")

# Verify using principal stresses
I1_check = np.sum(principals)
I2_check = principals[0]*principals[1] + principals[1]*principals[2] + principals[2]*principals[0]
I3_check = np.prod(principals)
print(f"\nVerification using principal stresses:")
print(f"I1 = {I1_check:.2f} (error: {abs(I1-I1_check):.2e})")
print(f"I2 = {I2_check:.2f} (error: {abs(I2-I2_check):.2e})")
print(f"I3 = {I3_check:.2f} (error: {abs(I3-I3_check):.2e})")

# Deviatoric decomposition
s, p = deviatoric_stress(sigma)
J2 = J2_invariant(s)

print(f"\nHydrostatic-deviatoric decomposition:")
print(f"Pressure p = {p:.2f} MPa")
print(f"Deviatoric stress s:\n{s}")
print(f"Trace of s (should be 0): {np.trace(s):.2e}")
print(f"J2 = {J2:.2f} MPa²")

# Alternative J2 calculation using principal stresses
s_principals, _ = principal_stresses(s)
J2_alt = (1/6) * ((s_principals[0]-s_principals[1])**2 + 
                   (s_principals[1]-s_principals[2])**2 + 
                   (s_principals[2]-s_principals[0])**2)
print(f"J2 (alternative): {J2_alt:.2f} MPa² (error: {abs(J2-J2_alt):.2e})")

# Test case 2: Pure shear
sigma_shear = np.array([[0,  50, 0],
                        [50, 0,  0],
                        [0,  0,  0]])

print("\n" + "="*50)
print("Pure shear stress:")
print(sigma_shear)

principals_shear, _ = principal_stresses(sigma_shear)
print(f"Principal stresses: {principals_shear}")

s_shear, p_shear = deviatoric_stress(sigma_shear)
print(f"Pressure (should be ~0): {p_shear:.2e}")
print(f"Deviatoric stress:\n{s_shear}")
```

**Your task:**
1. Run all test cases
2. Add uniaxial tension case: σ = diag(100, 0, 0)
3. Verify invariant invariance: rotate stress tensor 45°, recalculate I₁, I₂, I₃
4. Create function to verify σ = (σ₁, σ₂, σ₃) in principal frame

---

## ASSIGNMENT 4.6: Von Mises Stress and Yield Criterion

**Time Estimate:** 5-7 hours

### Reading

**Primary:**
- https://www.continuummechanics.org/vonmisesstress.html

**Background (you've already implemented this in 1D!):**
- Your Block 2-3 work on plasticity

### Theory Work (3-4 hours)

**Deliverable:** `reports/block04/assignment_4_6_von_mises.md`

#### 1. Von Mises Stress Definition (1 hour)
- σᵥₘ = √(3J₂)
- Alternative: σᵥₘ = √(3/2 s:s) = √(3/2 sᵢⱼsᵢⱼ)
- Principal stress form: 
  ```
  σᵥₘ = √[(1/2)((σ₁-σ₂)² + (σ₂-σ₃)² + (σ₃-σ₁)²)]
  ```
- Component form:
  ```
  σᵥₘ = √[(σₓₓ-σᵧᵧ)² + (σᵧᵧ-σᵤᵤ)² + (σᵤᵤ-σₓₓ)² + 6(σₓᵧ² + σᵧᵤ² + σᵤₓ²)]
  ```

**All these formulas are EQUIVALENT!**

#### 2. Why Von Mises? (1 hour)

**Physical meaning:**
- Effective stress for plastic yielding
- Measures "intensity" of deviatoric stress
- Independent of hydrostatic pressure

**Yield criterion:**
- f = σᵥₘ - σᵧ ≤ 0
- Same as your 1D: f = |σ| - σᵧ ≤ 0
- But now works in 3D!

**Why J₂ not I₁?**
- Hydrostatic stress doesn't cause yielding in metals
- Only deviatoric (shape change) causes yielding
- J₂ measures deviatoric intensity

#### 3. Connection to Your 1D Work (1 hour)

**1D plasticity (Block 2-3):**
- Yield: f = |σ| - σᵧ
- Return mapping: radial return to yield surface

**3D plasticity (coming in Block 7):**
- Yield: f = σᵥₘ - σᵧ = √(3J₂) - σᵧ
- Return mapping: radial return in deviatoric space
- **Algorithm is same conceptual structure!**

**Write comparison table:**
| Aspect | 1D | 3D |
|--------|----|----|
| Stress | σ | σᵢⱼ tensor |
| Yield function | \|σ\| - σᵧ | √(3J₂) - σᵧ |
| Return direction | sign(σ) | normal to yield surface |
| Algorithm | Same structure! | |

#### 4. Special Cases (1 hour)

Calculate σᵥₘ for these by hand:

**Uniaxial tension:**
- σ₁ = σ, σ₂ = σ₃ = 0
- σᵥₘ = σ (matches 1D!)

**Pure shear:**
- σ₁ = τ, σ₂ = -τ, σ₃ = 0
- σᵥₘ = √3 τ

**Hydrostatic pressure:**
- σ₁ = σ₂ = σ₃ = -p
- σᵥₘ = 0 (no deviatoric stress!)

### Hand Calculations (1-2 hours)

**Deliverable:** Add to `reports/block04/handwork_4_6.pdf`

**Problem 1:** Von Mises for general stress
Given:
```
σ = [[100, 30, 0],
     [30,  80, 10],
     [0,   10, 60]]
```

- Calculate deviatoric stress s
- Calculate J₂
- Calculate σᵥₘ = √(3J₂)
- Alternative: use component formula
- Verify both methods match

**Problem 2:** Special cases (verify formulas)
- Uniaxial: σ = diag(100, 0, 0) → σᵥₘ = 100
- Pure shear: σ = [[0, 50], [50, 0]] → σᵥₘ = √3 × 50
- Biaxial: σ = diag(100, 50, 0) → calculate σᵥₘ

**Problem 3:** Yield check
Given σ from Problem 1 and σᵧ = 200 MPa:
- Calculate f = σᵥₘ - σᵧ
- Is material yielding? (f > 0?)

### Python Exercise (1-2 hours)

**Deliverable:** `code/block04/ex4_6_von_mises.py`

```python
import numpy as np
import matplotlib.pyplot as plt

def von_mises_stress(sigma):
    """
    Calculate von Mises stress
    σ_vm = sqrt(3 * J2) = sqrt(3/2 * s:s)
    """
    # Method 1: Using deviatoric stress
    p = np.trace(sigma) / 3
    s = sigma - p * np.eye(len(sigma))
    J2 = 0.5 * np.einsum('ij,ij->', s, s)
    sigma_vm_1 = np.sqrt(3 * J2)
    
    # Method 2: Using principal stresses (for verification)
    eigenvalues = np.linalg.eigvalsh(sigma)
    s1, s2, s3 = eigenvalues
    sigma_vm_2 = np.sqrt(0.5 * ((s1-s2)**2 + (s2-s3)**2 + (s3-s1)**2))
    
    # Verify methods match
    assert np.isclose(sigma_vm_1, sigma_vm_2), "Methods don't match!"
    
    return sigma_vm_1

def yield_function(sigma, sigma_y):
    """
    von Mises yield function
    f = σ_vm - σ_y
    """
    sigma_vm = von_mises_stress(sigma)
    return sigma_vm - sigma_y

# Test cases from theory
test_cases = {
    "Uniaxial tension": np.diag([100, 0, 0]),
    "Pure shear": np.array([[0, 50, 0], [50, 0, 0], [0, 0, 0]]),
    "Hydrostatic": -50 * np.eye(3),
    "General": np.array([[100, 30, 0], [30, 80, 10], [0, 10, 60]])
}

print("Von Mises stress for different loading cases:\n")
for name, sigma in test_cases.items():
    sigma_vm = von_mises_stress(sigma)
    print(f"{name}:")
    print(f"  Stress tensor:\n{sigma}")
    print(f"  σ_vm = {sigma_vm:.2f} MPa\n")

# Verify special cases
print("Verification of special cases:")
sigma_uniaxial = np.diag([100, 0, 0])
print(f"Uniaxial (100 MPa): σ_vm = {von_mises_stress(sigma_uniaxial):.2f} (should be 100)")

sigma_shear = np.array([[0, 50, 0], [50, 0, 0], [0, 0, 0]])
print(f"Pure shear (50 MPa): σ_vm = {von_mises_stress(sigma_shear):.2f} (should be {np.sqrt(3)*50:.2f})")

sigma_hydro = -50 * np.eye(3)
print(f"Hydrostatic (-50 MPa): σ_vm = {von_mises_stress(sigma_hydro):.6f} (should be ~0)\n")

# Yield surface visualization (2D for simplicity)
def plot_yield_surface_2d(sigma_y):
    """
    Plot von Mises yield surface in 2D principal stress space
    """
    # Create grid
    s1 = np.linspace(-1.5*sigma_y, 1.5*sigma_y, 200)
    s2 = np.linspace(-1.5*sigma_y, 1.5*sigma_y, 200)
    S1, S2 = np.meshgrid(s1, s2)
    
    # Plane stress: s3 = 0
    # Von Mises: s1² - s1*s2 + s2² = sigma_y²
    F = S1**2 - S1*S2 + S2**2 - sigma_y**2
    
    plt.figure(figsize=(8, 8))
    plt.contour(S1, S2, F, levels=[0], colors='red', linewidths=2)
    plt.xlabel('σ₁ (MPa)', fontsize=12)
    plt.ylabel('σ₂ (MPa)', fontsize=12)
    plt.title(f'Von Mises Yield Surface (σ_y = {sigma_y} MPa)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    
    # Mark special points
    plt.plot([sigma_y, 0], [0, sigma_y], 'bo', markersize=8, label='Yield points')
    plt.plot([-sigma_y, 0], [0, -sigma_y], 'bo', markersize=8)
    
    plt.legend()
    plt.tight_layout()
    plt.savefig('/home/claude/von_mises_yield_surface.png', dpi=150)
    print("Yield surface plot saved!")

plot_yield_surface_2d(200)
```

**Your task:**
1. Run all test cases and verify
2. Extend yield surface plot to show elastic vs plastic regions
3. Add 3D stress states and check if yielding occurs
4. Create function that connects to your 1D return mapping

---

## ASSIGNMENT 4.7: Voigt Notation and Elasticity

**Time Estimate:** 4-6 hours

### Reading

**Primary:**
- https://www.continuummechanics.org/hookeslaw2.html (3D Hooke's law)

**Required:**
- Belytschko Appendix (check for Voigt notation) OR find section in Crisfield

### Theory Work (2-3 hours)

**Deliverable:** `reports/block04/assignment_4_7_voigt_notation.md`

#### 1. Voigt Notation Mapping (1 hour)

**Stress vector (6×1):**
```
{σ} = [σ_xx, σ_yy, σ_zz, σ_xy, σ_yz, σ_xz]ᵀ
```

**Strain vector (6×1):**
```
{ε} = [ε_xx, ε_yy, ε_zz, 2ε_xy, 2ε_yz, 2ε_xz]ᵀ
```

**CRITICAL:** Factor of 2 on shear strains!

**Why factor of 2?**
- Energy equivalence: σ:ε = {σ}ᵀ{ε}
- Tensor notation: σᵢⱼεᵢⱼ (includes off-diagonals twice)
- Voigt notation: must compensate with factor of 2

**Index mapping:**
```
Tensor (i,j) → Voigt index
(1,1) → 1
(2,2) → 2  
(3,3) → 3
(1,2) or (2,1) → 4
(2,3) or (3,2) → 5
(1,3) or (3,1) → 6
```

#### 2. Elasticity Tensor in Voigt Notation (1.5 hours)

**General anisotropic (21 independent):**
```
{σ} = [C]{ε}
```
C is 6×6 symmetric matrix

**Isotropic elasticity (2 parameters: E, ν):**
```
      [λ+2μ   λ     λ     0   0   0 ]
      [ λ   λ+2μ   λ     0   0   0 ]
[C] = [ λ     λ   λ+2μ   0   0   0 ]
      [ 0     0     0     μ   0   0 ]
      [ 0     0     0     0   μ   0 ]
      [ 0     0     0     0   0   μ ]
```

Where:
- λ = Eν/[(1+ν)(1-2ν)] (Lamé's first parameter)
- μ = E/[2(1+ν)] = G (shear modulus)

#### 3. Plane Stress vs Plane Strain (30 min)

**Plane stress (σ_zz = 0):**
- Thin plates
- 3×3 reduced matrix

**Plane strain (ε_zz = 0):**
- Long bodies (dam, tunnel)
- 3×3 reduced matrix (different from plane stress!)

**Write both 3×3 matrices**

### Hand Calculations (1-2 hours)

**Deliverable:** Add to `reports/block04/handwork_4_7.pdf`

**Problem 1:** Energy equivalence verification
Given:
```
σ = [[100, 30, 0],
     [30,  80, 10],
     [0,   10, 60]]
     
ε = [[0.001, 0.0002, 0     ],
     [0.0002, 0.0008, 0.0001],
     [0,      0.0001, 0.0005]]
```

- Calculate σ:ε using tensor notation (6 terms)
- Convert to Voigt: {σ}ᵀ{ε}
- Verify they're equal
- Show why factor of 2 is needed

**Problem 2:** Isotropic elasticity matrix
Given E = 200 GPa, ν = 0.3:
- Calculate λ
- Calculate μ
- Write full 6×6 [C] matrix
- Calculate {σ} for {ε} = [0.001, 0.0008, 0.0005, 0.0004, 0, 0]ᵀ

**Problem 3:** Plane stress
- Derive 3×3 plane stress [C] from 6×6
- Apply σ_zz = 0 constraint
- Eliminate ε_zz

### Python Exercise (1-2 hours)

**Deliverable:** `code/block04/ex4_7_voigt_notation.py`

```python
import numpy as np

def tensor_to_voigt_stress(sigma):
    """
    Convert 3x3 stress tensor to 6x1 Voigt vector
    """
    return np.array([sigma[0,0], sigma[1,1], sigma[2,2],
                     sigma[0,1], sigma[1,2], sigma[0,2]])

def tensor_to_voigt_strain(epsilon):
    """
    Convert 3x3 strain tensor to 6x1 Voigt vector
    Note: Factor of 2 on shear components!
    """
    return np.array([epsilon[0,0], epsilon[1,1], epsilon[2,2],
                     2*epsilon[0,1], 2*epsilon[1,2], 2*epsilon[0,2]])

def voigt_to_tensor_stress(sigma_voigt):
    """
    Convert 6x1 Voigt vector to 3x3 stress tensor
    """
    return np.array([[sigma_voigt[0], sigma_voigt[3], sigma_voigt[5]],
                     [sigma_voigt[3], sigma_voigt[1], sigma_voigt[4]],
                     [sigma_voigt[5], sigma_voigt[4], sigma_voigt[2]]])

def voigt_to_tensor_strain(epsilon_voigt):
    """
    Convert 6x1 Voigt vector to 3x3 strain tensor
    Note: Divide shear components by 2!
    """
    return np.array([[epsilon_voigt[0], epsilon_voigt[3]/2, epsilon_voigt[5]/2],
                     [epsilon_voigt[3]/2, epsilon_voigt[1], epsilon_voigt[4]/2],
                     [epsilon_voigt[5]/2, epsilon_voigt[4]/2, epsilon_voigt[2]]])

def isotropic_elasticity_matrix(E, nu):
    """
    Generate 6x6 isotropic elasticity tensor in Voigt notation
    """
    lam = E * nu / ((1 + nu) * (1 - 2*nu))
    mu = E / (2 * (1 + nu))
    
    C = np.zeros((6, 6))
    
    # Diagonal blocks
    C[0:3, 0:3] = lam
    C[0:3, 0:3] += np.diag([2*mu, 2*mu, 2*mu])
    
    # Shear terms
    C[3:6, 3:6] = np.diag([mu, mu, mu])
    
    return C

# Test energy equivalence
sigma = np.array([[100, 30, 0],
                  [30,  80, 10],
                  [0,   10, 60]])

epsilon = np.array([[0.001, 0.0002, 0],
                    [0.0002, 0.0008, 0.0001],
                    [0, 0.0001, 0.0005]])

# Tensor notation: σ:ε
energy_tensor = np.einsum('ij,ij->', sigma, epsilon)

# Voigt notation: {σ}^T {ε}
sigma_voigt = tensor_to_voigt_stress(sigma)
epsilon_voigt = tensor_to_voigt_strain(epsilon)
energy_voigt = np.dot(sigma_voigt, epsilon_voigt)

print("Energy equivalence test:")
print(f"Tensor notation (σ:ε): {energy_tensor:.6f}")
print(f"Voigt notation {{σ}}^T{{ε}}: {energy_voigt:.6f}")
print(f"Match: {np.isclose(energy_tensor, energy_voigt)}\n")

# Test elasticity matrix
E = 200e3  # MPa
nu = 0.3
C = isotropic_elasticity_matrix(E, nu)

print("Isotropic elasticity matrix:")
print(f"E = {E} MPa, ν = {nu}")
print(f"C:\n{C}\n")

# Apply to strain
epsilon_voigt_test = np.array([0.001, 0.0008, 0.0005, 0.0004, 0, 0])
sigma_voigt_test = C @ epsilon_voigt_test

print("Stress-strain calculation:")
print(f"Strain vector: {epsilon_voigt_test}")
print(f"Stress vector: {sigma_voigt_test}")

# Convert back to tensor
sigma_result = voigt_to_tensor_stress(sigma_voigt_test)
print(f"Stress tensor:\n{sigma_result}")
```

**Your task:**
1. Run and verify all conversions
2. Add plane stress elasticity matrix
3. Add plane strain elasticity matrix
4. Verify conversion round-trip: tensor → Voigt → tensor

---

## ASSIGNMENT 4.8: Synthesis and 3D Return Mapping Design

**Time Estimate:** 6-8 hours

### Reading

**Primary:**
- Review ALL previous assignments in Block 4
- Review your Block 2-3 return mapping implementations

**Optional:**
- Belytschko §3.7 (frame invariance concepts)

### Theory Work (4-5 hours)

**Deliverable:** `reports/block04/assignment_4_8_synthesis.md`

#### 1. Conceptual Algorithm for 3D Return Mapping (2 hours)

**Based on your 1D experience, design the 3D algorithm:**

**Input:** 
- σ_trial (trial stress tensor from elastic predictor)
- E_trial (Green strain)
- σ_y (yield stress)
- Material parameters (E, ν, hardening)

**Algorithm outline:**

1. **Spectral decomposition**
   - Calculate principal stresses of σ_trial
   - Get principal directions (eigenvectors)

2. **Check yield in principal space**
   - Calculate σ_vm_trial = √(3J₂)
   - If σ_vm_trial ≤ σ_y: ELASTIC, return σ_trial

3. **Plastic correction (if yielding)**
   - Work in principal stress space
   - Decompose: σ_trial = p𝐈 + s_trial
   - Keep pressure p (hydrostatic doesn't yield)
   - Scale deviatoric: s_new = (σ_y/σ_vm_trial) × s_trial
   - Assemble: σ_new = p𝐈 + s_new

4. **Return to Cartesian coordinates**
   - Transform back using eigenvectors
   - σ = Q·σ_principal·Qᵀ

**Write this in pseudocode!**

#### 2. Extension from 1D to 3D (1.5 hours)

**Create comparison table:**

| Concept | 1D Implementation | 3D Extension |
|---------|------------------|--------------|
| Stress | scalar σ | tensor σᵢⱼ |
| Yield | \|σ\| ≤ σ_y | √(3J₂) ≤ σ_y |
| Return | σ_new = sign(σ)σ_y | Radial in deviatoric space |
| Pressure | N/A | p = (1/3)tr(σ), preserved |
| Data structure | float | 3×3 array or 6×1 Voigt |

**Key insights:**
- Conceptual algorithm is SAME
- Mathematical complexity increases
- Tensor operations replace scalar operations

#### 3. Large Displacement Considerations (1.5 hours)

**You wanted to understand large displacement analysis!**

**Summary of what you've learned:**

**Kinematics:**
- Deformation gradient F: THE fundamental object
- Polar decomposition: F = R·U (separate rotation from stretch)
- Green strain E: frame-invariant, works for large rotation

**Stresses:**
- Multiple measures (Cauchy σ, 2nd PK S)
- S and E are work conjugate (used in constitutive laws)
- Transform to σ for output/postprocessing

**Plasticity framework:**
- Work in material frame (S, E)
- Return mapping in principal stress space
- Frame-invariance critical for large rotations

**For MFEM implementation (Block 6+):**
- FE formulation uses S and E
- Constitutive law: S = f(E, history)
- Return mapping at each quadrature point

**Write a 1-page summary:** "Large Displacement Framework for Plasticity"

### Synthesis Questions (2-3 hours)

**Deliverable:** Add to `reports/block04/assignment_4_8_synthesis.md`

**Question 1:** Why do we need different strain measures?
- When is small strain ε adequate?
- When do you MUST use Green strain E?
- Give specific examples from your work

**Question 2:** Frame invariance in plasticity
- Why does small strain fail for large rotation?
- How does Green strain solve this?
- Why does this matter for return mapping?

**Question 3:** Stress measures and work conjugacy
- What does "work conjugate" mean?
- Why use S (2nd PK) with E (Green strain)?
- When do you use Cauchy stress σ?

**Question 4:** Von Mises in context
- Why is von Mises better than Tresca for metals?
- Why is J₂ invariant important?
- How does this extend your 1D work?

**Question 5:** Preparation for MFEM
- What tensor operations will you need in MFEM?
- What data structures make sense?
- How will return mapping fit into FE solve?

**Question 6:** Large displacement viscoplasticity
- Your PhD goal: viscoplastic ROM for high temps
- Large displacements expected? (thermal expansion, creep)
- Which formulation will you use? (justify)

### Python Exercise: Complete Return Mapping (2-3 hours)

**Deliverable:** `code/block04/ex4_8_return_mapping_3d.py`

**Implement complete 3D von Mises return mapping:**

```python
import numpy as np
from scipy.linalg import eigh

def von_mises_return_mapping_3d(sigma_trial, sigma_y, E_modulus, nu):
    """
    3D von Mises return mapping algorithm
    
    Parameters:
    -----------
    sigma_trial : 3x3 array
        Trial stress tensor (elastic predictor)
    sigma_y : float
        Yield stress
    E_modulus : float
        Young's modulus
    nu : float
        Poisson's ratio
        
    Returns:
    --------
    sigma : 3x3 array
        Updated stress tensor
    plastic : bool
        True if plastic loading occurred
    """
    
    # Step 1: Spectral decomposition
    principals_trial, Q = eigh(sigma_trial)
    
    # Step 2: Check yield
    # Calculate von Mises of trial stress
    p_trial = np.mean(principals_trial)
    s_trial_principals = principals_trial - p_trial
    sigma_vm_trial = np.sqrt(1.5 * np.sum(s_trial_principals**2))
    
    # Yield function
    f = sigma_vm_trial - sigma_y
    
    if f <= 0:
        # Elastic: no return needed
        return sigma_trial, False
    
    # Step 3: Plastic correction
    # Preserve pressure, scale deviatoric
    factor = sigma_y / sigma_vm_trial
    s_new_principals = factor * s_trial_principals
    principals_new = s_new_principals + p_trial
    
    # Step 4: Transform back to Cartesian
    sigma_principal = np.diag(principals_new)
    sigma = Q @ sigma_principal @ Q.T
    
    return sigma, True

# Test cases
def test_return_mapping():
    E = 200e3  # MPa
    nu = 0.3
    sigma_y = 200  # MPa
    
    print("3D Return Mapping Tests\n" + "="*50)
    
    # Test 1: Elastic (should not change)
    sigma_elastic = np.diag([100, 80, 60])
    sigma_1, plastic_1 = von_mises_return_mapping_3d(sigma_elastic, sigma_y, E, nu)
    print("\nTest 1: Elastic loading")
    print(f"Trial stress:\n{sigma_elastic}")
    print(f"Plastic: {plastic_1}")
    print(f"Returned stress:\n{sigma_1}")
    
    # Test 2: Plastic (should return to yield surface)
    sigma_plastic = np.diag([300, 200, 100])
    sigma_2, plastic_2 = von_mises_return_mapping_3d(sigma_plastic, sigma_y, E, nu)
    print("\nTest 2: Plastic loading")
    print(f"Trial stress:\n{sigma_plastic}")
    print(f"Plastic: {plastic_2}")
    print(f"Returned stress:\n{sigma_2}")
    
    # Verify on yield surface
    p = np.trace(sigma_2) / 3
    s = sigma_2 - p * np.eye(3)
    J2 = 0.5 * np.einsum('ij,ij->', s, s)
    sigma_vm = np.sqrt(3 * J2)
    print(f"von Mises stress: {sigma_vm:.2f} (should be {sigma_y})")
    
    # Test 3: General stress state with shear
    sigma_general = np.array([[250, 80, 0],
                              [80, 200, 50],
                              [0, 50, 150]])
    sigma_3, plastic_3 = von_mises_return_mapping_3d(sigma_general, sigma_y, E, nu)
    print("\nTest 3: General stress with shear")
    print(f"Trial stress:\n{sigma_general}")
    print(f"Plastic: {plastic_3}")
    print(f"Returned stress:\n{sigma_3}")
    
    # Test 4: Verify hydrostatic preservation
    sigma_hydro_test = np.array([[300, 0, 0],
                                  [0, 300, 0],
                                  [0, 0, 300]])
    sigma_4, plastic_4 = von_mises_return_mapping_3d(sigma_hydro_test, sigma_y, E, nu)
    print("\nTest 4: Hydrostatic stress")
    print(f"Trial stress:\n{sigma_hydro_test}")
    print(f"Plastic: {plastic_4}")
    print(f"Note: Pure hydrostatic should not yield (σ_vm = 0)")

if __name__ == "__main__":
    test_return_mapping()
```

**Your task:**
1. Complete the implementation
2. Run all test cases and verify
3. Add visualization: plot trial and returned stress in principal space
4. Compare to your 1D implementation - same algorithm structure?

---

## BLOCK 4 SUMMARY AND REFLECTION

**Deliverable:** `reports/block04/block04_summary.md` (2-3 pages)

### Content

**1. What you learned (1 page)**
- Tensor notation and index notation
- Deformation gradient and kinematics
- Strain measures (small vs finite)
- Stress measures (multiple definitions)
- Principal stresses and invariants
- Von Mises plasticity in 3D
- Voigt notation for implementation

**2. Connection to your PhD goals (0.5 page)**
- Large displacement framework for high-temp components
- Why frame invariance matters
- Preparation for MFEM implementation
- Path to ROM (reduced order modeling)

**3. Key insights (0.5 page)**
- What surprised you?
- What was harder than expected?
- What clicked after the exercises?

**4. Looking ahead to Block 5 (MFEM) (0.5 page)**
- What do you feel prepared for?
- What concerns remain?
- Specific questions for MFEM implementation

---

## SUBMISSION CHECKLIST

When Block 4 is complete, you should have:

**Theory Documents:**
- [ ] `assignment_4_1_index_notation.md`
- [ ] `assignment_4_2_deformation_gradient.md`
- [ ] `assignment_4_3_strain_measures.md`
- [ ] `assignment_4_4_stress_tensor.md`
- [ ] `assignment_4_5_principal_stresses.md`
- [ ] `assignment_4_6_von_mises.md`
- [ ] `assignment_4_7_voigt_notation.md`
- [ ] `assignment_4_8_synthesis.md`
- [ ] `block04_summary.md`

**Hand Calculations:**
- [ ] `handwork_4_1.pdf` (5 problems)
- [ ] `handwork_4_2.pdf` (4 problems)
- [ ] `handwork_4_3.pdf` (4 problems)
- [ ] `handwork_4_4.pdf` (4 problems)
- [ ] `handwork_4_5.pdf` (3 problems)
- [ ] `handwork_4_6.pdf` (3 problems)
- [ ] `handwork_4_7.pdf` (3 problems)

**Python Exercises:**
- [ ] `ex4_1_index_notation.py`
- [ ] `ex4_2_deformation_gradient.py`
- [ ] `ex4_3_strain_measures.py`
- [ ] `ex4_4_stress_tensor.py`
- [ ] `ex4_5_principal_stresses.py`
- [ ] `ex4_6_von_mises.py`
- [ ] `ex4_7_voigt_notation.py`
- [ ] `ex4_8_return_mapping_3d.py`

**Journal:**
- [ ] Daily entries during Block 4
- [ ] Weekly reflections

---

## TIMELINE

**Week 1:** Assignments 4.1-4.2 (Index notation, deformation gradient)
**Week 2:** Assignment 4.3 (Strain measures)  
**Week 3:** Assignments 4.4-4.5 (Stress tensor, principal stresses)
**Week 4:** Assignment 4.6 (Von Mises)
**Week 5:** Assignment 4.7 (Voigt notation)
**Week 6-7:** Assignment 4.8 (Synthesis, 3D return mapping)
**Week 8:** Summary and reflection

**Total: 40-50 hours over 7-8 weeks at 6h/week**

---

## GRADING CRITERIA

**Theory Understanding (40%):**
- Can you explain concepts in your own words?
- Do derivations show understanding?
- Are connections made between topics?

**Implementation (30%):**
- Do Python exercises work correctly?
- Are numpy/scipy used appropriately?
- Does code demonstrate understanding?

**Problem Solving (20%):**
- Are hand calculations correct?
- Is work shown clearly?
- Are answers verified?

**Synthesis (10%):**
- Can you connect 1D to 3D?
- Is large displacement framework understood?
- Are you ready for MFEM?

---

**Ready to start when you are. Let me know when Block 4 is complete!**

**Questions before beginning?**
