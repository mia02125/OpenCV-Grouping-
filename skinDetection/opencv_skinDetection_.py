
import cv2 
import numpy as np 
# hsv 색상 검출하기 (살색)
img_color = cv2.imread("C:\\Users\\mia02\\openCV\\skin.jpg")
img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2YCrCb)

lower_blue = np.array([0, 133, 77]) 
upper_blue = np.array([255,173,127])
img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
#inRange : lower, Upper의 지정된 범위의 해당되는 부분은 그 값 그대로 나머지는 0으로 채워져 결과값 반환
img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask)
#bitwise_and : 비트연산(이미지에서 배경을 지우거나 일부를 찾아내는 함수)
# 출처 : https://copycoding.tistory.com/156
cv2.imshow('img_color', img_color) #원본 
cv2.imshow('img_mask', img_mask) # 디텍딩된 부분만 YCrCb값 그대로 출력
cv2.imshow('img_result', img_result) # 디텍팅된 부분을 1 출력 / 나머지는 0 

cv2.waitKey(0)
cv2.destroyAllWindows()