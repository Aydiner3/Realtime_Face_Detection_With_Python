import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("faceD_Webcam/haarcascade_frontalface_default.xml")
while True:
    ret , frame = cap.read()
    face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 9)
    if ret:
        
        for (x,y,w,h) in face_rect:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,255), 10)

        cv2.imshow("Webcam",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): break