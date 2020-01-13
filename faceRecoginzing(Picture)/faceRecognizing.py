#openCV 사진 얼굴 인식 
#출처 : https://hwangpy.tistory.com/1
import numpy as np
import cv2
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('C:\\Users\\com4in\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
#라이브러리 생성 
img = cv2.imread('iub.jpg') #이미지 읽어들이기 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#이미지를 불러오고 이미지를 흑백으로 바꿈(이미지 처리에 색깔이 필요없기 떄문에)
faces = face_cascade.detectMultiScale(gray, 1.5, 2, minSize = (10,10))
#얼굴의 스케일 조정
#괄호안의 숫자를 바꾸면서 얼굴의 크기에 따라 얼굴과 눈을 검출 
#괄호안의 숫자가 커질수록 작은 얼굴 감지 
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 
    # (R,G,B)의 명도
#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = img[y:y+h, x:x+w]
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()