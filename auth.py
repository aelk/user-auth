import hashlib
import yaml

def is_valid_credentials(username, password):
    with open("credentials.yaml", "r") as stream:
        users = yaml.safe_load(stream)
        password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
        for i in range(len(users)):
            if username == users[i]["username"] and \
                password_hash == users[i]["password_hash"]:
                return True
        return False

if __name__ == '__main__':
    username = input("User name: ")
    password = input("Password: ")

    if is_valid_credentials(username, password):
        print("<deep, dark secret>")
    else:
        print("Get lost.")
