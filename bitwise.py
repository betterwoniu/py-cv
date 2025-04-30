import cv2 as cv
import numpy as np

img1 =cv.imread('./img/messi5.jpg')
img2 = cv.imread('./img/opencv-logo-white.png')

assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"

rows, cols = img2.shape[:2]
roi = img1[0:rows, 0:cols]

gary = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(gary, 0, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)

img2_fg = cv.bitwise_and(img2,img2,mask = mask)

dst = cv.add(img1_bg,img2_fg)

cv.imshow("dst", dst)
cv.imshow("img1_bg", img1_bg)
cv.imshow("img2_fg", img2_fg)
cv.imshow('roi',roi)
cv.imshow("mask", mask)
cv.imshow("mask_inv", mask_inv)


# img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# img = cv.resize(img,(300,300))
# ret, mask = cv.threshold(img, 10, 255, cv.THRESH_BINARY)
#
# rect = np.zeros((300,300), dtype=np.uint8)
# cv.rectangle(rect, (0,0), (200,200), (255,255,255), -1)
#
# circle = np.zeros((300,300), dtype=np.uint8)
# cv.circle(circle, (200,200), 100, (255,255,255), -1)
#
# # band = cv.bitwise_and(rect, circle,mask=mask)
# # band = cv.bitwise_or(rect, circle,mask=mask)
# # band = cv.bitwise_not(rect, circle,mask=mask)
# # band = cv.bitwise_xor(rect, circle,mask=mask)
#
# cv.imshow("mask", mask)
# cv.imshow("rect", rect)
# cv.imshow("circle", circle)
# cv.imshow("band", band)
cv.waitKey(0)
cv.destroyAllWindows()