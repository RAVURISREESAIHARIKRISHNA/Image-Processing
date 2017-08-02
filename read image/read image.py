import numpy as np
import cv2

#Load an image
"""
Second Argument for imread() is
cv2.IMREAD_COLOR    1
cv2.IMREAD_GRAYSCALE    0
cv2.IMREAD_UNCHANGED    -1
"""
my_img = cv2.imread("G:\\Python DB\\images\\face sample10.jpg" , 1)
cv2.imshow('image' , my_img)
my_img_gray = cv2.imread("G:\\Python DB\\images\\face sample10.jpg",0)
cv2.imshow("Gray scale" , my_img_gray)
my_img_unch = cv2.imread("G:\\Python DB\\images\\face sample10.jpg",-1)
cv2.imshow("Unchanged",my_img_unch)
cv2.waitKey(0)
cv2.destroyAllWindows()
