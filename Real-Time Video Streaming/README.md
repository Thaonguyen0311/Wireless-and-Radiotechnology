
# 📹 Flask Webcam Streaming Project
## 1. Overview

**Camera → Capture → Encode → Stream → Viewer**
## 2. Roles
Sender (Laptop A):
The device running the Flask application and capturing video from its webcam.
Viewer (Laptop B):
The device accessing the live stream through a browser using the sender's IP address.

## 3. How the Stream Was Started

Install required libraries:

pip install flask opencv-python

Run the Flask application:

python app.py

The server starts on:

http://0.0.0.0:5000

The video stream endpoint:

/video_feed

Open a browser on the sender or another device and visit:

http://<sender-ip>:5000

## 5. Problems and Fixes
Problem 1: Webcam Not Opening
Error: Could not open webcam
Cause: Webcam already in use by another application
Fix: Closed applications like Zoom/Teams
Problem 2: Viewer Cannot Access Stream
Cause: Wrong IP address or different network
Fix:
Verified correct IP using ipconfig
Ensured both devices are on the same network
Problem 3: Firewall Blocking Connection
Cause: System firewall blocked port 5000
Fix:
Allowed Python/Flask through firewall
Opened port 5000
Problem 4: Slow or Laggy Stream
Cause: High resolution / network limitations
Fix:
Reduced frame size in OpenCV
Ensed stable Wi-Fi connection

<img width="1303" height="1238" alt="image" src="https://github.com/user-attachments/assets/2115fe44-ab0a-41b7-b1a0-5390016217e2" />
