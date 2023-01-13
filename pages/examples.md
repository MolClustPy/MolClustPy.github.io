---
title: Examples
layout: default
permalink: examples
---

# Examples of package usage

### Nephrin-Nck-NWasp clustering under low concentration
 
This example has low concentrations of molecules coresponding to 100 molecules of  Nephrin, 300 Nck and 150 NWasp. The MolClustPy calculations demonstrate that the cluster distribution for this concentration is linear, with most clusters of low number of molecules and some rare large clusters. 

<img src="/images/aco_low.png" width=300>

- [Jupyter notebook](/notebooks/Tutorial_Nephrin_Nck_NWASP.ipynb)
- [Web-page describing notebook](https://github.com/achattaraj/MolClustPy/blob/master/Tutorial_Nephrin_Nck_NWASP.ipynb)
- [Python code](/notebooks/Tutorial_Nephrin_Nck_NWASP.py)
- [BNGL code](/notebooks/Tutorial_Nephrin_Nck_NWASP.bngl)


### Nephrin-Nck-NWASP clustering with high_concentration

This example has high concentrations of molecules coresponding to 300 molecules of Nephrin, 900 Nck and 450 NWasp. The MolClustPy calculations demonstrate that the cluster distribution for this concentration is bimodal, with most molecules in either small or very big clusters. 

<img src="/images/aco_high.png" width=300>

- [Jupyter notebook](/notebooks/Nephrin_Nck_NWASP_high_concentration.ipynb)
- [Web-page describing notebook](https://github.com/achattaraj/MolClustPy/blob/master/Nephrin_Nck_NWASP_high_concentration.ipynb)
- [Python code](/notebooks/Nephrin_Nck_NWASP_high_concentration.py)
- [BNGL code](/notebooks/Nephrin_Nck_NWASP_high_concentration.bngl)

### TLBR Model: Clustering of bivalent receptors (BR) by trivalent ligands (TL) [Goldstein & Perelson, 1984](https://pubmed.ncbi.nlm.nih.gov/6204698/)
This model is a classic example of studying sol-gel transition in the context of ligand mediated (cell surface) receptor clustering. Note that NFSim does not prevent physiologically impossible clusters from forming - each molecule is assumed to be a long elastic string with sites on it, so every site can be bound to any other site.

- [Jupyter notebook](/notebooks/TLBR_model.ipynb)
- [Web-page describing notebook](https://github.com/achattaraj/MolClustPy/blob/master/TLBR_model.ipynb)
- [Python code](/notebooks/TLBR_model.py)
- [BNGL code](/notebooks/TLBR_model.bngl)

### Modeling the early events in signaling by the epidermal growth factor receptor (EGFR), [Blinov et al., 2006](https://www.sciencedirect.com/science/article/abs/pii/S0303264705001231/)
In this model signaling complexes formed around receptor dimer, with maximum size of a complex being 14 molecules (2 ligands, 2 receptors, and all combinetions of Grb2, Shc and Sos proteins bound to 2 receptor phoisphotyrosines. Contrary to the preevious model, all such complexes are physically possible.

- [Jupyter notebook](/notebooks/EGFR_model.ipynb)
- [Web-page describing notebook](https://github.com/achattaraj/MolClustPy/blob/master/EGFR_model.ipynb)
- [Python code](/notebooks/EGFR_model.py)
- [BNGL code](/notebooks/EGFR_model.bngl)
