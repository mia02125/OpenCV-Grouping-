
import cv2 
cap = cv2.VideoCapture('ub.mp4') # 카메라 생성
font  = cv2.FONT_HERSHEY_SIMPLEX

cv2.namedWindow('Face')
face_cascade = cv2.CascadeClassifier('C:\\Users\\com4in\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

while(True) : 
    ret, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayframe, 1.8, 2, 0, (30,30))
    
    for(x,y,w,h) in faces : 
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3,4,0)
        cv2.putText(frame, 'Detected Face', (x-5,y-5), font, 0.9, (255,255,0),2)
    cv2.imshow('Face', frame)

