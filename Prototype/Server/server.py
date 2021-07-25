import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def start_server():
    global clients
    server.listen(5)
    print(f'[STARTING] Server is starting...')
    while True:
        conn, addr = server.accept()
        clients += [conn]
        thread = threading.Thread(target=receive_msg, args=(conn,))
        thread.start()
        print(f'[CONNECTION] {addr} has connected!')


def broadcast(msg, name):
    for client in clients:
        client.send(f'[{name}]: {msg}'.encode(FORMAT))


def close_conn(conn):
    clients.remove(conn)
    conn.close()


def receive_msg(conn):
    connected = True

    name = conn.recv(1024).decode(FORMAT)
    conn.send(f"Welcome to the chat {name}!".encode(FORMAT))

    while connected:
        msg = conn.recv(1024).decode(FORMAT)
        print(f'[{name}] {msg}')
        broadcast(msg, name)
        if msg == "!DISCONNECT":
            broadcast("has left the chat", name)
            connected = False
    close_conn(conn)

start_server()


