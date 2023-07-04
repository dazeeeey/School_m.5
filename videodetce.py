import cv2 as cv

eye_casecse = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
face_casecse = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
vid = cv.VideoCapture(0)

while (vid.isOpened()):
      check,fram = vid.read()
      if check :
            gay_cap = cv.cvtColor(fram,cv.COLOR_BGR2GRAY)
            eye_detect = eye_casecse.detectMultiScale(gay_cap)
            face_detect = face_casecse.detectMultiScale(gay_cap)
            for (x,y,w,h) in eye_detect :
                  cv.rectangle(fram,(x,y),(x+w,y+h),(0,255,0),thickness=2)
            for (x,y,w,h) in face_detect :
                  cv.rectangle(fram,(x,y),(x+w,y+h),(0,0,255),thickness=2)
            
            cv.imshow("facedetect",fram)
            if cv.waitKey(1) & 0xff ==ord("q"):
                  break
      else : 
            break
cv.destroyAllWindows(7)
    
