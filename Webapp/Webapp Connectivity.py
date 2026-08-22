import socket

print('ill try sockets in this file')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host is the ip, port can be any usable values
HOST = '127.0.0.1'
PORT = 5555

#bind connects particular ip and port to sockets
sock.bind((HOST, PORT))

#listen makes the server listen to the client without a loop
sock.listen()

print("server is listening... waiting for the client")

#accept gives (connection_object, address_of_client)
#conn = connection object obv
#addr = address of client(IP address and port)
conn, addr = sock.accept()

print(f"Connected to {addr}")

while True:
    #obv recv recieves messages, in this case upto 1024 bytes
    message = conn.recv(1024).decode()

    #if an empty message is recieved/no message, loop breaks
    #code is stopped up till recieve loop is on
    if not message:
        break

    print(f"[CLIENT]: {message}")

    reply = input("[YOU]: ")

    #obv send sends messages
    conn.send(reply.encode())

#closes the connection with the particular client
conn.close()
#closes all connections as server is closed
sock.close()