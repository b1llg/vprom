import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def return_mapping_perfect_plasticity(eps_n, d_eps, eps_p_n, E, sigma_y):
    """
    1D return mapping for elastic-perfectly plastic material
    
    Parameters:
    -----------
    eps_n : float
        Total strain at previous step n
    d_eps : float
        Strain increment (eps_{n+1} - eps_n)
    eps_p_n : float
        Plastic strain at previous step n
    E : float
        Young's modulus [Pa]
    sigma_y : float
        Yield stress [Pa] (constant)
    
    Returns:
    --------
    sigma : float
        Stress at step n+1 [Pa]
    eps_p : float
        Plastic strain at step n+1
    """
    # Yield function
    sigma_eq = lambda eps_n, d_eps, eps_p_n :  E*(eps_n + d_eps - eps_p_n)

    # Yield criterion
    f = lambda sigma_e, sigma_y : np.abs(sigma_e) - sigma_y # simo 2.2.37

    # Elastic predictor
    sigma_e = sigma_eq(eps_n, d_eps, eps_p_n)
    f_e = f(sigma_e, sigma_y)

    # Check yield condition
    if f_e <= 0: # elastic case
        return sigma_e, eps_p_n
    else: # f > 0 compute plastic corrector

        delta_gamma = f_e/E

        d_eps_p = delta_gamma * np.sign(sigma_e)
               
        return sigma_y, eps_p_n + d_eps_p

def test_perfect_plasticity():
    """Test against analytical solution from Assignment 2.2"""
    
    # Material properties
    E = 200e3  # MPa
    sigma_y = 250  # MPa
    
    # Loading history: Load -> Unload -> Reload

    N = 11 # Points per segments

    strain_load = np.linspace(0, 0.002,N)         # loading
    strain_unload = np.linspace(0.002, 0, N)[1:]   # de-loading
    strain_reload = np.linspace(0, 0.003, N)[1:]   # loading
    strain_history = np.concatenate([strain_load, strain_unload, strain_reload])
    
    # Initialize storage
    stress_history = []
    plastic_strain_history = []
    
    # Initialize state
    eps_n = 0.0
    eps_p_n = 0.0
    

    #for each target strain in strain_history:
    for id, target in enumerate(strain_history):
        d_eps = target - eps_n # strain increment
        sigma, eps_p_n = return_mapping_perfect_plasticity(eps_n, d_eps, eps_p_n, E, sigma_y) # return mapping   
        
        # update variables
        eps_n += d_eps
        stress_history.append(sigma)
        plastic_strain_history.append(eps_p_n)
        print(f"#{id+1:2} - eps: {eps_n:.2e} | stress: {sigma:.2e} | eps_p: {eps_p_n:.2e}")
    
    #
    #   Post processing
    #
       
    ## Plot stress vs strain
    # Read in analytical data
    path = os.getcwd()
    path += "/code/week02/plast_analytical.csv"
    analytical_data = pd.read_csv(path)
    
    fig, ax = plt.subplots()

    ax.plot(analytical_data["eps_total"], analytical_data["sigma_true"], lw = 2, label = "Analytical")
    ax.plot(strain_history, stress_history,lw = 1, ls = '--', marker = 'o', label = "Python code")
    
    # Axis labels and styling
    ax.set_xlabel("Strain (mm/mm)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title("Stress evolution")
    ax.grid(alpha = 0.3)
    ax.legend()
    plt.show()

    fig.savefig("week02_perfect_plasticity.png")

    ## Plot plastic strain vs total strain
    fig2, ax2 = plt.subplots()
    ax2.plot(strain_history, plastic_strain_history)
    ax2.set_ylabel("plastic Strain (mm/mm)")
    ax2.set_xlabel("total strain (MPa)")
    ax2.set_title("Stress evolution")
    ax2.grid(alpha = 0.3)
    plt.show()

    fig2.savefig("week02_plastic_strain.png")

    ## Compute analytical vs algo error
    error = np.array(analytical_data["sigma_true"]) - np.array(stress_history)
    error = np.linalg.norm(error)
    print(f"Error: {error:.4e} ")

if __name__ == '__main__':
    test_perfect_plasticity()