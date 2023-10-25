import hashlib
<<<<<<< HEAD
with open(r"D:\edoc\project\BTL-ATTT\function\brute-force\password_list.txt","r") as file:
=======
with open(r"/home/nukedukk/Main/edoc/project/BTL-ATTT/function/brute-force/password_list.txt","r") as file:
>>>>>>> 1c0c5e8040e78b2ecd3fcc65c67f1d7ac264ce92
    lines = file.read().splitlines()
def cal_hash(string):
    hash = hashlib.sha1(string=string.encode())
    pb_hash = hash.hexdigest()
    return pb_hash
target_hash = "db8ac1c259eb89d4a131b253bacfca5f319d54f2"
for line in lines:
    if cal_hash(line)  == target_hash:
        print(f"Found password : {line}")