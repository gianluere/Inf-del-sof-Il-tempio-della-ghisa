import sqlite3
import socket
import threading
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 63001))
server.listen()
print("avviato")

def handle_connection(c):
    print("connesso")
    username = c.recv(1024).decode()
    password = c.recv(1024).decode()
    #conn = sqlite3.connect(("login/model/dati.db"))
    conn = sqlite3.connect(("dati.db"))
    cur = conn.cursor()

    print(username + " " + password)
    cur.execute("SELECT * FROM dati WHERE username = ? AND password = ?", (username, password))
    results = cur.fetchall()
    print(results)
    if not results:
        c.send("Login failed".encode())
        #print("sbagliato")
    else:
        c.send(results[0][3].encode())
        time.sleep(0.1)
        c.send(results[0][0].encode())
        #print("giusto")
    #if cur.fetchall():
     #   c.send("Login successful".encode())
    #else:
     #   c.send("Login failed".encode())

    print("Fatto, riattendo\n")


while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()