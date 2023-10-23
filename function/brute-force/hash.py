import hashlib
hash_obj = hashlib.sha1(b"HelloWorld")
pb_hash = hash_obj.hexdigest()
print(pb_hash)
