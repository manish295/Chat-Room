import socket
import threading
# from Db.database import Database




class Server:

    def __init__(self):
        PORT = 5050
        SERVER = "192.168.1.216" #192.168.1.216
        self.ADDR = (SERVER, PORT)
        self.FORMAT = 'utf-8'
        self.clients = []
        self.names = []
        # self.messages = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    def start_server(self):
        
        self.server.bind(self.ADDR)
        self.server.listen(5)
        print(f'[STARTING] Server is starting...')
        while True:
            conn, addr = self.server.accept()
            self.clients += [conn]
            thread = threading.Thread(target=self.handle_client, args=(conn,))
            thread.start()
            print(f'[CONNECTION] {addr} has connected!')


    def broadcast(self, name, msg):
        for client in self.clients:
            client.send(f'[{name}]: {msg}\n'.encode(self.FORMAT))


    def close_conn(self, conn):
        self.clients.remove(conn)
        conn.close()


    def handle_client(self, conn):
        connected = True

        name = conn.recv(1024).decode(self.FORMAT)
        # conn.send(f"Welcome to the chat {name}!".encode(FORMAT))
        self.broadcast(name, "has entered the chat!" )
        self.names.append(name)
        self.broadcast("EXISTING USERS", ", ".join(self.names))

        while connected:
            msg = conn.recv(1024).decode(self.FORMAT)
            print(f'[{name}] {msg}')
            if msg == "!DISCONNECT":
                self.broadcast(name, "has left the chat" )
                connected = False
            else:
                self.broadcast(name, msg)
                # db = Database() # Cannot be run through Command line
                # db.save_messages(name, msg)
                # db.close()
                # self.messages.append(f"[{name}]: {msg}")
                # print(messages)

            
        self.close_conn(conn)
        # for msgs in self.messages[:]:
        #     if f"[{name}]:" in msgs:
        #         self.messages.remove(msgs)
        # db = Database()
        # db.remove_messages(name=name)
        # db.close()
        self.names.remove(name)
        self.broadcast("EXISTING USERS", ", ".join(self.names))
        



if __name__ == "__main__":
    server = Server()
    server.start_server()





