---
title: Analysis of Nephrin-Nck-NWasp clustering
layout: default
permalink: DEMO_neph_nck_nwasp
---

# Analysis of Nephrin-Nck-NWasp clustering

This script contains step by step instructions on how to run multiple [NFsim](http://michaelsneddon.net/nfsim/) simulations of a [BioNetGen](https://bionetgen.org/) model of [multivalent protein clustering](https://elifesciences.org/articles/67176) and collect statistics to analyze biophysical properties of these clusters.

###  Import the packages first 


```python
# You will need the 'bionetgen' python package, aprart from the standard ones like numpy, matplotlib and pandas. 
from nfsim_data_analyzer import *
from DataViz_NFsim import * 
from MultiRun_BNG import * 

# check_import: https://napuzba.com/check-if-module-exists/
```

### Run multiple NFsim simulations of a bionetgen model & analyze the data![neph_nck_nwasp_model.png](images/demo/Neph_nck_nwasp.png)
Example Model: A three-component system. Nephrin has three phosphotyrosin (pY) residues which can bind to Src Homology 2 domain (Sh2) of Nck molecule. Nck also contains three Src Homology 3 or SH3 domains (S) which interact with proline rich motif or PRM (p) of NWASP molecules. Two classes of binding rules are enough to define these reactions.  


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

    
    ***** // ***** 
    Class : BNG_multiTrials
    File Path : ./test_dataset/single_concentration_file/neph_nck_nwasp_10_30_15uM.bngl
    
    t_end : 0.02 seconds 	 output_steps : 20
    Number of runs: 20
    
    Molecules: ['NWASP', 'Nck', 'Nephrin']
    Number of binding sites: [6, 4, 3]
    Species Counts: [100.0, 300.0, 150.0]
    
    NFsim progress : [****************************************] 100%
    Execution time : 34.3563 seconds
    
    Processing gdat_files : [****************************************] 100%
    
    Observables:  {0: 'time', 1: 'tot_Nck', 2: 'free_Nck', 3: 'tot_NWASP', 4: 'free_NWASP', 5: 'tot_Nephrin', 6: 'free_Nephrin', 7: 'cluster_123', 8: 'cluster_23'}
    
    Processing species_files : [****************************************] 100%


### Visualization

### 1. Plot the observable timecourse


```python
# Enlist the observales that you want to plot
# Indices start from 0 in Python 
plotTimeCourse(outpath, obsList=[2,4,6])
plotTimeCourse(outpath, obsList=[7,8])
```


    
![png](output_7_0.png)
    



    
![png](output_7_1.png)
    


### 2. Plot system level quantities

> 2A. Cluster size distribution

> 2B. Number of bonds per molecule

> 2C. Bound fraction distribution


```python
# 2A: Cluster size distribution (ACO: Average Cluster Occupancy)
plotClusterDist(outpath)
# You can plot a binned distribution by providing cluster size ranges
plotClusterDist(outpath, sizeRange=[1,4,12])
```


    
![png](output_9_0.png)
    



    
![png](output_9_1.png)
    



```python
# 2B: Number of bonds per molecule
plotBondsPerMolecule(outpath)
# 2C: Bound fraction distribution
plotBoundFraction(outpath)
```


    
![png](output_10_0.png)
    



    
![png](output_10_1.png)
    


### 3. Plot molecule specific quantities

> 3A. How molecules are distributed across multiple clusters ?

> 3B. What is the average composition of the clusters? 

> 3C. How many bonds are coming out of each molecular types?



```python
# 3A. Molecular distribution.
# Default is all the molecules present in the system. 
# width is barplot width parameter, and alpha sets the transparency. Adjust these for visual clarity.
plotMolecularDistribution(outpath, molecules=[], width=0.25, alpha=0.6)

#You may provide a subset of molecules also
plotMolecularDistribution(outpath, molecules=['Nck'], width=0.5, alpha=0.8)
```


    
![png](output_12_0.png)
    



    
![png](output_12_1.png)
    



```python
# 3B. Average composition of indivual clusters. 
# Default is all the clusters present in the system. As before, adjust width and transparency (alpha) for visual clarity.
plotClusterComposition(outpath, specialClusters=[], width=0.15, alpha=0.5)

# You can look at the composition of a set of clusters (specialClusters) also
plotClusterComposition(outpath, specialClusters=[2, 4, 10], width=0.15, alpha=0.7)
```


    
![png](output_13_0.png)
    



    
![png](output_13_1.png)
    



```python
# 3C. Bondcount distribution of each molecular type 
# plotBondCounts(outpath, molecules=molecules) # Reading molecules from previous block

# You may provide a subset of molecules also
plotBondCounts(outpath, molecules=['Nck'])
```


    
![png](output_14_0.png)
    

