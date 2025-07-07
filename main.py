

import cv2
import numpy as np
import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Load Haar cascade for eye detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')



# Initialize variables
closed_eyes_frames = 0
fatigue_events = 0
threshold_closed_frames = 5  # Eye closed for >5 frames (~0.2 sec) is considered fatigue
monitor_duration = 60  # Monitor for 60 seconds

# Start webcam
cap = cv2.VideoCapture(0)
print("Monitoring started. Press 'q' to quit early.")

start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # If eyes not detected
    if len(eyes) == 0:
        closed_eyes_frames += 1
    else:
        if closed_eyes_frames >= threshold_closed_frames:
            fatigue_events += 1
        closed_eyes_frames = 0

    # Timer
    elapsed = time.time() - start_time
    remaining = int(monitor_duration - elapsed)

    # Show fatigue warning during session
    warning = ""
    if fatigue_events >= 8:
        warning = "⚠️ You look tired. Please take a short break."

    # Display info on the frame
    cv2.putText(frame, f"Fatigue Events: {fatigue_events}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
    cv2.putText(frame, f"Time left: {remaining}s", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, warning, (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Eye Fatigue Estimator", frame)

    # Break condition
    if cv2.waitKey(1) & 0xFF == ord('q') or elapsed >= monitor_duration:
        break

# Final screen message before exit
final_message = "You look tired. Please take a short break." if fatigue_events >= 8 else "Everything looks fine. No signs of fatigue."

# Show message on final frame
ret, frame = cap.read()
if ret:
    frame = cv2.flip(frame, 1)
    cv2.putText(frame, final_message, (50, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
    cv2.imshow("Eye Fatigue Estimator", frame)
    cv2.waitKey(3000)  # Show final message for 3 seconds

# Clean up
cap.release()
cv2.destroyAllWindows()
