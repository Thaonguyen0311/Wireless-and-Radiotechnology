import socket
import os
import json
import struct

HOST = "0.0.0.0"
PORT = 5001
SAVE_FOLDER = "received_videos"
BUFFER_SIZE = 4096

os.makedirs(SAVE_FOLDER, exist_ok=True)


def recv_exact(conn, num_bytes: int) -> bytes:
    """Receive exactly num_bytes bytes or raise error if connection closes."""
    data = b""
    while len(data) < num_bytes:
        chunk = conn.recv(num_bytes - len(data))
        if not chunk:
            raise ConnectionError("Connection closed while receiving data.")
        data += chunk
    return data


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print("Receiver is waiting for files...")

while True:
    conn, addr = None, None
    try:
        conn, addr = server.accept()
        print(f"[INFO] Connected by {addr}")

        with conn:
            conn.settimeout(15)

            # Read 4-byte header length
            raw_header_len = recv_exact(conn, 4)
            header_len = struct.unpack("!I", raw_header_len)[0]

            # Read header JSON
            header_json = recv_exact(conn, header_len)
            header = json.loads(header_json.decode("utf-8"))

            filename = header["filename"]
            filesize = int(header["filesize"])

            save_path = os.path.join(SAVE_FOLDER, filename)

            print(f"[INFO] Preparing to receive: {filename} ({filesize} bytes)")
            conn.sendall(b"READY")

            # Receive exactly filesize bytes
            received = 0
            with open(save_path, "wb") as f:
                while received < filesize:
                    remaining = filesize - received
                    chunk = conn.recv(min(BUFFER_SIZE, remaining))
                    if not chunk:
                        raise ConnectionError("Connection lost during file transfer.")
                    f.write(chunk)
                    received += len(chunk)

            print(f"[SUCCESS] Received: {filename}")
            conn.sendall(b"OK")

    except Exception as e:
        print(f"[ERROR] Receiver error: {e}")
        if conn:
            try:
                conn.close()
            except Exception:
                pass