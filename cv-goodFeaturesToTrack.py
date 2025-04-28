import cv2 as cv
import numpy as np

img = cv.imread('./img/subpixel5.png')
assert img is not None,"image No Found"

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray,0,0.01,10)
corners = np.int8(corners)

for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,255, -1)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
