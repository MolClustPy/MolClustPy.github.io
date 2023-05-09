from molclustpy import * 

bng_file = '.../mypath/.../TLBR_model.bngl'

# Initialization of the Simulation Object
simObj = BNG_multiTrials(bng_file, t_end=400.0, steps=40, numRuns=20)
print(simObj)
simObj.runTrials(delSim=False)
print()

# analyze data across multiple trials
outpath = simObj.getOutPath()
molecules, numSite, counts, _ = simObj.getMolecules()
nfsObj = NFSim_output_analyzer(outpath)
nfsObj.process_gdatfiles()
nfsObj.process_speciesfiles(molecules, counts, numSite)

# Visualization 
plotTimeCourse(outpath, obsList=[])

# 2A: Cluster size distribution (ACO: Average Cluster Occupancy)
plotClusterDist(outpath)
# You can plot a binned distribution by providing cluster size ranges
plotClusterDist(outpath, sizeRange=[1,10,500])
# 2B: Number of bonds per molecule
plotBondsPerMolecule(outpath)
# 2C: Bound fraction distribution
plotBoundFraction(outpath)

# 3A. Average composition of indivual clusters. 
# Default is all the clusters present in the system. As before, adjust width and transparency (alpha) for visual clarity.
plotClusterComposition(outpath, specialClusters=[], width=0.25, alpha=0.5)
# You can look at the composition of a set of clusters (specialClusters) also
plotClusterComposition(outpath, specialClusters=[521, 531], width=0.15, alpha=0.7)

# 3B. Bondcount distribution of each molecular type 
# You may provide a subset of molecules also
plotBondCounts(outpath, molecules=['L'])
plotBondCounts(outpath, molecules=['R'])

