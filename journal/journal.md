# GPU accelerated ROM framework for viscoplastic models
\table

```
Daily (2-3 sentences):

"Worked on mesh generation. Indexing was confusing at first but figured it out."
"Read Dunne Ch 1. Yield surface concept makes sense now."
"Convergence plot shows O(h²) - matches theory!"

Weekly reflection:

What worked well?
What was frustrating?
Interesting observations?
Questions for next meeting?
```

## Week 1: 2025-10-21 - 2025-10-26
### 2025-10-26:
- Completing the code assignment for linear element.
- The error plot seems off but the error is so small that it seems like a round off error.
- The displacement seems to be almost if not equal to the theoretical displaceent

### 2025-10-22:
- Worked on the code assignement for simple bar finite element code. Trouble getting it to run using the elemental integration and not the analitical itnegratin. Using analytical integration would be way easier and I should simply compute E*A/L[1,-1;-1,1] for each element, but I prefer working with elemental definition since most of other elements are dificult to directly integrate
- Meshing seems to work for 2nd order but node generation is not working for 1st order

### 2025-10-22:
- Completed lecture on Dunn (Introduciton to computational plasticity) and lecture on Simo (Computational inelasticity).
- The book by Simo seems a bit more difficult to grasp, because of the maths.
- The book by Dunn is quite straight forward but the one by Simo takes me a bit more time to read and to grasp. Will have to read it one more time to fully grasps the concepts.
- Start working on the python code assignement

### 2022-10-21: Day 1
- Defined the scope with Claude
- Refined the subject to ***GPU accelerated framework for hyper reduced viscoplastic models***
- Created developper environement
- Got required ressources: S&H Computationnal Inelasticity and Dunn Computational Plasticity
- Started reading Dunn, added the first chapter on microplasticity to better understand the mechanism of slip and dislocation.