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
    E : Young's modulus [MPa]
    sigma_y : Yield stress [MPa]
    eta : Viscosity [MPa·s]
    n : Rate sensitivity exponent (default=1)
    
    Returns:
    --------
    sigma : Stress [Pa]
    eps_vp : Viscoplastic strain
    """
    
    # Compute next step straina and trial stress
    eps_n_1 = eps_n + d_eps

    sigma_trial = E*(eps_n_1 - eps_vp_n)

    # Check yield condition
    f_trial = np.abs(sigma_trial) - sigma_y

    if f_trial < 0: # Elastic step
        return sigma_trial, eps_vp_n
    else: # Plastic step
        # Compute plastic multiplier, implemented the variable n
        # version to test other values of n eventually
        numerator = (dt / eta) * (f_trial / sigma_y)**n 
        denominator=  1 + (dt*E) / (eta * sigma_y**n) * f_trial**(n - 1)
        
        d_lambda = numerator/denominator
                
        # Update viscoplastic strain
        eps_vp_n += d_lambda * np.sign(sigma_trial)
        
        # Update stress
        sigma = sigma_trial - E * d_lambda * np.sign(sigma_trial)
        
        return sigma, eps_vp_n
    
def rate_sensitivity():
    '''
    Function to evaluate the strain rate sensitivity
    '''
    print("*******************************************************************")
    print("                       RATE SENSITIVITY                            ")
    print("                         output data                               ")
    print("*******************************************************************")
    # Material properties
    E = 200e3                           # MPa - Young's modulus
    SIGMA_Y0 = 250                      # MPa - Yield stress
            
   
    # (3.2.1) Constant visosity, variable strain rate
    DT = 1e-2                           # s -  constant time step
    ETA = 1                             # MPa*s - Viscosity
       
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
        d_eps = strain_rate*DT # Will be constant through the test
        
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
    
    # Maximum stress
    
    for strain_rate, stress in zip(strain_rates, stress_rate_i):
        print(f"Rate: {strain_rate:.2e} 1/s, sigma_max: {np.max(stress)} MPa")
   
def creep_test():
    '''
    Function to evaluate the creep test: Constant stress of 260 MPa
    
    Material is loaded to 260 MPa at t=0. Stress is plot over time
    '''
    print("*******************************************************************")
    print("                          CREEP TEST                               ")
    print("                         output data                               ")
    print("*******************************************************************")
    
    # Material properties (ref: 3.2.1)
    E = 200e3                           # MPa - Young's modulus
    SIGMA_Y0 = 250                      # MPa - Yield stress
    ETA = 4                             # MPa*s - Viscosity
        
    # Analysis parameters
    T_MAX = 100                         # s - End time
    DT = 1                              # s -  constant time step
    STRESS_INIT = 260                   # MPa - Initial constant stress
    
    # Initialize stresses and strains
    eps_n = 0
    eps_vp_n = 0
    d_eps =  STRESS_INIT/E              # Only at first time step in this case
    print(f"Initial stress: {STRESS_INIT} MPa")
    print(f"Initial strain: {d_eps:.3e}")
    print(f"Test E*deps: {E*d_eps} MPa")
    
    
    # Initialize history variable
    stress_history = [0.0]
    eps_history = [0.0]
    eps_vp_history = [0.0]
    time_history = [0.0]

    i = 0   # Counter for initial time step
    ti = 0  # Current time
    # Loop untill max strain is reached
    while ti < T_MAX:
                    
        stress, eps_vp_n = return_mapping_viscoplasticity(eps_n, d_eps, DT, eps_vp_n, E, SIGMA_Y0, ETA)
        
        # Update variables and append history variables
        eps_n += d_eps # needs to be updated after the integration
        eps_history.append(eps_n)
        stress_history.append(stress)
        eps_vp_history.append(eps_vp_n)
        time_history.append(ti)
        
        # Update d_eps for next step
        d_eps = STRESS_INIT/E + eps_vp_n - eps_n # Compute equivalent required strain to keep stress at constant value
        
        i += 1  # Update counter
        ti += DT # Update time counter
        
    # * Post processing
    ## Stress vs time
    fig, ax = plt.subplots()
    ax.plot(time_history, stress_history,ls = '--', marker = 'o')

    # Axis labels and styling
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title("Stress evolution over time in creep test")
    ax.grid(alpha = 0.3)
    plt.show()
    
    print(f"Last stress: {stress_history[-1]} MPa")
    
    ## Strain rate (creep rate) vs time
    creep_rate = np.gradient(eps_history, time_history)
    
    fig2, ax2 = plt.subplots()
    ax2.plot(time_history, creep_rate,ls = '--', marker = 'o')
    
    # Axis labels and styling
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Strain Rate (mm/mm)")
    ax2.set_title("Creep rate")
    ax2.grid(alpha = 0.3)
    plt.show()
    fig2.savefig("week03_creep.png")
    
    plt.show()
    pass
            
def relaxation_test():
    '''
    Function to evaluate the relaxation test: large initial strain
    
    init strain = 0.0015 mm/mm. Plot stress over time
    '''
    print("*******************************************************************")
    print("                    RELAXATION TEST                                ")
    print("                         output data                               ")
    print("*******************************************************************")
    
    # Material properties (ref: 3.2.1)
    E = 200e3                               # MPa - Young's modulus
    SIGMA_Y0 = 250                          # MPa - Yield stress
    ETA = 1                                 # MPa*s - Viscosity
        
    # Analysis parameters
    T_MAX = 0.1                             # s - End time
    DT = 1e-3                               # s -  constant time step
  
    # Initialize stresses and strains
    eps_n = 0
    eps_vp_n = 0
    d_eps =  0.0015                         # Only at firs time step in this case

    print(f"Initial strain: {d_eps:.3e}")
    print(f"Test E*deps (Initial stress): {E*d_eps} MPa")
    
    
    # Initialize history variable
    stress_history = [0.0]
    eps_history = [0.0]
    eps_vp_history = [0.0]
    time_history = [0.0]

    i = 0   # Counter for initial time step
    ti = 0  # Current time
    # Loop untill max strain is reached
    while ti < T_MAX:
        
        if i > 0:
            d_eps = 0 # Change rate of change in strain to 0 to mimic initial stress only
            
        stress, eps_vp_n = return_mapping_viscoplasticity(eps_n, d_eps, DT, eps_vp_n, E, SIGMA_Y0, ETA)
        
        # Update variables and append history variables
        eps_n += d_eps # needs to be updated after the integration
        eps_history.append(eps_n)
        stress_history.append(stress)
        eps_vp_history.append(eps_vp_n)
        time_history.append(ti)
        
        i += 1  # Update counter
        ti += DT # Update time counter
        
    # * Post processing
    ## Stress vs time
    fig, ax = plt.subplots()
    ax.plot(time_history, stress_history,ls = '--', marker = 'o')

    # Axis labels and styling
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title("Stress evolution over time in creep test")
    ax.grid(alpha = 0.3)
    plt.show()
    fig.savefig("week03_creep.png")  
    
    # Last stress
    last_stress = stress_history[-1]
    print(f"Last stress: {last_stress:.16e} MPa")
    print(f"yield - last stress: {SIGMA_Y0 - last_stress:.16e}")    
    
    
def viscosity_effect():
    # (3.2.4) Effect of viscosity
    pass
      

if __name__ == '__main__':
    # rate_sensitivity()
    creep_test()
    # relaxation_test()
    # viscosity_effect()
