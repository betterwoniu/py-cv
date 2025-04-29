import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('./img/water_coins.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

assert img is not None,"image No Found"

# 获取背景
# 二值化
ret,thread = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV  + cv.THRESH_OTSU)
#开运算去除噪点
kernel = np.ones((3,3), np.uint8)
result = cv.morphologyEx(thread, cv.MORPH_OPEN, kernel, iterations=2)
#通过膨胀获取背景
bg = cv.dilate(result,kernel,iterations=1)

# 获取前景物体
# 获取物体中心点到边缘的距离
dst = cv.distanceTransform(result,cv.DIST_L2,5)
ret,fg = cv.threshold(dst,0.8* dst.max(),255,cv.THRESH_BINARY)

# 获取未知待定区域  背景减去前景
unknown = cv.subtract(bg,np.uint8(fg))

# 获取前景联通域)
ret,marker = cv.connectedComponents(np.uint8(fg))
marker = marker+1
marker[unknown==255] = 0


# 分割图像
result = cv.watershed(img,marker)

img[result == -1] = [0,0,255]

cv.imshow('result',img)
cv.waitKey(0)

# plt.imshow(unknown,cmap='gray'),plt.show()
# cv.imshow('img',img)
# cv.imshow('thread',thread)
# cv.imshow('result',result)
# cv.waitKey(0)
# cv.destroyAllWindows()