import KeisukeKawamura as kk
import os
import cv2
#kk.file_rename("G:/TH14_Test_set_mp4/TH14_test_set_mp4")
cap = cv2.VideoCapture("G:/TH14_Test_set_mp4/TH14_test_set_mp4/1.mp4")
ret ,img = cap.read()
print(ret)