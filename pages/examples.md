---
title: Examples
layout: default
permalink: examples
---

# Examples of package usage

### Nephrin-Nck-NWasp clustering under low concentration
 
 Based on the <a href="https://pubmed.ncbi.nlm.nih.gov/34236318/">The solubility product extends the buffering concept to heterotypic biomolecular   condensates</a> manuscript. This example has low concentrations of molecules coresponding to 100 molecules of  Nephrin, 300 Nck and 150 NWasp. The MolClustPy demonstrates that the cluster distribution for this concentration is linear, with most clusters of low number of molecules and some rare large clusters.

- [Jupyter notebook](/notebooks/Nephrin_Nck_NWASP_low_concentration.ipynb)
- [Web-page describing notebook](/DEMO_neph_nck_nwasp)
- [Python code](/assets/test_datasets/Nephrin_Nck_NWASP_low_concentration.py)
- [BNGL code](/assets/test_datasets/Nephrin_Nck_NWASP_low_concentration.bngl)


### Nephrin-Nck-NWASP clustering with high_concentration

This example has high concentrations of molecules coresponding to 300 molecules of Nephrin, 900 Nck and 450 NWasp. The MolClustPy demonstrates that the cluster distribution for this concentration is bimodal, with most molecules in either small or very big clusters.

- [Jupyter notebook](/notebooks/Nephrin_Nck_NWASP_high_concentration.ipynb)
- [Web-page describing notebook](/Nephrin_Nck_NWASP_high_concentration_model)
- [Python code](/assets/test_datasets/Nephrin_Nck_NWASP_high_concentration.py)
- [BNGL code](/assets/test_datasets/Nephrin_Nck_NWASP_high_concentration.bngl)

### TLBR Model: Clustering of bivalent receptors (BR) by trivalent ligands (TL) [Goldstein & Perelson, 1984](https://pubmed.ncbi.nlm.nih.gov/6204698/)
This model is a classic example of studying sol-gel transition in the context of ligand mediated (cell surface) receptor clustering. Note that NFSim does not prevent physiologically impossible clusters from forming - each molecule is assumed to be a long elastic string with sites on it, so every site can be bound to any other site.

- [Jupyter notebook](/notebooks/TLBR_model.ipynb)
- [Web-page describing notebook](/TLBR_model)
- [Python code](/assets/test_datasets/TLBR_model.py)
- [BNGL code](/assets/test_datasets/TLBR_model.bngl)

### Modeling the early events in signaling by the epidermal growth factor receptor (EGFR), [Blinov et al., 2006](https://www.sciencedirect.com/science/article/abs/pii/S0303264705001231/)
In this model signaling complexes formed around receptor dimer, with maximum size of a complex being 14 molecules (2 ligands, 2 receptors, and all combinetions of Grb2, Shc and Sos proteins bound to 2 receptor phoisphotyrosines. Contrary to the preevious model, all such complexes are physically possible.

- [Jupyter notebook](/notebooks/EGFR_model.ipynb)
- [Web-page describing notebook](/EGFR_model)
- [Python code](/assets/test_datasets/EGFR_model.py)
- [BNGL code](/assets/test_datasets/EGFR_model.bngl)
