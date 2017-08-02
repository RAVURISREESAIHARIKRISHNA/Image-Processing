import cv2
import numpy as np
my_img = cv2.imread("G:\\Python DB\\images\\face sample10.jpg" , 1)
cv2.imshow('Image' , cv2.rectangle(my_img , (123,4) ,(332,210),(0,0,255)))
k = cv2.waitKey(0) &0xFF
if k==ord('q'):
    cv2.destroyAllWindows()
