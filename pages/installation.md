---
title: Installation
layout: default
permalink: installation
---

# Installation

## General Prerequisites
  - Python 2.7 or 3.1 (or higher) 
  - pip or pip3

The best way to install Python is to download [Anaconda distribution](https://www.anaconda.com/products/distribution) available for all operation systems. It has [Jupiter notebook](https://jupyter.org/) pre-installed that has a convenient way to run MolClustPy. It also must install pip. To check your installation, type in the terminal (command prompt on Windows):
```python
% python -i
% pip -V
```

## Required Packages

You will need to install these Python packages:
```python
% pip install numpy
% pip install matplotlib
% pip install pandas
% pip install bionetgen
```
While the first three packages may be already installed on yor machine, the bionetgen package is an essential package for the analyzer and most likely needs to be installed.

### Download Method 1: Zip folder

Load zip file with the code from [https://github.com/IndyCodeLab/....zip](https://github.com/IndyCodeLab/....zip), unzip.

### Download Method 2: Github

Git users may clone the repository using 
```python
clone https://github.com/IndyCodeLab/clusteranalyzer.git
```

### Download Method 3: Pip Install

Using this pip install, you will be able to download the cluster analyzer package.

```python
pip install -i https://test.pypi.org/simple/ clusteranalyzer==0.0.14
```
 
 After download/install, navigate to the directory/folder where clusteranalyzer is installed and follow steps at [Start Guide](/quickstart)
 

