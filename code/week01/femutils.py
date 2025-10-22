import numpy as np

def generate_mesh(L, n_elements):
    # Return nodes, elements
    n_nodes = n_elements + 1
    n_nodes_per_elements = 2 # linear element
    dx = L/n_elements

    nodes = np.arange(0,L,dx)
    elements = np.zeros((n_elements,n_nodes_per_elements))

    node_count = 0
    for i in range(n_elements):
        elements[i,0] = node_count
        node_count += 1
        elements[i,1] = node_count
    
    return nodes, elements

def assemble_stiffness(nodes, elements, E, A):
    # Return global K matrix
    pass

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