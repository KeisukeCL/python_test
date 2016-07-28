# coding = UTF-8
import cv2
import scipy as sp

svm = cv2.ml.SVM_create()
help(cv2.ml.SVM_create())
sv = svm.getUncompressedSupportVectors("1.xml")