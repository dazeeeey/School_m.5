import cv2 as cv 
import numpy as np

img = cv.imread("OIP.jpg",1)#color

def click_position(event,x,y,flages,param):
    if event == cv.EVENT_LBUTTONDOWN or event == cv.EVENT_LBUTTONUP:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        text =(f'R:={red}G:{green}B:{blue}')
        cv.putText(img,text,(x,y),1,1,(0,0,255),3)
        cv.imshow("click puttext",img)
cv.imshow("click puttext",img)

cv.setMouseCallback("click puttext",click_position)
cv.waitKey(0)
cv.destroyAllWindows()
    

