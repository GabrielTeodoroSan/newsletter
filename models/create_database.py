import sqlite3


def create():
    con = sqlite3.connect("../database.db")
    cur = con.cursor()

    cur.execute("""CREATE TABLE notices(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(30),
        url VARCHAR(50),
        image VARCHAR(30),
        created_in timestamp
        )""")

    con.commit()

if __name__ == "__main__":
    create()

