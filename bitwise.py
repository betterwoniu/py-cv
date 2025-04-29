import cv2 as cv
import numpy as np

img = cv.imread("./img/opencv-logo.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret,mask = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
mask_inv = cv.bitwise_not(mask)

bg = cv.bitwise_and(gray, gray, mask=mask_inv)

cv.imshow("mask_inv", mask_inv)
cv.imshow("mask", mask)
# cv.imshow("img", img)
cv.imshow("bg", bg)
cv.waitKey(0)
cv.destroyAllWindows()