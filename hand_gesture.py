import cv2
import mediapipe as mp
import time
import math


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRgb)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    cv2.waitKey(1)