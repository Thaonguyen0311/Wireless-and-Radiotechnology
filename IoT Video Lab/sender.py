import socket
import os
import time
import json
import struct

HOST = "127.0.0.1"
PORT = 5001
VIDEO_FOLDER = "videos"
CHECK_INTERVAL = 5  # seconds
BUFFER_SIZE = 4096

os.makedirs(VIDEO_FOLDER, exist_ok=True)

print("Sender started. Watching video folder...")


def send_all(sock, data: bytes):
    """Send all bytes reliably."""
    sock.sendall(data)


def recv_exact(sock, num_bytes: int) -> bytes:
    """Receive exactly num_bytes bytes or raise error if connection closes."""
    data = b""
    while len(data) < num_bytes:
        chunk = sock.recv(num_bytes - len(data))
        if not chunk:
            raise ConnectionError("Connection closed while receiving data.")
        data += chunk
    return data


def send_file(filepath: str) -> bool:
    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    try:
        print(f"[INFO] Connecting to receiver for: {filename}")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(15)
            client.connect((HOST, PORT))

            # Prepare header
            header_dict = {
                "filename": filename,
                "filesize": filesize
            }
            header_json = json.dumps(header_dict).encode("utf-8")
            header_len = struct.pack("!I", len(header_json))  # 4 bytes unsigned int, network byte order

            # Send header length + header
            send_all(client, header_len)
            send_all(client, header_json)

            # Wait for receiver acknowledgement
            response = client.recv(1024)
            if response != b"READY":
                print(f"[ERROR] Receiver not ready for {filename}. Response: {response}")
                return False

            # Send file content
            print(f"[INFO] Sending file: {filename} ({filesize} bytes)")
            with open(filepath, "rb") as f:
                while True:
                    chunk = f.read(BUFFER_SIZE)
                    if not chunk:
                        break
                    send_all(client, chunk)

            # Wait for final confirmation
            response = client.recv(1024)
            if response == b"OK":
                print(f"[SUCCESS] Transfer confirmed: {filename}")
                os.remove(filepath)
                print(f"[INFO] Deleted local file: {filename}\n")
                return True
            else:
                print(f"[ERROR] Invalid confirmation for {filename}. Response: {response}")
                return False

    except Exception as e:
        print(f"[ERROR] Error sending {filename}: {e}")
        return False


while True:
    try:
        files = [f for f in os.listdir(VIDEO_FOLDER) if f.lower().endswith(".mp4")]
        files.sort()

        if files:
            print(f"[INFO] Found {len(files)} file(s): {files}")

        for file in files:
            filepath = os.path.join(VIDEO_FOLDER, file)
            if os.path.isfile(filepath):
                send_file(filepath)

        time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\n[INFO] Sender stopped.")
        break
    except Exception as e:
        print(f"[ERROR] Main loop error: {e}")
        time.sleep(CHECK_INTERVAL)