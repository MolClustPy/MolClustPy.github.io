---
title: Quickstart
layout: default
permalink: quickstart
---

# Quickstart Guide

Welcome to the ClusterAnalyzer Package tutorial!

# Jupyter Notebook

Jupyter Notebook is the easiest way to use this package. The package comes with the set of sample BNGL files in the folder ..... See the [How to Use page] for details on how to write BNGL code, how to access data in different folders, etc.

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
