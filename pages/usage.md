---
title: Usage
layout: default
permalink: usage
---

## MolClustPy Tutorial
### Package Import   
```python
from NFsim_data_analyzer import *
from DataViz_NFsim import * 
from MultiRun_BNG import *
```

### Simulations

```python
# Define the bngl file (BioNetGen model) 
bng_file = './test_dataset/Tutorial_Nephrin_Nck_NWASP.bngl'

# Initialization of the Simulation Object
simObj = BNG_multiTrials(bng_file, t_end=0.02, steps=20, numRuns=20)
print(simObj)
simObj.runTrials(delSim=False)
print()
```
### Data Analysis
```python
# analyze data across multiple trials
outpath = simObj.getOutPath()
molecules, numSite, counts, _ = simObj.getMolecules()
nfsObj = NFSim_output_analyzer(outpath)
print(nfsObj)
nfsObj.process_gdatfiles()
nfsObj.process_speciesfiles(molecules, counts, numSite)
```

### Visualization
#### 1. Plot the observable timecourse
```python
# indexList for observables (A list of observables can be passed by the indexList (as printed earlier))
plotTimeCourse(outpath, obsList=[2,4,6])
plotTimeCourse(outpath, obsList=[10,11])
```
#### 2. Plot cluster size distribution
```python
plotClusterDist(outpath)
```
[Full documentation](https://github.com/achattaraj/MolClustPy/blob/master/Tutorial_Nephrin_Nck_NWASP.ipynb) 

