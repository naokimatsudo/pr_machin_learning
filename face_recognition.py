import cv2
import matplotlib.pyplot as plt
%matplotlib inline
#顔
face_cascade_path = "haarcascade_frontalface_alt.xml"
# カスケード分類器を作成
face_cascade = cv2.CascadeClassifier(face_cascade_path)
# 画像を読み込む
img = cv2.imread('face_jpg/tanaka.jpg')
# グレースケール化
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 出力結果用にコピー & RGB化
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#囲む色
color = (0, 255, 0)
#顔を検知
faces = face_cascade.detectMultiScale(img_gray)
for (x,y,w,h) in faces:
# 検知した顔を矩形で囲む
  cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
  roi_color = img[y:y+h, x:x+w]
#画像表示
plt.imshow(img)
