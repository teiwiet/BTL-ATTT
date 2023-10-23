def crack(hostname,username,password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    try :
        result = client.connect(hostname=hostname,username=username,password=password)
        print(result)
        print("connected")
    except socket.timeout:
        print("Timeout!")
    else :
        print("Connected")