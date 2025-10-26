# Elastic_bar_1d.py
Simple code to solve the bar in traction problem

## Parameters
User need to supply the material properties (E, A, L) and element size parameters
(See 'generate_mesh' and 'assemble_stiffness' in femutils.py)

## Problem
The problem stated in the elastic_bar_1d.py file solve for different element size the bar in traction problem.
The L2 error is computed for each element size and the error graph is ploted.

## Results
Since the pde is easy to integrate, the solution is linear. Thus, the finite element implementation error is really small and the l2 error seems so small that the convergence graph makes no sense.