---
title: Quickstart
layout: default
permalink: quickstart
---

# Quickstart Guide for the MolClustPy Python package

This package contains all the code and functionality of the MolClustPy in a package

### The first step is to install the MolClustPy package

You can use this command in the Terminal to install the latest version of the package onto your device:

```python
pip install MolClustPy
```

The package will be installed into your device in the site-packages area

The package contains:
- three primarily used .py files: MultiRun_BNG.py, NFsim_data_analyzer.py, and DataViz_Nfsim.py. These are the files that will be imported into your code when you are using the package. Each of the files contains the functions that make up the MolClustPy package. The package contains other .py files to supplement these files.

- several files with extension <b>.ipynb</b>: [Tutorial_neph_nck_nwasp.ipynb](DEMO_neph_nck_nwasp.md), [EGFR.ipynb](EGFR.md) and [TLBR.ipynb](TLBR.md). Each of them corresponds to the description of cluster formation given in [BioNetGen](http://bionetgen.org) files located in <tt>test_datasets</tt> folder within clusteranalyzer directory. These files have the same name with extension <b>.bngl</b>. 

Here is an example pathway of the location of the package:

```python
/Users/name/opt/anaconda3/lib/python3.9/site-packages/MolClustPy
```
You can use the "pip list" command in terminal to ensure that the package has installed and you have the latest version

```python
pip uninstall bionetgen
pip install bionetgen
```
### Using the MolClustPy Package

Using the package is the same as using the code downloaded through the other methods(zip or github clone) but you will need to make a few changes.

The main difference will be in the imports:

Instead of doing this:
```python
from NFsim_data_analyzer import *
from DataViz_NFsim import * 
from MultiRun_BNG import * 
```

You should do this:
```python
from MolClustPy import *
```

You will also have to assign a bngl file of your own and its path when coding.
```python  
    # bngl file (BioNetGen model) 
    bng_file = '/Users/name/Downloads/nfsimPy/test_dataset/single_concentration_file/neph_nck_nwasp_10_30_15uM.bngl'
```
You can follow the tutorial given at [How to use](usage.md) page and make these changes as you go.
It will provide step-by-step guide to modifying inputs and analyzing outputs of cluster formation while using the package. 

<b> You can check [MolClustPy Jupyter Notebook DEMO](pages/MolClustPy Usage/MolClustPy Usage.md) for an example of how the package is used. </b>

### Common Error Identification
- An error can occur involving Bionetgen due to version control issues when running the package so it is best to pip uninstall bionetgen then pip install bionetgen in order to prevent the error from occuring.

AttributeError: module 'bionetgen' has no attribute 'bngmodel'
