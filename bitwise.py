import numpy as np 
import cv2 as cv 

rectangle = np.zeros((300,300,3), dtype='uint8')
rectangle[:] = [255,255,255]
cv.rectangle(rectangle,(25,25),(275,275),(0,0,255),-1)
cv.imshow("Rectrangle",rectangle)

circle = np.zeros((300,300,3),dtype='uint8')
circle[:] = [255,255,255]
cv.circle(circle,(150,150),150,(0,0,255),-1)
cv.imshow("Circle",circle)

bitwise1 = cv.bitwise_and(rectangle,circle)
cv.imshow("and",bitwise1)

bitwise2 = cv.bitwise_or(rectangle,circle)
cv.imshow("or",bitwise2)

bitwise3 = cv.bitwise_not(rectangle)
cv.imshow("not",bitwise3)


bitwise4 = cv.bitwise_xor(rectangle,circle)
cv.imshow("xor",bitwise4)

cv.waitKey(0)
cv.destroyAllWindows