import os
import glob
import scipy as sp

def file_rename(imageclass, folderpath, fextension):
    files = sp.array(glob.glob(folderpath + '/*.*')) # ディレクトリ内のファイルを全て取得

    for i in range(0, len(files)):
        fdir = folderpath + "/"
        #frename= str(imageclass) + "_" + str(i+1) + "." + str(fextension)
        frename= str(i+1)+ "." + str(fextension)
        os.rename(files[i], fdir+frename)

if __name__ == "__main__":
    for i in range(1, 34):
        file_rename(i,"G:/UCF50/"+str(i),"avi")