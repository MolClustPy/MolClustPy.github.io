from MolClustPy import * 

# bngl file (BioNetGen model) 
bng_file = '.../mypath/.../Nephrin_Nck_NWASP_high_concentration.bngl'

# Initialization of the Simulation Object
simObj = BNG_multiTrials(bng_file, t_end=0.02, steps=20, numRuns=20)
print(simObj)
simObj.runTrials(delSim=False)
print()

# analyze data across multiple trials
outpath = simObj.getOutPath()
molecules, numSite, counts, _ = simObj.getMolecules()
nfsObj = NFSim_output_analyzer(outpath)
print(nfsObj)
nfsObj.process_gdatfiles()
nfsObj.process_speciesfiles(molecules, counts, numSite)

# indexList for observables
plotTimeCourse(outpath, obsList=[2,4,6])
plotTimeCourse(outpath, obsList=[10,11])

# 2A: Cluster size distribution (ACO: Average Cluster Occupancy)
plotClusterDist(outpath)
# Binned distribution by providing cluster size ranges
plotClusterDist(outpath, sizeRange=[1,10,100])

# 2B: Number of bonds per molecule
plotBondsPerMolecule(outpath)

# 2C: Bound fraction distribution
plotBoundFraction(outpath)

# 3A. Average composition of indivual clusters. 
# Default is all the clusters present in the system. As before, adjust width and transparency (alpha) for visual clarity.
plotClusterComposition(outpath, specialClusters=[], width=0.15, alpha=0.5)

# You can look at the composition of a set of clusters (specialClusters) also
plotClusterComposition(outpath, specialClusters=[2, 4, 10], width=0.15, alpha=0.7)
plotClusterComposition(outpath, specialClusters=[580, 587], width=0.15, alpha=0.7)

# 3B. Bondcount distribution of each molecular type 
# plotBondCounts(outpath, molecules=molecules) 

# You may provide a subset of molecules also
plotBondCounts(outpath, molecules=['Nck'])



