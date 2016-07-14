import cv2
import scipy as sp
import os
import multiprocessing

def video_shot_segmentation(videodetasetpath, segmentvideopath, videonumber):
    Threshold = 0.8 #相関関数の閾値の設定
    videopath = str(segmentvideopath)+"/" + str(videonumber) 
    os.mkdir(videopath)   #映像ごとにディレクトリを作成
    cap = cv2.VideoCapture(str(videodetasetpath)+"/" + str(videonumber)+".mp4") #映像の読み込み
    frame_number = 1  #フレーム番号の初期化
    shot_number = 1 #ショット番号の初期化

    while cap.isOpened():
        ret, now_frame = cap.read() #フレームとかを取得

        if ret == False:   #次のフレームがなかったらbreak
         out.release()
         break

        hsv = cv2.cvtColor(now_frame, cv2.COLOR_BGR2HSV)    #フレームの色空間の変換
        hist_now = cv2.calcHist([hsv], [0, 1], None, [30, 32], [0, 180, 0, 256])  #フレームのHSV2次元ヒストグラムを算出（[30, 32]がヒストグラムの量子化レベル）

        if frame_number == 1:   #最初のフレーム用の例外処理
            frame_number += 1
            hist_prev = hist_now
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            size = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            out = cv2.VideoWriter(videopath + "/" + str(shot_number)+".mp4", cv2.VideoWriter_fourcc("X","V","I","D"), fps, size)
            continue
    
        corr = cv2.compareHist(hist_prev, hist_now, cv2.HISTCMP_CORREL) #ヒストグラムの比較（相関係数を利用）
        hist_prev = hist_now    #今のフレームのヒストグラムを前のフレームのヒストグラムを格納している変数に移動
        if corr < Threshold:    #相関が閾値未満なら、映像を分割
            out.release()
            shot_number += 1
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            size = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            out = cv2.VideoWriter(videopath + "/" + str(shot_number) + ".mp4", cv2.VideoWriter_fourcc("X", "V", "I", "D"), fps, size)

        else:   #相関が大きければそのまま
            out.write(now_frame)
  
    cap.release()
 

if __name__ == '__main__':
    for i in range(1, 1575):
       video_shot_segmentation("G:/TH14_Test_set_mp4/TH14_Test_set_mp4","G:/TH14_Test_set_mp4", i)
       print(str(i)+ "番目の映像ショット作成")