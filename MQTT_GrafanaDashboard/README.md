# IoT Temperature Monitoring System using MQTT and Grafana
## 1. System Overview
<img width="1932" height="1000" alt="image" src="https://github.com/user-attachments/assets/2b26b44f-e321-4728-a638-48242a8973eb" />


<img width="1377" height="959" alt="Screenshot 2026-03-25 125242" src="https://github.com/user-attachments/assets/13b385cf-2472-43e2-ba8a-4031bf2d2cc3" />
This project demonstrates a simple real-time IoT monitoring system.
Temperature data is sent from one laptop (publisher) to another laptop (subscriber) using socket communication, then forwarded to an MQTT broker, and finally visualized in Grafana.

## 2. Data Flow

<img width="734" height="608" alt="Screenshot 2026-03-25 125339" src="https://github.com/user-attachments/assets/8141751a-78a2-4782-8992-a1114c421225" />

## 3. MQTT Configuration
Broker used: broker.emqx.io
Port: 1883
Topic: savonia/iot/thao/temperature
## 4. Limitation of Live MQTT Visualization

Grafana with MQTT only supports live data streaming.

Limitations:

No built-in data storage
Cannot view past data
No historical analysis unless integrated with a database (e.g., InfluxDB)

## Why is MQTT useful for monitoring applications?

MQTT is useful because:

It is lightweight and fast
Uses publish/subscribe model
Supports real-time communication
Efficient for devices with limited resources

This makes it ideal for IoT and monitoring systems.

## What is the difference between live monitoring and historical storage?
Live Monitoring	Historical Storage
Shows data in real time	Stores past data
No persistence	Data saved in database
Immediate updates	Supports analysis and trends
Temporary data	Permanent records
