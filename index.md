---
layout: default
---

# MolClustPy

## Python package to analyze composition of multivalent biomolecular clusters 

Interactions among multi-valent molecules are known to result in polymeric structures - large molecular clusters consisting of hundreds to thousands of connected molecules. When the affinities of the individual molecular interactions are relatively weak, multivalent clusters maintain their integrity but allow various molecular compositions (Mayer et al, 2009), so multiple simulation runs are required to determine the average behavior of such bimolecular system. <b>MolClustPy</b> is a Python package to perform multiple stochastic simulation runs using NFSim (Network-Free stochastic simulator, ) and characterize distribution of cluster sizes, molecular composition, and bonds across molecular clusters and individual molecules of different types. 

## Input: rule-based model specification in BioNetGen Language (BNGL) format

Such systems require a special kind of modeling technique called Rule based modeling (RBM) (Blinov et al., 2004). In this approach, a molecule is modelled as an object with multiple sites.  

<table>
  <tr>
    <td><img src="images/molecules.png" width=300></td>
    <td>  ```python
Nsk(SH2,s1,s2,s3)
Nephrin(Y1,Y2,Y3)
NWasp(p1,p2,p3,p4,p5,p6)
```</td>
  </tr>
 </table>
<img src="images/molecules.png" width=300>

Here Nck has 4 binding sites - one SH2 and three SH3 (called s1, s2, s3); Nephrin has three tyrosine binfing sites Y1, Y2 and Y3; and N-Wasp has 6 PRM binding sites coded p1, p2, ..p6.

In BNGL notations these three molecules would be defined as
```python
Nsk(SH2,s1,s2,s3)
Nephrin(Y1,Y2,Y3)
NWasp(p1,p2,p3,p4,p5,p6)
```

A set of rules then specifies the interactions among molecules.
<table>
  <tr>
    <td><img src="images/rule1.png" width=250></td>
    <td>  <img src="images/rule2.png" width=150></td>
  </tr>
 </table>

Here we show two example of rules

Finally, the essential part of model specification is the observables - the pattern that specify properties of molecular complexes we'd like to track. 


## Output: visual characterization of molecular clusters composition


