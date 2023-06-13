import cv2 as cv 

vid = cv.VideoCapture(0)
frame_width = vid.get(cv.CAP_PROP_FRAME_WIDTH)
frame_hight = vid.get(cv.CAP_PROP_FRAME_HEIGHT)
frame_size = (int(frame_width) , int(frame_hight))
fps = 30 

result =cv.VideoWriter('video/video.avi',cv.VideoWriter_fourcc(*'MPJG'),30,frame_size)

while(vid.isOpened()):
    ret ,frame = vid.read()
    if ret == True :
        
        result.write(frame)

        cv.imshow('Frame',frame)
        key = cv.waitKey(1)
        if key == ord('q'):
            break 
    else:
     break

vid.release()
result.release()

cv.destroyAllWindows()