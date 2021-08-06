import time
import socket
import threading


class Client:
    PORT = 5050
    FORMAT = 'utf-8'
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)


    def __init__(self, name):
        self.msgs = []
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        self.set_name(name)
        


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


    def set_name(self, name):
        self.send_msg(name)
    







# usr1 = Client("Test")
# time.sleep(2)
# usr2 = Client("Test2")
# time.sleep(2)
# usr1.send_msg("waddup!")
# time.sleep(2)
# usr2.send_msg("yo")
# time.sleep(2)
# usr1.send_msg("wassup")
# time.sleep(2)
# usr2.send_msg('nm wbu?')
# time.sleep(2)
# usr1.send_msg("!DISCONNECT")
# time.sleep(2)
# usr2.send_msg('!DISCONNECT')

# print(msgs)
