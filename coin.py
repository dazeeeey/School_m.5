import matplotlib.pyplot as plt 
import cv2 as cv 
import numpy as np
img = cv.imread("MicrosoftTeams-image (4).png")
img_grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imh = img.shape[0]
imw = img.shape[1]
binary = np.zeros((imh,imw),dtype=np.uint8)
for i in range(imh):
    for k in range(imw):
        if img_grey[i,k] > 80 :
            binary[i,k] = 255
        else : 
            binary[i,k] = 0
plt.imshow(binary , cmap="gray") 
plt.show()