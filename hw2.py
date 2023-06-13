import cv2 as cv
import numpy as np 
import datetime


pointA = (0,0)
pointB = (3000,200)
img = cv.imread('OIP (1).jpg',1)
dtdatatime = str(datetime.datetime.now())

text ="when you see ur friend talk with girl"

cv.putText(img,dtdatatime,(1024,1024),1,2,(255,0,0),2)

cv.rectangle(img,pointA,pointB,(0,0,0),-1)
cv.putText(img,text,(800,100),1,2,(0,0,255),2)


cv.imshow("Image line",img)
cv.imwrite('hw2pic.jpgq',img)#save pic
cv.waitKey(0)