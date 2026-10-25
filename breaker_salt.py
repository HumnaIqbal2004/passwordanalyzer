import hashlib

def dictionary_attack_salt(password):

    salt = "xyz"
    target_hash = hashlib.sha256(((password) + salt).encode('utf-8')).hexdigest()


    with open("common_password.txt") as common_passwords:
        common_passwords_list = [line.strip() for line in common_passwords]

    cracked = True

    for passwords in common_passwords_list:
        hashed_password = hashlib.sha256(passwords.encode('utf-8')).hexdigest()
        if hashed_password == target_hash:
            print(f"Password cracked! Password is {passwords}")
            cracked = True
            break
            

        else:
            cracked = False
            continue

    if cracked == False:
        print("Password not cracked")