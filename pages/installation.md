---
title: Installation
layout: default
permalink: installation
---

# Installation

### General Prerequisites
  - Python 2.7 or 3.1 (or higher) 
  - pip or pip3

The best way to install Python is to download [Anaconda distribution](https://www.anaconda.com/products/distribution) available for all operation systems. It has [Jupyter notebook](https://jupyter.org/) pre-installed that has a convenient way to run molclustpy. Anaconda install also should install pip. To check your installation, type in the terminal (command prompt on Windows):
```python
python -i
pip -V
jupyter --version 
```
In case Jupyter is missing and you prefer to use it (recommended for beginners), download it from [https://jupyter.org/install](https://jupyter.org/install).

### Required Packages
Apart from the standard Python libraries, required third-party packages: 
* [pyBioNetGen](https://pybionetgen.readthedocs.io/en/latest/)
* Numpy
* Pandas 
* Matplotlib   

### Install MolClustPy 

```python
pip install molclustpy
```
Installation of molclustpy will check for the third-party libraries and install them in case your machine does not have them.  


#### Optional Github Clone for source code

Git users may [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the [repository](https://github.com/achattaraj/MolClustPy) using 
```python
git clone https://github.com/achattaraj/MolClustPy.git
```

 
 After download/install, follow the [Start Guide](https://molclustpy.github.io/quickstartJupyter)
 

