import cv2 as cv 

vid = cv.VideoCapture("Recording 2023-06-06 134851.mp4")
# img = cv.imread('Recording 2023-06-06 134851.mp4',1)
# image_copy = img.copy() 
# imgheight=img.shape[0]
# imgwidth=img.shape[1]
# print("Original Height and Width:", imgheight,"x", imgwidth)

# cv.imshow('Original Image', img)

# cropped_image = img[126:632,47:474] 
# cv.imshow("cropped", cropped_image)

while(vid.isOpened()):
    ret ,frame = vid.read()
    if ret == True :
        
        cropped_image = frame[150:632,47:474] 
        scale_f_up = cv.resize(cropped_image , None , fx = 1.8 , fy =1.8 ,interpolation=cv.INTER_LINEAR)
        cv.imshow('Frame',cropped_image)
        cv.imshow("scale up ",scale_f_up)
        key = cv.waitKey(1)
        if key == ord('q'):
            break 
    else:
     break
