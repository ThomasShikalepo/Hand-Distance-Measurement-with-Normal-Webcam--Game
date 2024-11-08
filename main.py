import math
import cv2
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector


#webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

#hand dectetor

detector = HandDetector(detectionCon=0.8, maxHands=3)

#find function
#x is the raw distance y is the value in cm
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 75, 80, 67, 59, 57]
y = [20, 25, 30, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 95, 100]
coff =np.polyfit(x, y, 2) # y =  Ax^2 + Bx + C


#loop
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # Update to get hands and img

    if hands:
        lmList = hands[0]['lmList']  # Correct way to access the landmarks
        x, y, w, h = hands[0]['bbox']  # Correct way to access the bounding box
        x1, y1, _= lmList[5]
        x2, y2, _= lmList[17]

        distance = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))

        A, B, C = coff
        distanceCM = A * distance ** 2 + B * distance + C

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)

        cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x + 5, y - 10))

    cv2.imshow("Image", img)
    cv2.waitKey(1)
