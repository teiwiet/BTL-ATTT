import socket
import urllib.parse
from scrape import common_port
def scan():
    ip = input("URL or IP : ")
    if ip.startswith("https://"):
        parsed_url = urllib.parse.urlparse(ip)
        ip = socket.gethostbyname(parsed_url.hostname)
    for lmao in range(len(common_port)):
        common_port[lmao] = int(common_port[lmao])
    print(common_port)
    for _ in range(len(common_port)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, common_port[_]))
        if result == 0:
            print(f"Port {common_port[_]} is open")
        # else:
        #     print(f"Port {common_port[_]} is close")
        s.close()
scan()