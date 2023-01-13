---
title: Quickstart Pip Install
layout: default
permalink: quickstartpip
---

# Quickstart Guide for the Command Line
 
### Install Python
- Download and install [Anaconda Distribution](https://www.anaconda.com/products/distribution) for Python

### Download .py File

Downloadable .py files that can be ran in Python: 
- [Nephrin_Nck_NWASP_high_concentration.py](../assets/test_datasets/Nephrin_Nck_NWASP_high_concentration.py)
- [EGFR_model.py](../assets/test_datasets/EGFR_model.py)
- [TLBR_model.py](../assets/test_datasets/TLBR_model.py) 

### Running .py File

Open Command Line and type

```python
python __file_name__.py
```
or

```python
python3 __file_name__.y
```

### Summary
- Download and install [Anaconda Distribution](https://www.anaconda.com/products/distribution) for Python
- Download .py file from the link provided above
- Type ```python file.py``` or ``` python3 file.py``` to run file
- 

You can follow the tutorial given at [How to use](usage.md) page and make these changes as you go.
It will provide step-by-step guide to modifying inputs and analyzing outputs of cluster formation while using the package. 

<b> You can check [MolClustPy Jupyter Notebook DEMO](MolClustPy_Usage/MolClustPy_Usage.md) for an example of how the package is used. </b>

### Common Error Identification
- An error can occur involving Bionetgen due to version control issues when running the package so it is best to pip uninstall bionetgen then pip install bionetgen in order to prevent the error from occuring.

AttributeError: module 'bionetgen' has no attribute 'bngmodel'
