import cv2 as cv
import numpy as np



def openOperation_denoise(imag):
    # 自动计算适合的核大小去除噪点,效果不是很好
    height,width = imag.shape[:2]
    kernel_size =  max(1, min(height, width) // 100)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    result = cv.morphologyEx(imag, cv.MORPH_OPEN, kernel)
    return result

def progressive_denoise(image, max_iter=3):
    temp = image.copy()
    for i in range(1, max_iter+1):
        kernel = np.ones((i,i), np.uint8)
        opened = cv.morphologyEx(temp, cv.MORPH_OPEN, kernel)
        # 比较与原图的差异，保留足够大的连通区域
        diff = cv.absdiff(opened, temp)
        _, diff = cv.threshold(diff, 0, 255, cv.THRESH_BINARY)
        temp = cv.bitwise_or(temp, diff)
    return temp

img = cv.imread('../py-pillow/captcha_001.png')
assert img is not None,"image No Found"
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# 二值化
ret,thread = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

# result = openOperation_denoise(thread)

result = progressive_denoise(thread,10)

cv.imshow('img',result)
cv.waitKey(0)

