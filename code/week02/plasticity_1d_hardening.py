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
    # TODO: Compute total strain at step n+1
    
    # TODO: Compute current yield stress: sigma_y = sigma_y0 + H * alpha_n
    
    # TODO: Elastic predictor - compute trial stress
    
    # TODO: Check yield condition (f_trial)
    
    # TODO: If elastic (f_trial <= 0):
    #       - sigma = sigma_trial
    #       - eps_p = eps_p_n (no change)
    #       - alpha = alpha_n (no change)
    
    # TODO: If plastic (f_trial > 0):
    #       - Compute plastic multiplier: d_lambda = f_trial / (E + H)
    #       - sigma = (sigma_y + H * d_lambda) * sign(sigma_trial)
    #       - eps_p = eps_p_n + d_lambda * sign(sigma_trial)
    #       - alpha = alpha_n + d_lambda
    
    pass

def test_hardening_comparison():
    """Parameter study: H = 0, 1 GPa, 5 GPa"""
    
    # Material properties
    E = 200e9  # Pa
    sigma_y0 = 250e6  # Pa
    H_values = [0, 1e9, 5e9]  # Pa
    
    # Same loading history as Assignment 2.3
    strain_load = np.linspace(0, 0.002, 11)
    strain_unload = np.linspace(0.002, 0, 11)[1:]
    strain_reload = np.linspace(0, 0.003, 11)[1:]
    strain_history = np.concatenate([strain_load, strain_unload, strain_reload])
    
    # TODO: For each H value:
    #       - Initialize state (eps_n=0, eps_p_n=0, alpha_n=0)
    #       - Run time integration loop
    #       - Store stress history
    
    # TODO: Plot all three curves on same figure
    #       - Label: "H = 0 (perfect)", "H = 1 GPa", "H = 5 GPa"
    #       - Save as 'week02_hardening_comparison.png'
    
    # TODO: Write analysis document answering:
    #       - How does H affect loading curve?
    #       - How does H affect unloading?
    #       - Residual stress for each case?
    #       - Physical explanation?
    
    pass

if __name__ == '__main__':
    test_hardening_comparison()