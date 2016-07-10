
import io
import numpy as np
import pickle as pc
# read dense trajectories to list
with open('test5.txt','r') as f:
       d = np.array([v.rstrip().split('\t') for v in f.readlines()])

# convert to float
d = [list(map(lambda x:float(x), d[v])) for v in range(0,len(d))]
with open ("test5.pkl", "wb") as dd:
    pc.dump(d, dd)