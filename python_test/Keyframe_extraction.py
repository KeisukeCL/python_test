# coding = UTF-8
import cv2
import scipy as sp
import os


def Keyframe_extraction(videodetasetpath, keypath, videonumber):
    Threshold = 0.8  # 相関関数の閾値の設定
    keyframepath = str(keypath) + "/" + str(videonumber)
    os.mkdir(keyframepath)  # 映像ごとにディレクトリを作成
    cap = cv2.VideoCapture(str(videodetasetpath) + "/" + str(videonumber) + ".avi")  # 映像の読み込み
    frame_number = 1  # フレーム番号の初期化
    keyframenumber = 1  # キーフレーム番号の初期化
    previousframe = 0   #最後にキーフレームを取得してから何フレームが経過したかを記録
    while cap.isOpened():
        ret, now_frame = cap.read()  # フレームとかを取得

        if ret == False:  # 次のフレームがなかったらbreak
            break

        hsv = cv2.cvtColor(now_frame, cv2.COLOR_BGR2HSV)  # フレームの色空間の変換
        hist_now = cv2.calcHist([hsv], [0, 1], None, [30, 32],
                                [0, 180, 0, 256])  # フレームのHSV2次元ヒストグラムを算出（[30, 32]がヒストグラムの量子化レベル）

        # 最初のフレーム用の例外処理
        if frame_number == 1:
            frame_number += 1
            hist_prev = hist_now
            cv2.imwrite(keyframepath + str(keyframenumber)+ ".jpg", now_frame)
            keyframenumber += 1

            continue

        corr = cv2.compareHist(hist_prev, hist_now, cv2.HISTCMP_CORREL)  # ヒストグラムの比較（相関係数を利用）
        hist_prev = hist_now  # 今のフレームのヒストグラムを前のフレームのヒストグラムを格納している変数に移動

        # 相関が閾値未満なら、そのフレームを保存
        if corr < Threshold:
            cv2.imwrite(keyframepath + str(keyframenumber) + ".jpg", now_frame)
            keyframenumber += 1
            previousframe = 0
            continue
        # 最後にキーフレームを取得してから10フレームが経過したらそのフレームもキーフレームとして保存
        elif previousframe == 10:
            cv2.imwrite(keyframepath + str(keyframenumber) + ".jpg", now_frame)
            keyframenumber += 1
            previousframe = 0
            continue
        #上記の条件を全く満たさないときはpreviousframeだけを+1
        else:
            previousframe += 1
            continue

    cap.release()


if __name__ == '__main__':
    for i in range(1, 51):
        Keyframe_extraction("G:/UCF50", "G:/UCF50_Segmentation", i)
        print(str(i) + "番目の映像ショット作成")