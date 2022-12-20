---
title: Usage
layout: default
permalink: usage
---

Cluster Analyzer

```python
# You will need the 'bionetgen' python package, aprart from the standard ones like numpy, matplotlib and pandas. 
from nfsim_data_analyzer import *
from DataViz_NFsim import * 
from MultiRun_BNG import * 

# check_import: https://napuzba.com/check-if-module-exists/
```

More Code

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
