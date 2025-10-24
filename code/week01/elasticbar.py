from femutils import *

# define problems constant
order = 1       # Trial/Test function order. Ritz-Galerkin -> trial = test function
L = 1           # lenght of bar
E = 2e11        # Young's modulus - Pa
A = 1           # Surface area in traction - m**2
n_elements = 1  # Number of elements

# generated nodes and elements
nodes, elements = generate_mesh(L, n_elements, order)
print("Nodes: ", nodes)
print("Problem, works only for second order, check node generation")
print("Elements: ", elements)

# Assemble matrix
Ak, bf = assemble_stiffness(nodes, elements, order, E, A)

