import cv2 as cv 

img = cv.imread("OIP.jpg",1)#color

def click_position(event,x,y,flages,param):
    if event == cv.EVENT_LBUTTONDOWN or event == cv.EVENT_LBUTTONUP:
        cv.putText(img,f'x = {x}y = {y}',(x,y),1,3,(0,0,255),3)
        cv.imshow("click puttext",img)

cv.imshow("click puttext",img)

cv.setMouseCallback("click puttext",click_position)
cv.waitKey(0)
cv.destroyAllWindows()
    

