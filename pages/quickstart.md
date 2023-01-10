---
title: Quickstart
layout: default
permalink: quickstart
---

# Quickstart Guide

Non-experts in Python are recommended to use the [Jupyter Notebook](https://jupyter.org/). 

To launch it from Terminal, navigate to the installation directory/folder and type

```python
jupyter notebook &
```
Note that the notebook interface will appear in a new browser window or tab that has address http://localhost:8888/tree.

1. You will see several files with extension <b>.ipynb</b>: [Tutorial_neph_nck_nwasp.ipynb](DEMO_neph_nck_nwasp.md), [EGFR.ipynb](EGFR.md) and [TLBR.ipynb](TLBR.md). Each of them corresponds to the description of cluster formation given in [BioNetGen](http://bionetgen.org) files located in <tt>test_datasets</tt> folder within clusteranalyzer directory. These files have the same name with extension <b>.bngl</b>. 

2. The most commented model is [Tutorial_neph_nck_nwasp.ipynb](DEMO_neph_nck_nwasp.md). We will use it in the tutorial given at [How to use](usage.md) page
It will provide step-by-step guide to modifying inputs and analyzing outputs of cluster formation. 

3. Here we give some general remarks on how to run models with Jupyter notebook. Put your mouse into the first cell. e.g. where you see <font color = blue>In [1] :</font>

```python
from NFsim_data_analyzer import *
from DataViz_NFsim import * 
from MultiRun_BNG import * 
```
After clicking on the <b>Run</b> button (the top of the browser window) the content of the cell will be executed, and you can click on the next cell and again click on <b>Run</b> to operform the next actions.

4. After clicking one cell after another, you can obtain all results of the file.

6. The path to the input BNGL file is defined in the second cell <font color = blue>In [2] :</font>. One can open this file in the editor, vary some numbers and see how the results change.

```python
    
    # bngl file (BioNetGen model) 
    bng_file = './test_dataset/neph_nck_nwasp_10_30_15uM.bngl'
```
