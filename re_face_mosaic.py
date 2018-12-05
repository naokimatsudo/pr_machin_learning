#coding:utf-8

import numpy as np
import cv2

#顔探索用のカスケード型分類器を取得
cascade_file = "haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(cascade_file)

img = cv2.imread("tanaka.jpg")
result = cv2.imread("tanaka.jpg")

#読み込んだ画像をグレースケールに変換
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#分類器で顔を認識する
face = face_cascade.detectMultiScale(gray,1.3,5)

if 0 < len(face):

    print("get face")

    for (x,y,w,h) in face:

        #顔の部分だけ切り抜いてモザイク処理をする
        cut_img = img[y:y+h,x:x+w]
        cut_face = cut_img.shape[:2][::-1]
        #10分の1にする
        cut_img = cv2.resize(cut_img,(cut_face[0]//10, cut_face[0]//10))
        #画像を元のサイズに拡大
        cut_img = cv2.resize(cut_img,cut_face,interpolation = cv2.INTER_NEAREST)

        #モザイク処理した部分を重ねる
        result[y:y+h,x:x+w] = cut_img

else:

    print("no face")


cv2.imshow("face mosaic",result)
#cv2.imwrite("output file name",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
