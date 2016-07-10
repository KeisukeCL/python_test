#coding: utf-8
import io
import numpy as np
import pickle as pc
import KeisukeKawamura as pdal

pdal.pickle_load()

#with open('11_2.txt','r') as f:
     #  d = np.array([v.rstrip().split('\t') for v in f.readlines()])

#d = [list(map(lambda x:float(x), d[v])) for v in range(0,len(d))]
print("x座標：")
x = np.array(d[0][10:10+32:2])
xx = np.sum(x)
print (d[0][10:10+32:2])
print(xx*1.0/16)

print("y座標：")
y = np.array(d[0][11:11+32:2])
yy = np.sum(y)
print (d[0][11:11+32:2])
print(yy*1.0/16)
