import hashlib 
import sqlite3

def is_valid_credentials(username, password):
    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    conn = sqlite3.connect('ppab6.db')
    c = conn.cursor()
    for row in c.execute('''SELECT username, password_hash FROM users WHERE
            username LIKE ?''', (username,)):
        print(row)

    return False

if __name__ == '__main__':
    username = input("User name: ")
    password = input("Password: ")

    if is_valid_credentials(username, password):
        print("<deep, dark secret>")
    else:
        print("Get lost.")
