import cv2
import numpy as np

my_img = cv2.imread("G:\\Python DB\\images\\face sample11.jpg")

#Defining Kernel(Filter) as 1/9([3x3]1)
kernel = np.ones((3,3) , np.float32) /9

#processed_img = cv2.filter2D(src_img ,-1 , Kernel)
op_my_img_3 = cv2.filter2D(my_img , -1 , kernel)
kernel = np.ones((5,5) , np.float32) /25
op_my_img_5 = cv2.filter2D(my_img , -1 , kernel)
kernel = np.ones((7,7) , np.float32) /49
op_my_img_7 = cv2.filter2D(my_img , -1 , kernel)
kernel = np.ones((13,13) , np.float32) /169
op_my_img_13 = cv2.filter2D(my_img , -1 , kernel)
kernel = np.ones((20,20) , np.float32) /400
op_my_img_20 = cv2.filter2D(my_img , -1 , kernel)
display_img = np.hstack((my_img , op_my_img_3,op_my_img_5,op_my_img_7,op_my_img_13,op_my_img_20))

cv2.imshow("Display" , display_img)

k = cv2.waitKey(0) &0xFF
if(k==ord('q')):
    cv2.destroyAllWindows()
