#type: ignore
import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0) 


solutions_hand = mp.solutions.hands 
solutions_draw = mp.solutions.drawing_utils

hands = solutions_hand.Hands(min_detection_confidence=0.8,
                             min_tracking_confidence=0.5) 

while True:
    success, image = camera.read()
    image = cv2.flip(image, 1)
    cv2.imshow("Screen", image)

    results = hands.process(image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()
