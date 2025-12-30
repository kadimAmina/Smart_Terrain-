from picamera2 import Picamera2 
import cv2 
import time 
import os 
import numpy as np
import RPi.GPIO as GPIO
from datetime import datetime

# ===== GPIO ===== 
LED = 18 
BUZZER = 23 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(LED, GPIO.OUT) 
GPIO.setup(BUZZER, GPIO.OUT) 
# ===== Camera ===== 
picam2 = Picamera2() 
config = picam2.create_preview_configuration(
     main={"format": "RGB888", "size": (640, 480)} 
)
picam2.configure(config) 
picam2.start() 
# ===== Data ===== 
score = 0 
goal_detected = False 
recording = False 
os.makedirs("SmartGoal/goals", exist_ok=True) 
score_file = "SmartGoal/score.txt" 
# Goal zone 
GOAL_X1, GOAL_Y1 = 200, 250 
GOAL_X2, GOAL_Y2 = 440, 460 

video_writer = None 
start = 0 
print("Smart Goal started") 
while True: 
    frame = picam2.capture_array() 
    
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) 
    blur = cv2.GaussianBlur(gray, (9, 9), 1.5) 
    
    circles = cv2.HoughCircles(
        blur, 
        cv2.HOUGH_GRADIENT, 
        1, 
        80, 
        param1=100, 
        param2=30, 
        minRadius=15, 
        maxRadius=80 
    ) 
    # Draw goal zone 
    cv2.rectangle(
        frame, 
        (GOAL_X1, GOAL_Y1), 
        (GOAL_X2, GOAL_Y2), 
        (255, 0, 0), 
        2 
    ) 
    if circles is not None: 
        circles = np.uint16(np.around(circles)) 
        for x, y, r in circles[0]: 
            cv2.circle(frame, (x, y), r, (0, 255, 0), 2) 
            
            if GOAL_X1 < x < GOAL_X2 and GOAL_Y1 < y < GOAL_Y2 and not goal_detected: 
                score += 1 
                goal_detected = True 
                
                print("GOAL | Score =", score) 
                # GPIO alert 
                GPIO.output(LED, 1) 
                GPIO.output(BUZZER, 1) 
                # Save video 
                filename = ( 
                    "SmartGoal/goals/goal_"
                    + 
datetime.now().strftime("%Y%m%d_%H%M%S") 
                    + ".avi"
                )
                
                video_writer = cv2.VideoWriter(
                    filename, 
                    cv2.VideoWriter_fourcc(*"XVID"), 
                    20, 
                    (640, 480)
                )
                recording = True 
                start = time.time() 
                # Save score 
                with open(score_file, "w") as f: 
                    f.write(str(score)) 
    if recording: 
        video_writer.write(frame) 
        if time.time() - start > 3: 
            video_writer.release() 
            recording = False 
            GPIO.output(LED, 0) 
            GPIO.output(BUZZER, 0) 
    
    if circles is None: 
        goal_detected = False 
        
    cv2.imshow("Smart Goal", frame) 
    
    if cv2.waitKey(1) & 0xFF == 27: 
        break
cv2.destroyAllWindows() 
GPIO.cleanup() 
picam2.stop()