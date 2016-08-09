# coding = UTF-8
import numpy as np
import scipy.cluster
from sklearn.cluster import KMeans
import pickle as pc
import gc
import time


# Bag of Visual Wordsのコードブックを作成するコード
for i in range (1, 4):   # ランダムにtrajectoriesをロード
    with open(str(i) + ".txt","r") as f:
        d = np.array([v.rstrip().split('\t') for v in f.readlines()])
    print("Loading... " +  str(i) + ".txt" )
    print(str(d.ndim))
    d = d.astype(np.float)
    #d = [list(map(lambda x:float(x), d[v])) for v in range(0,len(d))]
    print(d.dtype)
    # それぞれの特徴を取り出す（予めTRAJFeatureを初期化する必要があるので代わりの方法）
    if i == 1:
        TRAJFeature = np.vstack(d[v][10:10 + 32]
                                for v in range(0, len(d)))
        #HOGFeature = np.vstack(d[v][42:42 + 96]
                              # for v in range(0, len(d)))
        #HOFFeature = np.vstack(d[v][138:138 + 108]
                              # for v in range(0, len(d)))
        #MBHFeature = np.vstack(d[v][246:246 + 192]
                              # for v in range(0, len(d)))
        print("サンプル数は"+str( len(TRAJFeature))+"個です")
    else:
        TRAJFeature2 = np.vstack(d[v][10:10 + 32]
                                 for v in range(0, len(d)))
        #HOGFeature2 = np.vstack(d[v][42:42 + 96]
                                #for v in range(0, len(d)))
        #HOFFeature2 = np.vstack(d[v][138:138 + 108]
                                #for v in range(0, len(d)))
        #MBHFeature2 = np.vstack(d[v][246:246 + 192]
                                #for v in range(0, len(d)))

        TRAJFeature = np.vstack((TRAJFeature, TRAJFeature2))
        #HOGFeature = np.vstack((HOGFeature, HOGFeature2))
        #HOFFeature = np.vstack((HOFFeature, HOFFeature2))
        #MBHFeature = np.vstack((MBHFeature, MBHFeature2))
        print("サンプル数は"+str( len(TRAJFeature))+"個です")
        del d, TRAJFeature2
        gc.collect()

    if len(TRAJFeature) > 1000000:   # 1000000以上のサンプルを取得できたらbreak
        print("十分なサンプル数を確保しました")
        break

print(str(len(TRAJFeature)) + "クラスタリングを実行します")


# クラスタリング
start = time.time()
[codebook, destortion] = scipy.cluster.vq.kmeans2(TRAJFeature, 70, iter=50)
elapsed_time = time.time() - start
print(str(elapsed_time)+ "[sec]")

print("scipy")

#kmeans_hog_model = KMeans(n_clusters).fit(HOGFeature)
#kmeans_hof_model = KMeans(n_clusters).fit(HOFFeature)
#kmeans_mbh_model = KMeans(n_clusters).fit(MBHFeature)
print("クラスタリング終了しました")
# pickleで保存
with open ("kmeanstraj.pkl", "wb") as aa:
    pc.dump(codebook, aa)
#with open ("kmeanshog.pkl", "wb") as aa:
    #pc.dump(kmeans_hog_model, aa)
#with open ("kmeanshof.pkl", "wb") as aa:
    #pc.dump(kmeans_hof_model, aa)
#with open ("kmeansmbh.pkl", "wb") as aa:
    #pc.dump(kmeans_mbh_model, aa)