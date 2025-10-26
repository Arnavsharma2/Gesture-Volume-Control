import cv2
import mediapipe as mp #trained ml model library by google
import time #fps

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.6, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, 
                                        max_num_hands = self.maxHands,
                                        min_detection_confidence = self.detectionCon,
                                        min_tracking_confidence = self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # detects hands 
        self.results = self.hands.process(imgRGB)
        
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handNum=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHands = self.results.multi_hand_landmarks[handNum]
            for id, lm in enumerate(myHands.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw: 
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)    
        return lmList
    
# def main():
#     pTime = 0
#     currTime = 0    
#     cap = cv2.VideoCapture(0) # default cam = 0
#     detector = handDetector()
#     while True:
#         success, img = cap.read()
#         img = detector.findHands(img)
#         lmList = detector.findPosition(img)
        
#         cTime = time.time()
#         fps = int(1/(cTime-pTime))
#         pTime = cTime
        
#         cv2.putText(img, str(fps), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 0, 255), 3)

#         cv2.imshow('Image', img)
#         cv2.waitKey(1)
            
# if __name__ == "__main__":
#     main()
        