"""
Simple fem functionnality to solve the elastic bar problem
"""
import numpy as np

def generate_mesh(L: float, n_elements: int, order:int):
    """
    Takes L and n_element.
    Returns a nodes and elements table
    """
    
    # Initialize variables
    # Here, since its in 1d we can take advantage of the fact that all elements
    # will be in line and that the spacing, for now will be constant.
    n_nodes_per_elements = order + 1 
    n_nodes = 2*n_elements + 1
    
    dx = L/(n_elements * order)

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

def assemble_stiffness(nodes: np.ndarray, elements : np.ndarray, order : int, E : float, A : float, qp=3):
    '''
    Takes nodes, elements, order and material property to compute each element rigidity.

    An optional argument 'qp=3' is used to define the number of integration points which is 3 by default.

    return A and b in Au=b
    '''
    # Initialize global stiffness matrix and load vector
    # define variables for element stiffness
    n_dof_per_node = 1 # for this physics, i.e. bar in traction.
    n_nodes_per_elements = order + 1
    n_dof_per_element = n_dof_per_node * n_nodes_per_elements
    n_elements = elements.shape[0]
    n_dofs = n_elements * n_dof_per_element

    

    Ak = np.zeros((n_dofs, n_dofs))
    bf = np.zeros(n_dofs) # since boundary conditions are treated later on, will
    # be returned as is


   

    # Loop on elements
    for i in range(elements.shape[0]):

        # Get element length
        n1 = elements[i,0]
        n2 = elements[i,order] # last node is stored as last entry in elements

        lk = nodes[n2] - nodes[n1]

        # jacobian and inverse jacobian
        jac = lk/2
        inv_jac = 2/lk

        # lambda for the shape/test function and their derivative
        if order == 1:
            psi = lambda ksi: 0.5*np.array([1-ksi, 1+ksi])
            dpsi = lambda ksi: 0.5*np.array([-1,1]) 
        elif order == 2:
            psi = lambda ksi: 0.5*np.array([-ksi*(1-ksi), 2*(1-ksi**2), ksi*(1+ksi)])
            dpsi = lambda ksi: 0.5*np.array([-1+2*ksi, -4*ksi, 1+2*ksi])
        else:
            raise(ValueError(f"gp invalid"))

        # Initialize elemental  and load vector
        aij = np.zeros((n_nodes_per_elements, n_dof_per_element))
        
        ksi, wi = np.polynomial.legendre.leggauss(qp)

        for j in range(qp):
            aij += wi[j]*np.outer(dpsi(ksi[j]), dpsi(ksi[j]))
        
        print("aij: ", aij)

        aij *= E*A/lk

        # Assign aij dof to global stiffness matrix
        for j in range(n_dof_per_element):
            for k in range(n_dof_per_element):
                Ak[elements[i,j],k] = aij[j,k] # Here, elements[i] gives the node number but also the dof number
                #! WIP

    return Ak, bf


def apply_bc(K, f, bc_dict):
    # Apply boundary conditions
    pass

def solve(K, f):
    # Solve Ku = f
    pass

def post_process(nodes, u, E):
    # Calculate strain, stress
    # Plot results
    pass

def main():
    print("Running main")

if __name__ == "__main__":
    main()