# coding = UTF-8
import scipy as sp
from sklearn.cluster import KMeans
import pickle as pc
import glob
import os
import gc

NUMOF_K = 1000  # codebookのクラス数と同じように

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

# Trajectoriesディレクトリ内のファイルを全て取得
lists = sp.array(glob.glob("G:/UCF50_Trajectories/*.txt*"))
for file in lists:
    print("Loading... "+str(file))
    # 「.」で分割、filename[0]が欲しいファイル名
    filename = os.path.basename(file).split(".")

    # Bag of Visual Wordsの初期化
    bowtraj = sp.zeros(NUMOF_K, dtype=int)
    bowhog = sp.zeros(NUMOF_K, dtype=int)
    bowhof = sp.zeros(NUMOF_K, dtype=int)
    bowmbh = sp.zeros(NUMOF_K, dtype=int)
   

    with open(file,"r") as f:  # trajectoriesの読み込み
        d = sp.array([v.rstrip().split('\t') for v in f.readlines()])

    d = [list(map(lambda x: float(x), d[v])) for v in range(0,len(d))]
    
    # Bag of Visual Wordsの作成（最初にreshapeしないとwarningが出る）
    for v in range(0, len(d)):
        trajfeature = sp.array(d[v][10:10+32]).reshape((1, -1))
        clstraj = codebooktraj.predict(trajfeature)
        bowtraj[clstraj] += 1
   
        hogfeature = sp.array(d[v][42:42+96]).reshape((1, -1))
        clshog = codebookhog.predict(hogfeature)
        bowhog[clshog] += 1

        hoffeature = sp.array(d[v][138:138+108]).reshape((1, -1))
        clshof = codebookhof.predict(hoffeature)
        bowhof[clshof] += 1

        mbhfeature = sp.array(d[v][246:246+192]).reshape((1, -1))
        clsmbh = codebookmbh.predict(mbhfeature)
        bowmbh[clsmbh] += 1
 
    del d
    gc.collect()

    # Bag of visual wordsの正規化
    bowtraj = bowtraj / sp.linalg.norm(bowtraj)
    bowhog = bowhog / sp.linalg.norm(bowhog)
    bowhof = bowhof / sp.linalg.norm(bowhof)
    bowmbh = bowmbh / sp.linalg.norm(bowmbh)
    # 特徴量ごとのbovwを全て連結
    bovw = sp.r_[bowtraj, bowhog, bowhof, bowmbh]

    # bovwの保存
    sp.savetxt("G:/UCF50_BoVW/" + str(filename[0]) + ".csv", bovw, delimiter = ',')
    print(str(filename[0]) + ".csv のBoVW作成完了")