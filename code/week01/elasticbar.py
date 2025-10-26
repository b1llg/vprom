from femutils import *
import numpy as np
import matplotlib.pyplot as plt


n_elements_vec = [1,2,5,10,100,1000,10000]
errors = []
hs = []

for n_elements in n_elements_vec:
    # define problems constant
    L = 1               # lenght of bar
    E = 2e11            # Young's modulus - Pa
    D = 0.1             # Diameter - m
    A = np.pi/4 * D**2  # Surface area in traction - m**2
    F = 100e3           # Force - N

    # generated nodes and elements
    nodes, elements = generate_mesh(L, n_elements)

    # Append h to h_vectors
    hs.append(nodes[1] - nodes[0])

    # Assemble matrix
    Ak, bf = assemble_stiffness(nodes, elements, E, A, qp=3)
    # print("Ak: ")
    # print(Ak)


    # Define two array with this notation (list of list):
    # [dofs id (node id in this particular cas), node/dofs value]
    disps = [[0, 0]]
    loads = [[elements[-1,-1], F]]

    # Dictionnary of dofs
    boundaries = {"disps" : disps, "loads" : loads}

    Ak, bf = apply_bc(Ak, bf, boundaries)

    u = solve(Ak, bf)

    stress, strain, total_disp = post_process(nodes, u, E)

    error = l2_error(nodes, u, E, A, F, L)
    errors.append(error)

    print(f"L2 error for {n_elements} : ", error)

fig, ax = plt.subplots()

ax.plot(hs, errors)
ax.set_xlabel("Element size (m)")
ax.set_ylabel("L2 error")