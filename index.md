---
layout: default
---

# MolClustPy:  Python Package to analyze com-position of multivalent biomolecular clusters 

Interactions among multi-valent molecules are known to result in polymeric structures - large molecular clusters consisting of hundreds to thousands of connected molecules. When the affinities of the individual molecular interactions are relatively weak, multivalent clusters maintain their integrity but allow various molecular compositions (Mayer et al, 2009), so multiple simulation runs are required to determine the average behavior of such bimolecular system. <b>MolClustPy</b> is a Python package to perform multiple stochastic simulation runs using NFSim (Network-Free stochastic simulator, ) and characterize distribution of cluster sizes, molecular composition, and bonds across molecular clusters and individual molecules of different types. 

# Input: rule-based model specification in BioNetGen Language (BNGL) format

Such systems require a special kind of modeling technique called Rule based modeling (RBM) (Blinov et al., 2004). In this approach, a molecule is modelled as an object with multiple sites.  

![image](images/molecules.png | width = 600)


Here 

A set of rules then specifies the interactions among molecules.



