import cv2 as cv

img = cv.imread("OIP.jpg",1)#color
img2 = cv.imread("OIP.jpg",0)#grey 
img3 = cv.imread("OIP.jpg",-1)#unchnage

cv.imshow('image_color',img)
cv.imshow('image_color2',img2)
cv.imshow('image_color3',img3)

cv.imwrite('OIP_geryscale.jpg',img2)#save pic

cv.waitKey(0)
cv.destroyAllWindows()
