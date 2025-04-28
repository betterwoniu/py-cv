import cv2 as cv
import numpy as np

img = cv.imread('./img/register.jfif')

cv.imshow('img', img)
cv.waitKey(0)