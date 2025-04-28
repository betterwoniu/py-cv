import cv2 as cv
import numpy as np

img = cv.imread('./img/subpixel5.png')
assert img is not None,"image No Found"

#灰度化
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blockSize:检测角区域  ksize - 使用的 Sobel 导数的孔径参数。 k - 方程中的 Harris 探测器自由参数。
dst = cv.cornerHarris(gray, 2, 3, 0.04)
print(dst.max())
img[dst>0.01*dst.max()]=[0,0,255]


cv.imshow('dst', img)
cv.waitKey(0)