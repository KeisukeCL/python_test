#coding: utf-8
import io
import numpy as np


with open('1.txt','r') as f:
    d = np.array([v.rstrip().split('\t') for v in f.readlines()])

d = [list(map(lambda x:float(x), d[v])) for v in range(0,len(d))]
print("x座標：")
x = np.array(d[0][10:10+32:2])
xx = np.sum(x)
print (d[0][10:10+32:2])
print (d[0][1])
print(xx*1.0/16)

print("y座標：")
y = np.array(d[0][11:11+32:2])
yy = np.sum(y)
print (d[0][11:11+32:2])
print (d[0][2])
print(yy*1.0/16)

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