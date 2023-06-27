import cv2 as cv 
import numpy as np 

img = cv.imread("lunares.png")
upper_green = np.array([100,255,130])
low_green = np.array([0,50,0])
mask = cv.inRange(img,low_green,upper_green)
result = cv.bitwise_and(img,img,mask=mask)

cv.imshow("orgin",img)
cv.imshow("detect colour mask",mask)
cv.imshow("result detect color",result)
cv.waitKey(0)
cv.destroyAllWindows()