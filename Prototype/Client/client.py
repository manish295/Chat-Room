import socket
import threading
import time

PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_msg(msg):
    msg = msg.encode(FORMAT)
    client.send(msg)


def receive():
    while True:
        data = client.recv(1024).decode(FORMAT)
        if not data:
            break
        print("\n" + data)


def set_name(name):
    send_msg(name)


if __name__ == "__main__":
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    set_name(input("What is your name?: "))

    while True:
        msg = input()
        send_msg(msg)
        if msg == "!DISCONNECT":
            break
