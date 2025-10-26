# Week 1 reading notes


## Questions
### Dunne and Petrinic
1. What is the von Mises yield criterion?
- The VM equivalent stress if based on the J2 stress invariant. The VM equivalent stress (f) is equal to the difference between the equivalent stress and the yield stress that can be a function of plastic strain
2. What is the **flow rules** and hwat **associated** mean?
- The flow rule defines the plastic strain flow direction. See definition of associated below
- Associated mean that the flow direction is based on the normal to the tangent at a loading point on the yield surface, where any subsequent loading induce plastic flow
3. How does isotropic hardening modify the yield surface.
- Isotropic hardening mean that for any plastic strain increase, the yield surface expands in such a way that it is equal in all principal direction.

### Simo and Hughes
4. How does the 1D friction model relate to plasticity?
- The simple friction/slip model takes into acound the elasticity of a spring (for the elastic part) and a sliping part that is not going back (for the plastic part). So, when a stress is applied the elastic part takes as much as it can, and once the limit of the friction element is reached (analogy of yield stress), the part starts to slip and keep this displacement as long as the stress keep rising (hardening) or beeing constant (perfectly plastic)
5. What are the **loading/unloading conditions**
- Loading is when f=0, unloading is when f<0. Where $f(\sigma)=|\sigma|-[\sigma_{y}+K\alpha]<=0$
6. What is **return mapping**
- When the actual stress state is returned to the yield surface after an initial guess. The initial guess is most likely the Young's modulus times the equivalent strain. When the strain is high enough, this make f >= 0 for a moment (with the initial guess) and then returned to the yield surface

## Confusing concept
- The physical signifiance of $\lambda$ the plastic multiplier(Dunn)/slip rate(Simo)

## Questions for next 
- Difference between associative and non associative
- How is the isotropic hardening behavior changing for multiaxial stress state? Formulas used are all based on uniaxial stress state.
- When is f(sigma)=0 supposed to happen so that the Kuhn-Tucker condition is respected
