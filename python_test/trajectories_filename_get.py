import os
import glob


g = open("video.txt", "r")
f = open("UCF_segmentation.txt", "w")
line = g.readline()
while line:
    filename1 = line.split(".")
    filename2 =filename1[0].split("/")
    #print(filename2[2])
    #print(filename2[3])
    trajectoriespath = "G:/UCF50_Segmentation/" + filename2[2] + "_" + filename2[3] + ".avi"
    print(trajectoriespath)
    f.write(trajectoriespath)
    f.write('\n')
    line = g.readline()

f.close() 