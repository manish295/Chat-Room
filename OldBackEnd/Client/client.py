import time
import socket
import threading


class Client:
    PORT = 5050
    FORMAT = 'utf-8'
    SERVER = "192.168.1.216"
    ADDR = (SERVER, PORT)


    def __init__(self, name):
        self.msgs = []
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        self.name = name
        self.set_name()
        


    def send_msg(self, msg):
        msg = msg.encode(self.FORMAT)
        self.client.send(msg)


    def receive(self):
        while True:
            data = self.client.recv(1024).decode(self.FORMAT)
            if not data:
                break
            self.msgs.append(data)
            #print("\n" + data)
    
    def receive_msgs(self):
        data = self.client.recv(1024).decode(self.FORMAT)
        return data


    def set_name(self):
        self.send_msg(self.name)
    
    def return_name(self):
        return self.name

