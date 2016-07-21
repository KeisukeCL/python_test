# coding = UTF-8
import scipy as sp
from sklearn.cluster import KMeans
import pickle as pc

with open('1.txt','r') as f:
    d = sp.array([v.rstrip().split('\t') for v in f.readlines()])

d = [list(map(lambda x:float(x), d[v])) for v in range(0,len(d))]

#HOG 96dim: 8(bin) x 2 x 2(spatio) x 3(temporal)
print ("HOG:")
print (d[0][42:42+96])

#HOF 108dim: 9(bin) x 2 x 2(spatio) x 3(temporal)
print ("HOF:")
print (d[0][138:138+108])

#MBHX 96dim: 8(bin) x 2 x 2(spatio) x 3(temporal)
print ("MBHX:")
print (d[0][246:246+96])

#MBHX 96dim: 8(bin) x 2 x 2(spatio) x 3(temporal)
print ("MBHY:")
print (d[0][342:342+96])

HOGFeature = sp.vstack(d[v][42:42+96] for v in range(0, len(d)))
#HOFFeature = sp.vstack(d[v][138:138+108] for v in range(0, len(d)))
#MBHXFeature = sp.vstack(d[v][246:246+96] for v in range(0, len(d)))
#MBHYFeature = sp.vstack(d[v][342:342+96] for v in range(0, len(d)))

kmeans_hog_model = KMeans(n_clusters = 50).fit(HOGFeature)
#kmeans_hof_model = KMeans(n_clusters = 4000, max_iter = 10).fit(HOFFeature)
#kmeans_mbhx_model = KMeans(n_clusters = 4000, max_iter = 10).fit(MBHXFeature)
#kmeans_mbhy_model = KMeans(n_clusters = 4000, max_iter = 10).fit(MBHYFeature)
labels = kmeans_hog_model.labels_
for label in labels:
    print (label)
#with open ("kmeanshog.pkl", "wb") as aa:
 #   pc.dump(kmeans_hog_model, aa)
