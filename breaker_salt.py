import hashlib

#Same code as breaker but added salt

#old_target_hash = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"

#salt = "xyz"
#s = hashlib.sha256(("password123" + salt).encode('utf-8'))
#print(s.hexdigest())
#new hash with salt: e26478bb1379f0d1b272a51924f391661824f2985c55e7e21ff4ac3f2565707d

target_hash = "e26478bb1379f0d1b272a51924f391661824f2985c55e7e21ff4ac3f2565707d"


with open("common_password.txt") as common_passwords:
    common_passwords_list = [line.strip() for line in common_passwords]

for passwords in common_passwords_list:
    hashed_password = hashlib.sha256(passwords.encode('utf-8')).hexdigest()
    if hashed_password == target_hash:
        print(f"Password cracked! Password is {passwords}")
        break

    else:
        continue
