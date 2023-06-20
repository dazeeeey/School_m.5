import cv2 as cv 
import numpy as np

img = cv.imread("OIP.jpg",1)#color
point = []
def click_position(event,x,y,flages,param):
     if event == cv.EVENT_LBUTTONDOWN :
        point.append((x,y))
     elif event == cv.EVENT_LBUTTONUP :
         point.append((x,y))
         if len(point) >2 :
             cv.rectangle(img,point[-1],point[-2],(255,255,0),thickness=3)
         cv.imshow("click puttext",img)
   
cv.imshow("click puttext",img)

cv.setMouseCallback("click puttext",click_position)
cv.waitKey(0)
cv.destroyAllWindows()

