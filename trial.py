import cv2
import socket
import struct
import pickle

# -------------------------
# SETTINGS
# -------------------------

SERVER_IP = "192.168.1.35"
PORT = 9999

# -------------------------
# CAMERA
# -------------------------

camera = cv2.VideoCapture(0)

# -------------------------
# CONNECT TO LAPTOP B
# -------------------------

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

print("Connecting to ScoutBot AI...")

client_socket.connect(
    (SERVER_IP, PORT)
)

print("Connected!")
print("Sending camera footage...")

# -------------------------
# SEND FRAMES
# -------------------------

while True:

    ret, frame = camera.read()

    if not ret:

        print("Could not access camera.")

        break

    # Resize frame
    frame = cv2.resize(
        frame,
        (480, 360)
    )

    # Compress frame
    encoded_frame = cv2.imencode(
        ".jpg",
        frame,
        [cv2.IMWRITE_JPEG_QUALITY, 50]
    )[1]

    # Convert to bytes
    data = pickle.dumps(
        encoded_frame
    )

    # Send size + frame
    message = struct.pack(
        "Q",
        len(data)
    ) + data

    client_socket.sendall(message)

    
  

camera.release()

client_socket.close()

cv2.destroyAllWindows()

print("Camera stopped.")