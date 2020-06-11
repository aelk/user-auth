import hashlib
import sqlite3

def add():
    username = input("User name: ")
    password = input("Password: ")

    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    conn = sqlite3.connect('ppab6.db')
    c = conn.cursor()
    c.execute('''INSERT INTO users VALUES (?,?)''', (username, password_hash))


if __name__ == '__main__':
    add()
