# Week 02 - Analytical exercise and code report
## Analytical exercise
Consider a bar in tension with these material properties:
- E = 200 GPa
- $\sigma_{y}$= 250 MPa (constant)

| Iter | $\varepsilon^{total}$ | $\sigma^{trial}$ | f          | $\Delta\varepsilon^{p}$  | $\varepsilon^{p}$    | $\varepsilon^{e}$      | $\sigma^{true}$ |
| ---- | --------- | ----------- | ---------- | -------- | -------- | ---------- | ---------- |
| 1    | 0         | 0.00E+00    | \-2.50E+02 | 0.00E+00 | 0        | 0          | 0.00E+00   |
| 2    | 0.0002    | 4.00E+01    | \-2.10E+02 | 0.00E+00 | 0.00E+00 | 2.00E-04   | 4.00E+01   |
| 3    | 0.0004    | 8.00E+01    | \-1.70E+02 | 0.00E+00 | 0.00E+00 | 4.00E-04   | 8.00E+01   |
| 4    | 0.0006    | 1.20E+02    | \-1.30E+02 | 0.00E+00 | 0.00E+00 | 6.00E-04   | 1.20E+02   |
| 5    | 0.0008    | 1.60E+02    | \-9.00E+01 | 0.00E+00 | 0.00E+00 | 8.00E-04   | 1.60E+02   |
| 6    | 0.001     | 2.00E+02    | \-5.00E+01 | 0.00E+00 | 0.00E+00 | 1.00E-03   | 2.00E+02   |
| 7    | 0.0012    | 2.40E+02    | \-1.00E+01 | 0.00E+00 | 0.00E+00 | 1.20E-03   | 2.40E+02   |
| 8    | 0.0014    | 2.80E+02    | 3.00E+01   | 1.50E-04 | 1.50E-04 | 1.25E-03   | 2.50E+02   |
| 9    | 0.0016    | 2.90E+02    | 4.00E+01   | 2.00E-04 | 3.50E-04 | 1.25E-03   | 2.50E+02   |
| 10   | 0.0018    | 2.90E+02    | 4.00E+01   | 2.00E-04 | 5.50E-04 | 1.25E-03   | 2.50E+02   |
| 11   | 0.002     | 2.90E+02    | 4.00E+01   | 2.00E-04 | 7.50E-04 | 1.25E-03   | 2.50E+02   |
| 12   | 0.0018    | 2.10E+02    | \-4.00E+01 | 0.00E+00 | 7.50E-04 | 1.05E-03   | 2.10E+02   |
| 13   | 0.0016    | 1.70E+02    | \-8.00E+01 | 0.00E+00 | 7.50E-04 | 8.50E-04   | 1.70E+02   |
| 14   | 0.0014    | 1.30E+02    | \-1.20E+02 | 0.00E+00 | 7.50E-04 | 6.50E-04   | 1.30E+02   |
| 15   | 0.0012    | 9.00E+01    | \-1.60E+02 | 0.00E+00 | 7.50E-04 | 4.50E-04   | 9.00E+01   |
| 16   | 0.001     | 5.00E+01    | \-2.00E+02 | 0.00E+00 | 7.50E-04 | 2.50E-04   | 5.00E+01   |
| 17   | 0.0008    | 1.00E+01    | \-2.40E+02 | 0.00E+00 | 7.50E-04 | 5.00E-05   | 1.00E+01   |
| 18   | 0.0006    | 3.00E+01    | \-2.20E+02 | 0.00E+00 | 7.50E-04 | \-1.50E-04 | \-3.00E+01 |
| 19   | 0.0004    | 7.00E+01    | \-1.80E+02 | 0.00E+00 | 7.50E-04 | \-3.50E-04 | \-7.00E+01 |
| 20   | 0.0002    | 1.10E+02    | \-1.40E+02 | 0.00E+00 | 7.50E-04 | \-5.50E-04 | \-1.10E+02 |
| 21   | 0         | 1.50E+02    | \-1.00E+02 | 0.00E+00 | 7.50E-04 | \-7.50E-04 | \-1.50E+02 |
| 22   | 0.0003    | 9.00E+01    | \-1.60E+02 | 0.00E+00 | 7.50E-04 | \-4.50E-04 | \-9.00E+01 |
| 23   | 0.0006    | 3.00E+01    | \-2.20E+02 | 0.00E+00 | 7.50E-04 | \-1.50E-04 | \-3.00E+01 |
| 24   | 0.0009    | 3.00E+01    | \-2.20E+02 | 0.00E+00 | 7.50E-04 | 1.50E-04   | 3.00E+01   |
| 25   | 0.0012    | 9.00E+01    | \-1.60E+02 | 0.00E+00 | 7.50E-04 | 4.50E-04   | 9.00E+01   |
| 26   | 0.0015    | 1.50E+02    | \-1.00E+02 | 0.00E+00 | 7.50E-04 | 7.50E-04   | 1.50E+02   |
| 27   | 0.0018    | 2.10E+02    | \-4.00E+01 | 0.00E+00 | 7.50E-04 | 1.05E-03   | 2.10E+02   |
| 28   | 0.0021    | 2.70E+02    | 2.00E+01   | 1.00E-04 | 8.50E-04 | 1.25E-03   | 2.50E+02   |
| 29   | 0.0024    | 3.10E+02    | 6.00E+01   | 3.00E-04 | 1.15E-03 | 1.25E-03   | 2.50E+02   |
| 30   | 0.0027    | 3.10E+02    | 6.00E+01   | 3.00E-04 | 1.45E-03 | 1.25E-03   | 2.50E+02   |
| 31   | 0.003     | 3.10E+02    | 6.00E+01   | 3.00E-04 | 1.75E-03 | 1.25E-03   | 2.50E+02   |

- We can see that yielding occurs for the first time at $\varepsilon=0.0014$ where the trial stress is $280 MPa$ initially (Then corrected to $\sigma_{y}=250 MPa$)
- The final plastic strain at $\varepsilon=0.002$ (first loading sequence) is equal to $\varepsilon^{p}=7.5\cdot10^{-4}$
- The residual stress at complete unload is $\sigma = -150 MPa$
- When reloading to $\varepsilon=0.003$, we induce even more plastic deformation, this shows in the $\varepsilon^{p} vs \varepsilon$ plot

## Code report - Perfect plasticity

The results from the code, wich works with incremental loading, is in good agreement with the analytical exercice wich is in total strain formulation. In  fact, the result is identical, which is what was expected:
| Iter | $\varepsilon^{total}$ | $\sigma^{true}$ | $\varepsilon^{p}$   |
| --------- | -------- | ---------- | ----------- |
| 1         | 0.00E+00 | 0.00E+00   | 0.00E+00    |
| 2         | 2.00E-04 | 4.00E+01   | 0.00E+00    |
| 3         | 4.00E-04 | 8.00E+01   | 0.00E+00    |
| 4         | 6.00E-04 | 1.20E+02   | 0.00E+00    |
| 5         | 8.00E-04 | 1.60E+02   | 0.00E+00    |
| 6         | 1.00E-03 | 2.00E+02   | 0.00E+00    |
| 7         | 1.20E-03 | 2.40E+02   | 0.00E+00    |
| 8         | 1.40E-03 | 2.50E+02   | 1.50E-04    |
| 9         | 1.60E-03 | 2.50E+02   | 3.50E-04    |
| 10        | 1.80E-03 | 2.50E+02   | 5.50E-04    |
| 11        | 2.00E-03 | 2.50E+02   | 7.50E-04    |
| 12        | 1.80E-03 | 2.10E+02   | 7.50E-04    |
| 13        | 1.60E-03 | 1.70E+02   | 7.50E-04    |
| 14        | 1.40E-03 | 1.30E+02   | 7.50E-04    |
| 15        | 1.20E-03 | 9.00E+01   | 7.50E-04    |
| 16        | 1.00E-03 | 5.00E+01   | 7.50E-04    |
| 17        | 8.00E-04 | 1.00E+01   | 7.50E-04    |
| 18        | 6.00E-04 | \-3.00E+01 | 7.50E-04    |
| 19        | 4.00E-04 | \-7.00E+01 | 7.50E-04    |
| 20        | 2.00E-04 | \-1.10E+02 | 7.50E-04    |
| 21        | 0.00E+00 | \-1.50E+02 | 7.50E-04    |
| 22        | 3.00E-04 | \-9.00E+01 | 7.50E-04    |
| 23        | 6.00E-04 | \-3.00E+01 | 7.50E-04    |
| 24        | 9.00E-04 | 3.00E+01   | 7.50E-04    |
| 25        | 1.20E-03 | 9.00E+01   | 7.50E-04    |
| 26        | 1.50E-03 | 1.50E+02   | 7.50E-04    |
| 27        | 1.80E-03 | 2.10E+02   | 7.50E-04    |
| 28        | 2.10E-03 | 2.50E+02   | 8.50E-04    |
| 29        | 2.40E-03 | 2.50E+02   | 1.15E-03    |
| 30        | 2.70E-03 | 2.50E+02   | 1.45E-03    |
| 31        | 3.00E-03 | 2.50E+02   | 1.75E-03    |

### Observations
- The norm of the error vector $||e||=||e_{analytical} - e_{algorithm}||=6.2045\cdot10^{-14}$ which is largely under 0.1% error, near machine precision. This result is expected since the problem is really simple and the calculation is basically the same. The only thing interesting is that it shows that the total strain vs incremental strain approach gives the same result.
- The plot (week02_perfect_plasticity.png) shows that the analytical line overlays the result from the algorithm:
  
![image](../../code/week02/week02_perfect_plasticity.png)
- The plastic strain increase function of total strain shows the two plateaus where initial loading and the unloading phase occur:
  
![image](../../code/week02/week02_plastic_strain.png)

