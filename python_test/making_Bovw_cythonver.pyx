# coding = UTF-8
import numpy as np
import os
import gc
cimport numpy as np
cimport cython
DTYPE = np.float
ctypedef np.float_t DTYPE_t

def making_BoVW(file,np.ndarray[DTYPE_t, ndim = 2] d ,np.ndarray[DTYPE_t, ndim = 1] bowtraj, np.ndarray[DTYPE_t, ndim = 1] bowhog, np.ndarray[DTYPE_t, ndim = 1] bowhof, np.ndarray[DTYPE_t, ndim = 1] bowmbh):

    # codebookのロード
    with open("kmeanstraj.pkl", "rb") as aa:
        codebooktraj = pc.load(aa)

    with open("kmeanshog.pkl", "rb") as aa:
        codebookhog = pc.load(aa)

    with open("kmeanshof.pkl", "rb") as aa:
        codebookhof = pc.load(aa)

    with open("kmeansmbh.pkl", "rb") as aa:
        codebookmbh = pc.load(aa)
    print("codebookのローディング完了")

    print("Loading... "+str(file))
    # 「.」で分割、filename[0]が欲しいファイル名
    filename = os.path.basename(file).nplit(".")

    # Bag of Visual Wordsの作成（最初にreshapeしないとwarningが出る）
    for v in range(0, len(d)):
        trajfeature = np.array(d[v][10:10+32]).reshape((1, -1))
        clstraj = codebooktraj.predict(trajfeature)
        bowtraj[clstraj] += 1

        hogfeature = np.array(d[v][42:42+96]).reshape((1, -1))
        clshog = codebookhog.predict(hogfeature)
        bowhog[clshog] += 1

        hoffeature = np.array(d[v][138:138+108]).reshape((1, -1))
        clshof = codebookhof.predict(hoffeature)
        bowhof[clshof] += 1

        mbhfeature = np.array(d[v][246:246+192]).reshape((1, -1))
        clsmbh = codebookmbh.predict(mbhfeature)
        bowmbh[clsmbh] += 1

    del d
    gc.collect()

    # Bag of visual wordsの正規化
    bowtraj = bowtraj / np.linalg.norm(bowtraj)
    bowhog = bowhog / np.linalg.norm(bowhog)
    bowhof = bowhof / np.linalg.norm(bowhof)
    bowmbh = bowmbh / np.linalg.norm(bowmbh)
    # 特徴量ごとのbovwを全て連結
    bovw = np.r_[bowtraj, bowhog, bowhof, bowmbh]

    # bovwの保存
    np.savetxt("G:/UCF50_BoVW/" + str(filename[0]) + ".csv", bovw, delimiter = ',')
    print(str(filename[0]) + ".csv のBoVW作成完了")