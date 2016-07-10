import os
import glob
import scipy as sp


files = sp.array(glob.glob('G:/test/*.*')) # ディレクトリ内のファイルを全て取得

for i in range(0, len(files)):
    fdir = "G:/test/"
    frename= str(i+1)+".mp4"
    os.rename(files[i], fdir+frename)