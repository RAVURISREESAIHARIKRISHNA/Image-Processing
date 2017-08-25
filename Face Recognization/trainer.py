import os
import cv2
import numpy as np
from PIL import Image
recognizer = cv2.createLBPHFaceRecognizer()
face_cascade  = cv2.CascadeClassifier('C://opencv//sources//data//haarcascades//haarcascade_frontalface_default.xml')

def getImagesAndLebels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage , 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = face_cascade.detectMultiScale(imageNp)

        for(x,y,w,h) in faces:
            faceSamples.append( imageNp[y:y+h , x:x+w] )
            Ids.append(Id)
    return faceSamples , Ids


faces,Ids  = getImagesAndLebels("dataSet")
recognizer.train(faces , np.array(Ids))
recognizer.save("trainer/Trainer.yml")
