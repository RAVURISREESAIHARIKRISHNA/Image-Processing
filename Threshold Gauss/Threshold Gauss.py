import cv2
import numpy as np

img = cv2.imread("G:\\Python DB\\images\\face sample10.jpg" , 1)


gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

retval2 , threshold_img_2 = cv2.threshold(gray_img , 100 , 255 , cv2.THRESH_BINARY)

gauss = cv2.adaptiveThreshold(gray_img , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 115 , 1)

cv2.imshow("Original",img)

cv2.imshow("Thresholded2" , threshold_img_2)
cv2.imshow("gauss" , gauss)


k = cv2.waitKey(0) &0xFF
if k==ord('q'):
    cv2.destroyAllWindows()
