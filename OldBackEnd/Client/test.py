from client import Client

c1 = Client(input("name"))


if __name__ == "__main__":
    while True:
        msg = input("msg:")
        c1.send_msg(msg)
        if msg == "!DISCONNECT":
            break
