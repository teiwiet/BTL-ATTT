import hashlib
hash_obj = hashlib.sha1("dream123456".encode())
pb_hash = hash_obj.hexdigest()
print(pb_hash)