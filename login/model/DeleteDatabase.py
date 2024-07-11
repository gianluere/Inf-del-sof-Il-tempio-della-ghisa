import sqlite3


def delete(chiave):
    conn = sqlite3.connect("login/model/dati.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM dati WHERE id=?", (chiave,))
    conn.commit()