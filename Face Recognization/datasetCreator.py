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
