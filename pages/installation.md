---
title: Installation
layout: default
permalink: installation
---

# Installation

## General Prerequisites
  - Python 2.7 or 3.1 (or higher) 
  - pip or pip3

The best way to install Python is to download [Anaconda distribution](https://www.anaconda.com/products/distribution) available for all operation systems. It has [Jupyter notebook](https://jupyter.org/) pre-installed that has a convenient way to run molclustpy. Anaconda install also should install pip. To check your installation, type in the terminal (command prompt on Windows):
```python
python -i
pip -V
jupyter --version 
```
In case Jupyter is missing and you prefer to use it (recommended for beginners), download it from [https://jupyter.org/install](https://jupyter.org/install).

## Required Packages

You will need to install the [pyBioNetGen](https://pybionetgen.readthedocs.io/en/latest/) package:
```python
pip install bionetgen
```

## Install MolClustPy 

### Option 1: Source folder: 

Download the zip file by clicking on [MolClustPy.zip](/downloads/MolClustPy.zip), unzip.


### Option 2: Github

Git users may [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the [repository](https://github.com/achattaraj/MolClustPy) using 
```python
git clone https://github.com/achattaraj/MolClustPy/MolClustPy.git
```

### Option 3: Pip Install

```python
pip install molclustpy
```
 
 After download/install, navigate to the directory/folder where MolClustPy is installed and follow steps at [Start Guide](https://molclustpy.github.io/quickstartJupyter)
 

