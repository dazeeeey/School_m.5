import cv2 as cv 

face_casecse = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv.imread("WIN_20230704_13_59_42_Pro.jpg")
gay_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

scale = 2
minNeighbor  = 3
face_detect  = face_casecse.detectMultiScale(gay_img)
print(face_detect)
for (x,y,w,h) in face_detect:
    cv.rectangle(img,(x,y),(w+x,y+h),(0,255,0),thickness=2)
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=10)
cv.imshow("facedetect",img)
cv.waitKey(0)
cv.destroyAllWindows