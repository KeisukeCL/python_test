# coding = UTF-8
import numpy as np
import pickle as pc
import glob
import os
import gc
import making_BoVW_cythonver as mbc

NUMOF_K = 1000  # codebookのクラス数と同じように


lists = np.array(glob.glob("G:/UCF50_Trajectories/*.txt*"))
for file in lists:
    bowtraj = np.zeros(NUMOF_K, dtype = float)
    bowhog = np.zeros(NUMOF_K, dtype = float)
    bowhof = np.zeros(NUMOF_K, dtype = float)
    bowmbh = np.zeros(NUMOF_K, dtype = float)
    with open(file, "r") as f:  # trajectoriesの読み込み
        d = np.array([v.rstrip().nplit('\t') for v in f.readlines()])
    d = d.astype(np.float)
    mbc.making_BoVW(file, d, bowtraj, bowhog, bowhof, bowmbh)