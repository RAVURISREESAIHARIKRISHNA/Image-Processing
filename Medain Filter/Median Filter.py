import cv2
import numpy as np

my_img = cv2.imread("G:\\Python DB\\images\\noise face sample11.jpeg")

# img = cv2.medianBlur( src_img , Kernel_Size)
median_my_img_3 = cv2.medianBlur(my_img , 3)
median_my_img_7 = cv2.medianBlur(my_img , 7)
median_my_img_11 = cv2.medianBlur(my_img , 11)

display = np.hstack((my_img , median_my_img_3,median_my_img_7,median_my_img_11))
cv2.imshow("display" , display)
k = cv2.waitKey(0) &0xFF
if(k==ord('q')):
    cv2.destroyAllWindows()
