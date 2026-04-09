

# YOLO Home Monitoring System
## 1. Overview
**Camera → Stream → AI Processing → Detection Result**

# 2. System Setup
Laptop A (Sender)
Role: Video streaming server
Function: Captures video from webcam and streams it over HTTP using Flask
IP Address: 127.0.0.1 (localhost) (or your actual local IP if different)
Laptop B (Receiver)
Role: Detection client
Function: Receives the video stream and performs object detection using YOLO
# 3. Sender IP Address

The video stream was accessed via:

http://127.0.0.1:5000/video_feed

If running across devices in the same network, the IP should be replaced with the sender's local IP address, for example:

http://192.168.x.x:5000/video_feed
# 4. How the Stream Was Started

On Laptop A, a Flask server was used to stream video from the webcam.

Steps:
Capture video using OpenCV (cv2.VideoCapture(0))
Encode frames as JPEG
Stream frames using Flask route /video_feed

Example:

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
# 5. How YOLO Was Run

On Laptop B, YOLOv8 was used to perform object detection on the incoming video stream.

Steps:
Load YOLO model:
model = YOLO("yolov8n.pt")
Open video stream:
cap = cv2.VideoCapture(STREAM_URL)
Run detection on each frame:
results = model(frame)
Draw bounding boxes:
annotated_frame = results[0].plot()
Display result:
cv2.imshow("YOLO Home Monitoring", annotated_frame)
# 6. Detected Objects

The YOLOv8n model (trained on COCO dataset) was able to detect common objects such as:

person
chair
laptop
bottle
phone

The detected objects were displayed with bounding boxes and class labels in real time.

# 7. Problems and Fixes
Problem 1: No bounding boxes displayed
Cause: YOLO did not detect any objects in the frame
Fix: Tested with clearer objects and reduced confidence threshold
Problem 2: Stream could not be opened
Cause: Incorrect IP address or server not running
Fix: Verified Flask server and correct IP
Problem 3: Window not showing (cv2.imshow)
Cause: Running in environment without GUI (e.g., remote server)
Fix: Ran code locally on machine with GUI support
Problem 4: Lag or low-quality frames
Cause: Network delay or low resolution
Fix: Improved network connection and adjusted frame size

<img width="1208" height="1023" alt="Screenshot 2026-04-09 140823" src="https://github.com/user-attachments/assets/e56c9a19-f7f6-41fb-81af-bee7f5dd61c1" />
