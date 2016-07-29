# coding = UTF-8
import scipy as sp
import os
import glob


lists = sp.array(glob.glob("/Users/Keisuke/PycharmProjects/ForResearch/python_test/*.txt*"))
for file in lists:
    sp = os.path.basename(file).split(".")
    print(file)
    print(sp[0])
    print(sp[-1])