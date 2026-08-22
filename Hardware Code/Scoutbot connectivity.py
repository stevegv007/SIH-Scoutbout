import socket

'''This is the client code for the connectivity'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 5555

sock.connect((HOST, PORT))
'''
NOTE: this part is to be run to check the connectivity only

while True:
    message = input("[YOU]: ")

    sock.send(message.encode())

    reply = sock.recv(1024).decode()

    print(f"[SERVER]: {reply}")'''