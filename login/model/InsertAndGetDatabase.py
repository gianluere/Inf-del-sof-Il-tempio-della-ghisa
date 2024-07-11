import sqlite3


def insert(key, user, passw, tipe):
    conn = sqlite3.connect("login/model/dati.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO dati (id, username, password, tipo) VALUES (?, ?, ?, ?)",
                (key, user, passw, tipe))
    conn.commit()


def all_key():
    conn = sqlite3.connect("login/model/dati.db")
    cur = conn.cursor()
    cur.execute("SELECT id FROM dati")
    risultato = cur.fetchall()
    risultato_formattato = [row[0] for row in risultato]
    return risultato_formattato

def all_username():
    conn = sqlite3.connect("login/model/dati.db")
    cur = conn.cursor()
    cur.execute("SELECT username FROM dati")
    risultato = cur.fetchall()
    risultato_formattato = [row[0] for row in risultato]
    return risultato_formattato
