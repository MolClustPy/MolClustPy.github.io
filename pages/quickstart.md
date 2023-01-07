---
title: Quickstart
layout: default
permalink: quickstart
---

# Quickstart Guide

Welcome to the ClusterAnalyzer Package tutorial!

# Jupyter Notebook

The suggested python distribution to use is the Jupyter Notebook IDE 

There are two ways to install the Jupyter Notebook
    
    - in the [Anaconda python distribution](https://www.anaconda.com/products/distribution)
    
    - [Install](https://jupyter.org/install) Jupyter Notebook

## To Open Jupyter Notebook

From Anaconda
    
    - Install the Jupyter Notebook IDE on the Navigator page
    
    - Click Launch
    
    - The notebook interface will appear in a new browser window or tab.

From Terminal
    
    - Click on spotlight, type terminal to open a terminal window.
    
    - Enter the startup folder by typing cd /some_folder_name.
    
    - Type jupyter notebook to launch the Jupyter Notebook App The notebook interface will appear in a new browser window or tab.
    

## Jupyter Notebook Instructions

Each cell can be ran individually using the run button

The cells have to be run in order. 

## Example of Code in Jupyter Notebook

### First start by importing the necessary packages:

-bionetgen

-clusteranalyzer
    
* we will be using individual modules from the clusteranalyzer package for the code

```python

    import sys
    import bionetgen
    from glob import glob
    import clusteranalyzer
    from clusteranalyzer.MultiRun_NFsim_execution import *
    from clusteranalyzer.nfsim_data_analyzer import *
    from clusteranalyzer.DataViz_NFsim import *
```    
   
### Set the program variables and path

These are the constants and variables that will be necessary to use the package.

The paths will be individualized to each device so be sure to change it to match the location of the files you would like to analyze.

```python
    
    # bngl file (BioNetGen model) 
    bng_file = './test_dataset/single_concentration_file/neph_nck_nwasp_10_30_15uM.bngl'

    # run multiple trials
    simObj = BNG_multiTrials(bng_file, t_end=0.02, steps=20, numRuns=20)
    print(simObj)
    simObj.runTrials(delSim=False)
    print()

    # analyze data across multiple trials
    outpath = simObj.getOutPath()
    molecules, numSite, counts, _ = simObj.getMolecules()
    nfsObj = NFSim_output_analyzer(outpath)
    nfsObj.process_gdatfiles()
    nfsObj.process_speciesfiles(molecules, counts, numSite)
```
## Visualization of Data

### Plot Observable Time Course

Example:
![png](images/demo/TCOuput1.png)

### Plot System Level Quantities

Example:
![png](images/demo/Screen Shot 2022-12-21 at 10.41.55 AM.png)

### Plot Molecule Specific Quantities

Example:
![png](images/demo/Screen Shot 2022-12-21 at 10.44.42 AM.png)

## Check the [How to Use Page](usage.md) to see details on changing code
