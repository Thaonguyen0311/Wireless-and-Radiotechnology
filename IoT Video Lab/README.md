# IoT Video Transfer System
## Overview

This project implements a simple IoT-style data pipeline for transferring video files from a sender device to a receiver device over a local network.

The system consists of three main components:

recorder.py – records video files on the sender device
sender.py – sends recorded video files to the receiver
receiver.py – receives and stores video files

This simulates a real-world large-data pipeline such as those used in surveillance systems or edge AI applications.

# System Roles
Sender Device: Laptop A (running recorder.py and sender.py)
Receiver Device: Laptop B (running receiver.py)
Receiver IP Address

# Workflow
Start the receiver (receiver.py)
Start the recorder (recorder.py)
Start the sender (sender.py)
Video is recorded on the sender device
Sender transfers the video file to the receiver
Receiver confirms successful receipt
Sender deletes the local file after confirmation


# Problems Encountered & Fixes
## 1. Connection Refused Error
Cause: Receiver was not started before sender
Fix: Always start receiver.py first
## 2. Incorrect IP Address
Cause: Using wrong or outdated IP address

Fix: Checked IP using:

ipconfig (Windows)
ifconfig / ip a (Linux/Mac)
## 3. Firewall Blocking Connection
Cause: OS firewall blocked socket communication
Fix: Disabled firewall temporarily or allowed Python through firewall
## 4. File Not Deleted
Cause: Missing confirmation logic
Fix: Added acknowledgment message from receiver before deletion
# Screenshots
<img width="2535" height="1442" alt="image" src="https://github.com/user-attachments/assets/f4116391-85ae-405c-80db-93cc86c65123" />
<img width="1107" height="272" alt="image" src="https://github.com/user-attachments/assets/8b017dfc-6244-4acd-85b8-896b11599401" />
<img width="495" height="587" alt="image" src="https://github.com/user-attachments/assets/97d412fa-678d-4a0b-9f35-07e72d793d5a" />


