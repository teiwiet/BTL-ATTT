import hashlib
with open(r"D:\edoc\project\BTL-ATTT\function\brute-force\password_list.txt","r") as file:
    lines = file.read().splitlines()
def cal_hash(string):
    hash = hashlib.sha1(string=string.encode())
    pb_hash = hash.hexdigest()
    return pb_hash
target_hash = "db8ac1c259eb89d4a131b253bacfca5f319d54f2"
for line in lines:
    if cal_hash(line)  == target_hash:
        print(f"Found password : {line}")