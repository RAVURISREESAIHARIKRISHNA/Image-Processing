import cv2
import numpy as np
from matplotlib import pyplot as plt

my_img = cv2.imread("G:\\Python DB\\images\\face sample10.jpg" )
color = ('b','g','r')
for i,col in enumerate(color):
    #  """
    #  cv2.calcHist(images , channels, mask , histSize , ranges [,hist[,accumulate]])
    #  More Information see docs
    #  """
    histr = cv2.calcHist(my_img , [i] , None , [256] , [0,256])
    plt.plot(histr , color = col)
    plt.xlim([0,256])
cv2.imshow("Image",my_img)
plt.show()
