import cv2
import numpy as np
from matplotlib import pyplot as plt

my_img = cv2.imread("G:\\Python DB\\images\\face sample10.jpg",0 )
img = cv2.imread("G:\\Python DB\\images\\face sample10.jpg")
cv2.imshow("Original",img)
eq_hist_my_img = cv2.equalizeHist(my_img)
final_img = np.hstack((my_img , eq_hist_my_img))
cv2.imshow("Histogram Equalization",final_img)
my_img_hist = my_img
eq_hist_my_img_hist = eq_hist_my_img
plt.hist(my_img_hist.ravel(),256,[0,256] , label='before');
plt.hist(eq_hist_my_img_hist.ravel(),256,[0,256] , label='after');
plt.legend(loc='upper right')
plt.show()

k = cv2.waitKey(0) & 0xFF
if k== ord('q'):
    cv2.destroyAllWindows()
