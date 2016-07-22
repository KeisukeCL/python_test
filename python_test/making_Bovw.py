# coding = UTF-8
import scipy as sp
from sklearn.cluster import KMeans
import pickle as pc

NUMOF_K = 50
with open("kmeanshog.pkl", "rb") as aa:
    codebook = pc.load(aa)

bow = sp.zeros(NUMOF_K)
