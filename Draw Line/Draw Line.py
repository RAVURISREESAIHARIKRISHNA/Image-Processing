import cv2
import numpy as np

my_img = cv2.imread("G:\\Python DB\\images\\face sample10.jpg" , 1)
cv2.imshow('Line' , cv2.line(my_img , (6,206) , (443,225) , (0,0,225)))
k = cv2.waitKey(0) &0xFF
if(k==ord('q')):
    cv2.destroyAllWindows()
