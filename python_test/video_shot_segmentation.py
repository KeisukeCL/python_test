import cv2
import scipy as sp

Threshold = 0.9
cap = cv2.VideoCapture("5.avi")
cv2.namedWindow("test")
frame_number = 1  #フレーム番号の初期化
shot_number = 1 #ショット番号の初期化
while cap.isOpened():
    ret, now_frame = cap.read() #フレームとかを取得
    if ret == False:   #次のフレームがなかったらbreak
        out.release()
        break

    hsv = cv2.cvtColor(now_frame, cv2.COLOR_BGR2HSV)    #フレームの色空間の変換
    hist_now = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])  #フレームのHSV2次元ヒストグラムを算出

    if frame_number == 1:   #最初のフレーム用の例外処理
        frame_number += 1
        hist_prev = hist_now
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        size = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(str(shot_number)+".mp4", cv2.VideoWriter_fourcc("D","I","V","X"), fps, size)
        continue
    
    corr = cv2.compareHist(hist_prev, hist_now, cv2.HISTCMP_CORREL) #ヒストグラムの比較（相関係数を利用）
    hist_prev = hist_now    #今のフレームのヒストグラムを前のフレームのヒストグラムを格納している変数に移動
    print(corr)
    if corr < Threshold:
        out.release()
        shot_number += 1
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        size = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(str(shot_number) + ".mp4", cv2.VideoWriter_fourcc("D", "I", "V", "X"), fps, size)

    else:
        out.write(now_frame)

    frame_number += 1
  
    cv2.imshow("test", now_frame)
    cv2.waitKey(1)
cap.release()
cv2.destroyWindow("test")