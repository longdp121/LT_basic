import threading
import socket

PORT = 5050
SERVER = "localhost"
ADDRESS = (SERVER, PORT)
FORMART = "utf-8"
DISCONNECT_MSG = "!Disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

clients = set()
clients_lock = threading.Lock()

def handle_client(conn, addr):
    print(f"[New connection] {addr} connected")
    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMART)
            if not msg:
                break
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}] {msg}")
            #print(f"This is connection {conn}")
            #print(f"This is clients set {clients}")
            with clients_lock:
                for c in clients:
                    if c != conn:
                        c.sendall(f"[{addr}] {msg}".encode(FORMART))
                    #print(c)
    finally:
        with clients_lock:
            clients.remove(conn)
            #print(clients)
        conn.close()

def start():
    print("[Server start]")
    server.listen()
    while True:
        conn, addr = server.accept()
        with clients_lock:
            clients.add(conn)
            #print(clients)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start()