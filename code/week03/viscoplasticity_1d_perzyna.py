import numpy as np
import matplotlib.pyplot as plt

def return_mapping_viscoplasticity(eps_n, d_eps, dt, eps_vp_n, E, sigma_y, eta, n=1):
    """
    Parameters:
    -----------
    eps_n : Total strain at step n
    d_eps : Strain increment
    dt : Time increment [s]
    eps_vp_n : Viscoplastic strain at step n
    E : Young's modulus [Pa]
    sigma_y : Yield stress [Pa]
    eta : Viscosity [Pa·s]
    n : Rate sensitivity exponent (default=1)
    
    Returns:
    --------
    sigma : Stress [Pa]
    eps_vp : Viscoplastic strain
    """
    # Define a lambda for macaulay brackets (ramp function)
    # TODO: remove if neaded  - macaulay = lambda x : (x + np.abs(x))/2

    # Compute next step straina and trial stress
    eps_n_1 = eps_n + d_eps

    sigma_trial = E*(eps_n_1 - eps_vp_n)

    # Check yield condition
    f_trial = np.abs(sigma_trial) - sigma_y

    if f_trial < 0: # Elastic step
        return sigma_trial, eps_vp_n
    else: # Plastic step
        # Compute plastic multiplier
        d_lambda = (dt / eta) * (f_trial / sigma_y)**n 
        d_lambda /= (1 + dt*E / (eta * sigma_y**n) * f_trial**(n - 1))
        
        d_lambda2 = (dt / eta) * f_trial / (1 + dt*E/eta)
        print(f"dlambda 1: {d_lambda:.2e}, 2:{d_lambda2:.2e}")
        
        # Update viscoplastic strain
        eps_vp_n += d_lambda * np.sign(sigma_trial)
        
        # Update stress
        sigma = sigma_trial - E * d_lambda * np.sign(sigma_trial)
        
        return sigma, eps_vp_n
    
def rate_sensitivity():
    '''
    Function to evaluate the strain rate sensitivity
    '''
    # Material properties
    E = 200e3                           # MPa - Young's modulus
    SIGMA_Y0 = 250                      # MPa - Yield stress
            
   
    # (3.2.1) Constant visosity, variable strain rate
    DT = 0.01                           # s -  constant time step
    ETA = 1e-6                          # Pa*s - Viscosity
       
    # Analysis parameters
    strain_rates = [1e-3, 1e-2, 1e-1]   # mm/mm*s
    MAX_EPS = 3e-3                      # mm/mm
    
    # History variables for each strain rate
    stress_rate_i = []
    eps_rate_i = []
    eps_vp_rate_i = []
    
    for strain_rate in strain_rates:
        # Initialize stresses and strains
        eps_n = 0
        eps_vp_n = 0
        d_eps = strain_rate*DT
        
        # Initialize history variable
        stress_history = [0.0]
        eps_history = [0.0]
        eps_vp_history = [0.0]

        # Loop untill max strain is reached
        while eps_n < MAX_EPS:
            stress, eps_vp_n = return_mapping_viscoplasticity(eps_n, d_eps, DT, eps_vp_n, E, SIGMA_Y0, ETA)
            
            # Update variables and append history variables
            eps_n += d_eps # needs to be updated after the integration
            eps_history.append(eps_n)
            stress_history.append(stress)
            eps_vp_history.append(eps_vp_n)
            
        # Keep track of each history variable evolution for each rates
        eps_rate_i.append(eps_history)
        stress_rate_i.append(stress_history)
        eps_vp_rate_i.append(eps_vp_history)
        
    # * Post processing
        # Plot all stress strain curves (f(H))
    fig, ax = plt.subplots()
    for strain, stress, strain_rate in zip(eps_rate_i, stress_rate_i, strain_rates):
        ax.plot(strain, stress,ls = '--', marker = 'o', label = f"rate={strain_rate:.2e}")

    # Axis labels and styling
    ax.set_xlabel("Strain (mm/mm)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title("Stress evolution")
    ax.grid(alpha = 0.3)
    ax.legend()
    plt.show()
    fig.savefig("week03_rate_sensitivity.png")

            
            
def creep_test():
    # (3.2.2) Creep test
    pass
    
def relaxation_test():
    # (3.2.3) Relaxation test
    pass
    
def viscosity_effect():
    # (3.2.4) Effect of viscosity
    pass

        

if __name__ == '__main__':
    rate_sensitivity()
    creep_test()
    relaxation_test()
    viscosity_effect()
