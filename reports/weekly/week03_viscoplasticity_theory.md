# Week 3 - Reading notes
- Simo & Hughes: Chapter 1, Section 1.7 (1D Viscoplasticity)
- Dunne & Petrinic: Chapter 2, Sections 2.7 (Viscoplasticity and creep)

## 1. Rate-Dependent vs Rate-Independent Plasticity

### What's the fundamental difference?
Rate independent means that the rate at which the material is deformed, doesn't have any impact on material properties. Rate dependent means the opposite. For example, some steels at elevated temperature exhibit rate dependance. Higher strain rate means higher yield stress and most likely lower strain at failure. Lower strain means lower yield stress and for very low strain rate the material could exhibit creep.

### Kuhn-Tucker conditions vs viscoplastic flow rule
The Kuhn-Tucker conditions specify that for any stress state, $\lambda f=0$, $\lambda \geq 0$ and $f \leq 0$. This means that for any stress state in the stress space, the stress must lie on the yield enveloppe ($\partial \mathbb{E_{\sigma}}$). However, viscoplastic material have ***over stress*** also called ***viscous stress*** which we could say hardened the material (in the sense of strength hardening), in reference to the last question. The KKT condition then is relaxed for these type of material to this new effect into account.

## 2. Perzyna Model :
Governing equation: $\varepsilon^{vp}=\tfrac{1}{\eta} \langle \Phi(f) \rangle^{n}$

### What is $\eta$ (viscosity parameter)?
The rate at which the over stress dissipate. Lower viscosity higher rate of dissipation. 
### What is $n$ (rate sensitivity exponent)?
Higher rate sensiticity means that the overstress gets higher as the strain rate gets higher
### What happens as $η \rightarrow 0$ ? As $\eta \rightarrow \infty$?
- $\eta \rightarrow 0$: The stress dissipate rapidly
- $\eta \rightarrow \infty$: The stress dissipate slowly

## 3. Time Integration Algorithm

### Why backward Euler for viscoplasticity?
### Implicit vs explicit integration
### Return mapping for viscoplastic case
### Derive plastic multiplier: $\Delta\lambda=\dfrac{\Delta t}{\eta}\langle \tfrac{f}{\sigma_{y}} \rangle^{n}$ for $n=1$
## 4. Physical Phenomena

### Creep: constant stress, strain increases
### Relaxation: constant strain, stress decreases
### Strain rate sensitivity: higher rate → higher stress
*Include sketch showing creep and relaxation behavior.*