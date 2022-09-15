import cv2
import mediapipe as mp
import time

#Capture from source 0
cap = cv2.VideoCapture(0)

#Define Processing Rules for Hands Objects
mpHands = mp.solutions.hands
hands = mpHands.Hands()

#Drawing Utilities with Specified Settings
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()

    #Convert CV2 BGR image to RGB
    vidRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #Recognize hands
    results = hands.process(vidRGB)

    #Draw over live feed with hand landmarks and connections between marks
    if results.multi_hand_landmarks:
        for handLandMark in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLandMark, mpHands.HAND_CONNECTIONS)

    #Display Captured Feed
    cv2.imshow("Image", img)
    cv2.waitKey(1)