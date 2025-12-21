# Code report - Perzyna viscoplasticity

## 1. Rate sensitivity:

### How does peak stress change with strain rate? Quantify.
The higher the strain rate, the higher the peak stress. This means that in those conditions, with the Perzyna model we observe strain hardening that positively correlate with strain rate:
- 1e-3 /s: 289.99 MPa
- 1e-2 /s: 479.64 MPa
- 1e-1 /s: 576.53 MPa
  
### Why does this happen physically?
Refering to the relogical model shown in the litterature, the viscous effect act as a damper. Thus, dependant on the speed at wich this "damper" is compressed/strained. This damping effect fades over time and should lower the stress on the material closer to the yield stress at a rate dependant on the viscosity/fluidity parameter.

## 2. Creep:

### What's the steady-state creep rate? (dε/dt at t→∞)
At constant stress (creep), the creep rate should be constant

### How does it relate to η and f?
- The more viscous the material is ($\eta \rightarrow \infty$), the lower the creep rate is.
- The higher the value of $f$ is, the higher the creep rate is.

Meaning that a non viscous material subject to higher stress will exert higher creep rate.

## 3. Relaxation:

### Final stress after 100s?
$\sigma_{final}=250 \space MPa$
### Does it reach yield stress exactly? Why/why not?
Yes it reaches the yield stress because the material properties combined with the loading let the material stress state return to viscoplastic equilibrium within the time frame shown.

## 4. Viscosity parameter:

###  η→0, what happens? Compare to rate-independent.
When $\eta=0$, we can observe perfectly plstic behavior (because the programmed Perzyna model doesn't accound for hardening)
### η→∞, what's the behavior?
The stress keeps rising since the viscous strain keeps rising at a very high rate,

## . Time step sensitivity:

### Try Δt = 0.1s and Δt = 0.001s for creep test
### Does solution change? Why?
No. Because the algorithm uses backward euler giving unconditional stability in time integration. 