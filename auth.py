import hashlib

def is_valid_credentials(username, password):
    users = {
        "andrew": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",
        "george": "c6ba91b90d922e159893f46c387e5dc1b3dc5c101a5a4522f03b987177a24a91"
    }
    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return username in users and users[username] == password_hash

if __name__ == '__main__':
    username = input("User name: ")
    password = input("Password: ")

    if is_valid_credentials(username, password):
        print("<deep, dark secret>")
    else:
        print("Get lost.")
