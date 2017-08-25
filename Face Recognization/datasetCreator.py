# MIT License
#
# Copyright (c) 2017 RAVURI SREE SAI HARI KRISHNA
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import cv2

cap = cv2.VideoCapture(0)
face_cascade  = cv2.CascadeClassifier('C://opencv//sources//data//haarcascades//haarcascade_frontalface_default.xml')

Id = raw_input("Please enter your ID : ")
sampleNumber = 0

while(True):
    ret , img = cap.read()
    grayImg = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImg , 1.3 , 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img , (x,y) , (x+w,y+h) , (0,0,255) , 0)
        sampleNumber = sampleNumber +1
        cv2.imwrite("dataSet/user."+Id+"."+str(sampleNumber)+".jpg" , grayImg[y:y+h , x:x+w])
        cv2.imshow("Frame" , img)
    k = cv2.waitKey(100) &0xFF
    if(k==ord('q')):
        break
        cv2.destroyAllWindows()
    else:
        if(sampleNumber>20):
            break
cap.release()
cv2.destroyAllWindows()
