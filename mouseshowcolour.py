import cv2 as cv 
import numpy as np

img = cv.imread("OIP.jpg",1)#color

def click_position(event,x,y,flages,param):
    if event == cv.EVENT_MOUSEMOVE :
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        imgcolour = np.zeros([300,300,3],np.uint8)
        imgcolour[:]=[blue,green,red]   
        cv.imshow("w",imgcolour)
        cv.imshow("click puttext",img)
cv.imshow("click puttext",img)

cv.setMouseCallback("click puttext",click_position)
cv.waitKey(0)
cv.destroyAllWindows()
    

