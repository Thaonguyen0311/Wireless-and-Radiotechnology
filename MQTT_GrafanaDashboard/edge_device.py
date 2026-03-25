import socket
import paho.mqtt.client as mqtt

HOST = "127.0.0.1"
PORT = 5000

broker = "broker.emqx.io"
topic1 = "savonia/iot/thao/temperature"
topic2 = "savonia/iot/thao/humidity"
topic3 = "savonia/iot/thao/light"

mqtt_client = mqtt.Client()
mqtt_client.connect(broker,1883)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Edge device waiting for sensor...")

conn, addr = server.accept()

print("Sensor connected:", addr)

while True:

    data = conn.recv(1024)

    if not data:
        break
    raw_value = data.decode().strip()

    parts = raw_value.split(",")
    temp, hum, light = parts

    print("Edge received:", raw_value)
    # Gửi đúng dữ liệu vào đúng topic
    mqtt_client.publish(topic1, temp)
    mqtt_client.publish(topic2, hum)
    mqtt_client.publish(topic3, light)

    print("Forwarded to MQTT:", raw_value)