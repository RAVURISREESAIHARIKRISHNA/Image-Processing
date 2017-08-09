import cv2
import numpy as np
from matplotlib import pyplot as plt

my_img = cv2.imread("G:\\Python DB\\images\\face sample10.jpg" )
plt.hist(my_img.ravel() , 256 , [0,256]);
cv2.imshow("image",my_img)
plt.show()
