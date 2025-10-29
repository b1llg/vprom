import numpy as np
import matplotlib.pyplot as plt

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
    # Elastic predictor
    sigma_e = E*(eps_n + d_eps)

    f = np.abs(sigma_e) - sigma_y # simo 2.2.37

    # Check yield condition
    if f <= 0: # elastic case
        return sigma_e, eps_p_n
    else: # f > 0 compute plastic corrector
        df_dsigma = np.sign(sigma_e)
        gamma = df_dsigma*d_eps
        d_eps_p = gamma * df_dsigma

        return sigma_y, eps_p_n + d_eps_p

def test_perfect_plasticity():
    """Test against analytical solution from Assignment 2.2"""
    
    # Material properties
    E = 200e9  # Pa
    sigma_y = 250e6  # Pa
    
    # Loading history: Load -> Unload -> Reload
    strain_load = np.linspace(0, 0.002, 11)
    strain_unload = np.linspace(0.002, 0, 11)[1:]
    strain_reload = np.linspace(0, 0.003, 11)[1:]
    strain_history = np.concatenate([strain_load, strain_unload, strain_reload])
    
    # Initialize storage
    stress_history = []
    plastic_strain_history = []
    
    # Initialize state
    eps_n = 0.0
    eps_p_n = 0.0
    

    #for each target strain in strain_history:
    for target in strain_history:
        d_eps = target - eps_n # strain increment
        sigma, epsp_n = return_mapping_perfect_plasticity(eps_n, d_eps, eps_p_n, E, sigma_y) # return mapping   
        
        # update variables
        stress_history.append(sigma)
        plastic_strain_history.append(sigma)
    
    # TODO: Convert to numpy arrays: why?
    
    # TODO: Plot stress-strain curve
    fig, ax = plt.subplots()
    ax.plot(strain_history, stress_history)
    ax.set_xlabel("Total Strain")
    ax.set_ylabel("Stress")
    fig.savefig("stress_history.png")

    # yield_array = np.ones((strain_history.size))

    # ax.hlines(yield_array, 0, np.max(strain_history))

    #       - Compare to analytical from Assignment 2.2
    #       - Mark yield stress with horizontal line
    #       - Save as 'week02_perfect_plasticity.png'
    
    # TODO: Plot plastic strain evolution
    #       - Save as 'week02_plastic_strain.png'
    
    pass

if __name__ == '__main__':
    test_perfect_plasticity()