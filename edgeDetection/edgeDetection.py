
# 출처 : https://leembedded.tistory.com/22?category=698391
# 명함 인식하기 
import numpy as np 
import cv2 

image = cv2.imread("naming_3.png")
orig = image.copy()

r = 800.0 / image.shape[0]
dim = (int(image.shape[1] * r), 800)
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) #이미지를 resize


#윤곽선 설정
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#그레이이미지로 바꿈
gray = cv2.GaussianBlur(gray, (3,3), 0) #가우시안블러 사용하여 외각 검출을 더 쉽게 함 
edged = cv2.Canny(gray, 75, 200) #Canny Edge Detection을 통해 edge을 검출 

print("step1 : edge detection")

cv2.namedWindow("image", cv2.WINDOW_NORMAL)#윈도우 사이즈 지정 
cv2.namedWindow("edged", cv2.WINDOW_NORMAL)#윈도우 사이즈 지정 
cv2.imshow("image", image)
cv2.imshow("edged", edged)

cv2.waitKey(0)
cv2.destroyAllWindows()


#--------------------------------------------------------------------------

import numpy as np 
import cv2 

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) 
# cv2.findContours(image, mode, method) / 출처 : https://datascienceschool.net/view-notebook/f9f8983941254a34bf0fee42c66c5539/
# image : 이진화된 이미지
# mode : 컨투어 찾는 방법 
# method : 컨투어를 찾을 때 사용하는 근사화 방법 
#_ : 계층관계는 필요가 없기 때문에 contour만 명시적으로 반환 받음
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5] #반환 받은 contour를 외곽이 그린 면적이 큰 순서대로 정렬해서 5만개만 받아옴 
#cv2.contourArea는 contour가 그린 면적을 의미 

#그렇게 받아온 contour를 순차적으로 탐색하면서 
for c in cnts : 
    peri = cv2.arcLength(c, True) #contour가 그리는 길이를 반환 
    approx = cv2.approxPolyDP(c, 0.02 * peri, True) #그 길이에 2%정도 오차를 해서 approxPolyDP을 통해 조금을 조금 근사해서 구함
    
    if len(approx) == 4 : #도형을 근사해서 추출한 외곽이 꼭지점 4개라면 그것을 명암의 외곽으로 본다
        screenCnt = approx 
        break
        
print("step2 : find Contours of Paper")
cv2.drawContours(image, [screenCnt], -1, (0,255,0),2) #drawContours를 통해 contours를 그림 
cv2.imshow("outline", image)

cv2.waitKey(0) 
cv2.destoryAllWindows()