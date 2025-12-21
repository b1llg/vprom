# Week 3 Check-in

## Deliverables:
**Theory:** https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/reports/weekly/week0304_viscoplasticity_theory.md

**Code:** https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/code/week0304/viscoplasticity_1d_perzyna.py

**Analysis:** (https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/reports/weekly/week0304_viscoplasticity_analysis.md)

**Journal:** https://github.com/b1llg/vprom/blob/main/journal/week0304submission.md

**Plots:**
- Rate sensitivity: https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/code/week0304/week0304_rate_sensitivity.png
- Creep: https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/code/week0304/week0304_creep.png
- Relaxation: https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/code/week0304/week0304_relaxation.png
- Viscosity effect: https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/code/week0304/week0304_viscosity_effect.png

## Key Results:
- Rate sensitivity: σ_peak(fast)/σ_peak(slow) = 576.53/289.99 = 1.9881
- Creep rate at t=100s: dε/dt = 2e-6
- Relaxation: σ(t=0) = ?, σ(t=100) = t=0s -> 392.86 MPa, t=100s -> 250 MPa

## Code snippet:
```python
def return_mapping_viscoplasticity(eps_n, sig_n, d_eps, dt, eps_vp_n, E, sigma_y, eta, n=1):
    """
    1D viscoplastic return mapping (Perzyna model)
    UMAT-style interface with support for general exponent n
    
    Parameters:
    -----------
    eps_n : float
        Total strain at step n
    sig_n : float
        Stress at step n [MPa]
    d_eps : float
        Strain increment (eps_{n+1} - eps_n)
    dt : float
        Time increment [s]
    eps_vp_n : float
        Viscoplastic strain at step n
    E : float
        Young's modulus [MPa]
    sigma_y : float
        Yield stress [MPa]
    eta : float
        Viscosity [MPa·s]
    n : int or float, optional
        Rate sensitivity exponent (default=1)
        n=1: Linear Perzyna (closed-form solution)
        n>1: Nonlinear (requires Newton-Raphson iteration)
    
    Returns:
    --------
    sigma_np1 : float
        Stress at step n+1 [MPa]
    eps_vp_np1 : float
        Viscoplastic strain at step n+1
    
    Notes:
    ------
    - For n=1, uses closed-form solution (no iteration required)
    - For n≠1, uses Newton-Raphson to solve nonlinear equation
    - Implements backward Euler time integration (unconditionally stable)
    """
    
    # 1. Update total strain
    eps_np1 = eps_n + d_eps
    
    # 2. Elastic predictor (trial stress)
    sigma_trial = E * (eps_np1 - eps_vp_n)
    
    # 3. Check yield condition
    f_trial = abs(sigma_trial) - sigma_y
    
    if f_trial <= 0:
        # Elastic step - no viscoplastic flow
        sigma_np1 = sigma_trial
        eps_vp_np1 = eps_vp_n
        
        return sigma_np1, eps_vp_np1
    
    else:
        # Viscoplastic step - compute plastic multiplier
        
        if abs(n - 1.0) < 1e-10:
            # Linear case (n=1): closed-form solution
            d_lambda = _compute_dlambda_linear(f_trial, dt, E, sigma_y, eta)
        else:
            # Nonlinear case (n≠1): Newton-Raphson iteration
            d_lambda = _compute_dlambda_nonlinear(f_trial, dt, E, sigma_y, eta, n)
        
        # 4. Update viscoplastic strain
        eps_vp_np1 = eps_vp_n + d_lambda * np.sign(sigma_trial)
        
        # 5. Update stress (return toward yield surface)
        sigma_np1 = sigma_trial - E * d_lambda * np.sign(sigma_trial)
        
        return sigma_np1, eps_vp_np1


def _compute_dlambda_linear(f_trial, dt, E, sigma_y, eta):
    """
    Compute plastic multiplier for linear Perzyna (n=1)
    Closed-form solution (no iteration needed)
    
    Parameters:
    -----------
    f_trial : float
        Trial yield function (overstress) [MPa]
    dt : float
        Time increment [s]
    E : float
        Young's modulus [MPa]
    sigma_y : float
        Yield stress [MPa]
    eta : float
        Viscosity [MPa·s]
    
    Returns:
    --------
    d_lambda : float
        Plastic multiplier increment
    """
    # For n=1, the equation is linear:
    # Δλ = (Δt/η) * (f_trial/σy) / (1 + Δt*E/(η*σy))
    # 
    # Simplified (multiply by σy):
    # Δλ = Δt*f_trial / (η + Δt*E)
    
    d_lambda = (dt * f_trial) / (eta + dt * E)
    
    return d_lambda


def _compute_dlambda_nonlinear(f_trial, dt, E, sigma_y, eta, n, 
                                 max_iter=20, tol=1e-10):
    """
    Compute plastic multiplier for nonlinear Perzyna (n≠1)
    Uses Newton-Raphson iteration to solve nonlinear equation
    
    Parameters:
    -----------
    f_trial : float
        Trial yield function (overstress) [MPa]
    dt : float
        Time increment [s]
    E : float
        Young's modulus [MPa]
    sigma_y : float
        Yield stress [MPa]
    eta : float
        Viscosity [MPa·s]
    n : float
        Rate sensitivity exponent
    max_iter : int, optional
        Maximum Newton-Raphson iterations (default=20)
    tol : float, optional
        Convergence tolerance (default=1e-10)
    
    Returns:
    --------
    d_lambda : float
        Plastic multiplier increment
    
    Notes:
    ------
    Solves: Δλ = (Δt/η) * ((f_trial - E*Δλ)/σy)^n
    Using Newton-Raphson on residual:
        R(Δλ) = Δλ - (Δt/η) * ((f_trial - E*Δλ)/σy)^n = 0
    """
    
    # Initial guess: use linearized approximation
    # (one Newton step from Δλ=0)
    numerator = (dt / eta) * (f_trial / sigma_y)**n
    denominator = 1.0 + n * (dt * E) / (eta * sigma_y**n) * f_trial**(n-1)
    d_lambda = numerator / denominator
    
    # Newton-Raphson iteration
    for iteration in range(max_iter):
        # Current overstress after return
        f_current = f_trial - E * d_lambda
        
        # Safety check: overstress should remain positive
        if f_current < 0:
            # Overshot - use smaller Δλ
            d_lambda *= 0.5
            continue
        
        # Residual: R(Δλ) = Δλ - (Δt/η) * (f_current/σy)^n
        R = d_lambda - (dt / eta) * (f_current / sigma_y)**n
        
        # Derivative: dR/dΔλ = 1 + n*(Δt*E)/(η*σy^n) * (f_current/σy)^(n-1)
        dR_ddlambda = 1.0 + n * (dt * E) / (eta * sigma_y**n) * \
                      (f_current / sigma_y)**(n - 1)
        
        # Newton-Raphson update
        d_lambda_new = d_lambda - R / dR_ddlambda
        
        # Check for negative Δλ (shouldn't happen, but safety check)
        if d_lambda_new < 0:
            d_lambda_new = d_lambda * 0.5
        
        # Check convergence
        if abs(d_lambda_new - d_lambda) < tol:
            return d_lambda_new
        
        # Update for next iteration
        d_lambda = d_lambda_new
        
        if iteration == max_iter-1:
            # If we reach here, convergence failed
            print(f"Warning: Newton-Raphson did not converge in {max_iter} iterations")
            print(f"  Final residual: {np.abs(R):.6e}")
            print(f"  Returning current value: Δλ = {d_lambda:.6e}")
    


    
    return d_lambda
```

## Questions/Issues:
- It is still unclear how to obtain the incremental form of $\Delta \lambda$. The time integration part hasn't really been really covered by the given litterature (Simo and Dunn). I relied a lot on Crisfield book which gives the equations directly but is not as math heavy as Simo.
- It is not really clear how the paramete $n$ makes the problem linear or non linear
- It has not been explicitely ask this week to complete a montly report. I would like to do a Latex article (to practice latex for further article publishing in this project) and I think it would be a good idea to take 2 weeks to introduce the next concept slowly (MFEM or C++ or 3D viscoplasticity) and also include this Latex article to wrap up the first month and maybe have a better understanding of the concepts I'm lagging (time itegration and viscoplasticity in general)

## Time: 
- 20 hours over about two weeks. Must expect lower volume of effort in the coming weeks since I'm going back to work afte parental leave. Time must be restrained to maximum 12 hours a week with possibility to extend each expected module/time frame to last 2 weeks to cap 20 hours of work. I want to get as much as possible in 4 years, and maybe use this project as an "on ramp to a real PhD". 