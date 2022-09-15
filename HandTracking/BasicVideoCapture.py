import cv2
import mediapipe as mp
import time

#Capture from source 0
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    #Display Captured Feed
    cv2.imshow("Image", img)
    cv2.waitKey(1)