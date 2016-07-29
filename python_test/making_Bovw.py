# coding = UTF-8
import scipy as sp
from sklearn.cluster import KMeans
import pickle as pc
import glob
import os


NUMOF_K = 4000  # codebookのクラス数と同じように

# codebookのロード
with open("kmeanstraj.pkl", "rb") as aa:
    codebooktraj = pc.load(aa)

with open("kmeanshog.pkl", "rb") as aa:
    codebookhog = pc.load(aa)

with open("kmeanshof.pkl", "rb") as aa:
    codebookhof = pc.load(aa)

with open("kmeanmbh.pkl", "rb") as aa:
    codebookmbh = pc.load(aa)

# Bag of Visual Wordsの初期化
bowtraj = sp.zeros(NUMOF_K)
bowhog = sp.zeros(NUMOF_K)
bowhof = sp.zeros(NUMOF_K)
bowmbh = sp.zeros(NUMOF_K)

# Trajectoriesディレクトリ内のファイルを全て取得
lists = sp.array(glob.glob("G:/UCF50_Trajectories/*.txt*"))
for file in lists:
    filename = os.path.basename(file).split(".")  #「.」で分割、filename[0]が欲しいファイル名

    with open(file,"r") as f:  # trajectoriesの読み込み
        d = sp.array([v.rstrip().split('\t') for v in f.readlines()])

    d = [list(map(lambda x:float(x), d[v])) for v in range(0,len(d))]

    for v in range(0, len(d)):  # Bag of Visual Wordsの作成
        clstraj = codebooktraj.predict(d[v][10:10+32])
        bowtraj[clstraj] += 1
        clshog = codebookhog.predict(d[v][42:42+96])
        bowhog[clshog] += 1
        clshof = codebooktraj.predict(d[v][138:138+108])
        bowhof[clshof] += 1
        clsmbh = codebooktraj.predict(d[v][246:246+192])
        bowmbh[clsmbh] += 1
    # Bag of visual wordsの正規化
    bowtraj /= sp.linalg.norm(bowtraj)
    bowhog /= sp.linalg.norm(bowhog)
    bowhof /= sp.linalg.norm(bowhof)
    bowmbh /= sp.linalg.norm(bowmbh)
    # 特徴量ごとのbovwを全て連結
    bovw = sp.r_[bowtraj, bowhog, bowhof, bowmbh]

    # bovwの保存
    sp.save("G:/UCF50_BoVW/" + str(filename[0]) + ".csv", bovw)