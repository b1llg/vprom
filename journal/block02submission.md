# Week 2 Check-in

## Deliverables (Raw GitHub URLs):

**Assignment 2.1 - Theory:**
https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/reports/weekly/week02_return-mapping-theory.md
return mapping figure: https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/reports/weekly/returnmapping_figure.png


**Assignment 2.2 - Analytical:**
https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/reports/weekly/week02_analytical_ecercise.md

**Assignment 2.3 - Perfect Plasticity Code:**
https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/code/week02/plasticity_1d_perfect.py
stress figure: https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/code/week02/week02_perfect_plasticity.png
plastic strain figure: https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/code/week02/week02_plastic_strain.png

**Assignment 2.4 - Hardening Code:**
https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/code/week02/plasticity_1d_hardening.py
figure: https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/code/week02/week02_hardening_comparison.png

**Assignment 2.4 - Hardening Analysis:**
https://raw.githubusercontent.com/b1llg/vprom/refs/heads/main/reports/weekly/week02_hardening_analysis.md

**Journal:**
https://raw.githubusercontent.com/b1llg/vprom/main/journal/journal.md

**Plots:**
- See figures above

## Summary
- Completed the code assignements and it helped me a lot. The theory makes a lot more sense now
- The analytical exercice wich fits with the algorithm version with strain increment is really nice to see.
- The reading assignement has been done at the end. Doing the applications first made it easier to understand

## Key Results

**From Assignment 2.2 (Analytical):**
- First yield occurred at: ε = 0.0014
- Final plastic strain after loading: εᵖ = 1.75E-03
- Stress at complete unload: σ = -150 MPa

**From Assignment 2.3 (Validation):**
- Maximum error vs analytical: $||e||=||e_{analytical} - e_{algorithm}||=6.2045\cdot10^{-14}$
- Behavior verified: yes

**From Assignment 2.4 (Parameter study):**
- H=0: Final stress at ε=0.003: 250 MPa
- H=1GPa: Final stress at ε=0.003: 254.26 MPa
- H=5GPa: Final stress at ε=0.003: 270.76 MPa
- H=50GPa: Final stress at ε=0.003: 409.38 MPa


## Code Snippet for Review
- See links above

## Questions/Issues
- Difference between $\varepsilon^{p}$ and $\alpha$

## Time Spent
Total: approx. 25 hours

The time given this week is somehow near your estimate, but it needs to be shorter each week. It needs to be close to 12 hours, at most 15 hours.