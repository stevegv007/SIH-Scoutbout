from vidstream import CameraClient
import threading

camera = CameraClient("192.168.1.35", 9999)

camera_thread = threading.Thread(target=camera.start_stream)
camera_thread.start()

print("Camera started!")
print("Sending camera footage to Laptop B.")
print("Type STOP to stop the camera.")

while True:
    command = input()

    if command.upper() == "STOP":
        camera.stop_stream()
        print("Camera stopped.")
        break