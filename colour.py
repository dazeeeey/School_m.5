import cv2 

picture = cv2.imread("images.bin")
picture2 = cv2.imread("starrr.jpg")
print(picture.shape) # check pixel 
print(picture.ndim) #เช็กมิติ 

print(picture2.shape)
print(picture2.ndim)
