---
title: Quickstart
layout: default
permalink: quickstart
---

# Quickstart Guide

Welcome to the ClusterAnalyzer Package tutorial!


### First start by importing the necessary packages:

-bionetgen

-clusteranalyzer
    
* we will be using individual modules from the clusteranalyzer package for the code

.. code-block::shell

    import sys
    import bionetgen
    from glob import glob
    import clusteranalyzer
    from clusteranalyzer.MultiRun_NFsim_execution import *
    from clusteranalyzer.nfsim_data_analyzer import *
    from clusteranalyzer.DataViz_NFsim import *
    
   
### Set the program variables and path

These are the constants and variables that will be necessary to use the package.

The paths will be individualized to each device so be sure to change it to match the location of the files you would like to analyze.

.. code-block:: shell
    
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

