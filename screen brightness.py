import cv2
import mediapipe as mp
from math import hypot
import screen_brightness_control as sbc
import numpy as np

#Modules for hand detection
mpHands=mp.solutions.hands
hands=mpHands.Hands(static_image_mode=False,min_detection_confidence=0.75,max_num_hands=1)
Draw=mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)
while True:
    sucess,frame=cap.read()
    frame=cv2.flip(frame,1)
    framergb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    process=hands.process(framergb)

    landmarklist=[]
    if process.multi_hand_landmarks:
        for handlm in process.multi_hand_landmarks:
            for id,lm in enumerate(handlm.landmark):

                height,width,color_channels=frame.shape
                x,y=int(lm.x*width),int(lm.y*height)
                landmarklist.append([id,x,y])

            Draw.draw_landmarks(frame,handlm,mpHands.HAND_CONNECTIONS)

    if landmarklist!=[]:

        x1,y1=landmarklist[4][1],landmarklist[4][2]
        x2,y2=landmarklist[8][1],landmarklist[8][2]

        cv2.circle(frame,(x1,y1),7,(0,255,0),cv2.FILLED)
        cv2.circle(frame,(x2,y2),7,(0,255,0),cv2.FILLED)
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),3)

        L=hypot(x2-x1,y2-y1)
        b_level=np.interp(L,(15,220),[0,100])
        sbc.set_brightness(int(b_level))

    cv2.imshow('BV',frame)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
cv2.destroyAllWindows



