# coding = UTF-8
import scipy as sp
from sklearn.cluster import KMeans
import pickle as pc

NUMOF_K = 50
with open("kmeanshog.pkl", "rb") as aa:
    codebook = pc.load(aa)

bow = sp.zeros(NUMOF_K)
with open('1.txt','r') as f:
    d = sp.array([v.rstrip().split('\t') for v in f.readlines()])

d = [list(map(lambda x:float(x), d[v])) for v in range(0,len(d))]
for v in range(0, len(d)):
    cls = codebook.predict(d[v][42:42+96])
    bow[cls] += 1
bow /= sp.linalg.norm(bow)
print (bow)