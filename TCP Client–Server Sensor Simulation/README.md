

# Python TCP Client–Server Temperature Sensor Simulation

## Project Description

This project demonstrates the basics of **TCP socket communication in Python** by implementing a simple **client–server system**.

The server listens for incoming connections and receives messages from a client.
The client simulates a **temperature sensor** by generating random temperature values and sending them to the server every **5 seconds**.

<img width="1675" height="333" alt="image" src="https://github.com/user-attachments/assets/4f30914c-128b-4525-97b8-646b9dbc5309" />

This project helps understand fundamental networking concepts such as:

* TCP communication
* Socket programming
* Client–server architecture
* Data transmission over a network

---

## Project Structure

```
tcp-socket-sensor
│
├── server.py
├── client.py
└── README.md
```

**server.py**

* Starts a TCP server
* Waits for client connections
* Receives and prints incoming data

**client.py**

* Connects to the server
* Generates random temperature data
* Sends data every 5 seconds

---

## Requirements

* Python 3.x
* VS Code or any Python-compatible editor
* Basic knowledge of Python

Install Python if needed:
https://www.python.org/downloads/

---

## How to Run the Project

### 1. Start the Server

Open a terminal and run:

```bash
python server.py
```

Expected output:

```
Listening on 127.0.0.1:8000
```

---

### 2. Start the Client

Open a **second terminal** and run:

```bash
python client.py
```

Example output:

```
Sent: Temperature: 23.4 C
Sent: Temperature: 24.1 C
Sent: Temperature: 22.8 C
```

---

## Example Server Output

```
Listening on 127.0.0.1:8000
Accepted connection from 127.0.0.1:54231
Received: Temperature: 23.4 C
Received: Temperature: 24.1 C
Received: Temperature: 22.8 C
```

---

## Testing

### Localhost Test

The server and client were successfully tested on the same computer using:

```
127.0.0.1
```

### Network Test

The system can also be tested on two different devices connected to the same WiFi network.

Steps:

1. Find the server computer IP address using:

```
ipconfig
```

2. Replace the server IP in `client.py` with the server's IP address.

3. Run the server on one device and the client on another device.

---

## Screenshot

(Add a screenshot showing the server receiving temperature data from the client.)

Example:

```
Server Terminal:
Received: Temperature: 23.4 C
Received: Temperature: 24.1 C
Received: Temperature: 22.8 C
```

---

## Concepts Demonstrated

* TCP Socket Programming
* Client–Server Communication
* Real-time Data Simulation
* Network Communication using Python

---

## Author

Student Project – Wireless Networking Assignment
University Coursework
