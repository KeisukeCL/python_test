import cv2
import numpy as np
import scipy as sp

cap = cv2.VideoCapture("5.avi")
cv2.namedWindow("test")
hist = sp.zeros(2)
while cap.isOpened():
    ret, now_frame = cap.read()
    if ret ==False:
        break
    hsv = cv2.cvtColor(now_frame, cv2.COLOR_BGR2HSV)
    hist[1], xbins, ybins = sp.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])
    hist[0]=hist[1]
    corr = sp.corrcoef(hist[0], hist[1])
    if corr < 0.9:

    cv2.imshow("test", now_frame)
    cv2.waitKey(1)
cap.release()
cv2.destroyWindow("test")