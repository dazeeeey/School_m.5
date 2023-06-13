import cv2 as cv
import numpy as np 
import datetime    
img = cv.imread("OIP.jpg",1)#color
cv.imshow('image_color',img)
vid = cv.VideoCapture(0)

while(vid.isOpened()):
    ret ,frame = vid.read()
    if ret == True :
        dtdatatime = str(datetime.datetime.now())
        cv.putText(frame,dtdatatime,(125,220),1,2,(255,0,0),2)
        cv.imshow('Frame',frame)
        key = cv.waitKey(33)
       
        if key == ord('q'):
            break 
    else:
     break

vid.release()
cv.destroyAllWindows()

cv.waitKey(0)
cv.destroyAllWindows()

imageLine = img.copy()
x,y =imageLine.shape[:2]
print(x,y)
y =int(y/2)
x=int(x/2)
circle_center = (y,x)
# pointA = (200,80)0
# pointB = (450,500)
radius = 100 
axus1 = (100,50)
axus2 = (125,50)
# cv.arrowedLine(imageLine,pointA,pointB,(255,255,0),thickness=3)
# cv.rectangle(imageLine,pointA,pointB,(255,255,0),thickness=3) # tkicnes -1 =ทึบ
# cv.circle(imageLine,circle_center,radius,(0,0,255),thickness=3)#tkicnes -1 =ทึบ
# cv.ellipse(imageLine,circle_center,axus1,0,0,360,(255,0,0),thickness=3)
# cv.ellipse(imageLine,circle_center,axus2,0,0,180,(255,0,0),thickness=-1)
# point = np.array ([(100,100),(150,150),(125,200),(75,200),(50,150)])
# cv.fillConvexPoly(imageLine,point,(255,0,0))
cv.putText(imageLine,"Praphat",circle_center,1,10,(255,0,0),2)
cv.imshow("Image line",imageLine)
cv.waitKey(0)