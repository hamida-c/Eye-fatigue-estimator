# 👁️ Eye Fatigue Estimator

![image](https://github.com/user-attachments/assets/3e88f815-876a-4c8d-a2ae-a452378d07db)


A lightweight desktop tool that uses your webcam and OpenCV's Haarcascade eye detector to monitor eye fatigue in real-time. It tracks how long your eyes stay closed and alerts you when signs of tiredness appear — because your eyes need breaks too.

### Project Overview:
This project helps identify signs of eye fatigue based on prolonged eye closure. It's built with simple but effective computer vision techniques — no deep learning, just OpenCV doing its job.
Whether you're working long hours or binge-watching something, this tool helps remind you when it's time to pause and blink.

### Features:
* Detects eyes using Haar Cascade 
* Tracks eye closure duration across frames
* Monitors fatigue events over a 60-second session
* Displays fatigue warnings when thresholds are crossed
* Shows final fatigue status at session end
* Works completely offline

### Technologies Used:

* Python
* OpenCV – for webcam access and eye detection
* NumPy – array operations
* Tkinter – To display final alert messages

### How Fatigue is Measured
* Eyes are tracked using a Haar cascade classifier.
* If no eyes are detected for more than 5 consecutive frames, it's considered a fatigue incident.
* Over 60 seconds, if 8 or more incidents are detected, the app warns the user to take a break.

### Installation

Make sure Python is installed 

1. Clone the repository:
   git clone https://github.com/hamida-c/Eye-fatigue-estimator.git
   cd eye-fatigue-estimator

2. Install dependencies:
pip install -r requirements.txt

3. Run the App:
python main.py

Press q to quit the monitoring session early.
