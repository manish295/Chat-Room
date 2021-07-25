import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
clients = []
names = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def start_server():
    global clients
    server.listen(5)
    print(f'[STARTING] Server is starting...')
    while True:
        conn, addr = server.accept()
        clients += [conn]
        thread = threading.Thread(target=handle_client, args=(conn,))
        thread.start()
        print(f'[CONNECTION] {addr} has connected!')


def broadcast(name, msg):
    for client in clients:
        client.send(f'[{name}]: {msg}\n'.encode(FORMAT))


def close_conn(conn):
    clients.remove(conn)
    conn.close()


def handle_client(conn):
    connected = True

    name = conn.recv(1024).decode(FORMAT)
    conn.send(f"Welcome to the chat {name}!".encode(FORMAT))
    broadcast(name, "has entered the chat!" )
    names.append(name)
    broadcast("EXISTING USERS", ", ".join(names))

    while connected:
        msg = conn.recv(1024).decode(FORMAT)
        print(f'[{name}] {msg}')
        if msg == "!DISCONNECT":
            broadcast(name, "has left the chat" )
            connected = False
        else:
            broadcast(name, msg)
        
    close_conn(conn)
    names.remove(name)
    broadcast("EXISTING USERS", ", ".join(names))


if __name__ == "__main__":
    start_server()


