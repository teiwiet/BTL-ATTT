import hashlib
hash_obj = hashlib.sha1(b"webstudio")
pb_hash = hash_obj.hexdigest()
print(pb_hash)