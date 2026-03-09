# Bluetooth Client–Server IoT Sensor Simulation

## Project Description

This project implements a simple **Bluetooth client–server communication system in Python** using **RFCOMM sockets**.

The system simulates an **IoT sensor node** that sends temperature data to a **gateway device** over a Bluetooth connection.

The **client program** acts as a sensor that generates a random temperature value every **5 seconds** and sends it to the server.

The **server program** acts as a gateway that receives the sensor data and displays it in the terminal.

This demonstrates how Bluetooth communication can be used in **Internet of Things (IoT)** systems for short-range data transfer.

## How to Run the Project

### 1. Pair the Devices

Before running the program, ensure that both devices are paired using the operating system Bluetooth settings.


### 2. Start the Server

Run the server program on the gateway device:

```
python server.py
```

The server will display:

```
Waiting for Bluetooth client connection...
```

---

### 3. Start the Client

Run the client program on the sensor device:

```
python client.py
```

The client will connect to the server and start sending temperature data every **5 seconds**.

Example client output:

```
Connected to Bluetooth server
Sent: Temperature: 23.1 C
Sent: Temperature: 25.4 C
Sent: Temperature: 21.7 C
```

---


## Difference Between Bluetooth Socket Communication and WiFi Socket Communication

The main difference between Bluetooth and WiFi socket communication is **range, speed, and typical use cases**.

Bluetooth communication is designed for **short-range, low-power connections** between nearby devices. It is commonly used in IoT devices, wearables, and personal area networks.

WiFi socket communication uses **TCP/IP over a wireless network**, allowing devices to communicate over much larger distances through routers and internet infrastructure. WiFi generally provides **higher data transfer speeds** but consumes more power.

In practice, Bluetooth is suitable for **device-to-device communication at short distances**, while WiFi is better for **network-based communication and internet connectivity**.

