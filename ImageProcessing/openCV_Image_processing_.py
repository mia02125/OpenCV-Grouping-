import cv2
#케니 엣지 검출하기 
img_gray = cv2.imread('naming.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("original", img_gray)

img_canny = cv2.Canny(img_gray, 50, 150)
cv2.imshow("Canny Edge", img_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------------------------------------------------------

import cv2


def nothing():
    pass


img_gray = cv2.imread('naming.png', cv2.IMREAD_GRAYSCALE)


cv2.namedWindow("Canny Edge")
#트랙바 이용하여 Canny엣지 조절하기 
cv2.createTrackbar('low threshold', 'Canny Edge', 0, 1000, nothing)
cv2.createTrackbar('high threshold', 'Canny Edge', 0, 1000, nothing)
#                     trackbarname    indowname    min max
cv2.setTrackbarPos('low threshold', 'Canny Edge', 50)
cv2.setTrackbarPos('high threshold', 'Canny Edge', 150)

cv2.imshow("Original", img_gray)

while True:

    low = cv2.getTrackbarPos('low threshold', 'Canny Edge')
    high = cv2.getTrackbarPos('high threshold', 'Canny Edge')

    img_canny = cv2.Canny(img_gray, low, high)
    cv2.imshow("Canny Edge", img_canny)

    if cv2.waitKey(1)&0xFF == 27:
        break


cv2.destroyAllWindows()

#--------------------------------------------------------------------

#허프 변환 직선 검출 예제(사진)
# -*- coding: cp949 -*-
# -*- coding: utf-8 -*- # 한글 주석쓰려면 이거 해야함
import cv2 # opencv 사용
import numpy as np

def grayscale(img): # 흑백이미지로 변환
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def canny(img, low_threshold, high_threshold): # Canny 알고리즘
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size): # 가우시안 필터
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices, color3=(255,255,255), color1=255): # ROI 셋팅

    mask = np.zeros_like(img) # mask = img와 같은 크기의 빈 이미지
    
    if len(img.shape) > 2: # Color 이미지(3채널)라면 :
        color = color3
    else: # 흑백 이미지(1채널)라면 :
        color = color1
        
    # vertices에 정한 점들로 이뤄진 다각형부분(ROI 설정부분)을 color로 채움 
    cv2.fillPoly(mask, vertices, color)
    
    # 이미지와 color로 채워진 ROI를 합침
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image

def draw_lines(img, lines, color=[0, 0, 255], thickness=2): # 선 그리기
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap): # 허프 변환
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)

    return line_img

def weighted_img(img, initial_img, α=1, β=1., λ=0.): # 두 이미지 operlap 하기
    return cv2.addWeighted(initial_img, α, img, β, λ)

image = cv2.imread('road.jpg') # 이미지 읽기
height, width = image.shape[:2] # 이미지 높이, 너비

gray_img = grayscale(image) # 흑백이미지로 변환
    
blur_img = gaussian_blur(gray_img, 3) # Blur 효과
        
canny_img = canny(blur_img, 70, 210) # Canny edge 알고리즘

vertices = np.array([[(50,height),(width/2-45, height/2+60), (width/2+45, height/2+60), (width-50,height)]], dtype=np.int32)
ROI_img = region_of_interest(canny_img, vertices) # ROI 설정

hough_img = hough_lines(ROI_img, 1, 1 * np.pi/180, 30, 10, 20) # 허프 변환

result = weighted_img(hough_img, image) # 원본 이미지에 검출된 선 overlap
cv2.imshow('result',result) # 결과 이미지 출력
cv2.waitKey(0) 



#--------------------------------------------------------------------

#허프 원 변환
import cv2
import numpy as np
 
img = cv2.imread('circle.png',0)

img = cv2.GaussianBlur(img, (3,3),0)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
 
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, # 1 : 
                            param1=50,param2=30,minRadius=0,maxRadius=0)
 #Hough_Gradient : 원 찾는 방법  # 1 : 원본이미지와 허브변환 카운팅 결과 이미지의 비
 #10 : 찾은 원들의 중심간 최소 거리, 중심과의 거리 > 입력값 => 나중에 찾은 원 무시
 #param1 : Canny Edge Detection의 Canny()함수의 인자로 들어가는 maxVal값
 #param2 : 허프변환 카운팅값(적으면 원하지않은 많은 원들이, 너무 크면 원을 못찾음)
circles = np.uint16(np.around(circles))
#circles 값들을 반올림하고 이를 UNIT16으로 변환 
for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)
 
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------------------------------------------------------

import cv2 
#이미지를 그레이 스케어화 하기 
img = cv2.imread("fruit.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------------------------------------------------------

#BGR컬러 영상의 채널 나누기 
import cv2
import numpy as np 

img = cv2.imread("fruit.jpg")
b, g, r = cv2.split(img)
# cv2.imshow('blue',b)
# cv2.imshow('green',g)
# cv2.imshow('red',r)

img[:,:,2] = 0
#img[:,:,1] = 0
#img[:,:,0] = 0
cv2.imshow('noRed',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------------------------------------------------------

#히스토그램 평활화 (명암비 높이기 )
import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('fruit.jpg', 0)
equ = cv2.equalizeHist(img) #opencv에서 제공하는 히스토그램평활화 함수 사용
res = np.hstack((img, equ)) # 그림을 옆으로 쌓는 함수

cv2.imshow('result', res)

#그래프로 표현 
plt.hist(img.ravel(), 256, [0, 256])
plt.hist(equ.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2 

#-------------------------------------------------------------------

# hsv 색상 검출하기
img_color = cv2.imread("fruit.jpg")
height, width = img_color.shape[:2]
img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

lower_blue = (20, 80-10, 20)
upper_blue = (60+30, 220, 220)
img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask)

cv2.imshow('img_color', img_color)
cv2.imshow('img_mask', img_mask)
cv2.imshow('img_result', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()


#-------------------------------------------------------------------