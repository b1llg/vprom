"""
Simple fem functionnality to solve the elastic bar problem
"""
import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import splu

def generate_mesh(L: float, n_elements: int):
    """
    Takes L and n_element.
    Returns a nodes and elements table
    """
    
    # Initialize variables
    # Here, since its in 1d we can take advantage of the fact that all elements
    # will be in line and that the spacing, for now will be constant.
    n_nodes_per_elements = 2
    n_nodes = n_elements + 1
    
    dx = L/(n_elements)

    # Initialize tables
    nodes = np.zeros((n_nodes))

    for i in range(1,n_nodes):
        nodes[i] = nodes[i-1] + dx 
    

    # For elements, assign node numbers to each element. Straightforward
    elements = np.zeros((n_elements,n_nodes_per_elements)).astype(int)
    node_count = 0
    for i in range(n_elements):
        for j in range(n_nodes_per_elements):
            elements[i,j] = node_count
            if j!= n_nodes_per_elements - 1:
                node_count += 1
    
    return nodes, elements

def assemble_stiffness(nodes: np.ndarray, elements : np.ndarray, E : float, A : float, qp=3):
    '''
    Takes nodes, elements, order and material property to compute each element rigidity.

    An optional argument 'qp=3' is used to define the number of integration points which is 3 by default.

    return A and b in Au=b
    '''
    #! >>> Parameters to be defined. Linear element, 1d physic (ie bar in traction)
    n_dof_per_node = 1 
    n_node_per_element = 2
    psi = lambda ksi: 0.5*np.array([1-ksi, 1+ksi])
    dpsi = lambda ksi: 0.5*np.array([-1,1])
    # jacobian and inverse jacobian
    jac = lambda lk : lk/2
    inv_jac = lambda lk : 2/lk 

    #! <<< end of parameter definition

    # Computed parameters
    n_dof_per_element = n_dof_per_node * n_node_per_element
    n_nodes = nodes.shape[0]
    n_dofs = n_nodes * n_dof_per_node
    
    # Initialize global stiffness matrix and load vector
    # define variables for element stiffness
    Ak = np.zeros((n_dofs, n_dofs))
    bf = np.zeros(n_dofs) # since boundary conditions are treated later on, will
    # be returned as is, simply initialized
  

    # Loop on elements
    for i in range(elements.shape[0]):

        # Get element length
        n1 = elements[i,0]
        n2 = elements[i,1] # last node is stored as last entry in elements

        lk = nodes[n2] - nodes[n1]

        # Initialize elemental  and load vector
        aij = np.zeros((n_dof_per_element, n_dof_per_element))
        
        ksi, wi = np.polynomial.legendre.leggauss(qp)

        for j in range(qp):
            # Integration of the weak form using gauss quadrature
            aij += 2*wi[j]*np.outer(dpsi(ksi[j]), dpsi(ksi[j]))*jac(lk)*inv_jac(lk)

        aij *= E*A/lk # Multiply by the constant term, could be made using a lambda if f(x)

        # Assembly of aij into global stiffness matrix
        dofs = elements[i]
        for j in range(n_dof_per_element):
            for k in range(n_dof_per_element):
                Ak[dofs[j], dofs[k]] += aij[j,k] # Here, elements[i] gives the node number but also the dof number
    
    
    return Ak, bf

def apply_bc(K, f, bc_dict):
    '''
        Apply boundary conditions to linear system of equation.
        K: Stiffness matrix
        f: load vector
        bc_dict: Dictionnary containing boundary conditions
    '''
    # Few sanity checks
    disp_applied = True
    if len(bc_dict["disps"]) < 1: # Contains at least one dicplacement condition
        raise Warning("No displacement bc applied (Dirichlet). Solution might be unstable")
        disp_applied = False
    
    if disp_applied:
        no_fixed_condition = True # Check that at least one node is fixed

        for bc in bc_dict["disps"]:
            disp_condition = bc[1]
            if disp_condition == 0:
                no_fixed_condition = False
                break
        
        if no_fixed_condition:
            raise Warning("Displacement condition applied but no fixed condition applied. System might be unstable")
        
    if (len(bc_dict["loads"]) >0):
        contain_loads = True
    else:
        contain_loads = False

    if not(contain_loads) and not(disp_applied):
        raise ValueError("No conditions applied. Check model input")

    # loop over loads first
    for load in bc_dict["loads"]:
        # Get dof id
        dof_id = int(load[0])
        value = load[1]

        # apply load
        f[dof_id] = value

    for disp in bc_dict["disps"]:
        # get dof id
        dof_id = int(disp[0])
        value = disp[1]

        # zero out stiffness entry
        K[dof_id] = 0

        # set dof to 1
        K[dof_id, dof_id] = 1

        # assign value in reaction vector
        f[dof_id] = value
    
    return K, f

def solve(K, f):
    '''
    Solve linear system and return unknown using lu solver:
    K: Stiffness matrix
    f: load vector

    return unknown (displacement)
    '''
    cscK = csc_matrix(K)
    lu = splu(cscK)

    try:
        x = lu.solve(f)
        return x
    except:
        raise ValueError("Unable to solve sparse linear system")


def post_process(nodes, u, E):
    '''
    Compute stress, strain, total displacement
    nodes: nodes position
    u: displaceent at nodes
    E: Youngs modules to compute stress
    '''

    strain = u[-1] / (nodes[-1] - nodes[0]) # Total displacement over length
    stress = E*strain

    return stress, strain, u[-1]

def l2_error(nodes, u, E, A, F, L):
    '''
    Compute the L2 norm to determine the error related to the model comparated to the analytical solution
    nodes: node position vector. Only applicable if load is applied at end and fixed at the opposite.
    u: result vector
    E: Youngs modulus
    A: Surface area
    F: Load at end
    L: length of the bar

    returns: L2 error
    '''
    u_analytical = lambda x : F*x/(A*E) # Analytical formula for the displacement along x

    u_theo = u_analytical(nodes) # Compute analytical value

    du = (u_theo - u)**2 # Compute the squared difference between analytical and fem

    return np.trapezoid(du, nodes) # Integrate along lengt and return -> L2 error



def main():
    print("Running main")

if __name__ == "__main__":
    main()