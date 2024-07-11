import sqlite3

conn = sqlite3.connect("dati.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS dati (
    id VARCHAR(255) PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    tipo VARCHAR(255) NOT NULL
    )
""")

cur.execute("INSERT INTO dati (id, username, password, tipo) VALUES (?, ?, ?, ?)", ("00", "amm", "amm", "Amministratore"))
#cur.execute("DELETE FROM dati WHERE id=?", (22,))
conn.commit()
#conn.commit()



#cur.execute("SELECT * FROM dati")
#risultato = cur.fetchall()
#print(risultato)