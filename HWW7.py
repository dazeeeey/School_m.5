import matplotlib.pyplot as plt 
import cv2 as cv

img = cv.imread("MicrosoftTeams-image (4).png")
gary_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
plt.subplot(221,xticks=[],yticks=[])
plt.title("HW-WEEK7")
plt.imshow(gary_img)
result = cv.adaptiveThreshold(gary_img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,9,5)
plt.subplot(224,title="adyhg",xticks=[],yticks=[])
plt.imshow(result,cmap="gray")
plt.show()

#ใช้เพราะเอาadptive gauss มาเเบ่งระดับหนึ่งเเละเอาbinaryมาเพิ่ทความชัด อติน next