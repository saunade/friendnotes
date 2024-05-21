import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Note from Sanna', 
             'Hi guys!\nI am so happy with how this turned out. I learned many new skills such as learning how to use SQLite and deepen my knowledge of SQL.\nGive feedback if you have some ideas!\nThanks for participating :^)')
            )

connection.commit()
connection.close()