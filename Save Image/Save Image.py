import numpy as np
import cv2

my_img = cv2.imread("G:\\Python DB\\images\\face sample10.jpg" , 1)
cv2.imshow("Image" , my_img)
img = cv2.imread("G:\\Python DB\\images\\face sample10.jpg" , 0)
k = cv2.waitKey(0) & 0xFF
if k== ord('s'):
    cv2.imwrite("G:\\Python DB\\images\\face sample11.jpg",img)
    print("Success")
cv2.destroyAllWindows()
