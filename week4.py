import cv2 as cv

img = cv.imread("OIP.jpg",1)#color
cv.imshow('image_color',img)

cv.waitKey(0)
cv.destroyAllWindows()

imageLine = img.copy()
pointA = (200,80)
pointB = (450,500)

# cv.arrowedLine(imageLine,pointA,pointB,(255,255,0),thickness=3)
cv.rectangle(imageLine,pointA,pointB,(255,255,0),thickness=3) # tkicnes -1 =ทึบ
cv.imshow("Image line",imageLine)
cv.waitKey(0)