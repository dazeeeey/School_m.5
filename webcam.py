import cv2 as cv 

vid = cv.VideoCapture(0)

while(vid.isOpened()):
    ret ,frame = vid.read()
    if ret == True :
        cv.imshow('Frame',frame)
        key = cv.waitKey(33)
        if key == ord('q'):
            break 
    else:
     break

vid.release()
cv.destroyAllWindows()