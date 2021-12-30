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

def start_receive():
    connection = connect()
    while True:
        msg = connection.recv(1024).decode(FORMART)
        print(msg)

start_receive()