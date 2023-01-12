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
    <td>  <tt>
Nck(SH2,s1,s2,s3)<br>
Nephrin(Y1,Y2,Y3)<br>
NWasp(p1,p2,p3,p4,p5,p6)
      </tt></td>
  </tr>
 </table>

Here on the left we show visaulization of molecules in VCell notations (Blinov et al., 2016): Nck has 4 binding sites - one SH2 and three SH3 (called s1, s2, s3); Nephrin has three tyrosine binfing sites Y1, Y2 and Y3; and N-Wasp has 6 PRM binding sites coded p1, p2, ..p6. On the right we show how these molecules are defined in BNGL notations.


A set of rules then specifies the interactions among molecules.
<table>
  <tr>
    <td><img src="images/rule1.png" width=470></td>
    <td><img src="images/rule2.png" width=420></td>
  </tr>
 </table>

Here we show two example of rules: on the left is binding of Nck to NWasp via interaction of s1 site with p1. On the right is binding of Nephrin to Nck via interaction of Y1 site of Nephrin with SH2 domain of Nck. The full set of rules consists of 18 rules of the first type (6x3) and 3 rules of the second type (1x3). Below are the same rules written in BNGL notations. kon and koff are on and off rate constants for mass-action kinetic law - default kinetic law in BioNetGen.
```code
Nck(s1) + NWASP(p1) <-> Nck(S1!1).NWASP(p1!1)		        kon_23, koff_23
Nephrin(pY1) + Nck(Sh2) <-> Nephrin(pY1!1).Nck(Sh2!1)		kon_12, koff_12
```

Finally, the essential part of model specification is the observables - the pattern that specify properties of molecular complexes we'd like to track. Below are three observables - free Nephrin (no site is bound), fully bound Nephrin (all sites are bound), and a comples of Nick and NWasp with undefined connectivity. Underneath are the same observables written in BNGL notations.

<table>
  <tr>
    <td><img src="images/nep-f.png" width=200></td>
    <td><img src="images/nep-b.png" width=200></td>
    <td><img src="images/nw.png" width=400></td>
  </tr>
 </table>
 ```code
Molecules free_Nephrin Nephrin(pY1,pY2,pY3)
Molecules fully_bound_Nephrin Nephrin(pY1!+,pY2!+,pY3!+)
Molecules cluster_nck_nw Nck().NWASP()
```

## Output: visual characterization of molecular clusters composition


