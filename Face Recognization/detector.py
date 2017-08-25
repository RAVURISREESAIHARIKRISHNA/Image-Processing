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
import numpy as np

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load("trainer/Trainer.yml")

faceCascade = cv2.CascadeClassifier('C://opencv//sources//data//haarcascades//haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX , 1,1,0,1,1)

while True:
    ret , image = cap.read()
    grayImage = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayImage,1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(image , (x-50,y-50) , (x+w+50,y+h+50) , (0,0,255) ,1)
        Id , conf = recognizer.predict(grayImage[y:y+h , x:x+w])
        if(conf>=50):
            Id="Unknown"
        cv2.cv.PutText(cv2.cv.fromarray(image) , str(Id) , (x,y+h) , font , 255)
    cv2.imshow("image",image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
