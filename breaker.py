import hashlib


target_hash = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
#hash for password123

#s = hashlib.sha256("password123".encode('utf-8'))
#print(s.hexdigest())

#To get a different target hash remove the comment and change "password123" with a different password

with open("common_password.txt") as common_passwords:
    common_passwords_list = [line.strip() for line in common_passwords]

for passwords in common_passwords_list:
    hashed_password = hashlib.sha256(passwords.encode('utf-8')).hexdigest()
    if hashed_password == target_hash:
        print(f"Password cracked! Password is {passwords}")
        break

    else:
        continue

