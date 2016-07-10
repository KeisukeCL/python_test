import io
import numpy as np
import pickle as pc

with open ("test5.pkl", "rb") as f:
    x=pc.load(f)

xx = np.array(x[0][10:10+32:2])
print (x[0][10:10+32:2])