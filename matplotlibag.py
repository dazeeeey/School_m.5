import matplotlib.pyplot as plt 
import cv2 as cv

img = cv.imread("WIN_20230704_13_59_33_Pro.jpg")

# x = [1,3,4,8]
# x2 = [1,2,6,8]
# y = [7,10,8,9]
# y2 = [3,6,8,10]

# plt.plot(x,y,label='Sereies 1')
# plt.plot(x2,y2,label='Sereies 2')
# plt.xlabel('x-title')
# plt.ylabel('y-title')
# plt.title("ChartTitle1\nChartTitle2")
# plt.legend()

# plt.imshow(img[:,:,::-1])

plt.subplot(1,3,1,title="BRG",xticks=[],yticks=[])
plt.imshow(img)
plt.subplot(1,3,2,title="BRG",xticks=[],yticks=[])
plt.imshow(img[:,:,::-1])
plt.subplot(1,3,3,title="BRG",xticks=[],yticks=[])
plt.imshow(img)

plt.show()