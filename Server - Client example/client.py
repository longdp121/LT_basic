import socket
import time

PORT = 5050
SERVER = "localhost"
ADDRESS = (SERVER, PORT)
FORMART = "utf-8"
DISCONNECT_MSG = "!Disconnect"

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    return client

def send(client, msg):
    message = msg.encode(FORMART)
    client.send(message)

def start():
    connection = connect()
    while True:
        msg = input()
        if msg == "q":
            break
        send(connection, msg)
        receive_msg = connection.recv(1024).decode(FORMART)
        if receive_msg:
            print(receive_msg)
    
    send(connection, DISCONNECT_MSG)
    time.sleep(1)
    print("Discontect")

start()
# client = connect()
# send(client)
# #input()
# #send(client, DISCONNECT_MSG)

