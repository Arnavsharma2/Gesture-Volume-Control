import cv2
import mediapipe as mp #trained ml model library by google
import time #fps

cap = cv2.VideoCapture(0) # default cam = 0
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime = 0
currTime = 0

# Hand points guide
# https://mediapipe.readthedocs.io/en/latest/solutions/hands.html
while True:
    success, img = cap.read()
    if not success:
        print("Failed checks")
        continue
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # detects hands 
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks) # coords
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(img.shape)
                # print(id, ' ', cx, ' ', cy)
                # if id == 4:
                #     cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)    
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()
    fps = int(1/(cTime-pTime))
    pTime = cTime
    cv2.putText(img, str(fps), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 0, 255), 3)

    
    
    
    cv2.imshow('Image', img)
    cv2.waitKey(1)
    

    

