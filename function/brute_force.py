import hashlib
with open(r"D:\edoc\project\BTL-ATTT\10-million-password-list-top-1000000.txt","r") as file:
    lines = file.read().splitlines()
def cal_hash(string):
    hash = hashlib.sha1(string=string.encode())
    pb_hash = hash.hexdigest()
    return pb_hash
target_hash = "4b2214922b397560e09cb40dad5bfff8ded7fcc9"
# print(len(file))
for line in lines:
    if cal_hash(line)  == target_hash:
        print(f"Found password : {line}")