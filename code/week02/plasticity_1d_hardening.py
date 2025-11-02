import numpy as np
import matplotlib.pyplot as plt

def return_mapping_isotropic_hardening(eps_n, d_eps, eps_p_n, alpha_n, E, sigma_y0, H):
    """
    1D return mapping with linear isotropic hardening
    
    Parameters:
    -----------
    eps_n : float
        Total strain at previous step n
    d_eps : float
        Strain increment (eps_{n+1} - eps_n)
    eps_p_n : float
        Plastic strain at previous step n
    alpha_n : float
        Accumulated plastic strain at previous step n
    E : float
        Young's modulus [Pa]
    sigma_y0 : float
        Initial yield stress [Pa]
    H : float
        Hardening modulus [Pa]
    
    Returns:
    --------
    sigma : float
        Stress at step n+1 [Pa]
    eps_p : float
        Plastic strain at step n+1
    alpha : float
        Accumulated plastic strain at step n+1
    """
    # Total strain in current increment
    eps_n = eps_n + d_eps
    
    # Current yield stress
    sig_y = lambda : sigma_y0 + H*alpha_n
    
    # Yield function
    sigma_eq = lambda eps_n, d_eps, eps_p_n :  E*(eps_n + d_eps - eps_p_n)

    # Yield criterion
    f = lambda sigma_e, sigma_y : np.abs(sigma_e) - sigma_y # simo 2.2.37
            
    # Check yield condition
    sigma_e = sigma_eq(eps_n, d_eps, eps_p_n)
    f_e = f(sigma_e, sig_y())

    if f_e <= 0: # elastic case
        return sigma_e, eps_p_n, alpha_n
    else: # f > 0 compute plastic corrector

        # Compute plastic multiplier
        delta_gamma = f_e / (E + H) 

        # Compute plastic strain increment
        d_eps_p = delta_gamma * np.sign(sigma_e)
        eps_p_n += d_eps_p 

        # Compute accumulated plastic strain
        alpha_n += delta_gamma

        # Compute stress
        sigma = (1-delta_gamma*E/np.abs(sigma_e)) * sigma_e
               
        return sigma, eps_p_n + d_eps_p, alpha_n

def test_hardening_comparison():
    """Parameter study: H = 0, 1 GPa, 5 GPa"""
    
    # Material properties
    E = 210e3  # MPa
    sigma_y0 = 250  # MPa
    H_values = [0, 1e3, 5e3, 50e3] # MPa
    NINC = 20 # Number of increment in strain path
    
    # Same loading history as Assignment 2.3
    strain_load = np.linspace(0, 0.002, NINC)
    strain_unload = np.linspace(0.002, 0, NINC)[1:]
    strain_reload = np.linspace(0, 0.003, NINC)[1:]
    strain_history = np.concatenate([strain_load, strain_unload, strain_reload])
    


    Hi_stress = [] # list of stress evolution with respect to H

    for Hi in H_values:

        # Initialisation
        eps_n = 0
        eps_p_n = 0
        alpha_n = 0


        stress_history = []
        for strain in strain_history: # enumerate for test purpose
            d_eps = strain - eps_n
            sigma, eps_p_n, alpha_n = return_mapping_isotropic_hardening(eps_n, d_eps, eps_p_n, alpha_n, E, sigma_y0, Hi)
            stress_history.append(sigma)
            if strain == 0:
                print(f"H={Hi:.2e}, eps={strain:.2e}, sigma={sigma}")
        
        # Append current stress state to history
        Hi_stress.append(stress_history)
        print(f"H={Hi:.2e}, eps={strain_history[-1]:.2e}, sigma={stress_history[-1]}")

        
    # Plot all stress strain curves (f(H))
    fig, ax = plt.subplots()
    for stress, Hi in zip(Hi_stress, H_values):
        ax.plot(strain_history, stress,ls = '--', marker = 'o', label = f"H={Hi:.1e}")

    # Axis labels and styling
    ax.set_xlabel("Strain (mm/mm)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title("Stress evolution")
    ax.grid(alpha = 0.3)
    ax.legend()
    plt.show()
    fig.savefig("week02_hardening_comparison.png")

if __name__ == '__main__':
    test_hardening_comparison()