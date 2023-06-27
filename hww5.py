import numpy as np 
import cv2 as cv 

img = cv.imread("OR4EJI0 (1).jpg")
cv.imshow("w",img)
img2 = img.copy()
print(img2.shape)
lower_yellow = np.array([15, 50, 180])
upper_yellow = np.array([40, 255, 255])

circle = np.zeros((2000,2000,3),dtype='uint8')
circle[:] = [0,0,0]
cv.circle(circle,(1000,1000),1000,(255,255,255),-1)
cv.imshow("Circle",circle)

hsv = cv.cvtColor(img,cv.COLOR_HSV2BGR)

# x,y = img.shpe[:]
# x2 = int(x/2)
# y2 = int(y/2)



mask = cv.inRange(img,lower_yellow,upper_yellow)
bitwise1 = cv.bitwise_and(img,circle)
cv.imshow("and",bitwise1)

mask = cv.inRange(img,lower_yellow,upper_yellow)
result = cv.bitwise_and(img,img,mask=mask)
cv.imshow('result',result)
cv.waitKey(0)
cv.destroyAllWindows()
