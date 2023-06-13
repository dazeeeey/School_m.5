import cv2 as cv 

vid = cv.VideoCapture("Recording 2023-06-06 134851.mp4")

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