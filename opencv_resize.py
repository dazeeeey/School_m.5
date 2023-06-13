import cv2 as cv 

img = cv.imread('OIP.jpg',1)

cv.imshow("Original image",img)

h,w,c = img.shape
print("Original height and width",h,'x',w)

down_width = 300 
down_height = 100 
down_point =(down_width,down_height)
resized_down = cv.resize(img , down_point , interpolation=cv.INTER_LINEAR)

up_width = 1800
up_hight = 900 
up_points = (up_width , up_hight)
resized_up = cv.resize(img , up_points , interpolation=cv.INTER_LINEAR)


scale_up = 1.2 
scale_down = 0.6

scale_f_down = cv.resize(img , None , fx = scale_down , fy =scale_down ,interpolation=cv.INTER_LINEAR)
scale_f_up = cv.resize(img , None , fx = scale_up , fy =scale_up ,interpolation=cv.INTER_LINEAR)

cv.imshow("Resized Down by defening height and width",resized_down)
cv.imshow("Resized Up image by defending height and width",resized_up)
cv.imshow("Resized Down by defending scaling factor ",scale_f_down)
cv.imshow("Resised up by defeing scailing factor ",scale_f_up)
cv.waitKey(0)
cv.destroyAllWindows
