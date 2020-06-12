import sqlite3

def setup():
    conn = sqlite3.connect('ppab6.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE users (
                    username VARCHAR,
                    password_hash VARCHAR
                )''')
    conn.commit()

if __name__ == '__main__':
    setup()
