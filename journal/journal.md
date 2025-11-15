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
## Week 3: 25-11-03 - 25-11-19

### 2025-11-14:
- Worked on the derivation of the Perzyna model with a general approach. Things makes a bit more sense now however when going non linear ($n\neq1$) it requires a bit more thinking. (about 3hr)
- Worked on the code using the help of Claude. 

### 2025-11-10:
- Reading and analytic derivation from Simo textbook. Very high level (about 1hr)

### 2025-11-09:
- Had to postpone the submission for week 03. I'm not at ease with the subject and it bugs me. Might take the day off and start back tomorrow.

### 2025-11-08:
- Reworked the return mapping algorithm. Some thing is way off and I'm having trouble to identify what it is. Will def. need to read Simo, Dunn and Crisfield. Still haven't found what is the bug. Had to asked Claude, now at least I know that I was not wrong, the algorithm return maps correcly, It might be in the code. There is maybe something still off with the creep test (constant stress, strain driven. Quite weird to do). About 2hrs

### 2025-11-06:
- Updated rate sensitivity, creep and relaxation test. Some things look off. About 2hrs

### 2025-11-05:
- Did some test with strain rate and creep test. I wasn't sure that the strain rate sensitivity test was right so I did the creep test. Creep test results made sense so Im pretty sure that the results for rate sensitivity are now sane. Maybe that the combination of rates not so high with a somewhat neutral viscosity make the results look not too different from a non viscoplastic material. There is a change in stress though that confirms this, but visually it is not so evident. About 2hrs

### 2025-11-04:
- Started the coding assignement. Rate sensivity in about 2hr
- The peak stress doesnt seem to high. Something might be off
- Need to find a way to set constant stress

### 2025-11-03:
- Started the reading assignement. About 1hr

### 2025-11-02:
- Read both required chapters in Simo and Dunn. About 2hrs.

## Week 2: 2025-10-27 - 2025-11-02
### 2025-11-02:
- Completed reading assignment. 

### 2025-11-01:
- Finalized code and report assignment for the codes
- Started to fill the submission form
  
### 2025-10-31:
- Completed perfect plasticity code.
- Validated analytical vs code exercise

### 2025-10-29:
- Completed the analytical assignement. Had trouble finding the plastic corrector, needed help from Claude
- Worked on the plasticity_1d_perfect.py assignement. Stress history seems wrong (not unloading). Will check that tomorrow

### 2025-10-28:
- Installed Trilinos. Might be a good idea to use rather than MFEM for later in the project. It looks like very complex however.
- An idea could be to start with MFEM+libCEED/libROM and then create custom kernels/Framework with Trilinos once MFEM/libROM can't handle the work.
- I'd like to get rid of Python once working with 2d/3d problems. Might be a good idea to either work on a 1d problem with mfem next week.

### 2025-10-27:
- Started pseudo reading Simo and Dunn. I need to take my time and write the equations while reading because there is to much math to keep it all in my head.
- Started to install MFEM and make some tests. Might be a good idea to use it soon

## Week 1: 2025-10-21 - 2025-10-26
### Recap:
- After reading theory. Things started to make sense. Some stuff was seen a while ago, it was a good reminder.
- The coding assignement was also a good reminder of FE theory. Maybe need a refresher on that. 
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