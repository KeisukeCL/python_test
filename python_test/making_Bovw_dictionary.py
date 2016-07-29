# coding = UTF-8
import scipy as sp
from sklearn.cluster import KMeans
import pickle as pc
import gc

n_clusters = 4000   #k-meansのクラスタ数の設定

# Bag of Visual Wordsのコードブックを作成するコード
for i in range (1, 51):   # ランダムにtrajectoriesをロード
    with open("G:/UCF50_Trajectories/" + str(i) + "_1.txt","r") as f:
        d = sp.array([v.rstrip().split('\t') for v in f.readlines()])

    d = [list(map(lambda x:float(x), d[v])) for v in range(0,len(d))]

    # それぞれの特徴を取り出す（予めTRAJFeatureを初期化する必要があるので代わりの方法）
    if i == 1:
        TRAJFeature = sp.vstack(d[v][10:10 + 32]
                                for v in range(0, len(d)))
        HOGFeature = sp.vstack(d[v][42:42 + 96]
                               for v in range(0, len(d)))
        HOFFeature = sp.vstack(d[v][138:138 + 108]
                               for v in range(0, len(d)))
        MBHFeature = sp.vstack(d[v][246:246 + 192]
                               for v in range(0, len(d)))
    else:
        TRAJFeature2 = sp.vstack(d[v][10:10 + 32]
                                 for v in range(0, len(d)))
        HOGFeature2 = sp.vstack(d[v][42:42 + 96]
                                for v in range(0, len(d)))
        HOFFeature2 = sp.vstack(d[v][138:138 + 108]
                                for v in range(0, len(d)))
        MBHFeature2 = sp.vstack(d[v][246:246 + 192]
                                for v in range(0, len(d)))

        TRAJFeature = sp.vstack((TRAJFeature, TRAJFeature2))
        HOGFeature = sp.vstack((HOGFeature, HOGFeature2))
        HOFFeature = sp.vstack((HOFFeature, HOFFeature2))
        MBHFeature = sp.vstack((MBHFeature, MBHFeature2))

        del d, TRAJFeature2, HOFFeature2, MBHFeature2
        gc.collect()

    if len(TRAJFeature) > 1000000:   # 1000000以上のサンプルを取得できたらbreak
        break

# クラスタリング
kmeans_traj_model = KMeans(n_clusters).fit(TRAJFeature)
kmeans_hog_model = KMeans(n_clusters).fit(HOGFeature)
kmeans_hof_model = KMeans(n_clusters).fit(HOFFeature)
kmeans_mbh_model = KMeans(n_clusters).fit(MBHFeature)

# pickleで保存
with open ("kmeanstraj.pkl", "wb") as aa:
    pc.dump(kmeans_traj_model, aa)
with open ("kmeanshog.pkl", "wb") as aa:
    pc.dump(kmeans_hog_model, aa)
with open ("kmeanshof.pkl", "wb") as aa:
    pc.dump(kmeans_hof_model, aa)
with open ("kmeansmbh.pkl", "wb") as aa:
    pc.dump(kmeans_mbh_model, aa)