import math
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import numpy as np

#webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

#hand dictecor

detector = HandDetector(detectionCon=0.8, maxHands=1)

#find function
#x is the raw distance y is the value in cm
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 75, 80, 67, 59, 57]
y = [20, 25, 30, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 95, 100]
coff =np.polyfit(x, y, 2) # y =  Ax^2 + Bx + c


#loop
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
       lmList = hands[0]['lmList']
       x1, y1, _=lmList[5]
       x2, y2, _= lmList[17]
       distance = math.sqrt((y2 - y1) **2 + (x2-x1)**2)
       A, B, C = coff
       distanceCM = A** 2 + B*distance + C
       print(distanceCM, distance)

    cv2.imshow("Image", img)
    cv2.waitKey(1)