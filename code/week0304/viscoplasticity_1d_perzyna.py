import numpy as np
import matplotlib.pyplot as plt

def return_mapping_viscoplasticity(eps_n, sig_n, d_eps, dt, eps_vp_n, E, sigma_y, eta, n=1):
    """
    Parameters:
    -----------
    eps_n : Total strain at step n
    sig_n : stress at step n
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
    # Elastic predictor
    sigma_trial = E*(eps_n + d_eps - eps_vp_n)
    f_trial = np.abs(sigma_trial) - sigma_y
    
    # Check yielding
    if f_trial < 0: # Purely elastic
        return sigma_trial, eps_vp_n
    else : # Viscoplastic
        sigma_0 = sigma_y
        s = np.sign(sigma_trial)
               
        # * n=1 for the linear case and nonlinear case has been verified. Both cases 
        # * give the same results
        
        if n==1: # Linear overstress
            d_lambda =  dt * f_trial / (eta*sigma_0 + E * eta * dt)
            
        else: # Nonlinear overstress
            
            d_lambda = 0    # Initial guess
            tol = 1e-8      # Error tol
            res = 1e8       # Error initialization
            kmax = 30       # Maximum iteration
            k = 1           # Iteration counter
            
            while np.abs(res) > tol and k < kmax:
                # Compute yield criterion
                f = f_trial - E*d_lambda 
                
                # Compute residual and derivatives
                res = (f/sigma_0)**n - d_lambda*eta/dt
                dres = -n*E*(f/sigma_0)**(n-1) / sigma_0 - eta/dt
                
                # Update d_lambda
                d_lambda -= res/dres
                
                # Update counter
                k+=1
        
        # Update values
        sig_n = sigma_trial - E * d_lambda * s
        eps_vp_n += d_lambda * s
        
        return sig_n, eps_vp_n        
   
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
        sig_n = 0
        eps_vp_n = 0
        d_eps = strain_rate*DT # Will be constant through the test
        
        # Initialize history variable
        stress_history = [0.0]
        eps_history = [0.0]
        eps_vp_history = [0.0]

        # Loop untill max strain is reached
        while eps_n < MAX_EPS:
                            
            sig_n, eps_vp_n = return_mapping_viscoplasticity(eps_n, sig_n, d_eps, DT, eps_vp_n, E, SIGMA_Y0, ETA,n=1)
            
            # Update variables and append history variables
            eps_n += d_eps # needs to be updated after the integration
            eps_history.append(eps_n)
            stress_history.append(sig_n)
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
    # Material properties
    E = 200e3  # MPa
    sigma_y = 250  # MPa
    eta = 1  # MPa·s 
    sigma_applied = 260  # MPa (constant)
    
    # Time parameters
    T_MAX = 100  # seconds
    DT = 0.1  # time step
    
    # Initial conditions
    eps_vp = 0.0
    eps = sigma_applied / E  # Initial elastic strain
    
    # History
    time_history = [0.0]
    eps_history = [eps]
    eps_vp_history = [0.0]
    stress_history = [sigma_applied]
    
    t = 0.0
    while t < T_MAX:
        t += DT
        
        # Viscoplastic flow rate (constant stress)
        f = sigma_applied - sigma_y  # overstress
        
        if f > 0:
            # Viscoplastic strain rate
            eps_vp_dot = (1/eta) * (f / sigma_y)  # for n=1
            
            # Update viscoplastic strain
            d_eps_vp = eps_vp_dot * DT
            eps_vp += d_eps_vp
            
            # Total strain (to maintain constant stress)
            eps = sigma_applied / E + eps_vp
        
        # Store history
        time_history.append(t)
        eps_history.append(eps)
        eps_vp_history.append(eps_vp)
        stress_history.append(sigma_applied)
    
    # Plot strain vs time (creep curve)
    plt.figure()
    plt.plot(time_history, eps_history, 'o-')
    plt.xlabel('Time (s)')
    plt.ylabel('Strain')
    plt.title('Creep Test: Strain vs Time')
    plt.grid(True)
    plt.savefig('week03_creep.png')
    plt.show()
    
    # Plot creep rate
    creep_rate = np.gradient(eps_history, time_history)
    plt.figure()
    plt.plot(time_history, creep_rate, 'o-')
    plt.xlabel('Time (s)')
    plt.ylabel('Creep Rate (strain/s)')
    plt.title('Creep Rate vs Time')
    plt.grid(True)
    plt.show()
    
    print(f"Initial strain: {eps_history[0]:.6e}")
    print(f"Final strain: {eps_history[-1]:.6e}")
    print(f"Steady-state creep rate: {creep_rate[-1]:.6e} /s")  
          
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
    sig_n = 0
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
            
        stress, eps_vp_n = return_mapping_viscoplasticity(eps_n, sig_n, d_eps, DT, eps_vp_n, E, SIGMA_Y0, ETA, n=4)
        
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
    fig.savefig("week03_relaxation.png")  
    
    # Last stress
    last_stress = stress_history[-1]
    print(f"Last stress: {last_stress:.16e} MPa")
    print(f"yield - last stress: {SIGMA_Y0 - last_stress:.16e}")    
       
def viscosity_effect():
    '''
    Function to evaluate the effect of viscosity
    '''
    print("*******************************************************************")
    print("                      VISCOSITY SENSITIVITY                        ")
    print("                         output data                               ")
    print("*******************************************************************")
    # Material properties
    E = 200e3                           # MPa - Young's modulus
    SIGMA_Y0 = 250                      # MPa - Yield stress
            
   
    # (3.2.1) Constant visosity, variable strain rate
    DT = 1e-2                           # s -  constant time step
    eta_s = [1]#[0.01, 1, 100]                             # MPa*s - Viscosity
       
    # Analysis parameters
    strain_rates = [1e-3, 1e-2, 1e-1]   # mm/mm*s
    MAX_EPS = 3e-3                      # mm/mm
    
    # History variables for each strain rate
    stress_rate_i = []
    eps_rate_i = []
    eps_vp_rate_i = []
    
    fig, ax = plt.subplots()
    
    for strain_rate in strain_rates:
        for eta_i in eta_s: 
            # Initialize stresses and strains
            eps_n = 0
            sig_n = 0
            eps_vp_n = 0
            d_eps = strain_rate*DT
            
            # Initialize history variable
            stress_history = [0.0]
            eps_history = [0.0]
            eps_vp_history = [0.0]

            # Loop untill max strain is reached
            while eps_n < MAX_EPS:
                                
                sig_n, eps_vp_n = return_mapping_viscoplasticity(eps_n, sig_n, d_eps, DT, eps_vp_n, E, SIGMA_Y0, eta_i,n=4)
                
                
                # Update variables and append history variables
                eps_n += d_eps # needs to be updated after the integration
                eps_history.append(eps_n)
                stress_history.append(sig_n)
                eps_vp_history.append(eps_vp_n)
                
            # Keep track of each history variable evolution for each rates
            eps_rate_i.append(eps_history)
            stress_rate_i.append(stress_history)
            eps_vp_rate_i.append(eps_vp_history)
            
            for strain, stress, strain_rate in zip(eps_rate_i, stress_rate_i, strain_rates):
                ax.plot(strain, stress,ls = '--', marker = 'o', label = f"rate={strain_rate:.2e}, eta={eta_i:.2e}")
                
            for strain_rate, stress in zip(strain_rates, stress_rate_i):
                print(f"(Eta: {eta_i:.2e}, Rate: {strain_rate:.2e} 1/s, sigma_max: {np.max(stress)} MPa")

        
    # * Post processing
    # Plot all stress strain curves (f(H))
    
    # Axis labels and styling
    ax.set_xlabel("Strain (mm/mm)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title("Stress evolution")
    ax.grid(alpha = 0.3)
    ax.legend()
    plt.show()
    fig.savefig("week03_viscosity_effect.png")


if __name__ == '__main__':
    rate_sensitivity()
    # creep_test()
    # relaxation_test()
    # viscosity_effect()
