import cv2
import numpy as np

img = cv2.imread("G:\\Python DB\\images\\face sample10.jpg" , 1)
retval , threshold_img  = cv2.threshold(img , 100 , 255 , cv2.THRESH_BINARY)

gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

retval2 , threshold_img_2 = cv2.threshold(gray_img , 100 , 255 , cv2.THRESH_BINARY)

cv2.imshow("Original",img)
cv2.imshow("Thresholded" , threshold_img)
cv2.imshow("Thresholded2" , threshold_img_2)


k = cv2.waitKey(0) &0xFF
if k==ord('q'):
    cv2.destroyAllWindows()
