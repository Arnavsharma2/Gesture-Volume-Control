import cv2
import numpy as np
import time
import os, sys
import math
import osascript
import subprocess
# Add parent directory to path to find modules folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import modules.handTrackingModule as htm
wCam, hCam = 1980, 1080
cTime = 0
pTime = 0
vol = 0
minVol = 0
maxVol = 100
volBar = 700
volPer = 0


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    if not success:
        print("Camera read failed. Skipping frame.")
        continue
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw = False)
    if len(lmList) != 0:
        x4, y4 = lmList[4][1], lmList[4][2]
        x8, y8 = lmList[8][1], lmList[8][2]
        cv2.circle(img, (x4, y4), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x8, y8), 10, (0, 0, 255), cv2.FILLED)
        cv2.line(img, (x4, y4), (x8, y8), (0, 255, 0), 10)
        cx, cy = (x4+x8)//2, (y4+y8)//2
        cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
        
        length = int(math.hypot((x8-x4), (y8-y4)))
        # max: 450, min: 50
        # print(length)
        
        vol = np.interp(length, [50, 450], [minVol, maxVol])
        volBar = np.interp(length, [50, 450], [700, 150])
        volPer = np.interp(length, [50, 450], [0, 100])
        command = f"osascript -e 'set volume output volume {vol}'"
        os.system(command)
        # print(length, ' ', vol)
        if length < 50 or length > 450:
            cv2.circle(img, (cx, cy), 10, (255, 255, 255), cv2.FILLED)

        
    cv2.rectangle(img, (20, 150), (50, 700), (0, 255, 0), 2)
    cv2.rectangle(img, (20, int(volBar)), (50, 700), (0, 250, 0), cv2.FILLED)
    cv2.putText(img, f'{volPer} %', (20, 110), cv2.FONT_HERSHEY_COMPLEX, 1, (125, 0, 125), 3)
    cTime = time.time()
    fps = int(1/(cTime-pTime))
    pTime = cTime
    
    cv2.putText(img, f'FPS: {fps}', (30, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3)
    
    cv2.imshow('Image', img)
    cv2.waitKey(1)

