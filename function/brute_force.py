import hashlib
with open(r"D:\edoc\project\BTL-ATTT\10-million-password-list-top-1000000.txt","r") as file:
    lines = file.read().splitlines()
def cal_hash(string):
    hash = hashlib.sha1(string=string.encode())
    pb_hash = hash.hexdigest()
    return pb_hash
target_hash = "9f6c7c97d4623a6c98a8568e5338cd595e01cc8e"
for line in lines:
    if cal_hash(line)  == target_hash:
        print(f"Found password : {line}")