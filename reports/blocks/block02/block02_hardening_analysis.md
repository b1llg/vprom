## Code report - Hardening comparison

Below is the output from the isotropic hardening test, where multiple values of H are compared to each other to find out what is the effect on the stress vs strain curve:

![image](../../code/week02/week02_hardening_comparison.png)

Initially, only $H = [0, 1, 5] GPa$ was requested. I added $H=50GPa$ to show the effect on hardening

### Effect on loading curve
#### How does H change the stress-strain response during loading?
Because hardening increases yield stress. Meaning that for an increase in strain, the stress value has to be higher for and an higher value of H if the increase of strain is positive. The same goes if the increase of strain is negative (compression).
#### Why does stress continue increasing beyond σ_y0?
Because of hardening. The hardening law is says that for an increase of $\epsilon^{p}$, $\sigma_{y}$ must increase proportional to parameter $H$


### Effect on unloading:

#### How does H affect the unloading path?
For a given strain path, considering that the increase of strain is such that the unloading causes additional plastic strains, the unloading path distance from the loading path will get closer. Meaning that that elastic portion of the path (line with a slope equal to the Young's modulus) for loading and unloading will be closer. This can be seen in the above picture where we can assume that the "circular motion" of the loading path make it look like that the Higher H gets, the smalle the "circle" gets.

#### Is unloading always elastic? Why?
No, because it depends on how much plastic strain as been accumulated. For Example, as long as a loading is beyond yield stress, we could do as many cycles as we want and no plastic strain would be accumulated. In this case, the loading is such that on every loading and unloading, the plastic strian increase.


### Residual stress:

#### What is the stress at ε = 0 after complete unload for each H?
All of them are at 0 at the begining, the residual stress appears at the complete unload
| H (GPa) | $\sigma_{true}$ (MPa)|
|:---:|:----------------:|
|0 | 250  |
|1 | 252.37  |
|5 | 261.46  |
|50 | 341.97  |

It is clear that the residual stress gets higher with an higher value of $H$
#### Why is there residual stress (or lack thereof)?
In all those cases, there was residual stress. The reason is that, as explained before, accumulated plastic strain will induce residual stress when unloading in such a way that stress below 0 are induced in the element. 

### Reloading behavior:

#### When does re-yielding occur for each case?
For each case, re-yielding occurs when the stress induced by the strain controlled displacement is such that the plastic strain increase.
#### How does the accumulated hardening affect this?
The more accumulated hardening (accumulated plastic strain) the higher the new yield limit becomes.


### Physical interpretation:

#### Explain physically what isotropic hardening represents
Isotropic hardening means that when yielding occurs, the yield surface needs to expand in such a way that the yield criterion $f=0$. Also, that expansion needs to follow the vector normal to the yield surface, at that location.
#### Why does larger H make the material "stiffer" during plastic flow?
Because of the same reason explained in a previous question. Increased plastic strain directly increase the yield stress, raising the stress significantly to match the increase in total strain.
