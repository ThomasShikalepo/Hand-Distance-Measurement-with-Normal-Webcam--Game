import math
import cv2
import cvzone
import numpy as np
from PIL.ImagePalette import random
from cvzone.HandTrackingModule import HandDetector
import random


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

#game variable
cx, cy = 250, 250
color = (255,0,255)
counter = 0

#loop
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=False)  # Update to get hands and img

    if hands:
        lmList = hands[0]['lmList']  # Correct way to access the landmarks
        x, y, w, h = hands[0]['bbox']  # Correct way to access the bounding box
        x1, y1, _= lmList[5]
        x2, y2, _= lmList[17]

        distance = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))

        A, B, C = coff
        distanceCM = A * distance ** 2 + B * distance + C
        #print(distanceCM)
        if distanceCM < 40:
            if x< cx < x + w and y < cy < y + h:
                counter = 1

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
        cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x + 5, y - 10))

    if counter:
        counter +=1
        color = (0,255,0)
        if counter ==3:
            cx = random.randint(100, 1100)
            cy = random.randint(100, 600)
            color = (255,0,255)
            counter = 0


    #Draw Button
    cv2.circle(img, (cx, cy), 30,color, cv2.FILLED)
    cv2.circle(img, (cx, cy), 10,(255,255,255), cv2.FILLED)
    cv2.circle(img, (cx, cy), 20,(255,255,255), 2)
    cv2.circle(img, (cx, cy), 30,(50,50,50), 2)

    #game HUD
    cvzone.putTextRect(img, 'Time: 30',(1000,75),scale = 3, offset=20)
    cvzone.putTextRect(img, 'Scare: 04',(60,75),scale = 3, offset=20)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
