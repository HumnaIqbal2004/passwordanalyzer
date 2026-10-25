import hashlib

def dictionary_attack(password):


    target_hash = hashlib.sha256((password).encode('utf-8')).hexdigest()
    print(f"Your password hashed is: {target_hash}")
    print("Launching dictionary attack")
    #hash for password123

    #s = hashlib.sha256("password123".encode('utf-8'))
    #print(s.hexdigest())

    #To get a different target hash remove the comment and change "password123" with a different password

    with open("common_password.txt") as common_passwords:
        common_passwords_list = [line.strip() for line in common_passwords]

    cracked = True

    for passwords in common_passwords_list:
        hashed_password = hashlib.sha256(passwords.encode('utf-8')).hexdigest()
        if hashed_password == target_hash:
            cracked = True
            print(f"Password cracked! Password is {passwords}")
            break

        else:
            cracked = False
            continue

    if cracked == False:
        print("Password not cracked")